from tkinter import *
from tkinter import messagebox

conta = Tk()
# Variables to store
user_text = StringVar()
user_text2 = StringVar()
user_text3 = StringVar()
user_text4 = StringVar()

def venky():
        messagebox.showinfo("Venky", "This software is coded by Vyankatesh Pipalwa")

def show_message():
        messagebox.showinfo("VPN","Your VPN file is generated.")

def delete_message():
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)

def write_fun():
        User = user_text.get()
        Pass = user_text2.get()
        Host = user_text3.get()
        Domain = user_text4.get()

        if User and Pass and Host and Domain:
                file = open('VPN.bat', 'w')
                file.write(f'''
@echo off
echo.
color 0a
:a
echo Press 1 to Connect 
echo Press 2 to Disconnect
echo Press 3 to Connect(2)
set /p input=""
echo.
set PATH=%PATH%;"%ProgramFiles(x86)%\\SonicWall\\SSL-VPN\\NetExtender" 
set PATH=%PATH%;"%ProgramFiles%\\SonicWall\\SSL-VPN\\NetExtender"
if %input%==1 (
necli connect -s {Host} -d {Domain} -u {User} -p {Pass}
pause
)
if %input%==2 (
necli disconnect
pause
)else (
echo Wrong Option
goto :a
)
                ''')
                file.close()
                show_message()
                delete_message()
        elif len(user_text.get()) == 0:
                messagebox.showwarning("Warning", "Please enter username in the field!")
        elif len(user_text2.get()) == 0:
                messagebox.showwarning("Warning", "Please enter password in the field!")
        elif len(user_text3.get()) == 0:
                messagebox.showwarning("Warning", "Please enter Host IP in the field!")
        elif len(user_text4.get()) == 0:
                messagebox.showwarning("Warning", "Please enter Domain in the field!")

conta.title("VPN Script Maker")
conta.geometry("360x360")
conta.config(bg="lightblue")
# Username
user_label = Label(conta, text='User Name:')
user_label.grid(row=0, column=1, padx=25, pady=25)
e1 = Entry(conta, textvariable=user_text, bd=2)
e1.grid(row=0, column=2)
# Password
user_label2 = Label(conta, text='Password:')
user_label2.grid(row=1, column=1, padx=25, pady=25)
e2 = Entry(conta, textvariable=user_text2, bd=2)
e2.grid(row=1, column=2)
# Host IP
user_label3 = Label(conta, text='Host IP:')
user_label3.grid(row=2, column=1, padx=25, pady=25)
e3 = Entry(conta, textvariable=user_text3, bd=2)
e3.grid(row=2, column=2)
# Domain Name
user_label4 = Label(conta, text='Domain Name:')
user_label4.grid(row=3, column=1, padx=25, pady=25)
e4 = Entry(conta, textvariable=user_text4, bd=2)
e4.grid(row=3, column=2)
# Button
button = Button(conta, text='Generate', width=10, command=write_fun, activebackground='#78d6ff')
button.grid(row=4, column=2, padx=50, pady=5)
# Menu
menu = Menu(conta)
conta.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Exit', command=conta.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About', command=venky)
conta.mainloop()