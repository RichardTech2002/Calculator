#This is the code for a calculator.

#This line will create the window.
from tkinter import*

#These are varibles for the calculator.
calculator = Tk()
calculator.title("Calculator")
operator = ""
text_Input = StringVar()    

#This creates the display box and also cannot be written in with the keyboard.
Text_Display = Entry(calculator,state = "disabled",textvariable = text_Input, bd = 30, insertwidth = 5,bg = "gold",justify = "right",width = 32).grid(columnspan = 5)

#This will make the numbers appear in the display box.
def buttonNumberClick(number):
    global operator
    operator = operator + str(number)
    text_Input.set(operator)

#This will clear the calculator.
def buttonClearClick(clear):
    global operator
    operator = ""
    text_Input.set("")

#This will evaluate the equation.
def buttonEqualsClick():
    global operator
    answer = str(eval(operator))
    operator = ""
    text_Input.set(answer)

#This makes the quit button work.
def buttonQuitClick():
    calculator.destroy()

#This prevents bad questions such as 0/0.
def invalidFilter():
    zeroByZeroChecker = 0
    additionChecker = 0
    suctractionChecker = 0
    divideChecker = 0
    multiplyChecker = 0
    while multiplyChecker == 1:
        buttonMultiplication.config = "disabled"
    while zeroByZeroChecker and divideChecker == 1:
        buttonZero.config = "disabled"

#This gives the buttons funtionallity.
buttonOne = Button(calculator,padx = 18,pady = 18,bd = 8,bg = "red",text = "1",command = lambda:buttonNumberClick(1))
buttonTwo = Button(calculator,padx = 18,pady = 18,bd = 8,bg = "red",text = "2",command = lambda:buttonNumberClick(2))
buttonThree = Button(calculator,padx = 18,pady = 18,bd = 8,bg = "red",text = "3",command = lambda:buttonNumberClick(3))
buttonFour = Button(calculator,padx = 18,pady = 18,bd = 8,bg = "purple",text = "4",command = lambda:buttonNumberClick(4))
buttonFive = Button(calculator,padx = 18,pady = 18,bd = 8,bg = "purple",text = "5",command = lambda:buttonNumberClick(5))
buttonSix = Button(calculator,padx = 18,pady = 18,bd = 8,bg = "purple",text = "6",command = lambda:buttonNumberClick(6))
buttonSeven = Button(calculator,padx = 18,pady = 18,bd = 8,bg = "blue",text = "7",command = lambda:buttonNumberClick(7))
buttonEight = Button(calculator,padx = 18,pady = 18,bd = 8,bg = "blue",text = "8",command = lambda:buttonNumberClick(8))
buttonNine = Button(calculator,padx = 18,pady = 18,bd = 8,bg = "blue",text = "9",command = lambda:buttonNumberClick(9))
buttonZero = Button(calculator,padx = 18,pady = 18,bd = 8,bg = "green",text = "0",command = lambda:buttonNumberClick(0))
buttonAddition = Button(calculator,padx = 18,pady = 18,bd = 8,bg = "green",text = "+",command = lambda:buttonNumberClick("+"))
buttonSubtraction = Button(calculator,padx = 18,pady = 18,bd = 8,bg = "green",text = "-",command = lambda:buttonNumberClick("-"))
buttonMultiplication = Button(calculator,padx = 18,pady = 18,bd = 8,bg = "green",text = "*",command = lambda:buttonNumberClick("*"))
buttonDivision = Button(calculator,padx = 18,pady = 18,bd = 8,bg = "green",text = "/",command = lambda:buttonNumberClick("/"))
buttonDecimal = Button(calculator,padx = 18,pady = 18,bd = 8,bg = "green",text = ".",command = lambda:buttonNumberClick("."))
buttonClear = Button(calculator,padx = 18,pady = 18,bd = 8,bg = "green",text = "C",command = lambda:buttonClearClick(""))
buttonEquals = Button(calculator,padx = 18,pady = 18,bd = 8,bg = "gold",text = "=",command = buttonEqualsClick)
buttonQuit = Button(calculator,padx = 72,pady = 18,bd = 8,bg = "red",text = "Quit",command = buttonQuitClick)

#This array places the buttons in the "grid".
buttonOne.grid(row = 1,column = 0,rowspan = 1,columnspan = 1)
buttonTwo.grid(row = 2,column = 0,rowspan = 1,columnspan = 1)
buttonThree.grid(row = 3,column = 0,rowspan = 1,columnspan = 1)
buttonFour.grid(row = 1,column = 1,rowspan = 1,columnspan = 1)
buttonFive.grid(row = 2,column = 1,rowspan = 1,columnspan = 1)
buttonSix.grid(row = 3,column = 1,rowspan = 1,columnspan = 1)
buttonSeven.grid(row = 1,column = 2,rowspan = 1,columnspan = 1)
buttonEight.grid(row = 2,column = 2,rowspan = 1,columnspan = 1)
buttonNine.grid(row = 3,column = 2,rowspan = 1,columnspan = 1)
buttonZero.grid(row = 4,column = 1,rowspan = 1,columnspan = 1)
buttonAddition.grid(row = 1,column = 3,rowspan = 1,columnspan = 1)
buttonSubtraction.grid(row = 2,column = 3,rowspan = 1,columnspan = 1)
buttonMultiplication.grid(row = 3,column = 3,rowspan = 1,columnspan = 1)
buttonDivision.grid(row = 4,column = 3,rowspan = 1,columnspan = 1)
buttonDecimal.grid(row = 4,column = 2,rowspan = 1,columnspan = 1)
buttonClear.grid(row = 4,column = 0,rowspan = 1,columnspan = 1)
buttonEquals.grid(row = 5,column = 3,rowspan = 1,columnspan = 1)
buttonQuit.grid(row = 5,column = 0,rowspan = 9,columnspan = 3)

#This makes the window stay up longer, otherwise the window will only stay up for 1 nanosecond.
calculator.mainloop()