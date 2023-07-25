from tkinter import*
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import Menu
import math

#question0 = "calculator"
#print(question0)
#name =input()
#print("Hello "+name.capitalize()+"!")
frame = Tk()


def info(value):
    if value == 0:
        messagebox.showinfo("information","""HELLO USER ,IF YOU FOUND ANY BUG OR ERROR PLEASE REPORT TO THE DEVELOPER
REPORT THE BUG TO THIS EMAL ID: alstine.santosh@gmail.com""")



menubar = Menu(frame)
frame.config(menu=menubar)
about_us=Menu(menubar)
#menubar.add_cascade(label="about us",menu=about_us)
menubar.add_command(label="Information",command=lambda:info(0))

frame.geometry("300x425")
frame.resizable(False,False)
frame.iconbitmap("favicon.ico")
frame.title("Calculator(MPG)")
frame.image = Image.open('bgcalculator1.png')
frame.python_image = ImageTk.PhotoImage(frame.image)
hlo = Label(frame, image=frame.python_image).pack()
#icon= os.path.join(sys.path[0],'C:/Users/user/Desktop/pythonproject/bgcalculator.png')
#img = PhotoImage(file="Calculator.ico")
#frame.iconphoto(False, img)
#frame.iconbitmap=('favicon.ico')
#label = Label(frame,text=bgimg, font=("Arial",20))
#label.pack(pady=20)
frame.config(bg="black")




labelhlp=Label(text="",bg="#000099",padx=150,pady=35).place(x=0,y=50-20)
labelhlo=Label(text="",bg="black",padx=138,pady=25).place(x=10,y=60-20)
label3=Label(text="",bg="white",padx=200,pady=3)#image=bgimg)
label3.pack()
#labelhlp=Label(text="",bg="white",padx=180,pady=3).place(x=0,y=0)
#butinfo=Button(text="information",command = lambda: info(0),bg ="white",activebackground="white")
#butinfo.place(x=0)



displayint = []
labelA= Label(frame, text = "",bg ="black",fg="white",padx=10,pady=21,font=("Arial",15))
labelA.place(x=9,y=60-20)

intgerint = [0,1,2,3,4,5,6,7,8,9]
intgerstr = ["0","1","2","3","4","5","6","7","8","9"]

number =""
answer=""

displayint = [1,45]
def display(value):
    global number
    global answer
   


            
    try:
        if number =="":
                  
 #first number in the label
             
            if value == " / ":
                number=""
                labelA.config(text=number)

            elif value == " + ":
                number=""
                labelA.config(text=number)

            elif value == " - ":
                number=""
                labelA.config(text=number)

            elif value == " * ":
                number=""
                labelA.config(text=number)
                
            elif value == " % ":
                number=""
                labelA.config(text=number)
                

        
                    
                
            elif value =="0"or"1"or"2"or"3"or"4"or"5"or"6"or"7"or"8"or"9"or".":
                number=value
                labelA.config(text=number)


# the other number in the label
                
        elif number != "":
            if number[-1] == ".":
                if value ==".":
                    number+=""
                elif value ==" / ":
                    number+=""
                elif value ==" + ":
                    number+=""
                elif value ==" - ":
                    number+=""
                elif value ==" * ":
                    number+=""
    
                 #   labelA.config(text=number)
                    #if value == " * ":
                    #    number+=""
                      #  labelA.config(text=number)
                elif value =="0"or"1"or"2"or"3"or"4"or"5"or"6"or"7"or"8"or"9":
                    number+=value
                    labelA.config(text=number)

# To add number with mathamathical symbols

            elif number[-1] == " ":
                if value == " / ":#or" . "or" + "or" * "or" - ":
                    number+=""
                    labelA.config(text=number)
                elif value == " * ":
                    number+=""
                    labelA.config(text=number)
                elif value == " + ":
                    number+=""
                    labelA.config(text=number)
                elif value == " - ":
                    number+=""
                    labelA.config(text=number)
                elif value == " % ":
                    number+=""
                    labelA.config(text=number)
                
                elif value =="0"or"1"or"2"or"3"or"4"or"5"or"6"or"7"or"8"or"9":
                    number+=value
                    labelA.config(text=number)
                   # print("hlo")

# To add string numbers + string numbers

            
            elif number[-1] !=" ":
                number+=value
                labelA.config(text=number)
                #print("hllo")

               
                    
           
            
                
        

    
    except:
        if isinstance(number,int):
            
            number= str(answer)
            
            
            
            if value == " / ":
                number+=value
                labelA.config(text=number)

            elif value == " + ":
                number+=value
                labelA.config(text=number)

            elif value == " - ":
                number+=value
                labelA.config(text=number)

            elif value == " * ":
                number+=value
                labelA.config(text=number)
                
            elif value == " % ":
                number+=value
                labelA.config(text=number)

        
                
            elif value =="0"or"1"or"2"or"3"or"4"or"5"or"6"or"7"or"8"or"9"or".":
                number=value
                labelA.config(text=number)
                
        elif isinstance(number,float):
            
            number= str(answer)
            
            
            
            if value == " / ":
                number+=value
                labelA.config(text=number)

            elif value == " + ":
                number+=value
                labelA.config(text=number)

            elif value == " - ":
                number+=value
                labelA.config(text=number)

            elif value == " * ":
                number+=value
                labelA.config(text=number)
                
            elif value == " % ":
                number+=value
                labelA.config(text=number)
            

        
                
            elif value =="0"or"1"or"2"or"3"or"4"or"5"or"6"or"7"or"8"or"9"or".":
                number=value
                labelA.config(text=number)




def keyboard(a):
    global number
    global answer
    if a.char == "/":
        value=" "+a.char+" "
    elif a.char == "*":
        value=" "+a.char+" "
    elif a.char == "-":
        value=" "+a.char+" "
    elif a.char == "+":
        value=" "+a.char+" "


    
    else:
        value=a.char
   


            
    try:
        if number =="":
                  
 #first number in the label
             
            if  value == " / ":
                number=""
                labelA.config(text=number)

            elif value == " + ":
                number=""
                labelA.config(text=number)

            elif value == " - ":
                number=""
                labelA.config(text=number)

            elif value == " * ":
                number=""
                labelA.config(text=number)
                
            elif value == " % ":
                number=""
                labelA.config(text=number)
                

        
                    
                
            elif value =="0"or"1"or"2"or"3"or"4"or"5"or"6"or"7"or"8"or"9"or".":
                number=value
                labelA.config(text=number)


# the other number in the label
                
        elif number != "":
            if number[-1] == ".":
                if value ==".":
                    number+=""
                elif value ==" / ":
                    number+=""
                elif value ==" + ":
                    number+=""
                elif value ==" - ":
                    number+=""
                elif value ==" * ":
                    number+=""
    
                 #   labelA.config(text=number)
                    #if value == " * ":
                    #    number+=""
                      #  labelA.config(text=number)
                elif value =="0"or"1"or"2"or"3"or"4"or"5"or"6"or"7"or"8"or"9":
                    number+=value
                    labelA.config(text=number)

# To add number with mathamathical symbols

            elif number[-1] == " ":
                if value == " / ":#or" . "or" + "or" * "or" - ":
                    number+=""
                    labelA.config(text=number)
                elif value == " * ":
                    number+=""
                    labelA.config(text=number)
                elif value == " + ":
                    number+=""
                    labelA.config(text=number)
                elif value == " - ":
                    number+=""
                    labelA.config(text=number)
                elif value == " % ":
                    number+=""
                    labelA.config(text=number)
                
                elif value =="0"or"1"or"2"or"3"or"4"or"5"or"6"or"7"or"8"or"9":
                    number+=value
                    labelA.config(text=number)
                   # print("hlo")

# To add string numbers + string numbers

            
            elif number[-1] !=" ":
                number+=value
                labelA.config(text=number)
                #print("hllo")

               
                    
           
            
                
        

    
    except:
        if isinstance(number,int):
            
            number= str(answer)
            
            
            
            if value == " / ":
                number+=value
                labelA.config(text=number)

            elif value == " + ":
                number+=value
                labelA.config(text=number)

            elif value == " - ":
                number+=value
                labelA.config(text=number)

            elif value == " * ":
                number+=value
                labelA.config(text=number)
                
            elif value == " % ":
                number+=value
                labelA.config(text=number)

        
                
            elif value =="0"or"1"or"2"or"3"or"4"or"5"or"6"or"7"or"8"or"9"or".":
                number=value
                labelA.config(text=number)
                
        elif isinstance(number,float):
            
            number= str(answer)
            
            
            
            if value == " / ":
                number+=value
                labelA.config(text=number)

            elif value == " + ":
                number+=value
                labelA.config(text=number)

            elif value == " - ":
                number+=value
                labelA.config(text=number)

            elif value == " * ":
                number+=value
                labelA.config(text=number)
                
            elif value == " % ":
                number+=value
                labelA.config(text=number)
            

        
                
            elif value =="0"or"1"or"2"or"3"or"4"or"5"or"6"or"7"or"8"or"9"or".":
                number=value
                labelA.config(text=number)


                
     #len_number=len(number)
       # final_len_number=len_number -1
  #  try:
        
    #final_len_number=len_number - 1
     #       print(str(last_number))
      #      if last_number == "/"or"+"or"."or"*"or"-":
       #         number.replace(number[-2],value)
        #        labelA.config(text=number)
                
        #elif number[-1] =="/":
         #   print(1)



    #except:
     #   print("")
       # except:
            #if value == "/"or"*":
             #   number=str(answer)
              #  number+=1
               # labelA.config(text=number)
                

                    
    #except:

     #   print("O:")
def keyboardo(Event):
    global number
    number = ""
    labelA.config(text=number)

        
def C(vlaue):
    global number
    number = ""
    labelA.config(text=number)

def equal():
    global number
    global answer
    if number !="":
        try:
            if " / "not in number :
                if "."  in number:
                    answer = eval(number)
                    number = float(answer)
                else:
                    answer = eval(number)
                    number = int(answer)
            
            elif " / "  in number:
                answer = eval(number)
                number = float(answer)

                
            elif isinstance(number,str):
                print("hello")
                
               
        except:
            answer = """some error happen if your having some problem
please report the bug to "Alstine\""""
    labelA.config(text=number)



def keyboardequal(Event):
    global number
    global answer
    if number !="":
        try:
            if " / "not in number :
                if "."  in number:
                    answer = eval(number)
                    number = float(answer)
                else:
                    answer = eval(number)
                    number = int(answer)
            
            elif " / "  in number:
                answer = eval(number)
                number = float(answer)

                
            elif isinstance(number,str):
                print("hello")
                
               
        except:
            answer = """some error happen if your having some problem
please report the bug to "Alstine\""""
    labelA.config(text=number)








def keyboardback(Event):
    global number

    try:
        len_number0=len(number)
        Clen_number=len_number0-1
        temp_len=number[Clen_number:len_number0]
        
        if temp_len == " ":
            clen_numberspace = Clen_number -1
            temp_lenspace = number[clen_numberspace:len_number0]
            printstr = temp_lenspace.replace(temp_lenspace,"")
            temp = number[0:clen_numberspace]+printstr
            number = temp
            labelA.config(text=number)
        
        else:
            printstr = temp_len.replace(temp_len[0],"")
            temp = number[0:Clen_number]+printstr
            number = temp
            labelA.config(text=number)


    except:
        if number =="7":
            print("Alstine uyir")




def back(value):
    global number

    try:
        len_number0=len(number)
        Clen_number=len_number0-1
        temp_len=number[Clen_number:len_number0]
        
        if temp_len == " ":
            clen_numberspace = Clen_number -1
            temp_lenspace = number[clen_numberspace:len_number0]
            printstr = temp_lenspace.replace(temp_lenspace,"")
            temp = number[0:clen_numberspace]+printstr
            number = temp
            labelA.config(text=number)
        
        else:
            printstr = temp_len.replace(temp_len[0],"")
            temp = number[0:Clen_number]+printstr
            number = temp
            labelA.config(text=number)


    except:
        if number =="7":
            print("Alstine uyir")




    
    #if isinstance(number,float):
     #   print("hlo")
    #elif value == "del":
       # number_replace=number.replace(number[-1],"j",1)
       # number = number_replace
       # labelA.config(text=number)


#def three():
 #   three = intgers[3]
   
   
#def four():
 #   four = intgers[4]

#def five():
    
#def six():
    
#def seven():
    

#def display():
  #  labelA= Label(frame, text = displayint,bg ="white",padx=170,pady=15)
   # labelA.pack()


#def answer0():
 #   number = int(in0.get())

    
    #label0=Label(frame,text=number)
    #label0.pack()







but0 = Button(frame, text=0, bg="blue", padx=20, pady=5, command = lambda:display(intgerstr[0]),fg = "white",font=("Arial",15))
but1 = Button(frame, text=1, bg="blue",  padx=20, pady=8 -3, command = lambda:display(intgerstr[1]),fg = "white",font=("Arial",15))
but2 = Button(frame, text=2, bg="blue", padx=20, pady=8-3, command = lambda:display(intgerstr[2]),fg = "white",font=("Arial",15))
but3 = Button(frame, text=3, bg="blue", padx=20, pady=8-3, command = lambda:display(intgerstr[3]),fg = "white",font=("Arial",15))
but4 = Button(frame, text=4, bg="blue",  padx=20, pady=8-3, command = lambda:display(intgerstr[4]),fg = "white",font=("Arial",15))
but5 = Button(frame, text=5, bg="blue",  padx=25-5, pady=8-3, command = lambda:display(intgerstr[5]),fg = "white",font=("Arial",15))
but6 = Button(frame, text=6, bg="blue",  padx=25-5, pady=8-3, command = lambda:display(intgerstr[6]),fg = "white",font=("Arial",15))
but7 = Button(frame, text=7, bg="blue", padx=25-5, pady=8-3, command = lambda:display(intgerstr[7]),fg = "white",font=("Arial",15))
but8 = Button(frame, text=8, bg="blue",  padx=25-5, pady=8-3, command = lambda:display(intgerstr[8]),fg = "white",font=("Arial",15))
but9 = Button(frame, text=9, bg="blue", padx=25-5, pady=8-3, command = lambda:display(intgerstr[9]),fg = "white",font=("Arial",15))
butequal = Button(frame, text="=", bg="yellow",padx=97-5,pady=8-3, command = lambda: equal()  ,font=("Arial",15))
butadd = Button(frame, text = '+',bg="yellow",padx=24-5,pady=8-3, command = lambda:display(" + "),font=("Arial",15))
butminius = Button(frame, text = '-',bg="yellow",padx=26-5,pady=8-3, command = lambda:display(" - "),font=("Arial",15))
butmulitple = Button(frame, text = '*',bg="yellow",padx=26-5,pady=8-3, command = lambda:display(" * "),font=("Arial",15))
butdivide= Button(frame, text = '/',bg="yellow",padx=27-5,pady=8-3, command = lambda:display(" / "),font=("Arial",15))
butdot= Button(frame, text = '.',bg="yellow",padx=28-5,pady=8-3, command = lambda:display("."),font=("Arial",15))
butc = Button(frame, text = 'C',bg="yellow",padx=23-5,pady=8-3, command = lambda:C(""),font=("Arial",15))
butdel = Button(frame, text ="←",bg="yellow",padx=25-10,pady=8-3,font=("Arial",15),command = lambda:back ("del"))


but1.place(x=1*8,y=70*2)
but2.place(x=16*6 - 15,y=70*2)
but3.place(x=31*6- 32,y=70*2)
but4.place(x=1*8,y=102*2-8)
but5.place(x=16*6- 15,y=102*2-8)
but6.place(x=31*6- 32,y=102*2-8)
but7.place(x=1*8,y=134*2-16)
but8.place(x=16*6- 15,y=134*2-16)
but9.place(x=31*6- 32,y=134*2-16)

butdot.place(x=1*8,y=166*2-24)
but0.place(x=16*6-15,y=166*2-24)
butc.place(x=31*6-32,y=166*2-24)

butdel.place(x=46*6-49,y=70*2)
butminius.place(x=46*6-49,y=102*2-8)
butadd.place(x=46*6-49,y=134*2-16)
butmulitple.place(x=46*6-49,y=166*2-24)
butdivide.place(x=46*6-49,y=198*2-32)



butequal.place(x=1*8,y=198*2-32)








frame.bind(str("1"),keyboard)
frame.bind(str("2"),keyboard)
frame.bind(str("3"),keyboard)
frame.bind(str("4"),keyboard)
frame.bind(str("5"),keyboard)
frame.bind(str("6"),keyboard)
frame.bind(str("7"),keyboard)
frame.bind(str("8"),keyboard)
frame.bind(str("9"),keyboard)
frame.bind(str("0"),keyboard)
frame.bind(str(" - "),keyboard)
frame.bind(str("."),keyboard)
frame.bind(str(" * "),keyboard)
frame.bind(str(" / "),keyboard)
frame.bind(str(" % "),keyboard)
frame.bind(str(" + "),keyboard)
frame.bind("<Return>",keyboardequal)
frame.bind("<BackSpace>",keyboardback)
frame.bind("<Delete>" , keyboardo)













frame.mainloop()







# Completed the normal calculator in 9th/3/2023 at 10:54pm night

