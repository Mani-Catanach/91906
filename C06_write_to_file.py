from datetime import date

calculations = []

# get current date for heading and filename
today = date.today()

# get day month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

file_name = f"lengths_{year}-{month}-{day}"
write_to = f"{file_name}.txt"

with open(write_to, "w") as text_file:

    text_file.write(" Length Calculations \n")
    text_file.write(f"Generated: {day}/{month}/{year}\n\n")
    text_file.write("Here is your calculation history (oldes to newest)... \n")

    # write the item to file
    for item in calculations:
        text_file.write(item)
        text_file.write("\n")