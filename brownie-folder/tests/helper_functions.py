def remove_whitespace(file):
    lines = file.readlines()
    lines = [s.strip() for s in lines]
    return [s for s in lines if s]
