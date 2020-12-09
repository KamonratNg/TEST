
import tkinter as tk
import numpy 

root= tk.Tk()
root.title("BMI by Bamboo")
canvas1 = tk.Canvas(root, width = 400, height = 400, bg = 'gray90', relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Calculate Your BMI')


label1.config(font=('helvetica', 16))
canvas1.create_window(200, 60, window=label1)

label2 = tk.Label(root, text='Height (in meters):', bg = 'gray90')
canvas1.create_window(200, 100, window=label2)


entry1 = tk.Entry (root, width=27)
canvas1.create_window(200, 120, window=entry1)


label3 = tk.Label(root, text='Mass (in kilograms):', bg = 'gray90')
canvas1.create_window(200, 180, window=label3)

entry2 = tk.Entry (root, width=27)
canvas1.create_window(200, 200, window=entry2)




def bmical ():
    answerbmi = float(entry2.get()) / float(entry1.get())**2
    answer.config(text="Result is %d" % answerbmi)

    if (answerbmi < 10 or answerbmi > 50):
        label4.config(text = "OMG You are not a HUMAN", bg='red')

    elif (answerbmi < 18.5):
        label4.config(text = "Underweight", bg='orage')
        
    elif (answerbmi >= 18.5 and answerbmi <= 24.9):
        label4.config(text = "Normal weight", bg='green')

    elif (answerbmi >= 25 and answerbmi <= 29.9):
        label4.config(text = "Overweight", bg='pink')

    else:
        label4.config(text = "Obesity", bg='purple')


    


    
button1 = tk.Button(text='      Calculate    ', command=bmical, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(200, 300, window=button1)

answer = tk.Label(root, text = '')
canvas1.create_window(200, 350, window=answer)

label4 = tk.Label(root, text = '')
canvas1.create_window(200, 380, window=label4)


root.mainloop()