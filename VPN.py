from tkinter import *
from tkinter import messagebox


container = Tk()


# Variables to store
userVar = StringVar()
passVar = StringVar()
hostVar = StringVar()
domainVar = StringVar()


def about():
        messagebox.showinfo("About", "This software is coded by Vyankatesh Pipalwa")


def compati():
        #Compatibility
        messagebox.showinfo("Compatibility","This software is compatible with all Windows operating systems.")


def how():
        #How to
        messagebox.showinfo("How to use"," 1)Add Username in the user field.\n 2)Add Password in the pass field.\n 3)Add ip address in the host field.\n 4)Add domain name in the domain field.\n 5)Press Generate that's it.\n\n Note: You should have Sonicwall Netextender installed to use generated script.")


def show_message():
        #Done message
        messagebox.showinfo("Done","Your VPN file is generated.")


def delEntry():
        #Delete entry box characters
        userEntry.delete(0, END)
        passEntry.delete(0, END)
        hostEntry.delete(0, END)
        domainEntry.delete(0, END)


def write_fun():
        #Write function to process
        User = userVar.get()
        Pass = passVar.get()
        Host = hostVar.get()
        Domain = domainVar.get()

        if User and Pass and Host and Domain:
                file = open('VPN.bat', 'w')
                #Writing script 
                file.write(f'''
@echo off
echo.
color 0a
:a
echo Press 1 to Connect 
echo Press 2 to Disconnect
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
                delEntry()
        elif len(userVar.get()) == 0:
                #Checking that username field is empty
                messagebox.showwarning("Warning", "Please enter username in the field!")
        elif len(passVar.get()) == 0:
                #Checking that password field is empty
                messagebox.showwarning("Warning", "Please enter password in the field!")
        elif len(hostVar.get()) == 0:
                #Checking that host ip field is empty
                messagebox.showwarning("Warning", "Please enter Host IP in the field!")
        elif len(domainVar.get()) == 0:
                #Checking that domain field is empty
                messagebox.showwarning("Warning", "Please enter Domain in the field!")


#Title
container.title("VPN Script Maker")
#Width X Height
container.geometry("360x360")
#Background color
container.config(bg="lightblue")
#Icon
container.iconbitmap('D:\PycharmProjects\Exit_Message\logoV2.ico')

# Username
userLabel = Label(container, text='User Name:')
userLabel.grid(row=0, column=1, padx=25, pady=25)
userEntry = Entry(container, textvariable=userVar, bd=2)
userEntry.grid(row=0, column=2)


# Password
passLabel = Label(container, text='Password:')
passLabel.grid(row=1, column=1, padx=25, pady=25)
passEntry = Entry(container, textvariable=passVar, bd=2)
passEntry.grid(row=1, column=2)


# Host IP
hostLabel = Label(container, text='Host IP:')
hostLabel.grid(row=2, column=1, padx=25, pady=25)
hostEntry = Entry(container, textvariable=hostVar, bd=2)
hostEntry.grid(row=2, column=2)


# Domain Name
domainLabel = Label(container, text='Domain Name:')
domainLabel.grid(row=3, column=1, padx=25, pady=25)
domainEntry = Entry(container, textvariable=domainVar, bd=2)
domainEntry.grid(row=3, column=2)


# Button
generateButton = Button(container, text='Generate', width=10, command=write_fun, activebackground='#78d6ff')
generateButton.grid(row=4, column=2, padx=50, pady=5)


# Menu
menu = Menu(container)
container.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Exit', command=container.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About', command=about)
helpmenu.add_command(label='Compatibility', command=compati)
helpmenu.add_command(label='How', command=how)
container.mainloop()

