from tkinter import *
from main.py

window = Tk()
window.title("Automatic NumberPlate Recognition")
window.geometry('550x300')
lbl = Label(window, text="Choose_images", font=("Arial Bold", 30))
lbl.grid(column=0, row=0)
variable = StringVar(window)
variable.set(print ("---------")) # default value

w = OptionMenu(window, variable, *Script)
w.grid()
def ok():
    print ("image is:" + variable.get())

button1 = Button(window, text="OK", command=ok)
button1.grid()

lbl = Label(window, text="Choose Model for Training", font=("Arial Bold", 30))
lbl.grid(column=0, row=10)
variable1 = StringVar(window)
variable1.set(print ("---------")) # default value


w = OptionMenu(window, variable1, *Model)
w.grid()
def ok():
    print ("value is:" + variable1.get())

button = Button(window, text="OK", command=ok)
button.grid()

mainloop()
dataset = pd.read_csv(variable.get(),names=['Date','Time','Open','High','Low','Close','Volume'])
dataset['Date_Time'] = pd.to_datetime(dataset['Date'] + ' ' + dataset['Time'])
dataset.index=dataset['Date_Time']

print (dataset)
