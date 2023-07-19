import re

def stringLines(string):
    """преобразует в `json`"""
    string = ' '.join(string)
    return string

def splitLines(lines):
    """преобразование `str` в `array:str`"""
    lines = re.sub(r"[:-]", " ", lines)
    lines = lines.split()
    return lines
