from datetime import date

calculations = ['10.0 deg F is -12 deg C', '20.0 deg F is -7 deg C',
                                     '30.0 deg F is -1 deg C', '40.0 deg F is 4 deg C',
                                     '50.0 deg F is 10 deg C', '60.0 deg F is 16 deg C']

# get current date for heading and filename
today = date.today()

# get day month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

file_name = f"temperatures_{year}-{month}-{day}"
write_to = f"{file_name}.txt"

with open(write_to, "w") as text_file:

    text_file.write(" Temperature Calculations \n")
    text_file.write(f"Generated: {day}/{month}/{year}\n\n")
    text_file.write("Here is your calculation history (oldes to newest)... \n")

    # write theitem to file
    for item in calculations:
        text_file.write(item)
        text_file.write("\n")