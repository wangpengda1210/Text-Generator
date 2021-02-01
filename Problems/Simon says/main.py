def what_to_do(instructions):
    assert isinstance(instructions, str)
    if instructions.startswith("Simon says"):
        return f'I {instructions[11:]}'
    elif instructions.endswith("Simon says"):
        return f'I {instructions[:instructions.find("Simon says") - 1]}'
    else:
        return "I won't do it!"
