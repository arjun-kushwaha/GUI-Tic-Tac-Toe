from tkinter import *
from tkinter import messagebox as msg

root = Tk()
root.geometry('400x400')

#adding title
root.title('TicTocToe Developed By Arjun Kushwaha')

#icon 
root.wm_iconbitmap('tic.ico')

def restart():
    global count, button_color
    count=2 # it icrease at every click as even 0 and odd x

    # initializing empty button
    b1['text']=b2['text']=b3['text']=b4['text']=b5['text']=b6['text']=b7['text']=b8['text']=b9['text']=''
    
    #changing all button color as new game
    b1.configure(background=button_color)
    b2.configure(background=button_color)
    b3.configure(background=button_color)
    b4.configure(background=button_color)
    b5.configure(background=button_color)
    b6.configure(background=button_color)
    b7.configure(background=button_color)
    b8.configure(background=button_color)
    b9.configure(background=button_color)


# checking winning condition 
def win_func():
    global win_color,count 
       #checking horizantol vertical and diagonal whether is same symbol or not  
    if (b1['text'] == 'O' and  b2['text'] == 'O' and  b3['text'] == 'O'):

        # if same symbol then make it win_color color 
        b1.configure(background=win_color)
        b2.configure(background=win_color)
        b3.configure(background=win_color)

        #popup message 
        msg.showinfo('Winner','Player 1 winner !! ')

        #new game start
        restart()

     #checking horizantol vertical and diagonal whether is same symbol or not    
    elif b1['text'] == 'X' and  b2['text'] == 'X' and  b3['text'] == 'X':

        b1.configure(background=win_color)
        b2.configure(background=win_color)
        b3.configure(background=win_color)
        # b1.configure(fg='blue')
        # b2.configure(fg='blue')
        # b3.configure(fg='blue')
        msg.showinfo('Winner','Player 2 winner !! ')
        restart()

     #checking horizantol vertical and diagonal whether is same symbol or not   
    elif b4['text'] == 'O' and  b5['text'] == 'O' and  b6['text'] == 'O':
        b4.configure(background=win_color)
        b5.configure(background=win_color)
        b6.configure(background=win_color)
        msg.showinfo('Winner','Player 1 winner !! ')
        restart()

    #checking horizantol vertical and diagonal whether is same symbol or not 
    elif b4['text'] == 'X' and  b5['text'] == 'X' and  b6['text'] == 'X':
        b4.configure(background=win_color)
        b5.configure(background=win_color)
        b6.configure(background=win_color)
        msg.showinfo('Winner','Player 2 winner !! ')
        restart()
     
     #checking horizantol vertical and diagonal whether is same symbol or not 
    elif b7['text'] == 'O' and  b8['text'] == 'O' and  b9['text'] == 'O':
        b7.configure(background=win_color)
        b8.configure(background=win_color)
        b9.configure(background=win_color)
        msg.showinfo('Winner','Player 1 winner !! ')
        restart()
    
    #checking horizantol vertical and diagonal whether is same symbol or not 
    elif b7['text'] == 'X' and  b8['text'] == 'X' and  b9['text'] == 'X':
        b7.configure(background=win_color)
        b8.configure(background=win_color)
        b9.configure(background=win_color)
        msg.showinfo('Winner','Player 2 winner !! ')
        restart()

    #checking horizantol vertical and diagonal whether is same symbol or not 
    elif b1['text'] == 'O' and  b4['text'] == 'O' and  b7['text'] == 'O':
        b1.configure(background=win_color)
        b4.configure(background=win_color)
        b7.configure(background=win_color)
        msg.showinfo('Winner','Player 1 winner !! ')
        restart()

    elif b1['text'] == 'X' and  b4['text'] == 'X' and  b7['text'] == 'X':
        b1.configure(background=win_color)
        b4.configure(background=win_color)
        b7.configure(background=win_color)
        msg.showinfo('Winner','Player 2 winner !! ')
        restart()

    elif b2['text'] == 'O' and  b5['text'] == 'O' and  b8['text'] == 'O':
        b2.configure(background=win_color)
        b5.configure(background=win_color)
        b8.configure(background=win_color)
        msg.showinfo('Winner','Player 1 winner !! ')
        restart()
    elif b2['text'] == 'X' and  b5['text'] == 'X' and  b8['text'] == 'X':
        b2.configure(background=win_color)
        b5.configure(background=win_color)
        b8.configure(background=win_color)
        msg.showinfo('Winner','Player 2 winner !! ')
        restart()

    elif b3['text'] == 'O' and  b6['text'] == 'O' and  b9['text'] == 'O':
        b3.configure(background=win_color)
        b6.configure(background=win_color)
        b9.configure(background=win_color)
        msg.showinfo('Winner','Player 1 winner !! ')
        restart()
    elif b3['text'] == 'X' and  b6['text'] == 'X' and  b9['text'] == 'X':
        b3.configure(background=win_color)
        b6.configure(background=win_color)
        b9.configure(background=win_color)
        msg.showinfo('Winner','Player 2 winner !! ')
        restart()

    elif b1['text'] == 'O' and  b5['text'] == 'O' and  b9['text'] == 'O':
        b1.configure(background=win_color)
        b5.configure(background=win_color)
        b9.configure(background=win_color)
        msg.showinfo('Winner','Player 1 winner !! ')
        restart()
    elif b1['text'] == 'X' and  b5['text'] == 'X' and  b9['text'] == 'X':
        b1.configure(background=win_color)
        b5.configure(background=win_color)
        b9.configure(background=win_color)
        msg.showinfo('Winner','Player 2 winner !! ')
        restart()

    elif b3['text'] == 'O' and  b5['text'] == 'O' and  b7['text'] == 'O':
        b3.configure(background=win_color)
        b5.configure(background=win_color)
        b7.configure(background=win_color)
        msg.showinfo('Winner','Player 1 winner !! ')
        restart()
    elif b3['text'] == 'X' and  b5['text'] == 'X' and  b7['text'] == 'X':
        b3.configure(background=win_color)
        b5.configure(background=win_color)
        b7.configure(background=win_color)
        msg.showinfo('Winner','Player 2 winner !! ')
        restart()
        #if x values is 11 means all button is filled and above no condition is satisfied then Draw
    else:
        if count==11:
            b1.configure(background='#062c8c')
            b2.configure(background='#062c8c')
            b3.configure(background='#062c8c')
            b4.configure(background='#062c8c')
            b5.configure(background='#062c8c')
            b6.configure(background='#062c8c')
            b7.configure(background='#062c8c')
            b8.configure(background='#062c8c')
            b9.configure(background='#062c8c')
            msg.showinfo("Draw"," Game Draw !! ")
            restart()
            




#function to place O and X 
def getval(button):
    global count
    if button['text'] =='':
        if count %2==0:
            button['text'] = 'O'
            count += 1
        else:
            button['text'] = 'X'
            count += 1
    win_func()

# button color 
button_color = '#072a40'
win_color = '#07f3fb'
fg_color = 'white'
count = 2

# Specify Grid to fit window 
Grid.rowconfigure(root,0,weight=1)
Grid.rowconfigure(root,1,weight=1)
Grid.rowconfigure(root,2,weight=1)
Grid.columnconfigure(root,0,weight=1)
Grid.columnconfigure(root,1,weight=1)
Grid.columnconfigure(root,2,weight=1)

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

