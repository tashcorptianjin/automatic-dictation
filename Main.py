import pyttsx3 as pt
import time

engine = pt.init()
voc_list = []
def voc_read(voc_list=voc_list):
    
    for temp in voc_list:
        pt.speak(temp)
        sure = input('下一个回车')
def get_voc():
    run = True
    voc_list.clear()
    print('已进入单词输入模式，按Q退出')
    while run:
        temp = input('输入单词: ')
        if temp == 'Q':
            print('已退出单词更改模式')
            break
        else:
            voc_list.append(temp)
def speed_change(speed):
    speed=float(speed)
    rate = engine.getProperty('rate')   
    engine.setProperty('rate', speed)
def change_voc():
    for i in voc_list:
        print(voc_list.index(i)+1,i)
    num = int(input('请输入编号：'))
    temp = input('修改后的内容是：')
    voc_list[num-1] = temp
    
print('欢迎使用阿尔茨海默默写机制')
while True:
    mode = input('a.单词输入模式 b.朗读模式 c.单词修正模式 d.语速更改模式')
    if mode == 'a':
        get_voc()
    elif mode == 'b':
        for i in range(50):
            print('\n')
        voc_read()
        
        print('结束朗读')
    elif mode=='c':
        change_voc()
    elif mode == 'd':
        speed = float(input('请输入速度(默认200)'))
        speed_change(speed)
    
