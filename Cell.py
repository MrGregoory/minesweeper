import sys
from tkinter import Button, Label
import random
import setting
import ctypes
import sys


class Cell:
    all=[]
    cell_count=setting.cell_count
    cell_count_label_object=None
    def __init__(self, x, y, is_mine_candidate=False, is_opened=False, is_mine=False):
        self.is_mine = is_mine
        self.is_opened=is_opened
        self.is_mine_candidate=is_mine_candidate
        self.cell_btn_object=None
        self.x = x
        self.y = y

    #Append object to the Call.all list
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=10,
            height=3,
        )
        btn.bind('<Button-1>', self.left_click_action ) # Left Click
        btn.bind('<Button-3>', self.right_click_action ) # Right Click
        self.cell_btn_object = btn

    @staticmethod
    def create_cell_count_label(location):
        lbl=Label(
            location,
            bg='black',
            fg='white',
            text=f'Cells Left:{Cell.cell_count}',
            width=12,
            height=4,
            font=("",30),
        )
        Cell.cell_count_label_object=lbl

    def left_click_action(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length==0:
                self.check_for_zeros()
            self.show_cell()
        if Cell.cell_count==setting.mines_count:
            ctypes.windll.user32.MessageBoxW(0, 'You Won!', 'Congrats', 0)
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')


    def check_for_zeros(self):
        for cell_obj in self.surrounded_cells:
            cell_obj.show_cell()


    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x==x and cell.y==y:
                return cell

    @property
    def surrounded_cells(self):
        cells=[self.get_cell_by_axis(self.x-1,self.y-1),
                          self.get_cell_by_axis(self.x - 1, self.y),
                          self.get_cell_by_axis(self.x - 1, self.y + 1),
                          self.get_cell_by_axis(self.x, self.y - 1),
                          self.get_cell_by_axis(self.x+1, self.y - 1),
                          self.get_cell_by_axis(self.x + 1, self.y),
                          self.get_cell_by_axis(self.x, self.y + 1),
                          self.get_cell_by_axis(self.x + 1, self.y + 1),
                          ]

        cells=[cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_mines_length(self):
        counter=0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter+=1

        return counter

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count-=1
            print(self.surrounded_cells_mines_length)
            if self.surrounded_cells_mines_length!=0:
                self.cell_btn_object.configure( text=f'{self.surrounded_cells_mines_length}')
            # Replace the text of cell count label with newer count
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(text=f'Cells Left:{Cell.cell_count}')
            self.cell_btn_object.configure(bg='grey', fg='white',state='disabled')

        self.is_opened=True

    def show_mine(self):
        ctypes.windll.user32.MessageBoxW(0,'Boom!', 'Game Over',0)
        self.cell_btn_object.configure(bg='red')
        sys.exit()



    def right_click_action(self, event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(bg='blue')
            self.is_mine_candidate=True
        else:
            self.cell_btn_object.configure(bg='SystemButtonFace')
            self.is_mine_candidate = False


    @staticmethod
    def randomize_mines():
        picked_cells=random.sample(
            Cell.all, setting.mines_count
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine=True


    def __repr__(self):
        return f'Cell({self.x},{self.y})'