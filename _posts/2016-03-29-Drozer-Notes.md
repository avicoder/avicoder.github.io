---
layout: post
title: "Drozer Notes"
subtitle: ""
date:   2016-03-29 10:00:00
categories: [Android]
permalink: "Drozer-Notes"
---

Certian commands and points which I came accross while learning drozer. Still in learning phase so expect more modification in future.

 - Forward the TCP port:
 
`$ adb forward tcp:<Local_Port> tcp:<Device_Port>`

 - Connect ot the agent

`$ drozer console connect`

 - Find Package Identifier

`dz> run app.package.list -f  <Application_Label>`

 - Find a package with specific permission

`dz> run app.package.list -p android.permission.<Permission_Name>`

`dz> run app.package.info -p android.permission.<Permission_Name>`

 - List available modules:

`dz> list package` or `dz> ls`

 - Search for modules with description:

`dz> module search -d`

 - Install a module:

`dz> module install <module_name>`

 - Retrieving Package Information (like permissions and whatever in android manifest file)

`dz> run app.package.info -a <Package_Identifier>`

`dz> run app.package.info -a <Package_Identifier> > /path/to/saveit.txt`

 - Identify Attack Surface

`dz> run app.package.attacksurface <Package_Identifier>`

 - View AndroidManifest file
 
`dz> app.package.manifest <Package_Identifier>`

 - List Activities 

`dz> run app.activity.info -a <Package_Identifier>`

 - Start an exported activity

`dz> run app.activity.start --component <Package_Identifier> <Package_Activity_Name>`

 - Content Provider information

`dz> run app.provider.info -a <Package_Identifier>`

 - Guess Content Provider path

`dz> run scanner.provider.finduris -a <Package_Identifier>`

 - Retrieve information from Content URI

`dz> run app.provider.query content://<Package_Indentifier>.<Content_Provider>/<Path>/ --vertical`

 - SQL injection in Content Provider 

`dz> run app.provider.query content://<Package_Identifier>.<Content_Provider>/<Path>/ --projection "'"` 

`dz> run app.provider.query content://<Package_Identifier>.<Content_Provider>/<Path>/ --selection "'"` 


 - File System backed Content Provider

`dz> run app.provider.read content://<Package_Identifier>.<Content_Provider>/<Path>`

`<dz> run app.provider.download content://<package_Identifier>.<Content_Provider>/<Path>  <Local><DIR><Path>`

 - Automatically test Content Provider Vulnerabilities

`dz> run scanner.provider.injection -a <Package_Identifier>`

`dz> run scanner.provider.traversal -a <Package_Identifier>`

 - Service info

`dz> run app.service.info -a <Package_Identifier>`

### Other Modules...

 - Shell

`dz> shell`

 - Upload

`dz> tools.file.upload`

 - Download

`dz> tools.file.download`

 - Install Binaries on device

`dz tools.setup.busybox`

`dz tools.setup.minimalsu`
