from tkinter import *
from functools import partial # To prevent unwanted windows
import all_constants as c
import conversion_rounding as cr

class Converter:
    """
    Length conversion tool (m to cm or cm to m)
    """

    def __init__(self):
        """
        Length converter GUI
        """

        self.all_calculations_list = []


        self.leng_frame = Frame(padx=10, pady=10)
        self.leng_frame.grid()

        self.leng_heading = Label(self.leng_frame,
                                  text="Length Convertor",
                                  font=("Arial", 16, "bold")
                                  )
        self.leng_heading.grid(row=0)

        instructions = ("Please enter a length below and press one of the buttons"
                        "to convert it to m or  cm")
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
        self.answer_error = Label(self.leng_frame, text=error,
                                  fg="#004C99")
        self.answer_error.grid(row=3)

        # Conversion, help and history / export buttons
        self.button_frame = Frame(self.leng_frame)
        self.button_frame.grid(row=4)

        # button list ( button text | bg colour | command | row | column)
        button_details_list = [
            ["To Metres", "#990099", lambda:self.check_leng(c.UNIT_CENTIMETRES), 0, 0],
            ["To Centimetres", "#009900", lambda:self.check_leng(c.UNIT_METRES), 0, 1],
            ["Help / Info", "#CC6600", self.to_help, 1, 0],
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

        # retrieve help button
        self.to_help_button = self.button_ref_list[2]

        # retrieve 'history / export' button and disable it at the start
        self.to_history_button = self.button_ref_list[3]
        self.to_history_button.config(state=DISABLED)



    def check_leng(self, min_leng):
        """
        Checks length is valid and either invokes calculation
        function or shows a custom error
        """

        # Retrieve length to be converted
        to_convert = self.leng_entry.get()

        # Reset label and entry box (if we had an error
        self.answer_error.config(fg="#004C99")
        self.leng_entry.config(bg="#FFFFFF")

        # check that amount to be converted is a number above absolute zero
        try:
            to_convert = float(to_convert)
            if to_convert >= 0:
                error = ""
                self.convert(min_leng, to_convert)
            else:
                error = "Too low"

        except ValueError:
            error = "Please enter a number"

        # display error if necessary
        if error != "":
            self.answer_error.config(text=error, fg="#9C0000")
            self.leng_entry.config(bg="#F4CCCC")
            self.leng_entry.delete(0, END)

    def convert(self, min_leng, to_convert):
        """
        Converts length and updates answer level. Also stores
        calculation for Export/History feature
        """

        if min_leng == c.UNIT_CENTIMETRES:
            answer = cr.to_centimetres(to_convert)
            answer_statement = f"{to_convert} m is {answer} cm"
        else:
            answer = cr.to_metres(to_convert)
            answer_statement = f"{to_convert} cm is {answer} m"

        # enable history export button as soon as we have a valid calculation
        self.to_history_button.config(state=NORMAL)

        self.answer_error.config(text=answer_statement)
        self.all_calculations_list.append(answer_statement)
        print(self.all_calculations_list)

    def to_help(self):
        """
        Opens help dialogue box and disables help button
        (so that users can't create multiple help boxes).
        """
        DisplayHelp(self)


class DisplayHelp:

    def __init__(self, partner):
        # setup dialogue box and background colour
        background = "#ffe6cc"
        self.help_box = Toplevel()

        # diable help button
        partner.to_help_button.config(state=DISABLED)

        # If users press cross at top, closes help and
        # 'releases' help button
        self.help_box.protocol("WM_DELETE_WINDOW",
                               partial(self.close_help, partner))

        self.help_frame = Frame(self.help_box, width=300,
                                height=200)
        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame,
                                     text="Help / Info",
                                      font=("Arial", 14, "bold"),)
        self.help_heading_label.grid(row=0)

        help_text = ("To use the program, simply enter the length"
                     "you wish to convert and then choose to convert to "
                     "either metres or "
                     "centimetres... \n\n"
                     "Note that 0 is the minimum length for both"
                     "m and cm. If you try to convert a"
                     "length that is less than 0,"
                     "you will get an error message. \n\n "
                     "To see your "
                     "calculation history and export it to a text "
                     "file, please click the History / Export button")

        self.help_text_label = Label(self.help_frame,
                                     text=help_text, wraplength=350,
                                     justify="left")
        self.help_text_label.grid(row=1, padx=5, pady=5)

        self.dismiss_button = Button(self.help_frame,
                                     font=("Arial", 12, "bold"),
                                     text="Dismiss", bg="#CC6600",
                                     fg="#FFFFFF", command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

        # List and kloop to set background colour on
        # everything except the buttons.
        recolour_list = [self.help_frame, self.help_heading_label,
                         self.help_text_label]

        for item in recolour_list:
            item.config(bg=background)

    def close_help(self, partner):
        """
        Closes help dialogue box and enables help button
        """
        # Put help button back to normal
        partner.to_help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Length Conversion")
    Converter()
    root.mainloop()
