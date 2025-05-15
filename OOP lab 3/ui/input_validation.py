def input_int(prompt="Please enter a whole number: ", ge=None, gt=None, le=None, lt=None):
    """

    :param prompt:
    :param ge:
    :param gt:
    :param le:
    :param lt:
    :return:
    """
    num = 0
    while True:
        try: 
            num = int(input(prompt))
            if ge is not None and num < ge:
                print("Number must be greater than or equal to:", ge)
                continue
            if gt is not None and num <= gt:
                print("Number must be greater than:", gt)
                continue
            if le is not None and num > le:
                print("Number must be less than or equal to:", le)
                continue
            if lt is not None and num >= lt:
                print("Number must be less than:", lt)
                continue
            return num
        except ValueError:
            print("Invalid answer, please enter a whole number.")


def input_float(prompt="Please enter a decimal number:", ge=None, gt=None, le=None, lt=None):
    """

    :param prompt:
    :param ge:
    :param gt:
    :param le:
    :param lt:
    :return:
    """
    num = 0.0
    while True:
        try:
            num = float(input(prompt))
            if ge is not None and num < ge:
                print("Number must be greater than or equal to:", ge)
                continue
            if gt is not None and num <= gt:
                print("Number must be greater than:", gt)
                continue
            if le is not None and num > le:
                print("Number must be less than or equal to:", le)
                continue
            if lt is not None and num >= lt:
                print("Number must be less than:", lt)
                continue
            return num
        except ValueError:
            print("Invalid answer, please enter a decimal number.")


def input_string(prompt="Please enter a string: ", valid=lambda x: x.strip() != ""):
    """
    Function to prompt for and return a string of characters.
    Validation is done by a validation function passed as a parameter.
    The default validation function treats non-empty input as valid.

    :param prompt: string Optional string to use as prompt
    :param valid: function A function that takes a string and returns True if valid, False otherwise
    :return: string Validated string of characters
    """
    while True:
        chars = input(prompt)
        if valid(chars):
            return chars
        else:
            print("Invalid string.")


def input_y_or_n(prompt="Please enter 'y' or 'n': "):
    """
    Function to prompt for and return 'y' or 'n'.
    'Y', 'N', and all cases of 'yes' and 'no' are accepted.
    :param prompt: string Optional string to use as prompt
    :return: string Non-empty string of characters
    """
    answer = ""
    answer = input(prompt)
    answer = answer.lower()

    while answer != "n" and answer != "y" and answer != "no" and answer != "yes":
        print("Invalid response.")
        answer = input(prompt)
        answer = answer.lower()

    return answer


def select_item(choices, prompt="Please select an option: ", mappings=None):
    """
    Prompt the user to select an item from a list of choices. The user input is case-insensitive.
    An optional dictionary of mappings can be provided to map user inputs to specific outputs.

    :param choices: List of valid choices to present to the user
    :param prompt: Prompt message to display to the user
    :param mappings: Optional dictionary to map user input to specific outputs
    :return: The item selected by the user
    """
    if mappings is None:
        mappings = {}
    while True:
        print("Choices: ", ', '.join(choices))
        user_input = input(prompt).strip().lower()
        if user_input in mappings:
            return mappings[user_input]
        for choice in choices:
            if user_input == choice.lower():
                return choice
        print("Invalid choice. Please enter a valid option.")
