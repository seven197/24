[app]

title = Roguelike Survival
package.name = roguelikesurvival
package.domain = org.roguegame
source.dir = .
version = 0.1
source.include_exts = py,png,jpg,kv,atlas
source.ignore_exts = pyc,pyo
requirements = python3,kivy==2.3.0
orientation = landscape
fullscreen = 1
android.api = 33
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a
android.build_mode = debug
android.permissions = INTERNET
android.logcat_filters = *:S python:D
android.copy_libs = 1
android.buildtools = 33.0.2
android.ndk = 25b
android.ndk_api = 21
android.sdk = 33
android.use_aapt2 = True
android.add_assets = assets/
android.enable_androidx = True
p4a.source_dir = ~/.buildozer/android/platform/python-for-android
p4a.bootstrap = sdl2
p4a.local_recipes =
p4a.libSDL2_ttf = True
