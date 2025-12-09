[app]
title = Grade Predictor
package.name = gradepredictor
package.domain = ir.mycompany
version = 1.0.0
main.py = main.py

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,ttf,ttc,otf,txt
source.include_dirs = fonts,data

icon.filename = data/icon.png
presplash.filename = data/splash.png

requirements = python3,kivy==2.3.0,arabic-reshaper,python-bidi,Pillow

android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.archs = arm64-v8a
android.ndk = 25b
p4a.bootstrap = sdl2
orientation = portrait
fullscreen = 0
android.accept_sdk_license = True

log_level = 2
warn_on_root = 1

[buildozer]
log_level = 2
