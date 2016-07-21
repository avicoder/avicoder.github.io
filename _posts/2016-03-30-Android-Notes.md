---
layout: post
title: "Android Notes"
subtitle: ""
date:   2016-03-30 10:00:00
categories: [Android]
permalink: "Android-Notes"
---


Few commands which are useful while assessing android application.

**Android Debug Bridge**



 - List Connected Devices:

`$ adb devices`

 - Get a shell on a device:

`$ adb shell`

 - Perform a shell command and return:

`$ adb shell <Command>`

 - Push a file to a device:

`$ adb push /path/to/local/file /path/on/android/device`

 - Retrieve a file from a device:

`$ adb pull /path/on/android/device /path/to/local/file`

 - Forward a TCP port on a local port to a port on the device (useful in case of **drozer**):

`$ adb forward tcp:<Local_Port> tcp:<Device_Port>`

 - View Device logs:

`$ adb logcat`

------

**Commands runs inside device $hell**

- List all installed packages

`shell@android:/ $ pm list packages `

- Find the stored APK path of an installed application 

`shell@android:/ $ pm path <Package_Name>`

- Install a package 

`shell@android:/ $ pm install /path/to/apk`

- Uninstall a package 

`shell@android:/ $ pm uninstall <Package_Name>`

- Disable an application

`shell@android:/ $ pm disable <Package_Name>`

- View Logs

`shell@android:/ $ logcat`

- Filter Logs

`shell@android:/ $ logcat -s <tag>`

- Get all Hardware and Software properties 

`shell@android:/ $ getprop`

- Get the status of system services:

`shell@android:/ $ dumpsys`

- Get the list of all services

`shell@android:/ $ service list`

-------

**Miscellaneous** 

 - Generate a x.509 Certificate

`keytool -genkey -v -keystore mykey. keystore -alias alias_name -keyalg RSA
-keysize 2048 -validity 10000`


 - Sign an unsigned application 

`$ jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore
mykey. keystore application. apk alias_name`


- View certificate information (in DER format)

`$ openssl pkcs7 -inform DER -in CERT. RSA -text -print_certs`

`$ keytool -printcert -file CERT. RSA`


- Read the AndroidManifest:

`Unzip <Application_Name>.apk`
`java -jar AXMLPrinter2.jar AndroidManifest.xml`

- Dexdump alternative to OAT (ART compatible applications):

`oatdump <Application_Name>.apk`

`oat2dex <Application_Name>.apk`

- Download Application APKs
	- http://apk-dl.com
	- http://apps.evozi.com/apk-downloader/
	- http://apkleecher.com/
	- https://apkpure.com (Download older apk)