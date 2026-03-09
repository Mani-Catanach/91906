def format_ans(val):
    """
    Formats value to be converted to a float
    """
    return "{:.4f}".format(val)

def to_metres(to_convert):
    """
    Converts from cm to m
    :param to_convert: Length to be converted in cm
    :return:  Converted length in m
    """
    answer = to_convert / 100
    return format_ans(answer)


def to_centimetres(to_convert):
    """
    Converts from m to cm
    :param to_convert: Length to be converted in m
    :return:  Converted length in cm
    """
    answer = to_convert * 100
    return format_ans(answer)