import pyttsx3 as pt
import time
import tkinter as tk
import pygame
import pypinyin
from tkinter.messagebox import showinfo

#BGM为卡农
pygame.init()
pygame.mixer.init()
engine = pt.init()
voc_list = []
pygame.mixer.music.load('mus.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)
#init
root = tk.Tk()
root.geometry('800x510')
root.title('阿尔茨海默自主默写 (V2.0.0Release)')
root.iconbitmap('./logo.ico') 
tk.Label(root,text='阿尔茨海默自主默写软件',font=('楷体',30)).pack()

en1 = tk.Entry(root,font=('楷体',20))
en1.place(x=10,y=65)
f=open('save.txt','r+')
def get_voc():
    
    temp = en1.get()
    voc_list.append(temp)

    en1.delete(0,tk.END)
    tex = str(len(voc_list))+'：'+temp+'\n'
    
    
    text.insert(tk.INSERT,tex)
sort = [0,True,True]

def reset_read():
    sort[0] = 0
disvar=tk.StringVar()
disvar.set('祝贺1号客户王志浩生日快乐！')
def voc_read(sort=sort,voc_list=voc_list,need=voc_list):
    text.delete(0.0,tk.END)
    if sort[2]:
        temp = voc_list[sort[0]]
        pt.speak(temp)
    if sort[1]:
        t = pypinyin.lazy_pinyin(need[sort[0]],style=pypinyin.Style.TONE)
        print(t)
        disvar.set('')
        disvar.set(t)
    sort[0]+=1
def change_pinyin(sort=sort):
    sort[1]= not sort[1]
    disvar.set('')
    text.insert(tk.INSERT,'拼音打开状态:'+str(sort[1])+'\n')    
def change_langdu(sort=sort):
    sort[2]= not sort[2]
    text.insert(tk.INSERT,'朗读打开状态:'+str(sort[2])+'\n')        
def before():
    sort[0]-=2
def pardon(sort=sort,voc_list=voc_list):
    temp = voc_list[sort[0]-1]
    pt.speak(temp)
def reset_voc():
    voc_list.clear()
    text.delete(0.0,tk.END)
    text.insert(tk.INSERT,'列表清除完毕\n')
    
def speed_change():
    
    speed=int(en2.get())
    rate = engine.getProperty('rate')   
    engine.setProperty('rate', speed)
    text.insert(tk.INSERT,'语速已更改为'+str(speed)+'\n')
    en2.delete(0,tk.END)
tip = '保存文件注意事项：\n1.请不要删除文件夹内的save.txt\n2.文件会导出路径为save.txt\n3.保存后不可立即调用，请重启程序\n4.如需将默写内容导出，请访问程序路径下save.txt\n如果您已经做到上述内容，请忽略'
def save_voc():
    result = showinfo('提示', tip)
    f.seek(0)
    f.truncate()
    for i in voc_list:
        f.writelines(i+'\n')
    text.insert(tk.INSERT,'保存成功\n')
def imp_voc():
    result = showinfo('提示',tip)
    temp = f.read().splitlines()
    voc_list.clear()
    for i in temp:
        voc_list.append(i)
    text.insert(tk.INSERT,'导入成功\n')
        
    


tk.Label(root,text = '调整语速(默认200字每分)',font=('楷体',15)).place(x=1,y=200)
en2 = tk.Entry(root)
en2.place(x=5,y=225)
button  = tk.Button(root,text='录入/下一个',font = ('楷体',20),command=get_voc)
button.place(x=10,y=100)
scrollbar = tk.Scrollbar(root)
scrollbar.place(x=780,y=50)
text = tk.Text(root,height=17,width=20,font=('楷体',15),yscrollcommand=scrollbar.set,wrap=tk.NONE)
text.place(x=560,y=50)
#text.insert()
def change_voc():
    text.delete(0.0,tk.END)
    ind = int(en3.get())-1
    wor = en4.get()
    voc_list[ind]=wor
    en3.delete(0,tk.END)
    en4.delete(0,tk.END)
    for i  in range(len(voc_list)):
        tex = str(i+1)+'：'+voc_list[i]+'\n'
        text.insert(tk.INSERT,tex)
def pause():
    pygame.mixer.music.pause()
def unpause():
    pygame.mixer.music.unpause()        
def get_text(need=voc_list):
    result_list=[]
    for i in need:
        result=pinyin(i,style=Style.TONE)
        result_list_temp=[]
        for i in result:
            result_list_temp.append(i[0])
        result_list.append(result_list_temp)
    print(result_list)
    for j in result_list:
        for k in j:
            dis.insert(tk.INSERT,k+' ')
        dis.insert(tk.INSERT,' , ')
            
tk.Label(root,text = '修改词语',font=('楷体',15)).place(x=350,y=250)
tk.Label(root,text = '索引',font=('楷体',15)).place(x=450,y=275)
tk.Label(root,text = '改为',font=('楷体',15)).place(x=450,y=300)
en3 = tk.Entry(root)
en3.place(x=300,y=275)
en4 = tk.Entry(root)
en4.place(x=300,y=300)
dis=tk.Entry(root,font=('Times New Roman',30),width=25,textvariable=disvar).place(x=10,y=440)

button2 = tk.Button(root,text='一键默写',font=('楷体',20),command=voc_read).pack()
button3 = tk.Button(root,text='清除录入内容',font=('楷体',20),command=reset_voc).place(x=10,y=150)
button4 = tk.Button(root,text='重置默写朗读',font=('楷体',20),command=reset_read).pack()
button5 = tk.Button(root,text='确定语速',font=('楷体',20),command=speed_change).place(x=5,y=250)
button6 = tk.Button(root,text='重复',font=('楷体',20),command=pardon).pack()
button7 = tk.Button(root,text='上一个(再按一键默写)',font=('楷体',15),command=before).pack()
button8 = tk.Button(root,text='从文件导入',font=('楷体',20),command=imp_voc).place(x=5,y=300)
button9 = tk.Button(root,text='导出到文件',font=('楷体',20),command=save_voc).place(x=5,y=350)
button10 = tk.Button(root,text='暂停音乐',font=('楷体',20),command=pause).place(x=600,y=400)
button11 = tk.Button(root,text='播放音乐',font=('楷体',20),command=unpause).place(x=600,y=450)
button12 = tk.Button(root,text='设置词语',font=('楷体',20),command=change_voc).place(x=300,y=330)
button13 = tk.Button(root,text='开/关拼音',font=('楷体',15),command=change_pinyin).place(x=10,y=400)
button14 = tk.Button(root,text='开/关朗读',font=('楷体',15),command=change_langdu).place(x=180,y=400)
root.mainloop()
pygame.mixer.music.fadeout(1000)
pygame.mixer.music.unload()
f.close()


    
