import tkinter
from tkinter import ttk
from projet import *


robots = [Robot(Position()) for i in range(5)]


root = tkinter.Tk()
root.geometry("600x600")


for i in range(20):
    for j in range(20):
        label = ttk.Label(root, text="", borderwidth=2, relief="groove", width=3, font=("Helvetica", 12))
        label.grid(column=i, row=j)


robot_colors = ["red", "green", "blue", "purple", "orange"]


def update_robots():
    for i, robot in enumerate(robots):
        x, y = robot.position.coo()
        label = root.grid_slaves(row=y, column=x)[0]
        label.configure(background=robot_colors[i % len(robot_colors)])

root.after(100, update_robots)

root.mainloop()

