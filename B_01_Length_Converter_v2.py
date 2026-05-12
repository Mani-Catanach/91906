from tkinter import *
from functools import partial # To prevent unwanted windows
import all_constants as c
from datetime import date
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
        self.answer_error = Label(self.leng_frame, text=error,
                                  fg="#004C99")
        self.answer_error.grid(row=3)

        # Conversion, help and history / export buttons
        self.button_frame = Frame(self.leng_frame)
        self.button_frame.grid(row=4)

        # button list ( button text | bg colour | command | row | column)
        button_details_list = [
            ["To Metres", "#FE00C4", lambda:self.check_leng(c.UNIT_METRES), 0, 0],
            ["To Centimetres", "#BC88AC", lambda:self.check_leng(c.UNIT_CENTIMETRES), 0, 1],
            ["Help / Info", "#d8b8ca", self.to_help, 1, 0],
            ["History / Export", "#AE0062", self.to_history, 1, 1],
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


    def check_leng(self, unit_leng):
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
            if c.MIN_LENGTH <= to_convert <= c.MAX_LENGTH:
                error = ""
                self.convert(unit_leng, to_convert)
            else:
                error = "Please enter a number between 0 and 1000 (inclusive)"

        except ValueError:
            error = "Please enter a number"

        # display error if necessary
        if error != "":
            self.answer_error.config(text=error, fg="#9C0000")
            self.leng_entry.config(bg="#F4CCCC")
            self.leng_entry.delete(0, END)

    def convert(self, unit_leng, to_convert):
        """
        Converts length and updates answer level. Also stores
        calculation for Export/History feature
        """

        if unit_leng == c.UNIT_CENTIMETRES:
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

    def to_history(self):
        """
        Opens history dialogue box and disables history button
        (so that users can't create multiple history boxes).
        """
        DisplayHistory(self, self.all_calculations_list)

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

        # List and loop to set background colour on
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

class DisplayHistory:

    def __init__(self, partner, calculations_list):
        # setup dialogue box and background colour

        self.history_box = Toplevel()

        # diable history button
        partner.to_history_button.config(state=DISABLED)

        # If users press cross at top, closes history and
        # 'releases' history button
        self.history_box.protocol("WM_DELETE_WINDOW",
                               partial(self.close_history, partner))

        self.history_frame = Frame(self.history_box, width=300,
                                height=200)
        self.history_frame.grid()

        # background colour and text for calculation area
        if len(calculations_list) <= c.MAX_CALCS:
            calc_back = "#D5E8D4"
            calc_amount = "all your"
        else:
            calc_back = "#ffe6cc"
            calc_amount = (f"your recent calculations -"
                           f"showing {c.MAX_CALCS} / {len(calculations_list)}")

        #strings for long labels
        recent_intro_txt = (f"Below are {calc_amount} calculations."
                     " All calculations are shown to the nearest degree.")

        # create string from calculations list (newest calculations first)
        newest_first_string = ""
        newest_first_list = list(reversed(calculations_list))

        if len(newest_first_list) <= c.MAX_CALCS:

            for item in newest_first_list[:-1]:
                newest_first_string += item + "\n"

            newest_first_string += newest_first_list[-1]

        #if we have more than 5 items
        else:
            for item in newest_first_list[:c.MAX_CALCS-1:]:
                newest_first_string += item + "\n"

            newest_first_string += newest_first_list[c.MAX_CALCS-1]

        export_instruction_txt = ("Please push <Export> to save your calculations in a text file. "
                         "If the filename already exists it will be overwritten!")


        #Label list (label text | format | bg)
        history_labels_list = [
            ["History / Export", ("Arial", 16, "bold"), None],
            [recent_intro_txt, ("Arial", 11), None],
            [newest_first_string, ("Arial", 14), calc_back],
            [export_instruction_txt, ("Arial", 12), None]
        ]

        history_label_ref = []

        for count, item in enumerate(history_labels_list):
            make_label = Label(self.history_box, text=item[0], font=item[1],
                               bg=item[2],
                               wraplength=300, justify="left", pady=10, padx=20)
            make_label.grid(row=count)

            history_label_ref.append(make_label)

        # retrieve export instruction label so that we can
        # configure it to show the filename if the user exports the file
        self.export_filename_label = history_label_ref[3]

        # export, close buttons
        self.button_frame = Frame(self.history_box)
        self.button_frame.grid(row=4)

        button_ref_list = []

        # button list ( button text | bg colour | command | row | column)
        button_details_list = [
            ["Export", "#004C99", lambda: self.export_data(calculations_list), 0, 0],
            ["Close", "#999999", partial(self.close_history, partner), 0, 1]
        ]

        # List to hold button once they have been made
        self.button_ref_list = []

        for btn in button_details_list:
            self.make_button = Button(self.button_frame,
                                      text=btn[0], bg=btn[1],
                                      fg="#000000", font=("Arial", 12, "bold"),
                                      width=12, command=btn[2])
            self.make_button.grid(row=btn[3], column=btn[4], padx=10, pady=10)

    def export_data(self, calculations_list):
        # get current date for heading and filename
        today = date.today()

        # get day month and year as individual strings
        day = today.strftime("%d")
        month = today.strftime("%m")
        year = today.strftime("%Y")

        file_name = f"lengths_{year}-{month}-{day}"

        # edit label so users know that their export is done
        success_string = ("Export Successful, The file is called"
                          f"{file_name}.txt")
        self.export_filename_label.config(bg="#009900", text=success_string)

        # write data to text file
        write_to = f"{file_name}.txt"

        with open(write_to, "w") as text_file:
            text_file.write(" Length Calculations \n")
            text_file.write(f"Generated: {day}/{month}/{year}\n\n")
            text_file.write("Here is your calculation history (oldes to newest)... \n")

            # write the item to file
            for item in calculations_list:
                text_file.write(item)
                text_file.write("\n")

    def close_history(self, partner):
        """
        Closes history dialogue box and enables history button
        """
        # Put history button back to normal
        partner.to_history_button.config(state=NORMAL)
        self.history_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Length Conversion")
    Converter()
    root.mainloop()
