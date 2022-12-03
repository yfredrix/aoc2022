
def char_to_rank(input_str):
    if ord(input_str) < 95:
        return ord(input_str) - 38
    else:
        return ord(input_str) - 96