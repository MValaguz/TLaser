echo on
rmdir build /S /Q
rmdir dist /S /Q
pyinstaller TLaser.py
rmdir build /S /Q
