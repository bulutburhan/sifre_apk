[app]

title = ZeusPass
package.name = zeuspass
package.domain = org.burhan
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,qrcode,Pillow,openssl,cython,setuptools,six
orientation = portrait
osx.python_version = 3
fullscreen = 1

[buildozer]

log_level = 2
warn_on_root = 1

[app.android]

android.api = 31
android.minapi = 21
android.ndk = 25b
android.build_tools_version = 34.0.0
android.ndk_api = 21
android.accept_sdk_license = True
# Eğer ikon eklemek istersen:
# icon.filename = icon.png

[app.android.permissions]

# Gerekli özel izin yok, boş bırakılabilir

[app.android.ndk]

# NDK ayarları özel olarak gerekmez, boş bırakılabilir

[app.android.gradle_dependencies]

# Gerekli bir şey yok, boş bırakılabilir

[app.android.requirements]

# requirements zaten üstte tanımlandı, ekstra gerek yok
