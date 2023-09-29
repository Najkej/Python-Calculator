from tkinter import *
from Functions import Functions

if __name__ == "__main__":

    def Oblicz():
        userinput = entrydzialanie.get()
        
        try:
            if userinput == "+":
                labelwynik.config(text="Wynik równania to : " + Functions.Add(entry1.get(), entry2.get()))
            elif userinput == "-":
                labelwynik.config(text="Wynik równania to : " + Functions.Subtract(entry1.get(), entry2.get()))
            elif userinput == "*":
                labelwynik.config(text="Wynik równania to : " + Functions.Multiply(entry1.get(), entry2.get()))
            elif userinput == "/":
                labelwynik.config(text="Wynik równania to : " + Functions.Divide(entry1.get(), entry2.get()))
            elif userinput == "**":
                labelwynik.config(text="Wynik równania to : " + Functions.Exponentiation(entry1.get(), entry2.get()))
            else:
                labelwynik.config(text="Błąd! Zły znak równania! ")

        except ZeroDivisionError:
            labelwynik.config(text="Błąd! Nie można dzielić przez 0!")
        
        except ValueError:
            labelwynik.config(text="Błąd! W obliczeniu nie znajduje sie liczba!")

        except Exception as e:
            labelwynik.config(text="Błąd równania!")



    root = Tk()

    root.title("Kalkulator")

    labeltitle = Label(root, text="Kalkulator")
    labeltitle.pack(pady=10)


    label1 = Label(root, text="Wprowadź pierwszą liczbę")
    label1.pack()

    entry1 = Entry(root)
    entry1.pack()


    labeldzialanie = Label(root, text="Wprowadź działanie jakie chcesz wykonać (+,-,*,/,**)")
    labeldzialanie.pack()

    entrydzialanie = Entry(root)
    entrydzialanie.pack()


    label2 = Label(root, text="Wprowadź drugą liczbę")
    label2.pack()

    entry2 = Entry(root)
    entry2.pack()

    button = Button(text="Oblicz", command=Oblicz)
    button.pack(pady=10)

    labelwynik = Label(root, text="Wynik równania to : N/A (niezdefiniowane równanie)")
    labelwynik.pack()

    root.mainloop()