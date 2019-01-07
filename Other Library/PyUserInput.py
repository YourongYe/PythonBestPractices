from pykeyboard import PyKeyboard
from pymouse import PyMouse

# 初始化
k = PyKeyboard()
m = PyMouse()

# 组合键保存
k.press_keys(['Command','s']) 

# ----------------以下均为在窗口中的实现---------------- #

# 组合键选桌面desktop
k.press_keys(['Command','d'])

# 组合键open
k.press_keys(['Command','o'])

# 组合键选模式1
k.press_keys(['Command','1'])

# ----------------以上均为在窗口中的实现---------------- #

# 输入框内打字 （不能打中文）
k.type_string('2019-01-10',interval=0.2) # interval是sleep的时间（s）

# 按回车
k.press_keys(['Return'])

# 鼠标点击对应的坐标位置
m.click(465, 195, button=1, n=1) 
# button=1: 左键，button=2:右键
# n=1:点击一下，n=2:点击两下
