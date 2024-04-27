import tkinter as tk
import random

characters = [
    "Anna Williams",
    "Kazumi Mishima",
    "Julia Chang",
    "Xiaoyu Ling",
    "Lucky Chloe",
    "Zafina",
    "Lili",
    "Alisa Bosconovitch"
    "Asuka Kazama",
    "Katarina Alves",
    "Nina Williams",
    "Josie Rizal"
]

def generate_label():
    string1=random.choice(characters)
    string2=random.choice(characters)

    string=string1+" vs "+string2

    label = tk.Label(text=string)
    x=random.randrange(800)
    y=random.randrange(800)
    label.place(x=x, y=y)

root = tk.Tk()
root.title("Get ready for the next battle!")
root.geometry("1200x1200")

btn = tk.Button(root, text="Generate duelling Tekken pairs",
    command = generate_label)
btn.pack()

root.mainloop()