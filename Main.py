from tkinter import *
from Functions import Functions

if __name__ == "__main__":

    def Calculate():
        userinput = operation_entry.get()
        
        try:
            if userinput == "+":
                result_label.config(text="The result of the equation is: " + Functions.Add(first_entry.get(), second_entry.get()))
            elif userinput == "-":
                result_label.config(text="The result of the equation is: " + Functions.Subtract(first_entry.get(), second_entry.get()))
            elif userinput == "*":
                result_label.config(text="The result of the equation is: " + Functions.Multiply(first_entry.get(), second_entry.get()))
            elif userinput == "/":
                result_label.config(text="The result of the equation is: " + Functions.Divide(first_entry.get(), second_entry.get()))
            elif userinput == "**":
                result_label.config(text="The result of the equation is: " + Functions.Exponentiation(first_entry.get(), second_entry.get()))
            else:
                result_label.config(text="Error! Invalid operator!")

        except ZeroDivisionError:
            result_label.config(text="Error! Cannot divide by 0!")
        
        except ValueError:
            result_label.config(text="Error! Invalid input!")

        except Exception as e:
            result_label.config(text="Equation error!")

    root = Tk()

    root.title("Calculator")

    title_label = Label(root, text="Calculator")
    title_label.pack(pady=10)

    first_label = Label(root, text="Enter the first number")
    first_label.pack()

    first_entry = Entry(root)
    first_entry.pack()

    operation_label = Label(root, text="Enter the operation (+, -, *, /, **)")
    operation_label.pack()

    operation_entry = Entry(root)
    operation_entry.pack()

    second_label = Label(root, text="Enter the second number")
    second_label.pack()

    second_entry = Entry(root)
    second_entry.pack()

    calculate_button = Button(text="Calculate", command=Calculate)
    calculate_button.pack(pady=10)

    result_label = Label(root, text="The result of the equation is: N/A (undefined equation)")
    result_label.pack()

    root.mainloop()
