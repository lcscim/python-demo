import os
import re

'获取手机屏幕大小'
size_str = os.popen('adb shell wm size').read()
if not size_str:
    print('请安装 ADB 及驱动并配置环境变量')
    sys.exit()
m = re.search(r'(\d+)x(\d+)', size_str)
if m:
    print(m)
