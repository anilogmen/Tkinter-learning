import tkinter

#window
window = tkinter.Tk()
window.title("Python Tkinter")
window.minsize(500, 500)

#label :
my_label = tkinter.Label(text="this is a label", font=("Arial", 10, "bold"))
my_label.config(bg="black", fg="white", width=20, height=10)
#my_label.pack(side="top")
#my_label.place(x=170, y=0)  #placeleride yorum satırı hale getirelim grid sistemini görelim:
my_label.grid(row=0, column=2)



#button
def click_button():
    user_input = my_entry.get()
    print(user_input)
my_button = tkinter.Button(text="this is a button", command=click_button)
#my_button.pack(side="top")
#my_button.place(x=200, y=200)
my_button.grid(row=1, column=2)



#Entry : kullanıcıdan klavyeyle bir şey yazdırma yeri
my_entry = tkinter.Entry(width=50)
#my_entry.pack(side="top")
#my_entry.place(x=100, y=300)
my_entry.grid(row=2, column=2)




window.mainloop()


