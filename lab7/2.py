from tkinter import *
import pygame
import sys

root = Tk()
root.title('Music Player')
root.geometry('500x300')

pygame.mixer.init()

menubar = Menu(root)
root.config(menu=menubar)

organise_menu = Menu(menubar)
organise_menu.add_command(Label='Select Folder')
menubar.add_cascade(Label='Organise', menu=organise_menu)

songlist = Listbox(root, bg='black', fg='white', width=100, height=15)
songlist.pack()

play_btn_image = PhotoImage(file='play-button.png')
back_image = PhotoImage(file='back.png')
next_image = PhotoImage(file='next.png')
pause_image = PhotoImage(file='pause.png')

control_frame = Frame(root)
control_frame.pack()

play_btn = Button(control_frame, image=play_btn_image, borderwidth=0)
pause_btn = Button(control_frame, image=pause_image, borderwidth=0)
next_btn = Button(control_frame, image=next_image, borderwidth=0)
back_btn = Button(control_frame, image=back_image, borderwidth=0)

play_btn.gird(row=0, column=1, padx=7, pady=10)
pause_btn.gird(row=0, column=2, padx=7, pady=10)
next_btn.gird(row=0, column=2, padx=7, pady=10)
back_btn.gird(row=0, column=0, padx=7, pady=10)

root.mainloop()
