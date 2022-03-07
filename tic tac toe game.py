from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("TIC TAC TOE GAME ")

p1=StringVar
p2=StringVar


counter=1
flag=True

def playbutton(btn):
        global flag,counter
        if btn["text"]==" " and flag==True:
                flag=False
                btn["text"]="X"
                counter=counter+1
                check()
        elif btn["text"]==" " and flag==False:
                flag=True
                btn["text"]="O"
                counter+=1
                check()
        else:
                messagebox.showinfo("tic tac toe","not allowed")

def clearbutton():
        button1["text"]=" "
        button2["text"]=" "
        button3["text"]=" "
        button4["text"]=" "
        button5["text"]=" "
        button6["text"]=" "
        button7["text"]=" "
        button8["text"]=" "
        button9["text"]=" "

def check():
        global counter
        if (button1["text"]=="X"and button2["text"]=="X"and button3["text"]=="X" or
           button4["text"]=="X"and button5["text"]=="X"and button6["text"]=="X" or
           button7["text"]=="X"and button8["text"]=="X"and button9["text"]=="X" or
           button1["text"]=="X"and button4["text"]=="X"and button7["text"]=="X"or
           button2["text"]=="X"and button5["text"]=="X"and button8["text"]=="X"or
           button3["text"]=="X"and button6["text"]=="X"and button9["text"]=="X"or
           button1["text"]=="X"and button5["text"]=="X"and button9["text"]=="X"or
           button3["text"]=="X"and button5["text"]=="X"and button7["text"]=="X"):
                clearbutton()
                messagebox.showinfo("tic tac toe","player 1 win")
                counter=0
        elif (button1["text"]=="O"and button2["text"]=="O"and button3["text"]=="O" or
              button4["text"]=="O"and button5["text"]=="O"and button6["text"]=="O"or
              button7["text"]=="O"and button8["text"]=="O"and button9["text"]=="O"or
              button1["text"]=="O"and button4["text"]=="O"and button7["text"]=="O"or
              button2["text"]=="O"and button5["text"]=="O"and button8["text"]=="O"or
              button3["text"]=="O"and button6["text"]=="O"and button9["text"]=="O"or
              button1["text"]=="O"and button5["text"]=="O"and button9["text"]=="O"or
              button3["text"]=="O"and button5["text"]=="O"and button7["text"]=="O"):
                clearbutton()
                messagebox.showinfo("tic tac toe","player 2 win")
                counter=0
        elif(counter==8):
                messagebox.showinfo("tic tac toe","mathch has been tie")

button1=Button(window,text=" ",bg="yellow",fg="black",height=3,width=5,bd=5,command=lambda:playbutton(button1))
button1.grid(row=0,column=0)
button2=Button(window,text=" ",bg="yellow",fg="black",height=3,width=5,bd=5,command=lambda:playbutton(button2))
button2.grid(row=0,column=1)
button3=Button(window,text=" ",bg="yellow",fg="black",height=3,width=5,bd=5,command=lambda:playbutton(button3))
button3.grid(row=0,column=2)
button4=Button(window,text=" ",bg="yellow",fg="black",height=3,width=5,bd=5,command=lambda:playbutton(button4))
button4.grid(row=1,column=0)
button5=Button(window,text=" ",bg="yellow",fg="black",height=3,width=5,bd=5,command=lambda:playbutton(button5))
button5.grid(row=1,column=1)
button6=Button(window,text=" ",bg="yellow",fg="black",height=3,width=5,bd=5,command=lambda:playbutton(button6))
button6.grid(row=1,column=2)
button7=Button(window,text=" ",bg="yellow",fg="black",height=3,width=5,bd=5,command=lambda:playbutton(button7))
button7.grid(row=2,column=0)
button8=Button(window,text=" ",bg="yellow",fg="black",height=3,width=5,bd=5,command=lambda:playbutton(button8))
button8.grid(row=2,column=1)
button9=Button(window,text=" ",bg="yellow",fg="black",height=3,width=5,bd=5,command=lambda:playbutton(button9))
button9.grid(row=2,column=2)

window.mainloop()