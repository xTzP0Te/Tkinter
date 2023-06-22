import tkinter as tk
import numpy as np

def button_click():
    a = int(coeffcient_first.get())
    b = int(coeffcient_second.get())
    c = int(coeffcient_third.get())

    d = b * b - 4 * a * c
    x1 = (-b + np.sqrt(d)) / (2 * a)
    x2 = (-b - np.sqrt(d)) / (2 * a)
    print(x1, x2)

    first_sq = tk.Label(root, text=f"Первый корень = {x1}")
    first_sq.grid(row=1, column=0)
    second_sq = tk.Label(root, text=f"Второй корень = {x2}")
    second_sq.grid(row=1, column=1)



root = tk.Tk()

coeffcient_first = tk.Entry(root)
# coeffcient_first.pack()

coeffcient_second = tk.Entry(root)
# coeffcient_second.pack()

coeffcient_third = tk.Entry(root)
# coeffcient_third.pack()

submit_button = tk.Button(root, text="dumb", command=button_click)
# submit_button.pack()

coeffcient_first.grid(row=0, column=0)
coeffcient_second.grid(row=0, column=1)
coeffcient_third.grid(row=0, column=2)
submit_button.grid(row=1, column=2)

root.mainloop()
