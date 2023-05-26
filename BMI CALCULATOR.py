from tkinter import *
#window
window = Tk()
window.title("BMI CALCULATOR")
window.minsize(300, 300)


#label1
my_kg_label = Label(text="Enter Your Weight(kg)", font=("Arial", 10, "normal"))
my_kg_label.config(fg="black", width=20, height=4)
my_kg_label.pack(side="top")

#Entry1
my_kg_entry = Entry(width=20)
my_kg_entry.pack(side="top")



#label2
my_height_label = Label(text="Enter Your Height(cm)", font=("Arial", 10, "normal"))
my_height_label.config(fg="black", width=20, height=4)
my_height_label.pack(side="top")

#Entry2
my_cm_entry = Entry(width=20)
my_cm_entry.pack()

#Result Label
bmi_value = StringVar(value="")
bmi_status = StringVar(value="")


def bmi_index(* args):
    try:
        kg =float(my_kg_entry.get())
        m = float(my_cm_entry.get()) / 100
        bmi = kg / (m ** 2)
        bmi_value.set(f"Your BMI is {bmi:.2f}")
        if bmi < 18.5:
            bmi_state = "You Are Underweight."
        elif bmi > 18.5 and bmi < 24.9:
            bmi_state = "You Are In Good Shape!"
        elif bmi > 24.9 and bmi < 29.9:
            bmi_state = "You Are Overweight"
        else:
            bmi_state = "You Are Obese."
        bmi_status.set(bmi_state)
    except ValueError:
        bmi_state = "please enter the values correctly!!"
        bmi_status.set(bmi_state)



#Button
my_calculate_button = Button(text="Calculate", command=bmi_index)
my_calculate_button.pack()

bmi_value_result = Label(textvariable=bmi_value)
bmi_value_result.pack()
bmi_status_result = Label(textvariable=bmi_status)
bmi_status_result.pack()

window.mainloop()