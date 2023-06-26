class TextColor:
    """
    Class can be used to colorize console text strings. Only works with compatible console output.
    Strings need to prepend with text code, and postpend with .end() code.
    Example:
        colors = TextColor()
        "{0} A string of text I want to be red. {1}".format(colors.red(), colors.end())
    """

    bold = "\033[1m"
    italic = "\033[3m"
    underline = "\033[4m"
    highlight = "\033[7m"
    strikethrough = "\033[9m"
    underline_thick = "\033[21m"
    boxed = "\033[51m"
    black = "\033[30m"
    black_highlight = "\33[40m"
    grey_dark = "\033[90m"
    grey_highlight = "\33[100m"
    grey_light = "\033[37m"
    red = "\033[91m"
    red_highlight = "\033[101m"
    orange = "\033[93m"
    orange_highlight = "\033[103m"
    blue = "\033[94m"
    blue_highlight = "\033[104m"
    purple = "\033[95m"
    purple_highlight = "\033[105m"
    cyan = "\033[96m"
    cyan_highlight = "\033[106m"
    white = "\033[97m"
    white_highlight = "\033[107m"
    magenta = "\033[95m"
    magenta_highlight = "\033[105m"
    green = "\033[92m"
    green_highlight = "\033[102m"
    warn = "\n\x1B[31;40m\u2588\33[5m"
    end = "\033[0m"


def testing():
    # Testing all string manipulation IDs...
    for x in range(0,999):
        print("{0}: \33[{0}mThis is a test string using index '{0}'\033[0m".format(x))

    print('\x1B[31;40m' + u"\u2588" + "\33[5m Blinking??")
    print(u"\u2588")
    CSI = "\x1B["
    print(CSI + "31;40m" + "Colored Text" + CSI + "0m")
    print(CSI + "31;40m" + u"\u2588" + CSI + "0m")

# testing()
