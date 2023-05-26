from tkinter import *

window = Tk()
window.title("Tkinter Python")
window.minsize(width=600, height=600)
window.config(padx=20, pady=20)

#LABEL
my_label = Label(text="my label")
my_label.config(bg="black")
my_label.config(fg="white")
my_label.config(padx=10, pady=10)
my_label.pack()

#BUTTON
def button_clicked():
    print("button clicked")
    print(my_text.get("1.3", END)) #text bizden indeks girmemizi istedi.DİKKAT!!.başlangıç ve son girdik
#1.0 için 1->hangi satırdan başladığı 0->hangi karakterden başladığı

my_button = Button(text="button", command=button_clicked)
my_button.config(padx=10, pady=10)
my_button.pack()



#ENTRY
#singleline:yani entry tek satır yapar.
my_entry = Entry(width=20)
my_entry.pack()

#TEXT
#multiline:yani text birden fazla satır yapar
my_text = Text(width=30, height=5)
my_text.focus() #focus farenin direk texten başlamasını sağlar.my_entry.focus() yapsaydık fare direk enrtyden başlardı.
my_text.pack()




window.mainloop()