"""
This program is heavily based on youtube video made by freeCodeCamp.org
All credits are due to them, although i made some quality of life improvements
"""


from tkinter import *
import setting
import utils
from Cell import Cell

root = Tk()

# Basic setting for graphical window
root.title('Minesweeper')
root.configure(bg='black')
root.geometry(f'{setting.width}x{setting.height}')
root.resizable(False, False)

# Divides window in 3 distinct frames
top_frame = Frame(root, bg='black', width=utils.width_prct(100), height = utils.height_prct(20))
top_frame.place(x = 0, y = 0)

game_title=Label(top_frame, bg='black',fg='white', text="Minesweeper Game", font=('', 48))
game_title.place(x=utils.width_prct(25), y=0)

left_frame = Frame(root, bg='black', width=utils.width_prct(25), height = utils.height_prct(80))
left_frame.place(x = 0, y = utils.height_prct(20))

center_frame = Frame(root, bg='black', width=utils.width_prct(75), height = utils.height_prct(80))
center_frame.place(x=utils.width_prct(25), y=utils.height_prct(20))


for x in range(setting.grid_size):
    for y in range(setting.grid_size):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(column=x, row=y)
#Call label from the Cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0,y=0)


Cell.randomize_mines()



if __name__ == '__main__':
    root.mainloop()