import requests,json
from os import path, environ


url = "https://hackerone.com/graphql"
custom_header = {'Accept-Encoding': 'gzip'}

cursor =""
nextpage = "hello"

data = {}

handles = []
totalPrograms=0
totalUrls=0

programs = []


H1_JSON = path.join(
    path.dirname(__file__),
    '../api/h1_inscope_urls.json',
)




while nextpage:


    payload = {"operationName":"DirectoryQuery","variables":{"where":{"_and":[{"_or":[{"submission_state":{"_eq":"open"}},{"external_program":{"id":{"_is_null":False}}}]},{"external_program":{"id":{"_is_null":True}}},{"_or":[{"_and":[{"state":{"_neq":"sandboxed"}},{"state":{"_neq":"soft_launched"}}]},{"external_program":{"id":{"_is_null":False}}}]}]},"first":25,"secureOrderBy":{"started_accepting_at":{"_direction":"DESC"}},"cursor":cursor},"query":"query DirectoryQuery($cursor: String, $secureOrderBy: FiltersTeamFilterOrder, $where: FiltersTeamFilterInput) {\n  me {\n    id\n    edit_unclaimed_profiles\n    h1_pentester\n    __typename\n  }\n  teams(first: 25, after: $cursor, secure_order_by: $secureOrderBy, where: $where) {\n    pageInfo {\n      endCursor\n      hasNextPage\n      __typename\n    }\n    edges {\n      node {\n        id\n        bookmarked\n        ...TeamTableResolvedReports\n        ...TeamTableAvatarAndTitle\n        ...TeamTableLaunchDate\n        ...TeamTableMinimumBounty\n        ...TeamTableAverageBounty\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment TeamTableResolvedReports on Team {\n  resolved_report_count\n  __typename\n}\n\nfragment TeamTableAvatarAndTitle on Team {\n  profile_picture(size: medium)\n  name\n  handle\n  submission_state\n  triage_active\n  state\n  external_program {\n    id\n    __typename\n  }\n  ...TeamLinkWithMiniProfile\n  __typename\n}\n\nfragment TeamLinkWithMiniProfile on Team {\n  handle\n  name\n  __typename\n}\n\nfragment TeamTableLaunchDate on Team {\n  started_accepting_at\n  __typename\n}\n\nfragment TeamTableMinimumBounty on Team {\n  currency\n  base_bounty\n  __typename\n}\n\nfragment TeamTableAverageBounty on Team {\n  currency\n  average_bounty_lower_amount\n  average_bounty_upper_amount\n  __typename\n}\n"}

    res = requests.post(url,json=payload,headers=custom_header)
    nextpage =  res.json()['data']['teams']['pageInfo']['hasNextPage']
    cursor = res.json()['data']['teams']['pageInfo']['endCursor']
    length = len(res.json()['data']['teams']['edges'])



    # for each program

    for i in range(0,length):

        totalPrograms = totalPrograms + 1

        h =   res.json()['data']['teams']['edges'][i]['node']['handle']
        handles.append(h)
        urlscope = []


        payload2 = {"query":"query Team_assets($first_0:Int!) {query {id,...F0}} fragment F0 on Query {_team3QHDcV:team(handle:\"" +h + "\") {handle,_structured_scope_versions2ZWKHQ:structured_scope_versions(archived:false) {max_updated_at},_structured_scopes2qeKP8:structured_scopes(first:$first_0,archived:false,eligible_for_submission:true) {edges {node {id,asset_type,asset_identifier,rendered_instruction,max_severity,eligible_for_bounty},cursor},pageInfo {hasNextPage,hasPreviousPage}},_structured_scopes1wWN6h:structured_scopes(first:$first_0,archived:false,eligible_for_submission:false) {edges {node {id,asset_type,asset_identifier,rendered_instruction},cursor},pageInfo {hasNextPage,hasPreviousPage}},id},id}","variables":{"first_0":500}}



        e = requests.post(url,json=payload2,headers=custom_header).json()['data']['query']['_team3QHDcV']['_structured_scopes2qeKP8']['edges']
        # get all urls in programs


        for q in e:
            if q['node']['asset_type'] == 'URL':
                urlscope.append(q['node']['asset_identifier'])
                totalUrls = totalUrls + 1

        program = {"name":h,"urls":urlscope}
        programs.append(program)

    data.update({"data":{"programs":programs,"metaData":{"totalPrograms":totalPrograms,"totalUrls":totalUrls}}})

# print json.dumps(data)

with open(H1_JSON, 'w') as outfile:
    json.dump(data, outfile, indent=4)
