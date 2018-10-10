from tkinter import *
import pymysql
import tkinter
import easygui
import tkinter.messagebox
import random
import threading
import socket
import os
import time
conn=pymysql.connect(host="localhost",port=3306,
                         user="root",password="admin123456",
                         database="guangbo",charset="utf8")
cur=conn.cursor()

# def check():
#     tk1=Tk()
#     tk1.title(" 电子教务系统")#窗口名称
#     tk1.geometry("450x300+550+200")
#     l1 = Label(tk1,bg="ivory",width=1300,height=700).pack()#背景色
#     tk1.iconbitmap(r'C:\Users\Administrator\Desktop\1.ico')
#     b1=Button(tk1 ,text='学生端',font=('宋体',20),command=studentlogin)#第一个功能栏
#     b1.place(x=80, y=120, width=120, height=60)
#     b2=Button(tk1 ,text='教师端',font=('宋体',20),command=teacherlogin)#第二个功能栏
#     b2.place(x=250, y=120, width=120, height=60)
#     tk1.mainloop()
def studentlogin():
    window = tkinter.Tk()
    window.geometry("450x300+550+200")
    window.title(" 软帝电子教务系统    作者：刘方园，陈宇，曹悦，余卓")
    l2 = tkinter.Label(window, bg="ivory", width=1300, height=700).pack()
    l2 = tkinter.Label(window, text="学生登录入口", bg="ivory", font=("宋体", 20))  # 信息框
    l2.place(x=100, y=25, width=200, height=60)

    text_id = tkinter.Label(window, text="学生编号:", bg="ivory", anchor="e", font=("仿宋", 18))
    text_id.place(x=20, y=100, width=130, height=30)
    identry = tkinter.Entry(window, font=("仿宋", 16))
    identry.place(x=150, y=100, width=230, height=30)
    text_name = tkinter.Label(window, text="学生姓名:", bg="ivory", anchor="e", font=("仿宋", 18))
    text_name.place(x=20, y=150, width=130, height=30)
    nameentry = tkinter.Entry(window, font=("仿宋", 16))
    nameentry.place(x=150, y=150, width=230, height=30)
    sid=10
    global  sid10
    def panduan():
        global sid10
        sid10 = identry.get()
        name = nameentry.get()
        sql = "select sname from student where sid=%s "
        cur.execute(sql,(sid10))
        sqlname=str(cur.fetchone()[0])
        if sqlname==name:
            window.destroy()
            xueshengduan()
        else:
            easygui.msgbox("输入有误！", "错误信息")

    sure = tkinter.Button(window, text="登录", command=panduan)
    sure.place(x=300, y=200, width=70, height=40)
    window.mainloop()

def xueshengduan():
    tk2=Tk()
    tk2.title('学生端')#窗口名称
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
    one1=Button(tk2 ,text='在线签到',font=('times',20),bg='lavender',command=Sqiandao)#第一个功能栏
    one1.place(x=550, y=30, width=120, height=60)
    two1=Button(tk2 ,text='上交作业',font=('times',20),bg='lavender',command=workstu)#第二个功能栏
    two1.place(x=550, y=110, width=120, height=60)
    three1=Button(tk2 ,text='考试',font=('times',20),bg='lavender',command=exam)#第三个功能栏
    three1.place(x=550, y=190, width=120, height=60)
    four1=Button(tk2,text='自测',font=('times',20),bg='lavender',command=zice)#第四个功能栏
    four1.place(x=550, y=270, width=120, height=60)
    five1=Button(tk2,text='查询信息',font=('times',20),bg='lavender',command=chaxun)#第五个功能栏
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

def zice():
        app =tkinter.Toplevel()
        app.title("在线自测平台")
        app.geometry('700x550+450+100')
        label = Label(app, bg="ivory", width=1300, height=700).pack()
        var = StringVar()
        var1 = StringVar()
        vara = StringVar()
        varb = StringVar()
        varc = StringVar()
        vard = StringVar()
        q = 0

        def select():
            nonlocal q
            sql1 = "SELECT COUNT(id) FROM test"
            cur.execute(sql1)
            count = cur.fetchone()[0]
            q = random.randint(1, count)
            sql4 = "SELECT a FROM test where id=%s"
            cur.execute(sql4, (q))
            aaa = cur.fetchone()[0]
            sql5 = "SELECT b FROM test where id=%s"
            cur.execute(sql5, (q))
            bbb = cur.fetchone()[0]
            sql6 = "SELECT c FROM test where id=%s"
            cur.execute(sql6, (q))
            ccc = cur.fetchone()[0]
            sql7 = "SELECT d FROM test where id=%s"
            cur.execute(sql7, (q))
            ddd = cur.fetchone()[0]
            sql2 = "select question from test where id=%s "
            cur.execute(sql2, (q))
            qusetion = cur.fetchone()[0]
            var.set(qusetion)
            vara.set(aaa)
            varb.set(bbb)
            varc.set(ccc)
            vard.set(ddd)

        def ask():
            a = var1.get()
            sql3 = "select answer from test where id=%s"
            cur.execute(sql3, (q))
            b = cur.fetchone()[0]
            if a == b:
                tkinter.messagebox.showinfo("恭喜", "回答正确")
            else:
                tkinter.messagebox.showerror("遗憾", "回答错误,正确答案为" + b)

        lq = tkinter.Label(app, textvariable=var, font=("楷体", 20))
        lq.place(x=100, y=50, height=150, width=500)
        la = tkinter.Label(app, textvariable=vara)
        la.place(x=140, y=250, height=25, width=460)
        lb = tkinter.Label(app, textvariable=varb)
        lb.place(x=140, y=300, height=25, width=460)
        lc = tkinter.Label(app, textvariable=varc)
        lc.place(x=140, y=350, height=25, width=460)
        ld = tkinter.Label(app, textvariable=vard)
        ld.place(x=140, y=400, height=25, width=460)
        ra = tkinter.Radiobutton(app, text="A:", variable=var1, value="A")
        ra.place(x=100, y=250)
        rb = tkinter.Radiobutton(app, text="B:", variable=var1, value="B")
        rb.place(x=100, y=300)
        rc = tkinter.Radiobutton(app, text="C:", variable=var1, value="C")
        rc.place(x=100, y=350)
        rd = tkinter.Radiobutton(app, text="D:", variable=var1, value="D")
        rd.place(x=100, y=400)

        ba = tkinter.Button(app, text="随机做题", command=lambda: select())
        ba.place(x=150, y=480, height=30, width=100)
        bb = tkinter.Button(app, text="提交答案", command=lambda: ask())
        bb.place(x=450, y=480, height=30, width=100)
        app.mainloop()

def Sqiandao():
    app=tkinter.Toplevel()
    app.title("学生平台")
    app.geometry("200x200")

    idlabel=tkinter.Label(app,text="学号:",width=80)
    idlabel.place(x=10,y=5,width=80,height=20)
    identry=tkinter.Entry(app,width=80)
    identry.place(x=100,y=5,width=80,height=20)

    namelabel=tkinter.Label(app,text="姓名:",width=80)
    namelabel.place(x=10,y=30,width=80,height=20)
    nameentry=tkinter.Entry(app,width=80)
    nameentry.place(x=100,y=30,width=80,height=20)

    s=socket.socket()
    s.connect(('192.168.10.142',6666))
    def check():
            id=identry.get()
            name=nameentry.get()
            print(id+name)
            s.send((id+" "+name).encode("utf-8"))
            mess=s.recv(1024).decode("utf-8")
            if mess=="notmath":
                tkinter.messagebox.showerror("失败","学号或者姓名输入错误")
            elif mess=="repeat1":
                tkinter.messagebox.showerror("失败","不允许重复签到")
            elif mess=="day":
                tkinter.messagebox.showerror("失败","一天只能签到一次")
            elif mess=="success":
                tkinter.messagebox.showinfo("恭喜","签到成功")


    b=tkinter.Button(app,text="签到",command=check)
    b.place(x=60,y=80,width=80,height=20)

    app.mainloop()
def workstu():
    app = tkinter.Tk()
    app.title("学生平台")
    app.geometry("200x200")

    def fileupload():
        s = socket.socket()
        s.connect(('192.168.10.142', 7777))
        filename = tkinter.filedialog.askopenfilename(title="请选择要导入的文件")
        s.send(filename.encode("utf-8"))
        file = open(filename, "rb")
        while True:
            data = file.read(1024)
            s.send(data)
            if data == b'':
                break
        file.close()
        s.close()

    b = tkinter.Button(app, text="导入文件", command=fileupload)
    b.place(x=40, y=40, height=80, width=100)
    app.mainloop()
def exam():
    s=socket.socket()
    s.connect(('192.168.10.142',8888))
    app=tkinter.Toplevel()
    app.title("在线考试平台")
    app.geometry("800x600")
    var=StringVar()
    var1=StringVar()
    vara=StringVar()
    varb=StringVar()
    varc=StringVar()
    vard=StringVar()
    count=0
    conn=pymysql.connect(host="localhost",port=3306,
                         user="root",password="admin123456",
                         database="guangbo",charset="utf8")
    cur=conn.cursor()

    def start():
        global id
        id=1
        sql1="select question from test where id=%s "
        cur.execute(sql1,(id))
        qusetion = cur.fetchone()[0]
        sql4 = "SELECT a FROM test where id=%s"
        cur.execute(sql4, (id))
        aaa = cur.fetchone()[0]
        sql5 = "SELECT b FROM test where id=%s"
        cur.execute(sql5, (id))
        bbb = cur.fetchone()[0]
        sql6 = "SELECT c FROM test where id=%s"
        cur.execute(sql6, (id))
        ccc = cur.fetchone()[0]
        sql7 = "SELECT d FROM test where id=%s"
        cur.execute(sql7, (id))
        ddd = cur.fetchone()[0]
        var.set(qusetion)
        vara.set(aaa)
        varb.set(bbb)
        varc.set(ccc)
        vard.set(ddd)
    def down():
        global id
        sql1 = "SELECT COUNT(id) FROM test"
        cur.execute(sql1)
        allid = cur.fetchone()[0]
        if int(id)<int(allid):
            id=id+1
            sql2 = "select question from test where id=%s "
            cur.execute(sql2, (id))
            qusetion = cur.fetchone()[0]
            sql4 = "SELECT a FROM test where id=%s"
            cur.execute(sql4, (id))
            aaa = cur.fetchone()[0]
            sql5 = "SELECT b FROM test where id=%s"
            cur.execute(sql5, (id))
            bbb = cur.fetchone()[0]
            sql6 = "SELECT c FROM test where id=%s"
            cur.execute(sql6, (id))
            ccc = cur.fetchone()[0]
            sql7 = "SELECT d FROM test where id=%s"
            cur.execute(sql7, (id))
            ddd = cur.fetchone()[0]
            var.set(qusetion)
            vara.set(aaa)
            varb.set(bbb)
            varc.set(ccc)
            vard.set(ddd)

        else:
            sql10 = "update checktable set score2=score2+5 where sid=%s"
            cur.execute(sql10, (id))
            conn.commit()
            app.destroy()
            tkinter.messagebox.showinfo("幸苦了","考试结束,您的分数为"+str(count))
    def sorce():
        nonlocal  count
        a = var1.get()
        sql3 = "select Answer from test where id=%s"
        cur.execute(sql3, (id))
        b = cur.fetchone()[0]
        if a == b:
            tkinter.messagebox.showinfo("恭喜", "回答正确")
            count=count+5
            sql10="update checktable set score2=score2+5 where sid=%s"
            cur.execute(sql10,(sid10))
            conn.commit()
        else:
            tkinter.messagebox.showerror("遗憾", "回答错误,正确答案为" + b)
        down()

    label=tkinter.Label(app,bg="white",textvariable=var,font = ("楷体",20))
    label.place(x=100,y=50,height=100,width=600)
    labela=tkinter.Label(app,bg="white",textvariable=vara)
    labela.place(x=120,y=200,height=25,width=300)
    labelb=tkinter.Label(app,bg="white",textvariable=varb)
    labelb.place(x=420,y=200,height=25,width=300)
    labelc=tkinter.Label(app,bg="white",textvariable=varc)
    labelc.place(x=120,y=250,height=25,width=300)
    labeld=tkinter.Label(app,bg="white",textvariable=vard)
    labeld.place(x=420,y=250,height=25,width=300)
    ra=tkinter.Radiobutton(app,text="A",variable=var1,value="A")
    ra.place(x=100,y=200)
    rb=tkinter.Radiobutton(app,text="B",variable=var1,value="B")
    rb.place(x=400,y=200)
    rc=tkinter.Radiobutton(app,text="C",variable=var1,value="C")
    rc.place(x=100,y=250)
    rd=tkinter.Radiobutton(app,text="D",variable=var1,value="D")
    rd.place(x=400,y=250)


    b1=tkinter.Button(app,text="开始答题",command=start)
    b1.place(x=200,y=400,height=30,width=100)
    b2=tkinter.Button(app,text="提交答案",command=sorce)
    b2.place(x=500,y=400,height=30,width=100)
    app.mainloop()
def tuichu(tk2):
    tk2.destroy()
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
        sql11="select score1 from checktable where sid=%s "
        cur.execute(sql11,(sid3))
        psf=int(cur.fetchone()[0])
        sql9 = "select score2 from checktable where sid=%s "
        cur.execute(sql9, (sid3))
        qimo = int(cur.fetchone()[0])
        zongfen=psf+qimo
        tkinter.messagebox.showinfo("已查询", "你的分数为:" +str (zongfen))
    b1=Label(app, bg="aliceblue",text='请输入你的学号:',font=('宋体',17))
    b1.place(x=80,y=70,height=30,width=170)
    b2=tkinter.Entry(app, textvariable=varPwd)
    b2.place(x=250,y=70,height=30,width=150)
    b3=tkinter.Button(app,text="查询你的信息",command=select1)
    b3.place(x=100,y=200,height=50,width=100)
    b4=tkinter.Button(app,text="查询你的分数",command=select2)
    b4.place(x=300,y=200,height=50,width=100)
    app.mainloop()
if __name__=="__main__":
   threading.Thread(target=studentlogin).start()






