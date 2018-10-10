from tkinter import *
import pymysql
import tkinter
import easygui
import tkinter.messagebox
import random
import threading
import socket
import time
import  os
import  datetime

conn=pymysql.connect(host="localhost",port=3306,
                         user="root",password="admin123456",
                         database="guangbo",charset="utf8")
cur=conn.cursor()

def teacherlogin():
    window = tkinter.Tk()
    window.geometry("450x300+550+200")
    window.title(" 电子教务系统 ")
    label = tkinter.Label(window, bg="ivory", width=1300, height=700).pack()
    label = tkinter.Label(window, text="教师登陆入口",bg="ivory", font=("宋体", 20))  # 信息框
    label.place(x=100, y=25, width=200, height=60)

    text_id=tkinter.Label(window,text="教师编号:",bg="ivory",anchor="e",font=("仿宋",18))
    text_id.place(x=20,y=100,width=130,height=30)
    identry=tkinter.Entry(window,font=("仿宋",16))
    identry.place(x=150,y=100,width=230,height=30)
    text_name=tkinter.Label(window,text="教师姓名:",bg="ivory",anchor="e",font=("仿宋",18))
    text_name.place(x=20,y=150,width=130,height=30)
    nameentry = tkinter.Entry(window, font=("仿宋", 16))
    nameentry.place(x=150, y=150, width=230, height=30)
    n=0
    def panduan(cur):
        global n
        id=identry.get()
        name=nameentry.get()
        sql = " select Tname from teacher    where Tid=%s      "
        cur.execute(sql,id)
        data=cur.fetchall()

        print(data)
        if  name in str(data):
            window.destroy()
            jiaoshiduan()
            return 1
        else:
            easygui.msgbox("输入错误","错误信息",image=r"C:\Users\Administrator\Desktop\teacher端\bomb-1.gif")
            return 0
    sure = tkinter.Button(window,text="登录",command=lambda:panduan(cur) )
    sure.place(x=300,y=200,width=70,height=40)
    window.mainloop()
    return panduan

def jiaoshiduan():
    tk2=Tk()
    tk2.title('教师端')#窗口名称
    tk2.geometry('700x550+450+100')
    tk2.attributes("-alpha", 0.85)#透明度
    tk2.iconbitmap(r'C:\Users\Administrator\Desktop\1.ico')
    label3 = Label(tk2, bg="ivory")
    label3.place(width=700, height=550)
    label2 = Label(tk2, bg="ivory", font=('宋体', 500), text='c')
    label2.place(width=500, height=500, x=100, y=-90)
    label4 = Label(tk2, bg="ivory", font=('草书', 15), text='载入中……')
    label4.place(width=100, height=50, x=500, y=450)
    label5 = Label(tk2, bg="ivory", font=('宋体', 20), text='作者:刘方园，陈宇，曹悦，余卓')
    label5.place(width=500, height=40, x=100, y=400)

    tk2.update()
    time.sleep(2)
    # tk=Frame(height=700,width=1300,bg='ivory').pack(expand=YES,fill=BOTH)
    l3 = Label(tk2,bg="ivory",width=1300,height=700).pack()#背景色
    # tk.iconbitmap('spider_128px_1169260_easyicon.net.ico')
    one1=Button(tk2 ,text='开始签到',font=('times',20),bg='lavender',command=Tqiandao)#第一个功能栏
    one1.place(x=550, y=30, width=120, height=60)
    two1=Button(tk2 ,text='收作业',font=('times',20),bg='lavender',command=workstart)#第二个功能栏
    two1.place(x=550, y=110, width=120, height=60)
    three1=Button(tk2 ,text='开始考试',font=('times',20),bg='lavender',command=examteacher)#第三个功能栏
    three1.place(x=550, y=190, width=120, height=60)
    four1=Button(tk2,text='随机提问',font=('times',20),bg='lavender',command=Rname)#第四个功能栏
    four1.place(x=550, y=270, width=120, height=60)
    five1=Button(tk2,text='查询学生',font=('times',20),bg='lavender',command=chaxun)#第五个功能栏
    five1.place(x=550, y=350, width=120, height=60)
    qu=Button(tk2,text='退出',font=('times',20),bg='lavender',command=lambda:tuichu(tk2))#退出功能栏
    qu.place(x=550, y=430, width=120, height=60)
    fa=Button(tk2,text='发送',font=('times',20),bg='lavender')#发送消息功能栏
    fa.place(x=420, y=450, width=90, height=45)
    l4 = Label(tk2,bg="aliceblue",width=30,height=2,font=("宋体",20))#信息框
    l4.place(x=40,y=25,width=470,height=400)
    ent=Entry(tk2,width=80)#输入框
    ent.place(x=40,y=450,width=360,height=45)
    tk2.mainloop()

def Tqiandao():
    iplist=[]
    def run(s,addr):
        while True:
            data=s.recv(1024).decode("utf-8")
            print(data)
            id,name=data.split(" ")
            sql="select sname from student where sid=%s"
            row1=cur.execute(sql,(id))
            if row1==0:
                s.send("notmath".encode("utf-8"))
            else:
                if cur.fetchone()[0]!=name:
                    s.send("notmath".encode("utf-8"))
                else:
                    if addr[0] in iplist:
                        s.send("repeat1".encode("utf-8"))
                    else:
                        sql1 = "select time from checktable where sid=%s"
                        cur.execute(sql1, (id))
                        today =str(datetime.date.today())  #今天的日期
                        sqltime=cur.fetchone()[0]          #数据库的最后一次签到日期
                        print(today)
                        print(sqltime)
                        print(type(today))
                        print(type(sqltime))
                        if today==sqltime:
                           s.send("day".encode("utf-8"))
                        else:
                            iplist.append(addr[0])
                            sql2 = "update checktable set time=CURDATE() where sid=%s"
                            cur.execute(sql2, (id))
                            conn.commit()
                            sql3="update checktable set score1=score1+5 where sid=%s"
                            cur.execute(sql3,(id))
                            conn.commit()
                            s.send("success".encode("utf-8"))
    def work():
        global  s,addr
        global  server
        server = socket.socket()
        server.bind(('192.168.10.142', 6666))
        server.listen(100)
        while True:
            s,addr=server.accept()
            iplist.append(s)

    def teachermain():
        tk = tkinter.Toplevel()
        tk.title("签到窗口")
        start=tkinter.Button(tk,text="开始签到",bg="lightblue",command=lambda:run(s,addr))
        start.place(x=20,y=20,width=100,height=20)
        end = tkinter.Button(tk,text="结束签到",bg="lightblue",command=tk.destroy)
        end.place(x=20,y=60,width=100,height=20)
        tk.mainloop()
    if __name__=="__main__":
        threading.Thread(target=teachermain).start()
        threading.Thread(target=work).start()
def workstart():
    threading.Thread(target=worktea).start()
def worktea():#收作业
    server = socket.socket()
    server.bind(('192.168.10.142', 7777))
    server.listen(100)

    def run(s):
        filename = s.recv(1024).decode("utf-8").split("/")[-1]
        file = open(r"D:\新建文件夹" + "\\" + filename, "wb")
        while True:
            data = s.recv(1024)
            if data == b"":
                break
            else:
                file.write(data)

    while True:
        s, addr = server.accept()
        threading.Thread(target=run, args=(s,)).start()
def examteacher():
    slist = []

    def start():
        for ss in slist:
            ss.send("start".encode("utf-8"))

    def teachermain():
        app = tkinter.Tk()
        b = tkinter.Button(app, text="开始考试", command=start)
        b.place
        app.mainloop()

    def teacherlisten():
        server = socket.socket()
        server.bind(('192.168.10.142', 8888))
        server.listen(100)

        def run(s):
            pass

        while True:
            s, add = server.accept()
            threading.Thread(target=run, args=(s,)).start()

    if __name__ == "__main__":
        threading.Thread(target=teachermain).start()
        threading.Thread(target=teacherlisten).start()

def tuichu(tk2):
    tk2.destroy()

def Rname():
        app=tkinter.Tk()
        app.title("在线随机提问页面")
        app.geometry("200x200")
        b = tkinter.Button(app, text="看看谁中奖", command=Run)
        b.place(x=50, y=50, width=100, height=50)
        app.mainloop()
def Run():
        sql1="SELECT COUNT(sid) FROM student"
        cur.execute(sql1)
        count=cur.fetchone()[0]
        id=random.randint(1,count)
        print(id)
        sql2="select sname from student where sid=%s "
        cur.execute(sql2,(id))
        name=cur.fetchone()[0]
        print(name)
        tkinter.messagebox.showinfo("提问", "请"+name+"同学回答")
def chaxun():
    app=tkinter.Tk()
    app.title("在线考试平台")
    app.geometry("500x350+550+200")
    label1 = tkinter.Label(app, bg="ivory", width=1300, height=700).pack()
    varPwd = tkinter.StringVar()
    varPwd.set('')
    def select1():
        sid2=b2.get()
        sql8 = "select * from student where sid=%s "
        cur.execute(sql8, (sid2))
        sqlname2 = str(cur.fetchall()[0])
        tkinter.messagebox.showinfo("已查询", "你的信息为:" +sqlname2)
        print(sqlname2)
    def select2():
        sid3 = b2.get()
        sql9 = "select gread from stg where sid=%s "
        cur.execute(sql9, (sid3))
        sqlname3 = str(cur.fetchall()[0])
        tkinter.messagebox.showinfo("已查询", "你的分数为:" + sqlname3)
    b1=Label(app, bg="aliceblue",text='请输入学生的学号:',font=('宋体',17))
    b1.place(x=80,y=70,height=30,width=170)
    b2=tkinter.Entry(app, textvariable=varPwd)
    b2.place(x=250,y=70,height=30,width=150)
    b3=tkinter.Button(app,text="查询学生信息",command=select1)
    b3.place(x=100,y=200,height=50,width=100)
    b4=tkinter.Button(app,text="查询学生期末成绩",command=select2)
    b4.place(x=300,y=200,height=50,width=100)
    app.mainloop()
if __name__ == "__main__":
    threading.Thread(target=teacherlogin).start()
