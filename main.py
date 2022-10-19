from tkinter import *
from tkinter import messagebox
count=0
turn=True
def disable():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)



def win():
    global winner
    winner=False

    if b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        messagebox.showinfo(message="CONGRATULATION!!! X WONNNNN")
        disable()
    elif b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        messagebox.showinfo(message="CONGRATULATION!!! X WONNNNN")
        disable()
    elif b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        messagebox.showinfo(message="CONGRATULATION!!! X WONNNNN")
        disable()
    elif b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        messagebox.showinfo(message="CONGRATULATION!!! X WONNNNN")
        disable()
    elif b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        messagebox.showinfo(message="CONGRATULATION!!! X WONNNNN")
        disable()
    elif b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        messagebox.showinfo(message="CONGRATULATION!!! X WONNNNN")
        disable()
    elif b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        messagebox.showinfo(message="CONGRATULATION!!! X WONNNNN")
        disable()
    elif b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X":
        b7.config(bg="red")
        b5.config(bg="red")
        b3.config(bg="red")
        messagebox.showinfo(message="CONGRATULATION!!! X WONNNNN")
        disable()
    if b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        messagebox.showinfo(message="CONGRATULATION!!! X WONNNNN")
        disable()
    elif b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        messagebox.showinfo(message="CONGRATULATION!!! X WONNNNN")
        disable()
    elif b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        messagebox.showinfo(message="CONGRATULATION!!! X WONNNNN")
        disable()
    elif b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        messagebox.showinfo(message="CONGRATULATION!!! X WONNNNN")
        disable()
    elif b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        messagebox.showinfo(message="CONGRATULATION!!! X WONNNNN")
        disable()
    elif b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        messagebox.showinfo(message="CONGRATULATION!!! X WONNNNN")
        disable()
    elif b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        messagebox.showinfo(message="CONGRATULATION!!! X WONNNNN")
        disable()
    elif b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O":
        b7.config(bg="red")
        b5.config(bg="red")
        b3.config(bg="red")
        messagebox.showinfo(message="CONGRATULATION!!! X WONNNNN")
        disable()

def buttonclicked(b):
    global count,turn
    if b["text"]==" " and turn==True:
        b["text"]="X"
        turn=False
        count+=1
        win()
    elif b["text"]==" " and turn==False:
        b["text"] = "O"
        turn = True
        count += 1
        win()
    else:
        messagebox.showerror(message="You Cant click twice ")


window=Tk()
window.title("Tic Tac Toe Game")
b1=Button(text=" ",font=("Arial",15,"normal"),width=6,height=3,command=lambda:buttonclicked(b1))
b1.grid(row=0,column=0)
b2=Button(text=" ",width=6,height=3,command=lambda:buttonclicked(b2))
b2.grid(row=0,column=1)
b3=Button(text=" ",width=6,height=3,command=lambda:buttonclicked(b3))
b3.grid(row=0,column=2)
b4=Button(text=" ",width=6,height=3,command=lambda:buttonclicked(b4))
b4.grid(row=1,column=0)
b5=Button(text=" ",width=6,height=3,command=lambda:buttonclicked(b5))
b5.grid(row=1,column=1)
b6=Button(text=" ",width=6,height=3,command=lambda:buttonclicked(b6))
b6.grid(row=1,column=2)
b7=Button(text=" ",width=6,height=3,command=lambda:buttonclicked(b7))
b7.grid(row=2,column=0)
b8=Button(text=" ",width=6,height=3,command=lambda:buttonclicked(b8))
b8.grid(row=2,column=1)
b9=Button(text=" ",width=6,height=3,command=lambda:buttonclicked(b9))
b9.grid(row=2,column=2)

window.mainloop()