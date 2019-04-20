# -*- coding: utf-8 -*-
from tkinter import *
import os
import datetime
import tkinter.messagebox


def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)

# 写新本子


def save_data():
    now = datetime.datetime.now()
    try:
        fileD = open("note/"+str(depot.get())+".txt", "a",encoding="utf-8")
        fileD.write("时间: "+now.strftime("%Y-%m-%d %H:%M:%S")+"\n")
        fileD.write("本本: %s\n" % depot.get())
        # fileD.write("%s\n"%depot.get())
        fileD.write("主题: %s\n" % description.get())
        # fileD.write("%s\n"%description.get())
        # fileD.write("内容:\n")
        fileD.write("内容：%s\n" % address.get("1.0", END))
        depot.set("默认")
        description.delete(0, END)
        address.delete("1.0", END)
    except Exception as ex:
        tkinter.messagebox.showerror("警告","发生错误:\n%s"%ex)


def read_depots(file):
    depots = []
    depots_t = open(file,encoding='utf-8')
    for line in depots_t:
        depots.append(line.rstrip())
    return depots

# 新窗口


def create():
    top = Toplevel()
    top.title('新本本')
    v1 = StringVar()
    Label(top, text='名字').grid(row=1, column=0, padx=1, pady=1)
    e1 = Entry(top, textvariable=v1, width=10)
    e1.grid(row=1, column=1, padx=1, pady=1)

    def mknote():
        folder = os.path.exists("note/"+e1.get()+".txt")
        if not folder:
            try:
                a = open("note/type.txt", mode="a+",encoding="utf-8")
                a.write(e1.get()+"\n")
                tkinter.messagebox.showinfo("提示","新本本已建好，重启小语后生效")
            except Exception as ex:
                tkinter.messagebox.showerror("警告","发生错误:\n%s"%ex)
        else:
            tkinter.messagebox.showinfo("提示","已经有这个本子了哦！")
    Button(top, text='确定', command=mknote).grid(
        row=1, column=2, padx=1, pady=1)


# 建立笔记文件夹
mkdir("note")
# 写入默认笔记类型
'''
file_type = open("note/type.txt", encoding="utf-8")
for line in file_type:
    if line == "Web":
        file_type.close()
    else:
        file_type.close()
        fi=open("note/type.txt",mode="w")
        fi.write('Web\nLinux\nDatabase\nLanguage\n')
        fi.close()
'''
folder = os.path.exists("note/type.txt")
if not folder:
    #os.makedirs("note/type.txt")
    er=open('note/type.txt','w',encoding="utf-8")
    er.write("默认\n")
    er.close()
'''
size = os.path.getsize('note/type.txt')
if size == 0:
    fi = open("note/type.txt", mode="w")
    fi.write('默认')
    fi.close()
'''
# 建GUI界面
app = Tk()
app.title('风语')
Label(app, text="本本:").pack(side='top', padx=10, pady=10)
#Label(app, text="门类:").grid(row=1, column=0, padx=1, pady=1)
depot = StringVar()
depot.set("默认")
options = read_depots("note/type.txt")
OptionMenu(app, depot, *options).pack(side='top')
#OptionMenu(app, depot, *options).grid(row=1, column=1, padx=1, pady=1)
Label(app, text="主题:").pack(side='top')
description = Entry(app)
description.pack(side='top')
Label(app, text="内容:").pack()
address = Text(app)
address.pack()
Button(app, text="保存", command=save_data).pack()
Button(app, text='我要建一个新本本', command=create).pack()
app.mainloop()