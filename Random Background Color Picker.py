from tkinter import*
import random

root = Tk()
root.title("Random Background Color")
root.geometry("400x200")
root.configure(bg = "white")

colors_available = ["Red", "Maroon", "CadetBlue", "SpringGreen", "Pink", "LightCoral", "PaleGreen"]
colors_syntax_finder = {"Red":"Red",
          "Maroon":"Maroon1",
          "CadetBlue":"CadetBlue2",
          "SpringGreen":"SpringGreen2",
          "Pink":"Pink3",
          "LightCoral":"LightCoral",
          "PaleGreen":"PaleGreen"}

colors = {"Colors":["red", "maroon1", "cadetblue2", "springgreen2", "pink3", "lightcoral", "palegreen"]}



def pickColor():
    color_index = random.randint(0,6)

    color_picked_key_value = colors_available[color_index]
    color_syntax = colors_syntax_finder[color_picked_key_value]
    print(color_syntax)


    color_picked = colors["Colors"][color_index]
    print(color_picked)
    
    root.configure(bg = color_picked)

pick_button = Button(root, font = ("Comic Sans MS", 24, "bold"), command = pickColor, text = "Pick Color")

pick_button.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()