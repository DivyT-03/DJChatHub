from tkinter import *
import tkinter.messagebox
import MySQLdb
import time
import datetime

def login_success():
    
    global f_login_success
    f_login_success=Frame(main,bg='black',height=500,width=300)
    global Search_e
    Search_e=Entry(f_login_success,width=40)
    Search_e.place(x=0,y=0)
    msg="Welcome User, Your Chats:"
    m=Label(f_login_success,text=msg,fg='white')
    m.config(bg="black",font=('times',12,'italic'))
    m.place(x=10,y=50)
    Add_Chats()
    global Search_b
    Search_b=Button(f_login_success,text='Search',command=lambda: [Search(Search_e)])
    Search_b.place(x=250,y=0)
    global Log_Out_b
    Log_Out_b=Button(f_login_success,text='Log Out',command=Logout)
    Log_Out_b.place(x=0,y=475,width=300)
    global Profile_b
    Profile_b=Button(f_login_success,text='Profile',command=lambda: [Profile(current_user),f_login_success.pack_forget()])
    Profile_b.place(x=0,y=450,width=300)
    global Delete_b
    Delete_b=Button(f_login_success,text='Delete Account',command=lambda: [Delete()])
    Delete_b.place(x=0,y=425,width=300)
    f_login.pack_forget()
    f_login_success.pack()
    Search_e.delete(0,END)
    Search_e.insert(0,'Search')

def lets_exit():
    error.destroy()
    on_closing() 

def Add_Chats():
    def query():
        try:
            print("YES")
            ycord=75
            cur.execute("SELECT person from Chat_Exists where chats_with=%s",(current_userno,))
            list1=cur.fetchall()
            cur.execute("SELECT chats_with from Chat_Exists where person=%s",(current_userno,))
            list2=cur.fetchall()
            list1=list1+list2
            open_chat = lambda x: (lambda p: do_it(x))
            for i in list1:
                if(ycord==400):
                    break
                cur.execute("SELECT username from User_Info NATURAL JOIN Login_Info where user_no=%s",(i,))
                username_disp=cur.fetchall()
                print(username_disp)
                if username_disp==():
                    pass
                else:
                    username_disp=username_disp[0][0]
                    print(username_disp)
                    l_user1=Label(f_login_success,text=username_disp)
                    l_user1.place(x=55,y=ycord)
                    l_user1.bind("<1>", open_chat(username_disp))
                    ycord=ycord+25
            if(ycord==400):
                chat_a_lot=Label(f_login_success,text="You chat a lot, we ran out of space, please search manually",font=("Times",8),bg='black',fg='white')
                chat_a_lot.place(x=10,y=400)
            def do_it(arg):
                global Search_user
                Search_user=arg
                Message()
        except:
                    global error;error=Tk()
                    error.title("No Network Connection")
                    error.geometry("300x50")
                    error_label=Label(error,text="Check your network connection and Restart")
                    error_label.place(x=70,y=0)
                    error_button=Button(error,text="OK",command=lambda:[lets_exit()])
                    error.protocol("WM_DELETE_WINDOW",lets_exit)
                    error_button.place(x=140,y=25)              
                    error.mainloop()
    query()

def Delete():
    def YES():
        def query():
            try:
                cur.execute("SELECT User_Info.email from User_Info NATURAL JOIN Login_Info where username=%s",(current_user,))
                d_email=cur.fetchall()[0][0]
                cur.execute("Delete from Login_Info where username=%s",(current_user,))
                cur.execute("Delete from User_Info where email=%s",(d_email,))
                d.destroy()
                Logout()
                conn.commit()
            except:
                    global error;error=Tk()
                    error.title("No Network Connection")
                    error.geometry("300x50")
                    error_label=Label(error,text="Check your network connection and Restart")
                    error_label.place(x=70,y=0)
                    error_button=Button(error,text="OK",command=lambda:[lets_exit()])
                    error.protocol("WM_DELETE_WINDOW",lets_exit)
                    error_button.place(x=140,y=25)             
                    error.mainloop()
        query()
    d=Tk() 
    d.title("It's a good app")
    d.geometry("150x60")
    d.grab_set()
    del_conf=Label(d,text="Are you Sure?")
    del_conf_yes=Button(d,text='Yes',command=YES)
    del_conf_no=Button(d,text='No',command=lambda:[d.grab_release(),d.destroy()])
    del_conf.place(x=30,y=5)
    del_conf_yes.place(x=30,y=30)
    del_conf_no.place(x=85,y=30)
    d.mainloop()

def Search(Search_entry):
    global Search_user
    Search_user=Search_entry.get().lower()
    def query():
        try:
            cur.execute("Select username from Login_Info where username=%s",(Search_user,))
        except:
                    global error;error=Tk()
                    error.title("No Network Connection")
                    error.geometry("300x50")
                    error_label=Label(error,text="Check your network connection and Restart")
                    error_label.place(x=70,y=0)
                    error_button=Button(error,text="OK",command=lambda:[lets_exit()])
                    error.protocol("WM_DELETE_WINDOW",lets_exit)
                    error_button.place(x=140,y=25)              
                    error.mainloop()
    query()
    Search_check=cur.fetchall()
    if Search_check==():
        tkinter.messagebox.showinfo("Error","User Not Found")
    else:
        f_search.pack()
        f_login_success.pack_forget()
        f_profile.pack_forget()
        unpack_profile()
        global l_username_al
        l_username_al=Label(f_search,text="Username:",bg='black',fg='white')
        global l_username_display
        l_username_display=Label(f_search,text=Search_user,bg='black',fg='white')
        Message_Button= Button(f_search, text='Message',command=lambda: [Message()])
        Profile_Button= Button(f_search, text='Profile',command=lambda: [unpack_serach(),Profile(Search_user),f_search.pack_forget()])
        l_username_al.place(x=55,y=75)
        l_username_display.place(x=55,y=100)
        Message_Button.place(x=55,y=150)
        Profile_Button.place(x=165,y=150)

def unpack_serach():
    try:
        l_username_al.place_forget()
        l_username_display.place_forget()
    except:
        pass
        
def Profile(User_Name):
        Search_e_p.delete(0,END)
        Search_e_p.insert(0,'Search')
        f_profile.pack()
        def query():
            try:
                cur.execute("Select First_Name,Last_Name,Email from User_Info Natural Join Login_Info where username=%s",(User_Name,))
            except:
                    global error;error=Tk()
                    error.title("No Network Connection")
                    error.geometry("300x50")
                    error_label=Label(error,text="Check your network connection and Restart")
                    error_label.place(x=70,y=0)
                    error_button=Button(error,text="OK",command=lambda:[lets_exit()])
                    error.protocol("WM_DELETE_WINDOW",lets_exit)
                    error_button.place(x=140,y=25)              
                    error.mainloop()
        query()
        data=cur.fetchall()
        global l_username_al_p
        l_username_al_p=Label(f_profile,text="Username:",bg='black',fg='white')
        global l_username_display_p
        l_username_display_p=Label(f_profile,text=User_Name,bg='black',fg='white')
        global l_email_al
        l_email_al=Label(f_profile,text="Email:",bg='black',fg='white')
        global l_email_display
        l_email_display=Label(f_profile,text=data[0][2],bg='black',fg='white')
        global l_fname_al
        l_fname_al=Label(f_profile,text="First Name:",bg='black',fg='white')
        global l_fname_display
        l_fname_display=Label(f_profile,text=data[0][0],bg='black',fg='white')
        global l_lname_al
        l_lname_al=Label(f_profile,text="Last Name:",bg='black',fg='white')
        global l_lname_display
        l_lname_display=Label(f_profile,text=data[0][1],bg='black',fg='white')
        l_username_al_p.place(x=55,y=75)
        l_username_display_p.place(x=55,y=100)
        l_email_al.place(x=55,y=125)
        l_email_display.place(x=55,y=150)
        l_fname_al.place(x=55,y=175)
        l_fname_display.place(x=55,y=200)
        l_lname_al.place(x=165,y=175)
        l_lname_display.place(x=165,y=200)

def unpack_profile():
    try:
        l_username_al_p.place_forget()
        l_username_display_p.place_forget()
        l_email_al.place_forget()
        l_email_display.place_forget()
        l_fname_al.place_forget()
        l_fname_display.place_forget()
        l_lname_al.place_forget()
        l_lname_display.place_forget()
    except:
        pass

   

def Message():
    def query():
        try:
            cur.execute("SELECT user_no from User_Info NATURAL JOIN Login_Info where username=%s",(Search_user,))
        except:
                    global error;error=Tk()
                    error.title("No Network Connection")
                    error.geometry("300x50")
                    error_label=Label(error,text="Check your network connection and Restart")
                    error_label.place(x=35,y=0)
                    error_button=Button(error,text="OK",command=lambda:[lets_exit()])
                    error.protocol("WM_DELETE_WINDOW",lets_exit)
                    error_button.place(x=140,y=25)              
                    error.mainloop()
    query()
    Search_userno=cur.fetchall()
    Search_userno=Search_userno[0][0]
    if current_userno==Search_userno:
        tkinter.messagebox.showinfo("So Lonely?","You wanna chat with yourself?\nBecome Socially Social ;)")
    else:
        if current_userno>Search_userno:
            person=Search_userno
            chats_with=current_userno
        else:
            chats_with=Search_userno
            person=current_userno
        def query2():
            try:
                cur.execute("SELECT person from Chat_Exists where person=%s and chats_with=%s",(person,chats_with))
            except:
                    global error;error=Tk()
                    error.title("No Network Connection")
                    error.geometry("300x50")
                    error_label=Label(error,text="Check your network connection and Restart")
                    error_label.place(x=70,y=0)
                    error_button=Button(error,text="OK",command=lambda:[lets_exit()])
                    error.protocol("WM_DELETE_WINDOW",lets_exit)
                    error_button.place(x=140,y=25)              
                    error.mainloop()
        query2()
        data_1=cur.fetchall()
        global tablename
        tablename="Chat"+str(person)+"with"+str(chats_with)
        if data_1==():
            def query1():
                try:
                    cur.execute("INSERT INTO Chat_Exists values(%s,%s)",(person,chats_with))
                    conn.commit()
                    command="CREATE TABLE "+tablename+" (username varchar(30),Message varchar(300),time int)"
                    cur.execute(command)
                except:
                    global error;error=Tk()
                    error.title("No Network Connection")
                    error.geometry("300x50")
                    error_label=Label(error,text="Check your network connection and Restart")
                    error_label.place(x=70,y=0)
                    error_button=Button(error,text="OK",command=lambda:[lets_exit()])
                    error.protocol("WM_DELETE_WINDOW",lets_exit)
                    error_button.place(x=140,y=25)              
                    error.mainloop()
            query1()
        else:
            pass
        Message_Frames()
        unpack_serach()
        f_search.pack_forget()
        f_login_success.pack_forget()
        

def Message_Frames():
    global row
    def destroy_Message():
        canvas_m.destroy()
        chatwith_l.place_forget()

    def onFrameConfigure(canvas):
        canvas.configure(scrollregion=canvas.bbox("all"))

    def refresh():
        conn.commit()
        destroy_Message()
        Message_Frames()
        f_m_header.pack_forget()

    
    row=0
    f_m_header=Frame(main,bg='black',height=50,width=300)
    global back_b
    back_b=Button(f_m_header,text='back',command=lambda:[destroy_Message(),f_login_success.pack(),unpack_serach(),f_m_header.pack_forget(),f_search.pack_forget()])
    back_b.place(x=25,y=5)
    global refresh_b
    refresh_b=Button(f_m_header,text='Refresh',command=lambda:[refresh()])
    refresh_b.place(x=225,y=5)
    global chatwith_l
    chatwith_l=Label(f_m_header, text=Search_user,bg='black',fg='white')
    chatwith_l.place(x=100,y=5)
    f_m_header.pack()

    global f_message
    canvas_m =Canvas(main, borderwidth=0, background="#999999",height=450,width=300)
    f_message =Frame(canvas_m, bg='gray')
    vsb = Scrollbar(canvas_m, orient="vertical", command=canvas_m.yview)
    canvas_m.configure(yscrollcommand=vsb.set)


    vsb.pack(side="right", fill="y")
    canvas_m.pack( fill="both", expand=True)
    canvas_m.create_window((4,4), window=f_message, anchor="nw") #Added Scrollbar to message window


    f_message.bind("<Configure>", lambda event, canvas=canvas_m: onFrameConfigure(canvas_m))
    global Message_e
    Message_e=Entry(f_message,width=40)
    global Message_b
    Message_b=Button(f_message,text='Send',command=lambda:[Message_Sent(),refresh()],background='gray')
    Message_e.grid(row=0, column=0)
    Message_b.grid(row=0, column=1)     
    recover_chat="Select * from "+tablename+" order by time desc"
    def query():
        try:
            cur.execute(recover_chat)
        except:
                    global error;error=Tk()
                    error.title("No Network Connection")
                    error.geometry("300x50")
                    error_label=Label(error,text="Check your network connection and Restart")
                    error_label.place(x=70,y=0)
                    error_button=Button(error,text="OK",command=lambda:[lets_exit()])
                    error.protocol("WM_DELETE_WINDOW",lets_exit)
                    error_button.place(x=140,y=25)              
                    error.mainloop()
    query()
    data=cur.fetchall()
    row=1
    for i in data:
        sent=datetime.datetime.fromtimestamp(i[2]).strftime('%c')
        if i[0]==current_user:
            Label(f_message, text="Username: "+i[0], borderwidth="1",relief="solid", bg='gray',justify=RIGHT).grid(sticky="w",row=row, column=0)
        else:
            Label(f_message, text="Username: "+i[0], borderwidth="1",relief="solid", bg='gray',justify=LEFT).grid(sticky="w",row=row, column=0)
        row=row+1
        message_retrived=i[1]
        message_retrived=message_retrived.replace("<<<Single_Inverted_Comma>>>","'")
        message_retrived=message_retrived.replace('<<<Double_Inverted_Comma>>>','"')
        Label(f_message, text=message_retrived,wraplength=300, bg='gray').grid(sticky="w",row=row, column=0)
        row=row+1
        Label(f_message, text="Sent: "+str(sent), bg='gray').grid(sticky="w",row=row, column=0)
        row=row+1 #Recovered Messages Sent Till Now
    
    
def Message_Sent():
    Message=Message_e.get()
    Message=Message.replace("'","<<<Single_Inverted_Comma>>>")
    Message=Message.replace('"',"<<<Double_Inverted_Comma>>>")
    command_insert="Insert into "+tablename+" values ('"+current_user+"','"+Message+"',%d)"%(time.time())
    def query():
        try:
            cur.execute(command_insert) #Adding Newly Sent Message to table
            conn.commit()
        except:
                    global error;error=Tk()
                    error.title("No Network Connection")
                    error.geometry("300x50")
                    error_label=Label(error,text="Check your network connection and Restart")
                    error_label.place(x=70,y=0)
                    error_button=Button(error,text="OK",command=lambda:[lets_exit()])
                    error.protocol("WM_DELETE_WINDOW",lets_exit)
                    error_button.place(x=140,y=25)              
                    error.mainloop()
    query()

def Logout():

    f_login_success.pack_forget()
    f_search.pack_forget()
    f_profile.pack_forget()
    f_login_success.destroy()
    Home()
    

def unpack_fp():
    Q1_label.place_forget()
    A1_entry.place_forget()
    Q2_label.place_forget()
    A2_entry.place_forget()
    Next_fp.place_forget()
    fp_home_0.place_forget()
    Home()
    
def unpack_fp_1():
    np_label.place_forget()
    np_entry.place_forget()
    Q1_label.place_forget()
    A1_entry.place_forget()
    Q2_label.place_forget()
    A2_entry.place_forget()
    Next_fp.place_forget()
    Next_fp1.place_forget()
    fp_home_0.place_forget()
    fp_home_1.place_forget()

    Home()

def Home():
    try:
        f_login_success.pack_forget()
    except:
        pass
    finally:
        f_login.pack_forget()
        f_signup.pack_forget()
        f_signup_1.pack_forget()
        f_about.pack_forget()
        f_signup_2.pack_forget()
        f_forgot.pack_forget()
        f.pack()

def Login():
    e_username.delete(0,END)
    e_password.delete(0,END)
    f.pack_forget()
    f_signup.pack_forget()
    f_about.pack_forget()
    f_signup_1.pack_forget()
    f_signup_2.pack_forget()
    f_forgot.pack_forget()
    f_login.pack()


def FP():
    f.pack_forget()
    f_signup.pack_forget()
    f_about.pack_forget()
    f_signup_1.pack_forget()
    f_signup_2.pack_forget()
    f_login.pack_forget()
    Next_SQ.place(x=120,y=410)
    fp_Home.place(x=55,y=410)
    fp_user.place(x=55,y=325)
    f_forgot.pack()

def SignUp():
    e_fname.delete(0,END)
    e_lname.delete(0,END)
    e_email.delete(0,END)
    f.pack_forget()
    f_login.pack_forget()
    f_about.pack_forget()
    f_signup_1.pack_forget()
    f_signup_2.pack_forget()
    f_forgot.pack_forget()
    f_signup.pack()

def AboutUs():
    f.pack_forget()
    f_login.pack_forget()
    f_signup.pack_forget()
    f_signup_1.pack_forget()
    f_signup_2.pack_forget()
    f_forgot.pack_forget()
    f_about.pack()

def SignUp2():
    global signup_fname
    signup_fname=e_fname.get()
    global signup_lname
    signup_lname=e_lname.get()
    global signup_email
    signup_email=e_email.get().lower()
    def query():
        try:
            cur.execute("SELECT email from User_Info where Email=%s",(signup_email,))
        except:
                    global error;error=Tk()
                    error.title("No Network Connection")
                    error.geometry("300x50")
                    error_label=Label(error,text="Check your network connection and Restart")
                    error_label.place(x=70,y=0)
                    error_button=Button(error,text="OK",command=lambda:[lets_exit()])
                    error.protocol("WM_DELETE_WINDOW",lets_exit)
                    error_button.place(x=140,y=25)              
                    error.mainloop()
    query()
    email_check=cur.fetchall()
    if signup_email=='':
            tkinter.messagebox.showinfo("Feild Required","Email can't be empty")
    elif signup_fname=='':
            tkinter.messagebox.showinfo("Feild Required","First Name can't be empty")
    elif signup_lname=='':
            tkinter.messagebox.showinfo("Feild Required","Last Name can't be empty")
    elif email_check==():
        Signup_next()
    elif email_check[0][0]==signup_email:
            tkinter.messagebox.showinfo("Email Exists","The Email you entered is already registered\nPlease Log in Instead")
    else:
            Signup_next()

def Signup_next():
            e_user.delete(0,END)
            e_pass.delete(0,END)
            e_re_pass.delete(0,END)
            f.pack_forget()
            f_login.pack_forget()
            f_signup.pack_forget()
            f_about.pack_forget()
            f_signup_2.pack_forget()
            f_signup_1.pack()

def Check_SignUp():
    global signup_user
    signup_user=e_user.get().lower()
    global signup_pass
    signup_pass=e_pass.get()
    signup_re_pass=e_re_pass.get()
    if signup_pass==signup_re_pass:
            def query():
                try:
                    cur.execute("SELECT username from Login_Info where username=%s",(signup_user,))
                except:
                    global error;error=Tk()
                    error.title("No Network Connection")
                    error.geometry("300x50")
                    error_label=Label(error,text="Check your network connection and Restart")
                    error_label.place(x=70,y=0)
                    error_button=Button(error,text="OK",command=lambda:[lets_exit()])
                    error.protocol("WM_DELETE_WINDOW",lets_exit)
                    error_button.place(x=140,y=25)              
                    error.mainloop()
            query()
            uname_check=cur.fetchall()
            if signup_user=='':
                tkinter.messagebox.showinfo("Feild Required","Username can't be empty")
            elif signup_pass=='':
                tkinter.messagebox.showinfo("Feild Required","Password can't be empty")
            elif signup_re_pass=='':
                tkinter.messagebox.showinfo("Feild Required","Passowrd can't be empty")
            elif uname_check==():
                    Final_Signup()
            elif uname_check[0][0]==signup_user:
                tkinter.messagebox.showinfo("Username Taken","The Username is already in use\nPlease try a different one")
            else:
                Final_Signup()
    else:
        tkinter.messagebox.showinfo("Password Mismatch","Both Entered Password Do Not Match\n Try Again")

def Final_Signup():
                f.pack_forget()
                e_SQ1_a.delete(0,END)
                e_SQ2_a.delete(0,END)
                f_login.pack_forget()
                f_signup.pack_forget()
                f_about.pack_forget()
                f_signup_1.pack_forget()
                f_signup_2.pack()

def Check_Login():
    login_username=e_username.get().lower()
    login_password=e_password.get()
    def query():
        try:
            print("YES")
            cur.execute("SELECT password from Login_Info where username=%s",(login_username,))
        except:
                print("NO")
                global error;error=Tk()
                error.title("No Network Connection")
                error.geometry("300x50")
                error_label=Label(error,text="Check your network connection and Restart")
                error_label.place(x=70,y=0)
                error_button=Button(error,text="OK",command=lambda:[lets_exit()])
                error.protocol("WM_DELETE_WINDOW",lets_exit)
                error_button.place(x=140,y=25)              
                error.mainloop()
    query()
    pass_check=cur.fetchall()
    if pass_check==():
        tkinter.messagebox.showinfo("Login Failed","Incorrect Username\n Try Again")
    elif pass_check[0][0]==login_password:
            tkinter.messagebox.showinfo("Login Successful","Welcome to DJ Chat Hub")
            def query1():
                try:
                    cur.execute("SELECT user_no from User_Info NATURAL JOIN Login_Info where username=%s",(login_username,))
                except:
                    global error;error=Tk()
                    error.title("No Network Connection")
                    error.geometry("300x50")
                    error_label=Label(error,text="Check your network connection and Restart")
                    error_label.place(x=70,y=0)
                    error_button=Button(error,text="OK",command=lambda:[lets_exit()])
                    error.protocol("WM_DELETE_WINDOW",lets_exit)
                    error_button.place(x=140,y=25)              
                    error.mainloop()
            query1()
            data=cur.fetchall()
            global current_userno
            current_userno=data[0][0]
            global current_user
            current_user=login_username
            login_success()
    else:
            tkinter.messagebox.showinfo("Login Failed","Incorrect Passowrd\n Try Again")
    

def Add_SignUp():
    Seq_Ques_1=var_SQ1.get()
    Seq_Ans_1=e_SQ1_a.get()
    Seq_Ques_2=var_SQ2.get()
    Seq_Ans_2=e_SQ2_a.get()
    if Seq_Ans_1=='':
        tkinter.messagebox.showinfo("Required Feild","Answer is required")
    elif Seq_Ans_2=='':
        tkinter.messagebox.showinfo("Required Feild","Answer is required")
    else:
        def query():
            try:
                cur.execute("Select max(user_no) from User_Info")
            except:
                global error;error=Tk()
                error.title("No Network Connection")
                error.geometry("300x50")
                error_label=Label(error,text="Check your network connection and Restart")
                error_label.place(x=70,y=0)
                error_button=Button(error,text="OK",command=lambda:[lets_exit()])
                error.protocol("WM_DELETE_WINDOW",lets_exit)
                error_button.place(x=140,y=25)              
                error.mainloop()
        query()
        data=cur.fetchall()
        if data[0][0]==None:
            user_no=1
        else:
            user_no=int(data[0][0])+1
        def query1():
            try:
                cur.execute("Insert Into User_Info values (%s,%s,%s,%s)",(signup_email,signup_fname,signup_lname,user_no))
                cur.execute("Insert Into Login_Info values (%s,%s,%s,%s,%s,%s,%s)",(signup_user,signup_pass,Seq_Ques_1,Seq_Ans_1,Seq_Ques_2,Seq_Ans_2,signup_email))
                conn.commit()
            except:
                global error;error=Tk()
                error.title("No Network Connection")
                error.geometry("300x50")
                error_label=Label(error,text="Check your network connection and Restart")
                error_label.place(x=70,y=0)
                error_button=Button(error,text="OK",command=lambda:[lets_exit()])
                error.protocol("WM_DELETE_WINDOW",lets_exit)
                error_button.place(x=140,y=25)              
                error.mainloop()
        query1()
        e_SQ1_a.delete(0,END)
        e_SQ2_a.delete(0,END)
        tkinter.messagebox.showinfo("Account Created","Your Account has been successfully created\nPlease Log In")
        Home()

def Forgot_Password():
    global fp_username
    fp_username=fp_user.get().lower()
    def query():
        try:
            cur.execute("SELECT username from Login_Info where username=%s",(fp_username,))
        except:
                global error;error=Tk()
                error.title("No Network Connection")
                error.geometry("300x50")
                error_label=Label(error,text="Check your network connection and Restart")
                error_label.place(x=70,y=0)
                error_button=Button(error,text="OK",command=lambda:[lets_exit()])
                error.protocol("WM_DELETE_WINDOW",lets_exit)
                error_button.place(x=140,y=25)              
                error.mainloop()
    query()
    uname_check=cur.fetchall()
    if uname_check==():
        tkinter.messagebox.showinfo("User Does Not Exist","User Does Not Exist\nPlease Try Again")
    elif uname_check[0][0]==fp_username:
        fp_user.place_forget()
        global fp_user_label
        fp_user_label=Label(f_forgot,text=fp_username,bg='gray')
        fp_user_label.place(x=55,y=325)
        Next_SQ.place_forget()
        fp_Home.place_forget()
        def query1():
            try:
                cur.execute("SELECT SQ1 from Login_Info where username=%s",(fp_username,))
                global Q1
                Q1=cur.fetchall()
                cur.execute("SELECT SQ2 from Login_Info where username=%s",(fp_username,))
                global Q2
                Q2=cur.fetchall()
            except:
                global error;error=Tk()
                error.title("No Network Connection")
                error.geometry("300x50")
                error_label=Label(error,text="Check your network connection and Restart")
                error_label.place(x=70,y=0)
                error_button=Button(error,text="OK",command=lambda:[lets_exit()])
                error.protocol("WM_DELETE_WINDOW",lets_exit)
                error_button.place(x=140,y=25)              
                error.mainloop()
                print("error")
        query1()
        global Q1_label
        Q1_label=Label(f_forgot,text=Q1[0][0],bg='gray')
        Q1_label.place(x=55,y=350)
        global A1_entry
        A1_entry=Entry(f_forgot,width=30)
        A1_entry.place(x=55,y=375)
        global Q2_label
        Q2_label=Label(f_forgot,text=Q2[0][0],bg='gray')
        Q2_label.place(x=55,y=400)
        global A2_entry
        A2_entry=Entry(f_forgot,width=30)
        A2_entry.place(x=55,y=425)
        global Next_fp
        Next_fp= Button(f_forgot, text='Next',command=Check_fp)
        Next_fp.place(x=120,y=450)
        global fp_home_0
        fp_home_0= Button(f_forgot, text='Home',command=lambda:[unpack_fp(),fp_user_label.pack_forget()])
        fp_home_0.place(x=55,y=450)
    else:
        tkinter.messagebox.showinfo("User Does Not Exist","User Does Not Exist\nPlease Try Again")

def Check_fp():
        A1=A1_entry.get()
        A2=A2_entry.get()
        def query():
            try:
                cur.execute("SELECT SQ1_Ans from Login_Info where username=%s",(fp_username,))
                global A1_tab
                A1_tab=cur.fetchall()
                cur.execute("SELECT SQ2_Ans from Login_Info where username=%s",(fp_username,))
                global A2_tab
                A2_tab=cur.fetchall()
            except:
                global error;error=Tk()
                error.title("No Network Connection")
                error.geometry("300x50")
                error_label=Label(error,text="Check your network connection and Restart")
                error_label.place(x=70,y=0)
                error_button=Button(error,text="OK",command=lambda:[lets_exit()])
                error.protocol("WM_DELETE_WINDOW",lets_exit)
                error_button.place(x=140,y=25)              
                error.mainloop()
        query()
        if A1==A1_tab[0][0] and A2==A2_tab[0][0]:
            Q1_label.place_forget()
            A1_entry.place_forget()
            Q2_label.place_forget()
            A2_entry.place_forget()
            Next_fp.place_forget()
            fp_home_0.place_forget()
            global np_label
            np_label=Label(f_forgot,text="Enter New Password:",bg='gray')
            np_label.place(x=55,y=350)
            global np_entry
            np_entry=Entry(f_forgot,width=30)
            np_entry.place(x=55,y=375)
            global Next_fp1
            Next_fp1= Button(f_forgot, text='Next',command=Change_Pass)
            Next_fp1.place(x=120,y=410)
            global fp_home_1
            fp_home_1= Button(f_forgot, text='Home',command=unpack_fp_1)
            fp_home_1.place(x=55,y=410)

        else:
           tkinter.messagebox.showinfo("Wrong Answer","Please Check your answer and try again\n Answers are case Sensitive") 
    
    
def Change_Pass():
    new_pass=np_entry.get()
    if new_pass=='':
        tkinter.messagebox.showinfo("Feild Required","Password can't be empty")
    else:
        def query():
            try:
                cur.execute("Update Login_Info SET password=%s where username=%s",(new_pass,fp_username))
            except:
                global error;error=Tk()
                error.title("No Network Connection")
                error.geometry("300x50")
                error_label=Label(error,text="Check your network connection and Restart")
                error_label.place(x=70,y=0)
                error_button=Button(error,text="OK",command=lambda:[lets_exit()])
                error.protocol("WM_DELETE_WINDOW",lets_exit)
                error_button.place(x=140,y=25)              
                error.mainloop()
        query()
        conn.commit()
        tkinter.messagebox.showinfo("Password Changed Successfully","Password Changed Successfully\nPlease Log In")
        unpack_fp_1()

def on_closing():
    try:
        conn.close()
        main.destroy()
    finally:
        raise SystemExit

def connection():
    try:
        global conn
        conn=MySQLdb.connect(host="remotemysql.com",user="uGu9fJVTjJ",passwd="xcZ7oQJir0",db="uGu9fJVTjJ")
        global cur
        cur=conn.cursor()
    except:
        Network_Error()

def Network_Error():

        global error;error=Tk()
        error.title("No Network Connection")
        error.geometry("300x50")
        error_label=Label(error,text="Check your network connection")
        error_label.place(x=70,y=0)
        error_button=Button(error,text="Retry",command=lambda:[error.destroy(),connection()])
        error.protocol("WM_DELETE_WINDOW",lets_exit)
        error_button.place(x=140,y=25)              
        error.mainloop()

connection()

#Main Window
main=Tk() 
main.title("DJ Chat Hub")
main.geometry("300x500")
main.protocol("WM_DELETE_WINDOW",on_closing)

pic='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'
DJ='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'
img=PhotoImage(data=pic)
JD=PhotoImage(data=DJ)
row=IntVar()

#Home Frame
f=Frame(main,bg='gray',height=500,width=300)
button1= Button(f, text='Login', width=25,command=Login)
button2= Button(f, text='Sign Up', width=25,command=SignUp)
button3= Button(f, text='About', width=25,command=AboutUs)
icon=Label(f,image=img)
icon.place(x=50,y=10)
f1=("Comic Sans MS",16)
Name=Label(f,text="DJ Chat Hub",font=f1,bg='gray')
f2=("Times New Roman",10)
Tagline=Label(f,text="Get Socially Social",bg='gray',font=f2)
Name.place(x=85,y=210)
Tagline.place(x=95,y=250)
button1.place(x=55,y=300)
button2.place(x=55,y=350)
button3.place(x=55,y=400)

#Login Frame
f_login=Frame(main,bg='gray',height=500,width=300)
icon=Label(f_login,image=img)
icon.place(x=50,y=10)
f1=("Comic Sans MS",16)
Name=Label(f_login,text="DJ Chat Hub",font=f1,bg='gray')
f2=("Times New Roman",10)
Tagline=Label(f_login,text="Get Socially Social",bg='gray',font=f2)
Name.place(x=85,y=210)
Tagline.place(x=95,y=250)#Basics

l_username=Label(f_login,text="Username:",bg='gray')
l_username.place(x=55,y=300)
e_username=Entry(f_login,width=30)
e_username.place(x=55,y=325)
l_password=Label(f_login,text="Passowrd:",bg='gray')
l_password.place(x=55,y=350)
e_password=Entry(f_login,width=30,show="*")
e_password.place(x=55,y=375) #Entry Feilds


Login_b= Button(f_login, text='Login',command=Check_Login)
SignUp_b= Button(f_login, text='Sign Up',command=SignUp)
Home_b= Button(f_login, text='Home',command=Home)
forgot_b= Button(f_login, text='Forgot Password',command=FP)

Login_b.place(x=55,y=410)
SignUp_b.place(x=120,y=410)
Home_b.place(x=195,y=410)
forgot_b.place(x=95,y=435)#Button

#SignUp Frame
f_signup=Frame(main,bg='gray',height=500,width=300)

icon=Label(f_signup,image=img)
icon.place(x=50,y=10)
f1=("Comic Sans MS",16)
Name=Label(f_signup,text="DJ Chat Hub",font=f1,bg='gray')
f2=("Times New Roman",10)
Tagline=Label(f_signup,text="Get Socially Social",bg='gray',font=f2)
Name.place(x=85,y=210)
Tagline.place(x=95,y=250) #Basics Page 1

l_fname=Label(f_signup,text="First Name:",bg='gray')
l_fname.place(x=55,y=300)
e_fname=Entry(f_signup,width=14)
e_fname.place(x=55,y=325)
l_lname=Label(f_signup,text="Last Name:",bg='gray')
l_lname.place(x=150,y=300)
e_lname=Entry(f_signup,width=15)
e_lname.place(x=150,y=325)
l_email=Label(f_signup,text="Email:",bg='gray')
l_email.place(x=55,y=350)
e_email=Entry(f_signup,width=30)
e_email.place(x=55,y=375) #Entry Page 1

Home_SU=Button(f_signup, text='Home',command=Home)
Next_SU= Button(f_signup, text='Next',command=SignUp2)
Login_SU= Button(f_signup, text='Login',command=Login)

Login_SU.place(x=55,y=410)
Home_SU.place(x=120,y=410)
Next_SU.place(x=195,y=410)

f_signup_1=Frame(main,bg='gray',height=500,width=300)

icon=Label(f_signup_1,image=img)
icon.place(x=50,y=10)
f1=("Comic Sans MS",16)
Name=Label(f_signup_1,text="DJ Chat Hub",font=f1,bg='gray')
f2=("Times New Roman",10)
Tagline=Label(f_signup_1,text="Get Socially Social",bg='gray',font=f2)
Name.place(x=85,y=210)
Tagline.place(x=95,y=250) #Basics Page 2

l_user=Label(f_signup_1,text="Username:",bg='gray')
l_user.place(x=55,y=300)
e_user=Entry(f_signup_1,width=30)
e_user.place(x=55,y=325)
l_pass=Label(f_signup_1,text="Passowrd:",bg='gray')
l_pass.place(x=55,y=350)
e_pass=Entry(f_signup_1,width=30,show="*")
e_pass.place(x=55,y=375)
l_re_pass=Label(f_signup_1,text="Re-enter Passowrd:",bg='gray')
l_re_pass.place(x=55,y=400)
e_re_pass=Entry(f_signup_1,width=30,show="*")
e_re_pass.place(x=55,y=425) #Entry Page 2

Home_SU=Button(f_signup_1, text='Home',command=Home)
Next2_SU= Button(f_signup_1, text='Next',command=Check_SignUp)
Login_SU= Button(f_signup_1, text='Login',command=Login)

Login_SU.place(x=55,y=450)
Home_SU.place(x=120,y=450)
Next2_SU.place(x=195,y=450)

f_signup_2=Frame(main,bg='gray',height=500,width=300)

icon=Label(f_signup_2,image=img)
icon.place(x=50,y=10)
f1=("Comic Sans MS",16)
Name=Label(f_signup_2,text="DJ Chat Hub",font=f1,bg='gray')
f2=("Times New Roman",10)
Tagline=Label(f_signup_2,text="Get Socially Social",bg='gray',font=f2)
Name.place(x=85,y=210)
Tagline.place(x=95,y=250) #Basics Page 3

var_SQ1 = StringVar(main)
var_SQ2 = StringVar(main)
SQ={"My hometown?","Childhood bestie name?","Father's middle name","Pet's name?"}
var_SQ1.set("My hometown?")
var_SQ2.set("My hometown?")
l_SQ1=Label(f_signup_2,text="Sequrity Question 1:",bg='gray')
l_SQ1.place(x=55,y=275)
e_SQ1=OptionMenu(f_signup_2,var_SQ1,*SQ)
e_SQ1.place(x=55,y=300)
l_SQ1_a=Label(f_signup_2,text="Answer:",bg='gray')
l_SQ1_a.place(x=55,y=325)
e_SQ1_a=Entry(f_signup_2,width=30)
e_SQ1_a.place(x=55,y=350)
l_SQ2=Label(f_signup_2,text="Sequrity Question 1:",bg='gray')
l_SQ2.place(x=55,y=375)
e_SQ2=OptionMenu(f_signup_2,var_SQ2,*SQ)
e_SQ2.place(x=55,y=400)
l_SQ2_a=Label(f_signup_2,text="Answer:",bg='gray')
l_SQ2_a.place(x=55,y=425)
e_SQ2_a=Entry(f_signup_2,width=30)
e_SQ2_a.place(x=55,y=450)#Entry Page 3

Home_SU=Button(f_signup_2, text='Home',command=Home)
SignUp_SU= Button(f_signup_2, text='Sign Up',command=Add_SignUp)
Login_SU= Button(f_signup_2, text='Login',command=Login)

Login_SU.place(x=55,y=475)
Home_SU.place(x=120,y=475)
SignUp_SU.place(x=195,y=475)

#About Frame
f_about=Frame(main,bg='gray',height=500,width=300)
icon=Label(f_about,image=JD)
icon.place(x=50,y=10)
f1=("Comic Sans MS",16)
Name=Label(f_about,text="DJ Chat Hub",font=f1,bg='gray')
f2=("Times New Roman",10)
Tagline=Label(f_about,text="Get Socially Social",bg='gray',font=f2)
Name.place(x=85,y=210)
Tagline.place(x=95,y=250)

About="This is a Chat App designed by \nJay Sharma and Divyansh Tiwari \nfor Windows.\n\nContact:\njustatrialman@gmail.com"
about_label=Label(f_about,text=About,bg='gray')
about_label.place(x=55,y=300)

Home_about=Button(f_about, text='Home',command=Home)
Home_about.place(x=120,y=410)

#Forgot Password Frame
f_forgot=Frame(main,bg='gray',height=500,width=300)
icon=Label(f_forgot,image=img)
icon.place(x=50,y=10)
f1=("Comic Sans MS",16)
Name=Label(f_forgot,text="DJ Chat Hub",font=f1,bg='gray')
f2=("Times New Roman",10)
Tagline=Label(f_forgot,text="Get Socially Social",bg='gray',font=f2)
Name.place(x=85,y=210)
Tagline.place(x=95,y=250)

fp_username=Label(f_forgot,text="Enter Your Username:",bg='gray')
fp_username.place(x=55,y=300)
fp_user=Entry(f_forgot,width=30)

Next_SQ=Button(f_forgot, text='Next',command=Forgot_Password)
fp_Home=Button(f_forgot, text='Home',command=Home)

#Without Login Operations End here
#After Login:

f_search=Frame(main,bg='black',height=500,width=300)
Search_e_s=Entry(f_search,width=40)
Search_e_s.place(x=0,y=0)
Search_b_s=Button(f_search,text='Search',command=lambda: [unpack_serach(),Search(Search_e_s)])
Search_b_s.place(x=250,y=0)
Home_b_s=Button(f_search,text='Home',command=lambda: [f_login_success.pack(),f_search.pack_forget(),unpack_serach()])
Home_b_s.place(x=0,y=450,width=300)
Log_Out_b_s=Button(f_search,text='Log Out',command=Logout)
Log_Out_b_s.place(x=0,y=475,width=300)

f_profile=Frame(main,bg='black',height=500,width=300)
Search_e_p=Entry(f_profile,width=40)
Search_e_p.place(x=0,y=0)
Search_b_p=Button(f_profile,text='Search',command=lambda: [Search(Search_e_p)])
Search_b_p.place(x=250,y=0)
Home_b_p=Button(f_profile,text='Home',command=lambda: [f_login_success.pack(),f_profile.pack_forget(),unpack_profile()])
Home_b_p.place(x=0,y=450,width=300)
Log_Out_b_p=Button(f_profile,text='Log Out',command=Logout)
Log_Out_b_p.place(x=0,y=475,width=300)

#Pack main frame initially
f.pack()
main.mainloop() 
