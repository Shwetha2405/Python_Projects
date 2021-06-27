from tkinter import *
import tkinter.font as font
import random

my_window = Tk()
my_window.title("Color Game")
my_window.geometry("500x300")
my_window.configure(background="gray")

app_font = font.Font(family="Helvetica bold italic",size=12)
game_desp = "Game Description: Enter the color of the words displayed below.\n And keep it in mind not to enter the word text itself !!"

game_description = Label(my_window,text=game_desp,font=app_font,fg="black",bg="gray")
game_description.pack()

game_score = Label(my_window ,text="Your Score",font=app_font,fg="Green")
game_score.pack()

display_words=Label(my_window,font=(font.Font(siz2=28)),pady =10)
display_words.pack()

time_left = Label(my_window,text="Game Ends in :-",font=(font.Font(size=14)),fg ="orange")
time_left.pack()



my_window.mainloop()
