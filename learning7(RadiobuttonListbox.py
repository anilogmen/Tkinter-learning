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

#SCALE
def scale_selected(value):    #value:değer #value diye yazmak zorundasın yoksa error.
    print(value)
my_scale = Scale(from_=0, to=50, command=scale_selected)
my_scale.pack()

#SPİNBOX
def spinbox_selected():         #value yazmıyoruz.
    print(my_spinbox.get())
my_spinbox = Spinbox(from_=0, to=50, command=spinbox_selected)
my_spinbox.pack()

#CHECKBUTTON
def checkbutton_selected():
    print(check_state.get())
check_state = IntVar() #checkbutton seçildiyse 0 seçilmediyse 1 olan birşey.
my_checkbutton = Checkbutton(text="check", variable=check_state, command=checkbutton_selected)
my_checkbutton.pack()

#RADİO BUTTON
def radio_selected():
    print(radio_checked_state.get())

radio_checked_state = IntVar()
my_radiobutton = Radiobutton(text="1.option", value=10, variable=radio_checked_state, command=radio_selected)
my_radiobutton_2 = Radiobutton(text="2.option", value=20, variable=radio_checked_state, command=radio_selected)
my_radiobutton.pack()
my_radiobutton_2.pack()

#LİSTBOX: herhangi  bir listeyi kullanıcıya daha düzgün göstermeye yarar.
def listbox_selected(event):
    print(my_listbox.get(my_listbox.curselection()))

my_listbox = Listbox()
name_list = ["atıl", "abc", "kjf", "asdas"]
for i in range(len(name_list)):
    my_listbox.insert(i, name_list[i])

my_listbox.bind('<<ListboxSelect>>', listbox_selected) #verdiğim fonksiyona bağlamak için bunu yapmam lazımmış
my_listbox.pack()




window.mainloop()