from tkinter import *
import math

def leftClickButton(event):
    Weight = float(textBoxWeight.get())
    Height = float(textBoxHeight.get())
    BMI = Weight/math.pow(Height/100, 2)
    print(BMI)
    LabelResult.configure(text=BMI)
    if BMI >= 30:
        LabelResult2.configure(text="BMI>=30 อ้วนมาก", fg="red")
    elif BMI >= 25 and BMI < 30:
        LabelResult2.configure(text="BMI ระหว่าง 25.0 - 29.9 อ้วน", fg="red")
    elif BMI >= 23 and BMI < 25:
        LabelResult2.configure(text="BMI ระหว่าง 23.0 - 24.9 น้ำหนักเกิน", fg="orange")
    elif BMI >= 18.6 and BMI < 23:
        LabelResult2.configure(text="BMI ระหว่าง 18.6 - 22.9 น้ำหนักปกติ", fg="green")
    else:
        LabelResult2.configure(text="BMI น้อยกว่า 18.5 ผอมเกินไป", fg="red")

MainWindow = Tk()
LabelHeight = Label(MainWindow, text="ส่วนสูง (Cm.)")
LabelHeight.grid(row=0, column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0, column=1)
LabelWeight = Label(MainWindow, text="น้ำหนัก (Kg.)")
LabelWeight.grid(row=1, column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1, column=1)
calculateButton = Button(MainWindow, text="คำนวณ")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2, column=0)
LabelResult = Label(MainWindow, text="ผลลัพธ์")
LabelResult.grid(row=2, column=1)
LabelResult2 = Label(MainWindow, text="คำอธิบาย")
LabelResult2.grid(row=3, column=1)
MainWindow.mainloop()