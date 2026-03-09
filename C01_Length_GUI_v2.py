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

        # button list ( button text | bg colour | command | row | column)
        button_details_list = [
            ["To Metres", "#990099", "", 0, 0],
            ["To Centimetres", "#009900", "", 0, 1],
            ["Help / Info", "#CC6600", "", 1, 0],
            ["History / Export", "#004C99", "", 1, 1],
        ]

        # List to hold button once they have been made
        self.button_ref_list = []

        for item in button_details_list:
            self.make_button = Button(self.button_frame,
                                      text=item[0], bg=item[1],
                                      fg="#FFFFFF", font=("Arial", 12, "bold"),
                                      width=12, command=item[2])
            self.make_button.grid(row=item[3], column=item[4], padx=5, pady=5)

            self.button_ref_list.append(self.make_button)

        # retrieve 'history / export' button and disable it at the start
        self.to_history_button = self.button_ref_list[3].config(state=DISABLED)


    # main routine


if __name__ == "__main__":
    root = Tk()
    root.title("Length Conversion")
    Converter()
    root.mainloop()
