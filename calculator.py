from tkinter import *

expression = "" 

def press(num): 
    global expression 
    expression = expression + str(num) 
    equation.set(expression) 

def equalpress(): 
    try: 
        global expression 
        total = str(eval(expression)) 
        equation.set(total) 
        expression = "" 
    except: 
        equation.set(" error ") 
        expression = "" 

def clear(): 
    global expression 
    expression = "" 
    equation.set("") 

if __name__ == "__main__": 
    gui = Tk() 
    gui.configure(background="light green") 
    gui.title("Simple Calculator") 
    gui.geometry("270x150") 

    equation = StringVar() 
    expression_field = Entry(gui, textvariable=equation) 
    expression_field.grid(columnspan=4, ipadx=70)

    buttons = [
        ('1', 2, 0), ('2', 2, 1), ('3', 2, 2),
        ('4', 3, 0), ('5', 3, 1), ('6', 3, 2),
        ('7', 4, 0), ('8', 4, 1), ('9', 4, 2),
        ('0', 5, 0), ('+', 2, 3), ('-', 3, 3),
        ('*', 4, 3), ('/', 5, 3), ('=', 5, 2),
        ('Clear', 5, 1), ('.', 6, 0)
    ]

    for (text, row, column) in buttons:
        button = Button(gui, text=f' {text} ', fg='black', bg='green', # Changed bg to green
                        command=lambda t=text: press(t) if t != '=' else equalpress(),
                        height=1, width=7)
        button.grid(row=row, column=column)

    gui.mainloop()
