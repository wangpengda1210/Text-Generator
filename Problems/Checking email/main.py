def check_email(string):
    assert isinstance(string, str)
    if " " in string:
        return False

    if "@" not in string:
        return False

    at_position = string.find("@")
    if at_position == len(string) - 1:
        return False

    if string[at_position + 1] == ".":
        return False

    if "." in string[at_position + 1:]:
        return True
    else:
        return False
