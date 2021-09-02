---
layout: post
title: "Root AVD and Install Magisk"
subtitle: "Let's set up Android App pentesting env"
date: 2021-09-02 00:00:00
---

Mostly I have done the android app penetration testing on GenyMotion.
The problem is that a few apps aren't working properly lately because of architectural requirements and incompatibility.

Android Virtual Devices (AVD) can be a good alternative, but the images do not support rooting.

So let's root the AVD to overcome this limitation. The following guide is what I used to setup env on Mac machines.

Start by downloading the SDK or installing Android Studio.
<img src="/images/andimages.png" alt="Android System Images" width="600px"/>

Next, we will create a virtual device. You can choose which System Image you want to download.
After booting the device, open the terminal and clone the [rootAVD](https://github.com/newbit1/rootAVD) script.

<img src="/images/notrooted.png" alt="Not Rooted" width="300px"/>



Change the system image (android-xx) accordingly and run:

```
 ./rootAVD.sh ~/Library/Android/sdk/system-images/android-30/google_apis/x86/ramdisk.img
```

```
./rootAVD.sh InstallApps
```

Wait for it to finish.

Your phone is now rooted.
```
adb shell                                                                                                                                                                                                                        
generic_x86_arm:/ $ su root
generic_x86_arm:/ # whoami
root
```
<img src="/images/rooted.png" alt="Rooted" width="300px"/>

In order to intercept traffic and get Frida installed, you need to install a few Magisk modules.
 Here are some options:
  - [Magisk Trust User Certs](https://github.com/NVISOsecurity/MagiskTrustUserCerts)
  - [MagiskFrida](https://github.com/ViRb3/magisk-frida)

  With this setup, you can begin conducting your security assessment.

  Thank you and see you next time
