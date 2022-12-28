from tkinter import *


def calculator(key):
    if key == 'C':
        entry.delete(0, END)
    elif key == '=':
        result = entry.get()
        entry.delete(0, END)
        entry.insert(END, eval(result))
    else:
        entry.insert(END, key)

def create_screen():
    global screen

    screen = Tk()
    screen.resizable(False, False)
    screen.title('Calculator')
    screen.iconbitmap('calculator.ico')

def main():
    global entry

    BUTTONS = ['7', '8', '9', '+',
               '4', '5', '6', '-',
               '1', '2', '3', '*',
               'C', '0', '=', '/']

    create_screen()
    entry = Entry(screen, justify=RIGHT, width=22, font='helvetica 15')
    entry.grid(row=0, column=0, columnspan=4)

    row = 1
    column = 0
    for button_name in BUTTONS:
        my_button = Button(screen, text=button_name, bd=3, width=6, height=4, font='helvetica 12',
                           command=lambda key=button_name: calculator(key))
        my_button.grid(row=row, column=column)
        column += 1


        if column == 4:
            row += 1
            column = 0



if __name__ == '__main__':
    main()
    screen.mainloop()
