pyinstaller .\backend\app.py -F --add-data=".\backend\img\logo.ico:img"
pyinstaller .\backend\main.py -F --add-binary=".\dist\app.exe:bin" -i ".\backend\img\logo.ico"