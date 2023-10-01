import ctypes
import os
import subprocess
from utils import getPath

# 调用Win32 API函数来隐藏窗口
def hide_console():
    kernel32 = ctypes.WinDLL('kernel32')
    user32 = ctypes.WinDLL('user32')
    SW_HIDE = 0
    hWnd = kernel32.GetConsoleWindow()
    user32.ShowWindow(hWnd, SW_HIDE)

if __name__ == '__main__':
    hide_console()
    # subprocess.Popen
    p = subprocess.Popen([os.path.join(getPath("bin"), '.\\app.exe')], cwd='.', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    code = p.wait()
    exit(code)