# 获取路径
import os, sys
def getPath(filename):
    # 方法一（如果要将资源文件打包到app中，使用此法）
    bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
    path = os.path.join(bundle_dir, filename)
    # 方法二获取路径可以，但如果打包资源好像不行。
    # path = os.path.join(os.path.dirname(sys.argv[0]), filename)
    return path