from tkinter import *
from tkinter import messagebox

conta = Tk()

user_text = StringVar()
def venky():
        messagebox.showinfo("Venky", "This software is coded by Vyankatesh Pipalwa")
def show_message():
        messagebox.showinfo("VPN","Your VPN file is generated.")

def delete_message():
        e1.delete(0, END)

def write_fun():
        User = user_text.get()
        if User:
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
necli connect -s 125.99.72.34:4433 -d LocalDomain -u {User} -p Dahotre@2022
pause
)
if %input%==2 (
necli disconnect
pause
)
if %input%==3 (
necli connect -s 114.143.49.126:4433 -d LocalDomain -u {User} -p Dahotre@2022
pause
)else (
echo Wrong Option
goto :a
)
                ''')
                file.close()
                show_message()
                delete_message()
        else:
                messagebox.showwarning("Warning", "Please enter username in the field!")

conta.title("VPN Maker")
conta.geometry("300x130")
# conta.maxsize(350, 200)
conta.config(bg="lightblue")
user_label = Label(conta, text='User Name:')
user_label.grid(row=0, column=1, padx=25, pady=25)
e1 = Entry(conta, textvariable=user_text, bd=2)
e1.grid(row=0, column=2)

button = Button(conta, text='Generate', width=10, command=write_fun, activebackground='#78d6ff')
button.grid(row=2, column=2, padx=50, pady=5)
menu = Menu(conta)
conta.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Exit', command=conta.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About', command=venky)
conta.mainloop()