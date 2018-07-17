import easygui as f
import sys

while 1:
    f.msgbox("欢迎进入游戏界面")
    
    msg = "请问你想学什么呢？"
    title = "小游戏互动"
    choices = ["篮球","足球","乒乓球","网球"]

    choice = f.choicebox(msg,title,choices)

    f.msgbox("您的选择是："+str(choice),"结果")
    msg = "您希望重新开始吗？"
    title = "请选择"
    if f.ccbox(msg,title):
        pass
    else:
        sys.exit(0)
