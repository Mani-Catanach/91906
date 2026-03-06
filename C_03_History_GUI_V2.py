from tkinter import *
from functools import partial # To prevent unwanted windows
import all_constants as c

class Converter:
    """
    Temperature conversion tool (deg C to deg F or deg F to deg C)
    """

    def __init__(self):
        """
        Temperature converter GUI
        """
        self.all_calculations_list = ['10.0 deg F is -12 deg C', '20.0 deg F is -7 deg C',
                                     '30.0 deg F is -1 deg C', '40.0 deg F is 4 deg C',
                                     '50.0 deg F is 10 deg C', '60.0 deg F is 16 deg C']


        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.to_history_button = Button(self.temp_frame,
                                     text="History / Export",
                                     bg="#004C99",
                                     fg="#FFFFFF",
                                     font=("Arial", 12, "bold"), width=12,
                                     command=self.to_history)
        self.to_history_button.grid(row=1, padx=5, pady=5)

    def to_history(self):
        """
        Opens history dialogue box and disables history button
        (so that users can't create multiple history boxes).
        """
        DisplayHistory(self, self.all_calculations_list)

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
            ["Export", "#004C99", "", 0, 0],
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
    root.title("Temperature Conversion")
    Converter()
    root.mainloop()
