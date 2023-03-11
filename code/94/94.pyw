import tkinter as tk
from tkinter import messagebox
from tkinter import *
from random import choice
import PIL.ImageTk, os, json, cv2, sys, time, datetime
win = tk.Tk()
win.title(f'抽签')
screenw = win.winfo_screenwidth()
screenh = win.winfo_screenheight()
win_width = 960
win_hight = 540
win.geometry("%dx%d+%d+%d" % (win_width, win_hight, (screenw - win_width) / 2, (screenh - win_hight) / 2))
win.resizable(False, False)
add = os.path.abspath('..')
sjson = (f'{add}\student.json')
button_png = PhotoImage(file=f'{add}\\png\\button.png')
L_png2 = PhotoImage(file=f"{add}\\png\\bno.png")
L_png3 = PhotoImage(file=f"{add}\\png\\byes.png")
mp4_1 = tk.Label(win)
mp4_1.place(x=-2,y=-2)
video = cv2.VideoCapture(f'{add}\png\\bg.mp4')
def about():
    d1 = datetime.date.today().strftime(f"{'%Y'}-{'%m'}-{'%d'}")
    d2 = '2023-06-26'
    date1 = datetime.datetime.strptime(d1, "%Y-%m-%d").date()
    date2 = datetime.datetime.strptime(d2, "%Y-%m-%d").date()
    Days = (date2 - date1).days
    messagebox.showinfo(title='YX',
    message=f'抽签软件\n———————————————————\n来源：惠阳区新世纪实验学校2022-2023届九年级四班\n\n未经允许禁止转载\n\n联系YX\n微信：yyx20216\n\n距离中考还有{Days}天\n中考时间{d2}\n\n制作者：YX')
def video_stream():
        _, frame = video.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = PIL.Image.fromarray(frame)
        frame = PIL.ImageTk.PhotoImage(image=frame)
        mp4_1.config(image=frame)
        mp4_1.image = frame
        win.after(25, video_stream)
video_stream()
def text():
    mp4_1.place_forget()
    mp4_2 = tk.Label(win)
    mp4_2.place(x=-2,y=-2)
    video2 = cv2.VideoCapture(f'{add}\png\\ck.mp4')
    s5 = PhotoImage(file=f'{add}\png\\5s.png')
    def video_stream2():
        try:
            _, frame = video2.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = PIL.Image.fromarray(frame)
            frame = PIL.ImageTk.PhotoImage(image=frame)
            mp4_2.config(image=frame)
            mp4_2.image = frame
            win.after(25, video_stream2)
        except cv2.error:
            click_button() 
    video_stream2()
    with open(f'{add}\Plog.txt') as Plog:
        l_num = len(Plog.read().split())
    with open(f'{add}\\var.json','r') as var:
            vars = json.load(var)
            un_num = vars['Pnum']
            name = vars['Pname']
            num = vars['Pnum']
            time_list = vars['time_l']
    if l_num == 0:
        with open(f'{add}\\var.json','r') as var:
            vars = json.load(var)
            list_num = vars['Plist']
            lnum = choice(list_num)
            vars['Pnum'] = lnum
            with open(f'{add}\\var.json','w') as var:
                json.dump(vars,var)
    with open(f'{add}\\var.json','r') as var:
        vars = json.load(var)
        Pof = vars['Pof']
    with open(f'{add}\student.json') as j:
        bname = json.load(j)
        xx = choice(bname)
    if Pof == 0:
        if num != l_num + 1:
            with open(f'{add}\Plog.txt', 'a') as Plog:
                Plog.write(xx)
                Plog.write('\t')
        if xx == name:
            with open(f'{add}\Plog.txt', 'w') as Plog:
                Plog.write('')
        if num == l_num + 1:
            with open(f'{add}\Plog.txt', 'w') as Plog:
                Plog.write('')
                xx = name
    if Pof == 1:
        time_H = int(time.strftime("%H"))
        time_M = int(time.strftime("%M"))
        time_now = time_H * 60+time_M
        if num != l_num + 1:
            with open(f'{add}\Plog.txt', 'a') as Plog:
                Plog.write(xx)
                Plog.write('\t')
            if xx == name:
                with open(f'{add}\Plog.txt', 'w') as Plog:
                    Plog.write('')
        for i in time_list:
            t_h=i//100
            t_m=(i//1)%100
            t_i = (i//100)*60+((i//1)%100)
            if num == l_num + 1:
                with open(f'{add}\Plog.txt', 'w') as Plog:
                    Plog.write('')
                    if 0 <= t_i - time_now <= 40:
                        xx = name
    with open(f'{add}\log.txt', 'a') as log:
        xx = str(xx)
        log.write(xx)
        log.write('\t')  
    if l_num > un_num:
        with open(f'{add}\Plog.txt', 'w') as Plog:
            Plog.write('')
    def click_button():
        b_s.place_forget()
        button_t.place_forget()
        mp4_2.destroy()
        button_e.place_forget()
        tl.place_forget()
        tl2.place_forget()
        tl3.place_forget()
        tl4.place_forget()
        about_s.place_forget()
        button_12.place_forget()  # bug!!!修复啦
        L1 = Label(win, text=xx,font=('汉仪文黑-85W', 120))
        L1.place(x=215, y=125, width=540, height=270)
        L2 = Label(win, image=s5)
        L2.place(x=423, y=400)
        def mp4_exit():
            button_t.place(x=778, y=488)
            button_e.place(x=914, y=16)
            L1.destroy()
            L2.destroy()
            about_s.place(x=139,y=502)
            button2.destroy()
            mp4_1.place(x=-2,y=-2)
            tl.place(x=772, y=16)
            tl2.place(x=860.5, y=16)
            tl3.place(x=52, y=477)
            tl4.place(x=102, y=477)
            b_s.place(x=41,y=501)
        button2 = Button(win, image=button_png2, borderwidth=0, command=mp4_exit)
        button2.place(x=914, y=16)
    button_12 = Button(win, text='跳过', command=click_button)
    button_12.place(x=925, y=0)
def new_win():
    def getEntry():
        num = entry.get()  # 获取Entry的内容
        num2 = int(num)
        number = 1
        root.destroy()
        with open(sjson) as j:
            bname = json.load(j)
        with open(f'{add}\log.txt', 'a') as log:
            while number <= num2: 
                xx = choice(bname)
                log.write(xx)
                log.write('\t')
                number += 1
    root = tk.Toplevel(win)
    root_width = 455
    root_hight = 263
    root.geometry("%dx%d+%d+%d" % (root_width, root_hight, (screenw - root_width) / 2, ((screenh - root_hight) / 2)+22))
    L_png1 = PhotoImage(file=f"{add}\\png\\mck.png")
    lr1 = tk.Label(root, image=L_png1).pack()
    entry = tk.Entry(root, font='汉仪文黑-85W',width=30,borderwidth=0)
    entry.place(x=45,y=104)
    button_n = tk.Button(root, command=root.destroy,image=L_png2,borderwidth=0,bg='#e2ded5').place(x=60,y=214)
    button_y = tk.Button(root, command=getEntry,image=L_png3,borderwidth=0,bg='#e2ded5')
    button_y.place(x=268,y=215)
    root.overrideredirect(True)
    root.wm_attributes('-topmost', 1)
    root.mainloop()
def reset_log():
    with open(f'{add}\log.txt', 'w') as log:
        log.write('')
    with open(f'{add}\Plog.txt', 'w') as Plog:
        Plog.write('')
def change_P():
    def password():
        passwd = entry.get()  # 获取Entry的内容
        with open(f'{add}\\var.json','r') as var:
            vars = json.load(var)
            r_pw = vars['password']
        if passwd == r_pw:
            root.destroy()
            L_Png4 = PhotoImage(file=f"{add}\\png\\set_P.png") 
            P_1 = PhotoImage(file=f"{add}\\png\\p1.png")
            P_2 = PhotoImage(file=f"{add}\\png\\p2.png")
            P_3 = PhotoImage(file=f"{add}\\png\\p3.png")
            P_4 = PhotoImage(file=f"{add}\\png\\p4.png")
            P_5 = PhotoImage(file=f"{add}\\png\\p5.png")
            P_exit = PhotoImage(file=f"{add}\\png\\s_exit.png")
            win2 = tk.Toplevel(win)
            win2.title('更改概率')
            win2_width = 455
            win2_hight = 263
            win2.geometry("%dx%d+%d+%d" % (win2_width, win2_hight, (screenw - win2_width) / 2, ((screenh - win2_hight) / 2)+22))
            win2.overrideredirect(True)
            win2.resizable(False, False)  ## 规定窗口不可缩放
            l_bg = Label(win2, image=L_Png4).place(x=-2, y=-2)
            e_name = Entry(win2, font='汉仪文黑-85W', width=15,borderwidth=0)
            e_name.place(x=195, y=92)
            e_num = Entry(win2, font='汉仪文黑-85W', width=6,borderwidth=0)
            e_num2 = Entry(win2, font='汉仪文黑-85W', width=6,borderwidth=0)
            e_num.place(x=194, y=172)
            e_num2.place(x=310, y=172)
            win2.wm_attributes('-topmost', 1)
            def c1():
                name = e_name.get()
                num = e_num.get()
                num_name = int(num)
                with open(sjson) as f:  # exe要加94
                    bname = json.load(f)
                    Tnum = 1
                    while Tnum <= num_name:
                        addstudent = name
                        Tnum += 1
                        bname.append(addstudent)
                        with open(sjson, 'w') as f:
                            json.dump(bname, f)
            def c2():
                name = e_name.get()
                with open(sjson) as f:
                    bname = json.load(f)
                    while name in bname:
                        bname.remove(name)
                    with open(sjson, 'w') as f:
                        json.dump(bname, f)
            def c3():
                name = e_name.get()
                num = e_num.get()
                num2 = e_num2.get()
                num = int(num)
                num2 = int(num2)
                with open(f'{add}\Plog.txt', 'w') as Plog:
                    Plog.write('')
                with open(f'{add}\\var.json','r') as var:
                    vars = json.load(var)
                    vars['Pname'] = name
                    num_l = [i for i in range(num, num2+1)]
                    vars['Plist'] = num_l
                    with open(f'{add}\\var.json','w') as var:
                        json.dump(vars,var)
            def c4():
                with open(f'{add}\student.txt', 'r', encoding='utf-8') as f:
                    student = f.readlines()
                    student1 = []
                    for w in student:
                        w = w.replace('\n', '')
                        student1.append(w)
                with open(sjson, 'w') as f:
                    json.dump(student1, f)
            def c5():
                with open(f'{add}\\var.json','r') as var:
                    vars = json.load(var)
                    vars['Pname'] = [-1]
                    vars['Pnum'] = -1
                    vars['Plist'] = [-1]
                    with open(f'{add}\\var.json','w') as var:
                        json.dump(vars,var)
            b1 = Button(win2, image=P_1, command=c1,borderwidth=0,bg='#e2ded5')
            b1.place(x=51, y=56)
            b1 = Button(win2, image=P_2, command=c2,borderwidth=0,bg='#e2ded5')
            b1.place(x=51, y=97)
            b1 = Button(win2, image=P_3, command=c3,borderwidth=0,bg='#e2ded5')
            b1.place(x=51, y=137)
            b1 = Button(win2, image=P_4, command=c4,borderwidth=0,bg='#e2ded5')
            b1.place(x=50, y=177)
            b1 = Button(win2, image=P_5, command=c5,borderwidth=0,bg='#e2ded5')
            b1.place(x=51, y=216)
            b1 = Button(win2, image=P_exit, command=win2.destroy,borderwidth=0,bg='#e2ded5')
            b1.place(x=414, y=20)
            win2.mainloop()
        if passwd != r_pw:
            root.destroy()  
    root = tk.Toplevel(win)
    root_width = 455
    root_hight = 263
    root.geometry("%dx%d+%d+%d" % (root_width, root_hight, (screenw - root_width) / 2,((screenh - root_hight) / 2)+22))
    root.overrideredirect(True)
    L_png1 = PhotoImage(file=f"{add}\\png\\pw.png")
    lr1 = tk.Label(root, image=L_png1).pack()
    button_n = tk.Button(root, command=root.destroy,image=L_png2,borderwidth=0,bg='#e2ded5').place(x=60,y=214)
    button_y = tk.Button(root, command=password,image=L_png3,borderwidth=0,bg='#e2ded5')
    button_y.place(x=268,y=215)
    entry = tk.Entry(root, font='汉仪文黑-85W', show='*',width=30,borderwidth=0)
    entry.place(x=45,y=104)
    root.wm_attributes('-topmost', 1)
    root.mainloop() 
with open(f'{add}\\var.json','r') as var:
    vars = json.load(var)
    set_var = vars['s_var']
def about_v():
    if set_var == 1:
        vars['s_var'] = 0
        with open(f'{add}\\var.json','w') as var:
            json.dump(vars,var)  
    if set_var == 0:
        vars['s_var'] = 1 
        with open(f'{add}\\var.json','w') as var:
            json.dump(vars,var)
button_t = Button(win, image=button_png, command=text, borderwidth=0,bg='#ffffff')
button_t.place(x=778, y=488)
button_png2 = PhotoImage(file=f'{add}\png\\exit.png')
button_e = Button(win, image=button_png2, borderwidth=0, command=sys.exit,bg='#e2dfd5')
button_e.place(x=914, y=16)
def gettime():
    timestr = time.strftime("%H%M")
    tl.configure(text=timestr)
    timestr2 = time.strftime("%S")
    tl2.configure(text=timestr2)
    timestr3 = time.strftime("%m")
    tl3.configure(text=timestr3)
    timestr4 = time.strftime("%d")
    tl4.configure(text=timestr4)
    win.after(1000, gettime)
tl = tk.Label(win, text='', borderwidth=0, bg='#4E657E', fg='white', font=('汉仪文黑-85W', 9))
tl.place(x=772, y=16)
tl2 = tk.Label(win, text='', borderwidth=0, bg='#4E657E', fg='white', font=('汉仪文黑-85W', 9))
tl2.place(x=861.5, y=16)
tl3 = tk.Label(win, text='', borderwidth=0, bg='#90B2C0', fg='white', font=('汉仪文黑-85W', 9))
tl3.place(x=51, y=477)
tl4 = tk.Label(win, text='', borderwidth=0, bg='#A0BDBF', fg='white', font=('汉仪文黑-85W', 9))
tl4.place(x=102, y=477)
gettime()
def look_P2():
    with open(f'{add}\\var.json','r') as var:
        vars = json.load(var)
        vars['l_var'] = 1
        with open(f'{add}\\var.json','w') as var:
            json.dump(vars,var)
            os.startfile(f'{add}\look_P\look_P.exe')
def look_P():
    with open(f'{add}\\var.json','r') as var:
        vars = json.load(var)
        vars['l_var'] = 0
        with open(f'{add}\\var.json','w') as var:
            json.dump(vars,var)
            os.startfile(f'{add}\look_P\look_P.exe')
def open_var():
    def password():
        passwd = entry.get()  # 获取Entry的内容
        with open(f'{add}\\var.json','r') as var:
            vars = json.load(var)
            r_pw = vars['password']
        if passwd == r_pw:
            root.destroy()
            os.startfile(f'{add}\\var.json') 
        if passwd != r_pw:
            root.destroy()
    root = tk.Toplevel(win)
    root_width = 455
    root_hight = 263
    root.geometry("%dx%d+%d+%d" % (root_width, root_hight, (screenw - root_width) / 2,((screenh - root_hight) / 2)+22))
    root.overrideredirect(True)
    L_png1 = PhotoImage(file=f"{add}\\png\\pw.png")
    lr1 = tk.Label(root, image=L_png1).pack()
    button_n = tk.Button(root, command=root.destroy,image=L_png2,borderwidth=0,bg='#e2ded5').place(x=60,y=214)
    button_y = tk.Button(root, command=password,image=L_png3,borderwidth=0,bg='#e2ded5')
    button_y.place(x=268,y=215)
    entry = tk.Entry(root, font='汉仪文黑-85W', show='*',width=30,borderwidth=0)
    entry.place(x=45,y=104)
    root.wm_attributes('-topmost', 1)
    root.mainloop()
set_bg = PhotoImage(file=f"{add}\\png\\set_bg.png")
set_ex = PhotoImage(file=f"{add}\\png\\s_exit.png")
s1 = PhotoImage(file=f"{add}\\png\\s1.png")
s2 = PhotoImage(file=f"{add}\\png\\s2.png")
s3 = PhotoImage(file=f"{add}\\png\\s3.png")
s4 = PhotoImage(file=f"{add}\\png\\s4.png")
s5 = PhotoImage(file=f"{add}\\png\\s5.png")
s6 = PhotoImage(file=f"{add}\\png\\s6.png")
s7 = PhotoImage(file=f"{add}\\png\\s7.png")
def setting():
    root = tk.Toplevel(win)
    root_width = 455
    root_hight = 263
    root.overrideredirect(True)
    root.wm_attributes('-topmost', 1)
    root.geometry("%dx%d+%d+%d" % (root_width, root_hight, (screenw - root_width) / 2, ((screenh - root_hight) / 2)+22))
    l_set = tk.Label(root,image=set_bg).place(x=-2,y=-2)
    s_exit = tk.Button(root,image=set_ex, command=root.destroy,borderwidth=0,bg='#e2dfd5').place(x=413.5,y=20) #抽多次
    b_set = tk.Button(root,image=s1, command=new_win,borderwidth=0,bg='#e2dfd5').place(x=45,y=54) #抽多次
    b_set = tk.Button(root,image=s2, command=reset_log,borderwidth=0,bg='#e2dfd5').place(x=45,y=105) # 清除日志
    b_set = tk.Button(root,image=s3, command=change_P,borderwidth=0,bg='#e2dfd5').place(x=45,y=158) #更改概率
    b_set = tk.Button(root,image=s4, command=about_v,borderwidth=0,bg='#e2dfd5').place(x=45,y=210) #不再提醒
    b_set = tk.Button(root,image=s5, command=look_P2,borderwidth=0,bg='#e2dfd5').place(x=177,y=54) #理论概率
    b_set = tk.Button(root,image=s6, command=look_P,borderwidth=0,bg='#e2dfd5').place(x=177,y=106) #看概率
    b_set = tk.Button(root,image=s7, command=open_var,borderwidth=0,bg='#e2dfd5').place(x=178,y=157)
S_png1 = PhotoImage(file=f"{add}\\png\\set.png")
S_png2 = PhotoImage(file=f"{add}\\png\\about.png")
b_s = tk.Button(win,command=setting,image=S_png1,borderwidth=0,bg='#e2ded5')
b_s.place(x=41,y=502)
about_s = tk.Button(win,command=about,image=S_png2,borderwidth=0,bg='#e2ded5')
about_s.place(x=139,y=502)
if set_var == 0:
    about()
win.mainloop()
