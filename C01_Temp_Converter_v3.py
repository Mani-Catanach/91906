from tkinter import *
import all_constants as c
import conversion_rounding as cr

class Converter:
    """
    Length conversion tool (deg C to deg F or deg F to deg C)
    """

    def __init__(self):
        """
        Length converter GUI
        """

        self.all_calculations_list = []

        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame,
                                  text="Length Convertor",
                                  font=("Arial", 16, "bold")
                                  )
        self.temp_heading.grid(row=0)

        instructions = ("Please enter a Length below and press one of the buttons"
                        "to convert it to degrees C or degrees F")
        self.temp_instructions = Label(self.temp_frame,
                                       text=instructions,
                                       wraplength=250, width=40,
                                       justify="left")
        self.temp_instructions.grid(row=1)

        self.temp_entry = Entry(self.temp_frame,
                                font=("Arial", 14)
                                )
        self.temp_entry.grid(row=2, padx=10, pady=10)

        error = "Please enter a number"
        self.answer_error = Label(self.temp_frame, text=error,
                                  fg="#004C99")
        self.answer_error.grid(row=3)

        # Conversion, help and history / export buttons
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        # button list ( button text | bg colour | command | row | column)
        button_details_list = [
            ["To Metres", "#990099", lambda:self.check_temp(c.UNIT_CENTIMETRES), 0, 0],
            ["To Centimetres", "#009900", lambda:self.check_temp(c.UNIT_METRES), 0, 1],
            ["Help / Info", "#CC6600", "", 1, 0],
            ["History / Export", "#004C99", "", 1, 1],
        ]

        # List to hold button once they have been made
        self.button_ref_list = []

        for item in button_details_list:
            self.make_button = Button(self.button_frame,
                                      text=item[0], bg=item[1],
                                      fg="#000000", font=("Arial", 12, "bold"),
                                      width=12, command=item[2])
            self.make_button.grid(row=item[3], column=item[4], padx=5, pady=5)

            self.button_ref_list.append(self.make_button)

        # retrieve 'history / export' button and disable it at the start
        self.to_history_button = self.button_ref_list[3]
        self.to_history_button.config(state=DISABLED)

    def check_temp(self, unit_leng):
        """
        Checks Length is valid and either invokes calculation
        function or shows a custom error
        """

        # Retrieve Length to be converted
        to_convert = self.temp_entry.get()

        # Reset label and entry box (if we had an error
        self.answer_error.config(fg="#004C99")
        self.temp_entry.config(bg="#FFFFFF")

        # check that amount to be converted is a number above absolute zero
        try:
            to_convert = float(to_convert)
            if to_convert >= unit_leng:
                error = ""
                self.convert(unit_leng, to_convert)
            else:
                error = "Too low"

        except ValueError:
            error = "Please enter a number"

        # display error if necessary
        if error != "":
            self.answer_error.config(text=error, fg="#9C0000")
            self.temp_entry.config(bg="#F4CCCC")
            self.temp_entry.delete(0, END)

    def convert(self, unit_leng, to_convert):
        """
        Converts Length and updates answer level. Also stores
        calculation for Export/History feature
        """

        if unit_leng == c.UNIT_METRES:
            answer = cr.to_centimetres(to_convert)
            answer_statement = f"{to_convert} deg C is {answer} deg F"
        else:
            answer = cr.to_metres(to_convert)
            answer_statement = f"{to_convert} deg F is {answer} deg C"

        # enable history export button as soon as we have a valid calculation
        self.to_history_button.config(state=NORMAL)

        self.answer_error.config(text=answer_statement)
        self.all_calculations_list.append(answer_statement)
        print(self.all_calculations_list)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Length Conversion")
    Converter()
    root.mainloop()
