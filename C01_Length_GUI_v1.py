from tkinter import *

class Converter:
    """
    Length conversion tool (m to cm or cm to m)
    """

    def __init__(self):
        """
        Length converter GUI
        """

        self.leng_frame = Frame(padx=10, pady=10)
        self.leng_frame.grid()

        self.leng_heading = Label(self.leng_frame,
                                  text="Length Convertor",
                                  font=("Arial", 16, "bold")
                                  )
        self.leng_heading.grid(row=0)

        instructions = ("Please enter a length below and press one of the buttons"
                        "to convert it to metres or centimetres")
        self.leng_instructions = Label(self.leng_frame,
                                       text=instructions,
                                       wraplength=250, width=40,
                                       justify="left")
        self.leng_instructions.grid(row=1)

        self.leng_entry = Entry(self.leng_frame,
                                font=("Arial", 14)
                                )
        self.leng_entry.grid(row=2, padx=10, pady=10)

        error = "Please enter a number"
        self.leng_error = Label(self.leng_frame, text=error,
                                fg="#9C0000")
        self.leng_error.grid(row=3)

        # Conversion, help and history / export buttons
        self.button_frame = Frame(self.leng_frame)
        self.button_frame.grid(row=4)

        self.to_metres_button = Button(self.button_frame,
                                        text="To Metres",
                                        bg="#990099",
                                        fg="#ffffff",
                                        font=("Arial", 12, "bold"), width=12)
        self.to_metres_button.grid(row=0, column=0,padx=5,pady=5)

        self.to_centimetres_button = Button(self.button_frame,
                                        text="To Centimetres",
                                        bg="#666666",
                                        fg="#ffffff",
                                        font=("Arial", 12, "bold"), width=12)
        self.to_centimetres_button.grid(row=0, column=1,padx=5,pady=5)

    # main routine


if __name__ == "__main__":
    root = Tk()
    root.title("Length Conversion")
    Converter()
    root.mainloop()