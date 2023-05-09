import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # create input field
        self.display = tk.Entry(master, width=25, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # create buttons for digits and operations
        self.button_1 = tk.Button(master, text="1", padx=40, pady=20, command=lambda: self.button_click(1))
        self.button_2 = tk.Button(master, text="2", padx=40, pady=20, command=lambda: self.button_click(2))
        self.button_3 = tk.Button(master, text="3", padx=40, pady=20, command=lambda: self.button_click(3))
        self.button_4 = tk.Button(master, text="4", padx=40, pady=20, command=lambda: self.button_click(4))
        self.button_5 = tk.Button(master, text="5", padx=40, pady=20, command=lambda: self.button_click(5))
        self.button_6 = tk.Button(master, text="6", padx=40, pady=20, command=lambda: self.button_click(6))
        self.button_7 = tk.Button(master, text="7", padx=40, pady=20, command=lambda: self.button_click(7))
        self.button_8 = tk.Button(master, text="8", padx=40, pady=20, command=lambda: self.button_click(8))
        self.button_9 = tk.Button(master, text="9", padx=40, pady=20, command=lambda: self.button_click(9))
        self.button_0 = tk.Button(master, text="0", padx=40, pady=20, command=lambda: self.button_click(0))

        self.button_add = tk.Button(master, text="+", padx=39, pady=20, command=lambda: self.operation_click("+"))
        self.button_subtract = tk.Button(master, text="-", padx=41, pady=20, command=lambda: self.operation_click("-"))
        self.button_multiply = tk.Button(master, text="*", padx=40, pady=20, command=lambda: self.operation_click("*"))
        self.button_divide = tk.Button(master, text="/", padx=41, pady=20, command=lambda: self.operation_click("/"))
        self.button_equal = tk.Button(master, text="=", padx=91, pady=20, command=self.equal_click)
        self.button_clear = tk.Button(master, text="Clear", padx=79, pady=20, command=self.clear_click)

        # display buttons on screen
        self.button_1.grid(row=3, column=0)
        self.button_2.grid(row=3, column=1)
        self.button_3.grid(row=3, column=2)

        self.button_4.grid(row=2, column=0)
        self.button_5.grid(row=2, column=1)
        self.button_6.grid(row=2, column=2)

        self.button_7.grid(row=1, column=0)
        self.button_8.grid(row=1, column=1)
        self.button_9.grid(row=1, column=2)

        self.button_0.grid(row=4, column=0)

        self.button_add.grid(row=5, column=0)
        self.button_subtract.grid(row=6, column=0)
        self.button_multiply.grid(row=6, column=1)
        self.button_divide.grid(row=6, column=2)

        self.button_clear.grid(row=4, column=1, columnspan=2)
        self.button_equal.grid(row=5, column=1, columnspan=2)

        # initialize calculator values
        self.current_number = None
        self.current_operation = None

    def button_click(self, number):
        current = self.display.get()
        self.display.delete(0, tk.END)
        self.display.insert(0, str(current) + str(number))

    def operation_click(self, operation):
        self.current_number = float(self.display.get())
        self.current_operation = operation
        self.display.delete(0, tk.END)

    def equal_click(self):
        second_number = float(self.display.get())
        self.display.delete(0, tk.END)

        if self.current_operation == "+":
            result = self.current_number + second_number
        elif self.current_operation == "-":
            result = self.current_number - second_number
        elif self.current_operation == "*":
            result = self.current_number * second_number
        elif self.current_operation == "/":
            result = self.current_number / second_number
        else:
            result = 0

        self.display.insert(0, str(result))

    def clear_click(self):
        self.display.delete(0, tk.END)


root = tk.Tk()
my_calculator = Calculator(root)
root.mainloop()
