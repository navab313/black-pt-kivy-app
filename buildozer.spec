[app]

title = Grade Predictor
package.name = gradepredictor
package.domain = ir.mycompany
version = 1.0.0

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,ttf,ttc,otf
source.include_dirs = fonts,data

icon.filename = data/icon.png
presplash.filename = data/splash.png

requirements = python3==3.10.9,kivy==2.3.0,arabic-reshaper,python-bidi,pillow

android.permissions = INTERNET,ACCESS_NETWORK_STATE
android.api = 33
android.minapi = 21
android.maxapi = 33
android.archs = arm64-v8a
android.ndk = 25b
android.build_tools = 34.0.0
p4a.bootstrap = sdl2
android.accept_sdk_license = True
orientation = portrait
fullscreen = 0

log_level = 2
warn_on_root = 1
bin_dir = ./bin

[buildozer]
log_level = 2
