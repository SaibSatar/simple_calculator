from tkinter import*
from tkinter.font import *
#import math


def calc(number):
    global adad
    #valau=(entry.get())
    adad=adad+str(number)
    voroodi.set(adad)#عدد رو روی ورودی ست بکن

def clear():
    global adad
    adad=""#رشته عدد رو پاک کن 
    voroodi.set(adad)
#def delet():
    #entry.delet(END)
def out():
    global adad
    out_put=str(eval(adad))
    print(out_put)
    voroodi.set(out_put)
    adad=out_put
    

window=Tk()
window.title('simple Calculater')
adad=""
voroodi=StringVar()
my_font=Font(family='arial',size=19)
my_font_s=Font(family='conso',size=20)

#lab=Label(window,text='simple caceulation')
#lab.grid(row=0,column=0,sticky=E+N,padx=100)
#tm.sleep(4)
lab=Label(window,text='design by Abolfazl',font=('arial',10,'bold'))
lab.grid(row=0,column=0,sticky=E+N,padx=100)
#tm.sleep(2)
#lab=Label(window,text='')
#lab.grid(row=0,column=0,sticky=E+N,padx=100)

entry=Entry(window,font=('Bnazanin',20,'bold'),textvariable=voroodi,bg="powder blue",justify= 'left',bd=30)
entry.grid(row=1,column=0,columnspan=4)

button_plus=Button(window,text='+',font=('arial',20,'bold'),command=lambda:calc("+"),bd=8)
button_plus.grid(row=2,column=0,sticky=E+N,padx=10)
button_sum=Button(window,text='--',font=('arial',20,'bold'),command=lambda:calc("-"),bd=8)
button_sum.grid(row=3,column=0,sticky=E+N,padx=10)
button_div=Button(window,text='÷',font=('arial',20,'bold'),command=lambda:calc("/"),bd=8)
button_div.grid(row=4,column=0,sticky=E+N,padx=10,pady=0)
button_zarb=Button(window,text='×',font=('arial',20,'bold'),command=lambda:calc("*"),bd=8)
button_zarb.grid(row=5,column=0,sticky=E,padx=10,pady=0)
button_mosavi=Button(window,text='=',font=('arial',20,'bold'),command=out,bd=8)
button_mosavi.grid(row=6,column=0,sticky=E,padx=10,pady=0)
button_dot=Button(window,text='.',font=('arial',20,'bold'),command=lambda:calc("."),bd=8)
button_dot.grid(row=5,column=0,sticky=W,padx=65,pady=5)
#button_cos=Button(window,text='cos(',font=('arial',20,'bold'),command=lambda:calc("cos"),bd=8)
#button_cos.grid(row=2,column=0,sticky=W,padx=225,pady=5)
button_zero=Button(window,text='0',font=('arial',20,'bold'),command=lambda:calc("0"),bd=8)
button_zero.grid(row=2,column=0,sticky=W,padx=10,pady=5)
button_one=Button(window,text='1',font=('arial',20,'bold'),command=lambda:calc(1),bd=8)
button_one.grid(row=2,column=0,sticky=W,padx=65,pady=5)
button_two=Button(window,text='2',font=('arial',20,'bold'),command=lambda:calc("2"),bd=8)
button_two.grid(row=2,column=0,sticky=W,padx=121,pady=5)
button_three=Button(window,text='3',font=('arial',20,'bold'),command=lambda:calc("3"),bd=8)
button_three.grid(row=3,column=0,sticky=W,padx=10,pady=5)
button_four=Button(window,text='4',font=('arial',20,'bold'),command=lambda:calc("4"),bd=8)
button_four.grid(row=3,column=0,sticky=W,padx=65,pady=5)
button_five=Button(window,text='5',font=('arial',20,'bold'),command=lambda:calc("5"),bd=8)
button_five.grid(row=3,column=0,sticky=W,padx=121,pady=5)
button_six=Button(window,text='6',font=('arial',20,'bold'),command=lambda:calc("6"),bd=8)
button_six.grid(row=4,column=0,sticky=W,padx=10,pady=5)
button_seven=Button(window,text='7',font=('arial',20,'bold'),command=lambda:calc("7"),bd=8)
button_seven.grid(row=4,column=0,sticky=W,padx=65,pady=5)
button_eight=Button(window,text='8',font=('arial',20,'bold'),command=lambda:calc("8"),bd=8)
button_eight.grid(row=4,column=0,sticky=W,padx=121,pady=5)
button_nine=Button(window,text='9',font=('arial',20,'bold'),command=lambda:calc("9"),bd=8)
button_nine.grid(row=5,column=0,sticky=W,padx=10,pady=5)
button_triangle=Button(window,text='#',font=('arial',20,'bold'),command=lambda:calc("#"),bd=8)
button_triangle.grid(row=5,column=0,sticky=W,padx=121,pady=5)
#button_delet=Button(window,text='delet',font=my_font_s,command=delet)
#button_delet.grid(row=5,column=0,padx=65,pady=5)
button_clear=Button(window,text='clear',font=('arial',20,'bold'),command=clear,bd=20,bg='green')
button_clear.grid(row=6,column=0,padx=10,pady=5,columnspan=2,sticky=W+N)
window.mainloop()
#این برنامه در تاریخ 7 بهمن 1401 تدوین شده است 
#ورژن یک