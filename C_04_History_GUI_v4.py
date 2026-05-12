from tkinter import *
from datetime import date
from functools import partial # To prevent unwanted windows
import all_constants as c
from tkinter import filedialog


class Converter:
    """
    Length conversion tool (m to cm or cm to m)
    """

    def __init__(self):
        """
        Length converter GUI
        """
        self.all_calculations_list = ['5.0 cm is 0.0500 m', '555.0 cm is 5.5500 m',
                                      '5.55 cm is 0.0555 m', '5.55 m is 555.0000 cm',
                                      '555.0 m is 55500.0000 cm', '555.0 cm is 5.5500 m']



        self.leng_frame = Frame(padx=10, pady=10)
        self.leng_frame.grid()

        self.to_history_button = Button(self.leng_frame,
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

        self.history_frame = Frame(self.history_box, width=300)
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
                     " All calculations are shown to the nearest 3dp.")

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
        """ Export file to location of users choice """
        # Get current date for heading and filename
        today = date.today()

        # Get day month and year as individual strings
        day = today.strftime("%d")
        month = today.strftime("%m")
        year = today.strftime("%Y")

        file_name = f"lengths_{year}-{month}-{day}.txt"

        # Ask the user where to save the file
        write_to = filedialog.asksaveasfilename(
            initialfile=file_name,
        )

        # If user cancels dialog, make file_path empty string
        if not write_to:
            self.export_filename_label.config(bg="#f4cccc",
                                              text="Export cancelled.")
            return

        # write the data and tell user if export successful or not
        try:
            with open(write_to, "w") as text_file:
                text_file.write("Length Calculations \n")
                text_file.write(f"Generated: {day}/{month}/{year}\n\n")
                text_file.write("Here is your calculation history (oldest to newest)...\n")
                for item in calculations_list:
                    text_file.write(item)
                    text_file.write("\n")

            # tell user export is done and crop name
            filename_only = write_to.split("/")[-1]
            success_string = f"Export Successful! File saved as {filename_only}"
            self.export_filename_label.config(bg="#009900", text=success_string)

        # tell user if export failed
        except Exception as e:
            self.export_filename_label.config(bg="#f4cccc",
                                              text=f"Export failed: {e}")

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
