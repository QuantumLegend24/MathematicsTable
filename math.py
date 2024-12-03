from tkinter import *
from tkinter.ttk import *

santa = Tk()
santa.title("MATHS TABLE")

title=Label(santa,text="Mathematical Table Generator (MTG)",font=("calibri",30,"bold"))
title.grid(row=0,column=0,columnspan=3,pady=25)

numinrange=Label(santa,text="Number and Range:",font=("calibri",15,"bold"))
numinrange.grid(row=1,column=0,padx=10)

theNum=IntVar()
numbers=Combobox(santa,textvariable=theNum,width=5)
numbers["values"]=tuple(range(100001))
numbers.grid(column=1,row=1)

endVal=IntVar()
pikachu=Radiobutton(santa,text="10",variable=endVal,value=10)
pikachu.grid(column=2,row=1)

doraemon=Radiobutton(santa,text="20",variable=endVal,value=20)
doraemon.grid(column=2,row=2,padx=30)

team_dragon=Radiobutton(santa,text="30",variable=endVal,value=30)
team_dragon.grid(column=2,row=3,padx=30)

demon_slayer=Radiobutton(santa,text="40",variable=endVal,value=40)
demon_slayer.grid(column=2,row=4,padx=30)

sinchan=Radiobutton(santa,text="50",variable=endVal,value=50)
sinchan.grid(column=2,row=5,padx=30)

endVal.set(10)


def nobita():
    tables=""
    for i in range(endVal.get()+1):
        tables+=str(theNum.get())+"  X  "+str(i)+"    =    "+str(theNum.get()*i)+"\n"
    answer.configure(text=tables)

generate=Button(santa,text="Generate",command=nobita)
generate.grid(column=1,row=4)

answer=Label(santa,anchor="center")
answer.grid(row=6,column=1,pady=25)


santa.mainloop()