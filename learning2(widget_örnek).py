import tkinter

#window
window = tkinter.Tk()
window.title("Python Tkinter")
window.minsize(500, 500)

#label : kullanıcıya bir metin göstermek için kullanılır
my_label = tkinter.Label(text="this is a label", font=("Arial", 10, "bold"))
#burada bg,fg,size gibi değerler girebilirdim.ama configte girmeyi tercih ettim:
my_label.config(bg="black", fg="white", width=20, height=10) #config:yapılandırma
my_label.pack()  #pack ekranımızın ortalarında konumlandırmak için kullanılır


#button
def click_button():
    user_input = my_entry.get()
    print(user_input)
my_button = tkinter.Button(text="this is a button", command=click_button)
#commanda fonksiyon atarken fonksiyonu üstüne yazman lazım DİKKAT!!
my_button.pack() #pack yazıları alt alta koymasına yaradı


#Entry : kullanıcıdan klavyeyle bir şey yazdırma yeri
my_entry = tkinter.Entry(width=50)
my_entry.pack()




window.mainloop()


