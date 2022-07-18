from tkinter import *
from tkinter import messagebox as msg

root = Tk()
root.geometry('400x400')

#adding title
root.title('TicTocToe Developed By Arjun Kushwaha')

#icon 
root.wm_iconbitmap('tic.ico')

def getval(button):
    global count
    if button['text'] =='':
        if count %2==0:
            button['text'] = 'O'
            count += 1
        else:
            button['text'] = 'X'
            count += 1


# Specify Grid to fit window 
Grid.rowconfigure(root,0,weight=1)
Grid.rowconfigure(root,1,weight=1)
Grid.rowconfigure(root,2,weight=1)
Grid.columnconfigure(root,0,weight=1)
Grid.columnconfigure(root,1,weight=1)
Grid.columnconfigure(root,2,weight=1)

# button color 
button_color = '#072a40'
fg_color = 'white'
count = 2

# creating 3x3 buttons 
b1 = Button(root,text='',bg=button_color, command=lambda:getval(b1),fg=fg_color,font='Arial 35 bold',width=7,height=3)
b1.grid(row=0,column=0,sticky=NSEW)

b2 = Button(root,text='',bg=button_color,command=lambda:getval(b2),fg=fg_color,font='Arial 35 bold',width=7,height=3)
b2.grid(row=0,column=1,sticky=NSEW)

b3 = Button(root,text='',bg=button_color,command=lambda:getval(b3),fg=fg_color,font='Arial 35 bold',width=7,height=3)
b3.grid(row=0,column=2,sticky=NSEW)

b4 = Button(root,text='',bg=button_color,command=lambda:getval(b4),fg=fg_color,font='Arial 35 bold',width=7,height=3)
b4.grid(row=1,column=0,sticky=NSEW)

b5 = Button(root,text='',bg=button_color,command=lambda:getval(b5),fg=fg_color,font='Arial 35 bold',width=7,height=3)
b5.grid(row=1,column=1,sticky=NSEW)

b6 = Button(root,text='',bg=button_color,command=lambda:getval(b6),fg=fg_color,font='Arial 35 bold',width=7,height=3)
b6.grid(row=1,column=2,sticky=NSEW)

b7 = Button(root,text='',bg=button_color,command=lambda:getval(b7),fg=fg_color,font='Arial 35 bold',width=7,height=3)
b7.grid(row=2,column=0,sticky=NSEW)

b8 = Button(root,text='',bg=button_color,command=lambda:getval(b8),fg=fg_color,font='Arial 35 bold',width=7,height=3)
b8.grid(row=2,column=1,sticky=NSEW)

b9 = Button(root,text='',bg=button_color,command=lambda:getval(b9),fg=fg_color,font='Arial 35 bold',width=7,height=3)
b9.grid(row=2,column=2,sticky=NSEW)



root.mainloop()

