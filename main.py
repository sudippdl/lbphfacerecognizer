import tkinter as tk 
from tkinter import Message, Text
import tkinter.ttk as ttk
import tkinter.font as font
import pickle
# import our functions
from detectionPart import capture
from trainingPart import training_lbph
from recognizerPart import our_recognition


window = tk.Tk()
window.title("Face Recognizer")
dialogue_title = "Quit"
dialogue_text = "Are you sure?"

window.geometry('740x400')
window.configure(background='#e0c596')
message = tk.Label(window, text="Face Attendance Registry" ,bg="#557387"  ,fg="white"  ,width=30  ,height=2,font=('times', 20, 'italic bold underline')) 

message.place(x=120, y=20)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)


lbl = tk.Label(window, text="Enter ID",width=15  ,height=1  ,fg="black"  ,bg="#ade0c9" ,font=('times', 15, ' bold ') ) 
lbl.place(x=120, y=120)

txt = tk.Entry(window,width=15  ,bg="#ade0c9" ,fg="black",font=('times', 15, ' bold '))
txt.place(x=350, y=120)

lbl2 = tk.Label(window, text="Enter Name",width=15 ,fg="black"  ,bg="#ade0c9" ,height=1 ,font=('times', 15, ' bold ')) 
lbl2.place(x=120, y=180)

txt2 = tk.Entry(window, width=15 ,bg="#ade0c9" ,fg="black",font=('times', 15, ' bold ')  )
txt2.place(x=350, y=180)


lbl3 = tk.Label(window, text="Message : ",width=15  ,fg="black"  ,bg="#ade0c9"  ,height=1 ,font=('times', 15, ' bold ')) 
lbl3.place(x=120, y=240)

message = tk.Label(window, text="", bg="#ade0c9"  ,fg="black" , width=30  ,height=1, activebackground = "yellow" ,font=('times', 15, ' bold ')) 
message.place(x=350, y=240)

lbl3 = tk.Label(window, text="Attendance : ",width=15 ,fg="black"  ,bg="#ade0c9"  ,height=2 ,font=('times', 15, ' bold  underline')) 
lbl3.place(x=400, y=650)

message2 = tk.Label(window, text="" ,fg="black"   ,bg="#ade0c9",activeforeground = "green",width=30  ,height=2  ,font=('times', 15, ' bold ')) 
message2.place(x=700, y=650)

def clear():
    txt.delete(0, 'end')    
    res = ""
    message.configure(text= res)

def clear2():
    txt2.delete(0, 'end')    
    res = ""
    message.configure(text= res)    
    
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False


def user_input():
    unique_id = txt.get()
    name = txt2.get()
    print(unique_id)
    print(name)
    writable = True
    # for unique num
    pickle_file = open("labels.pickle", 'rb')
    namefile = pickle.load(pickle_file)
    namelist = list(namefile)
    unique_num = []
    for name_ in namelist:
        unique_num.append(name_.split('(')[1].split(")")[0])
    print(unique_num)
    # if entered id is in unique_num writable is false
    if unique_id in unique_num:
        writable=False
        print("Do not write this")


    if(is_number(unique_id) and name.isalpha() and writable):
        print(unique_id)
        capture(name, unique_id)
        res = "Images Saved ( " + unique_id +" : "+ name + " )"
        message.configure(text=res)
    else:
        if(is_number(unique_id)):
            res = "Enter Alphabetical Name"
            message.configure(text= res)
        if(name.isalpha()):
            res = "Enter Numeric Id"
            message.configure(text= res)
        if not writable:
            message.configure(text="Unique Id required")
    print("System taking pictures of you.Please smile :) \n")
    



clearButton = tk.Button(window, text="x", command=clear  ,fg="black"  ,bg="#ade0c9"  ,width=4 ,height=1 ,activebackground = "Red" ,font=('times', 10, ' bold '))
clearButton.place(x=510, y=120)
clearButton2 = tk.Button(window, text="x", command=clear2  ,fg="black"  ,bg="#ade0c9"  ,width=4 ,height=1, activebackground = "Red" ,font=('times', 10, ' bold '))
clearButton2.place(x=510, y=180)    
takeImg = tk.Button(window, text="Take Images", command=user_input  ,fg="black"  ,bg="#ade0c9"  ,width=15  ,height=1, activebackground = "Red" ,font=('times', 10, ' bold '))
takeImg.place(x=120, y=300)
trainImg = tk.Button(window, text="Train Images", command=training_lbph ,fg="black"  ,bg="#ade0c9"  ,width=15  ,height=1, activebackground = "Red" ,font=('times', 10, ' bold '))
trainImg.place(x=250, y=300)
trackImg = tk.Button(window, text="Recognize", command=our_recognition ,fg="black"  ,bg="#ade0c9"  ,width=15  ,height=1, activebackground = "Red" ,font=('times', 10, ' bold '))
trackImg.place(x=380, y=300)
quitWindow = tk.Button(window, text="Quit", command=window.destroy, fg="black"  ,bg="#ade0c9"  ,width=15  ,height=1, activebackground = "Red" ,font=('times', 10, ' bold '))
quitWindow.place(x=510, y=300)

window.mainloop()