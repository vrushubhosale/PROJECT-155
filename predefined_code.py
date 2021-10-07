from pillow import *
from tkinter import *

root=Tk()
root.title("Dictionary")
root.geometry("600x400")

background_image=tk.PhotoImage(bg.png)
background_label = tk.Label(parent, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

label_of_mutable = Label(root)
label_of_imutable = Label(root)
label_of_tkinter = Label(root)


dict1 = {'Mutable':'VALUES CAN BE CHANGED LIKE A LIST',
         'Imutable': 'VALUES CANNOT BE CHANGED LIKE A TUPPLE',
         'Tkinter': 'IT IS A GUI LIABRAYRY OF PYTHON'} 

def mute():
    label_of_mutable ["text"] = dict1['Mutable']
    
def imute():
    label_of_imutable ["text"] = dict1['Imutable']
    
def TKIN():
    label_of_tkinter ["text"] = dict1['Tkinter']
    
    
btn_1 = Button(root,text="MUTABLE", command=mute)
btn_1.place(relx=0.5, rely=0.2, anchor= CENTER)
    
label_of_mutable.place(relx=0.5, rely=0.3, anchor= CENTER)

btn_2 = Button(root,text="IMUTABLE", command=imute)
btn_2.place(relx=0.5, rely=0.4, anchor= CENTER)
    
label_of_imutable.place(relx=0.5, rely=0.5, anchor= CENTER)

btn_3 = Button(root,text="TKINTER", command=TKIN)
btn_3.place(relx=0.5, rely=0.6, anchor= CENTER)
    
label_of_tkinter.place(relx=0.5, rely=0.7, anchor= CENTER)



root.mainloop()
