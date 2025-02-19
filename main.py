from tkinter import *

class Converter():
    """
    Temperature conversion tool (celcius to fahrenheit or fahrenheit to celcius)
    """

    def __init__(self):

        """
        Temperature converter Gui
        """

        self.temp_frame =Frame(padx=10, pady=10)
        self.temp_frame.grid()

#main routine


if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
