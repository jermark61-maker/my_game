[app]

# (str) Title of your application
title = My Game

# (str) Package name
package.name = mygame

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source files where the .py files reside
source.dir = .

# (list) Source files to include (let it empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (int) Android API to use
android.api = 33

# (int) Min API your APK will support
android.minapi = 21

# Android SDK version
android.sdk = 33

# Android NDK version
android.ndk = 25b

# (int) Fullscreen mode
fullscreen = 0
