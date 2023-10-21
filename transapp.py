from tkinter import *
import socket
from tkinter import filedialog
from tkinter import messagebox
import os

root =Tk()
root.title("Trans")
root.geometry("550x560+300+200")
root.configure(bg="black")
root.resizable(False,False)

def select_file():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                        title='select image file',
                                        filetypes=(('file_type','*.txt'),('all files','*.*')))
def sender():
    s=socket.socket()
    host=socket.gethostbyname()
    port=8080
    s.bind((host,port))
    s.listen(1)
    print(host)
    print('wating for any incoming connections...')
    conn,addr=s.accept()
    file=open(filename,'rb')
    file_data=file.read(1024)
    conn.send(file_data)
    print("data has been transmitted successfully..")
    

def send():
    main=Toplevel(root)
    main.title("send")
    main.geometry("550x560+300+200")
    main.configure(bg="#f4fdfe")
    main.resizable(False,False)

    image_icon1=PhotoImage(file="share-icon-qvb.png")
    main.iconphoto(False,image_icon1)
    Sbackground=PhotoImage(file="sender.png")
    Label(main,image=Sbackground).place(x=2,y=0)

    Mbackground=PhotoImage(file="share-icon-qvb.png")
    Label(main,image=Mbackground,bg='#f4fdfe').place(x=170,y=260)

    host=socket.gethostname()
    Label(main,text=f'ID:{host}',bg='white',fg='black').place(x=140,y=290)

    Button(main,text="+select file",width=10,height=1,font='arial 14 bold',bg="#fff",fg="#000",command=select_file).place(x=160,y=150)
    Button(main,text="send",width=10,height=1,font='arial 14 bold',bg="#fff",fg="#000").place(x=300,y=150)
    
    main.mainloop()

def receive():
    main=Toplevel(root)
    main.title("Receive")
    main.geometry("550x560+300+200")
    main.configure(bg="#f4fdfe")
    main.resizable(False,False)

    def receiver():
        ID=senderID.get()
        filename1=incoming_file.get()

        s=socket.socket()
        port=8080
        s.connect((ID,port))
        file=open(filename1,'wb')
        file_data=s.recv(1024)
        file.write(file_data)
        file.close()
        print("file has been receive ")


    #icon
    image_icon1=PhotoImage(file="share-icon-qvb.png")
    main.iconphoto(False,image_icon1)

    Hbackground=PhotoImage(file="received-design-sketch-name - Copy.png")
    Label(main,image=Hbackground).place(x=2,y=0)
    logo=PhotoImage(file='R.png')
    Label(main,image=logo,bg="#f4fdfe").place(x=10,y=250)

    Label(main,text="Receive",font=('arial',20),bg="#f4fefd").place(x=100,y=280)

    Label(main,text="input sender ID",font=('arial',10,'bold'),bg="#f4fefd").place(x=20,y=340)
    senderID=Entry(main,width=25,fg="black",border=2,bg="white",font=('arial',15))
    senderID.place(x=20,y=370)
    senderID.focus()

    Label(main,text="filename for the incoming file",font=('arial',10,'bold'),bg="#f4fdfe").place(x=20,y=420)
    incoming_file= Entry(main,width=25,fg="black",border=2,bg='white',font=('arial',15))
    incoming_file.place(x=20,y=450)
    
    image_icon=PhotoImage(file="unnamed.png")
    rr=Button(main,text="Receive",command=LEFT,image=image_icon,width=130,bg="#39c790",font="arial 14 bold",compound=receiver)
    rr.place(x=20,y=500)


    main.mainloop()
#icon
image_icon=PhotoImage(file="share-icon-qvb.png")
root.iconphoto(False,image_icon)

Label(root,text="File Transfer",font=('Acumin Variable concept',20,'bold'),bg="#f4fdfe").place(x=20,y=30)
Frame(root,width=400,height=2,bg="#f3f5f6").place(x=25,y=80)

send_image=PhotoImage(file="OIP.png")
send=Button(root,image=send_image,bg="#f4fdfe",bd=0,command=send)
send.place(x=50,y=100)

receive_image=PhotoImage(file="unnamed.png")
receive=Button(root,image=receive_image,bg="#f4fdfe",bd=0,command=receive)
receive.place(x=300,y=100)

#label
Label(root,text="send",font=('Acumin Variable Concept',17,'bold'),bg="#f4fdfe").place(x=65,y=200)
Label(root,text="Receive",font=('Acumin Variable Concept',17,'bold'),bg="#f4fdfe").place(x=300,y=200)

background=PhotoImage(file="share.png")
Label(root,image=background).place(x=2,y=323)

root.mainloop()