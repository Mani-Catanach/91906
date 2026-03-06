def format_ans(val):
    """
    Formats value to be converted to a float
    """
    return "{:.4f}".format(val)

def to_metres(to_convert):
    """
    Converts from deg F to deg C
    :param to_convert: Temperature to be converted in deg F
    :return:  Converted temperature in deg C
    """
    answer = to_convert / 100
    return format_ans(answer)


def to_centimetres(to_convert):
    """
    Converts from deg C to deg F
    :param to_convert: Temperature to be converted in deg C
    :return:  Converted temperature in deg F
    """
    answer = to_convert * 100
    return format_ans(answer)



# Main Routine / Testing starts here
# to_c_test = [0, 100, -459]
# to_f_test = [0, 100, 40, -273]
#
# for item in to_f_test:
#     ans = to_fahrenheit(item)
#     print(f"{item} C is {ans} F")
#
# print()
#
# for item in to_c_test:
#     ans = to_celsius(item)
#     print(f"{item} F is {ans} C")