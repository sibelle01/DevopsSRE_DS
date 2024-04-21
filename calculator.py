import math

# Initialize variables used with global keyword in functions
display = "0"
operation = ""
prev_button = ""
numberA = float(0)
numberB = float(0)

# Define ERROR display string
ERROR = "ERROR       "

# Define digit_set and operation_set
digit_set = set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
operation_set = set(["plus", "minus", "multiply", "divide"])

# Define button_set which includes digit_set and operation_set
button_set = set(["sign", "point", "clear", "backspace", "equals"])
button_set.update(digit_set)
button_set.update(operation_set)


def reset(reset_display: bool):
    """
    Function for resetting calculator
    reset_display: True  - Reset everything also the display
                   False - Reset everything except the display
    """
    global display
    global operation
    global prev_button
    global numberA
    global numberB

    if reset_display == True:
        display = "0"
    operation = ""
    prev_button = ""
    numberA = float(0)
    numberB = float(0)


def press_button(button):
    """Function for pressing button on calculator"""
    global prev_button
    update_display(button)
    prev_button = button


def update_display(button):
    """Function for updating calculator display according to button press"""
    global display
    global operation
    global prev_button
    global numberA
    global numberB

    # Do action for clear button
    if button == "clear":
        reset(True)

    # Return immediately if display contains ERROR, because only clear button is allowed in this case
    elif display == ERROR:
        return

    # Do action for digit buttons
    elif button in digit_set:
        if prev_button == "equals":
           reset(True)
        
        if display == "0" or prev_button in operation_set:
            display = button
            return

        if display == "-0":
            display = "-" + button
            return

        # Count number of digits already in display
        digit_count = 0
        for d in range(0, 10):
            digit_count += display.count(str(d))

        # If digit count is less than 10, insert new digit
        if digit_count < 10:
            display += button

    # Do action for sign button
    elif button == "sign":
        if prev_button == "equals":
            reset(False)

        if prev_button in operation_set:
            display = "-0"
            return

        # If first character is "-" remove it, otherwise add "-" as first character
        if display[0] == "-":
            display = display[1:]
        else:
            display = "-" + display

    # Do action for point button
    elif button == "point":
        if prev_button == "equals":
            reset(True)

        if prev_button in operation_set:
            display = "0."
            return

        if not "." in display:
            display += "."

    # Do action for operation buttons
    elif button in operation_set:
        if prev_button != "equals" and prev_button not in operation_set:
            calculate()
        numberA = float(display)
        operation = button

    # Do action for backspace button
    elif button == "backspace":
        if prev_button == "equals":
            reset(False)

        # Remove last character from display
        display = display[:-1]

        # Insert "0" if display is empty or only contains "-"
        if display == "" or display == "-":
            display = "0"

    # Do action for equals button
    elif button == "equals":
        calculate()


def calculate():
    """Function for calculating result of numberA operation numberB"""
    global display
    global prev_button
    global numberA
    global numberB

    # If previous button is not "equals" get new numberB from display, otherwise keep old numberB
    if prev_button != "equals":
        numberB = float(display)

    # Perform operation to get new numberA
    if operation == "":
        numberA = float(display)
    elif operation == "plus":
        numberA = numberA + numberB
    elif operation == "minus":
        numberA = numberA - numberB
    elif operation == "multiply":
        numberA = numberA * numberB
    elif operation == "divide":
        if numberB == 0:
            numberA = float("NAN")
        else:
            numberA = numberA / numberB

    # Write new numberA to display
    display = display_number(numberA)


def display_number(number: float) -> str:
    """Function for converting number to string to be written to display"""

    # Return ERROR in case of NAN or overflow
    if math.isnan(number) or number > 9999999999 or number < -9999999999:
        return ERROR

    # Number of digits before point
    if abs(number) >= 1:
        digits_before = int(math.log10(abs(number)))+1
    else:
        digits_before = 1

    # Number of digits after point (10 digits allowed in total)
    digits_after = 10 - digits_before

    # Format number as string with fixed number of digits after point
    string = ("{:." + str(digits_after) + "F}").format(number)

    # Remove trailing zeros after point
    if string.find(".") != -1:
        while string[-1] == "0":
            string = string[:-1]

    # Remove trailing point
    if string[-1] == ".":
        string = string[:-1]

    # Convert "-0" to 0
    if string == "-0":
        string = "0"

    # Return the string
    return string
