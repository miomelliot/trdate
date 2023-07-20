import re
from typing import List

def stringLines(string: List[str]) -> str:
    """преобразует в `json`"""
    string = ' '.join(string)
    return string

def splitLines(lines: str) -> List[str]:
    """преобразование `str` в `array:str`"""
    lines = re.sub(r"[:-]", " ", lines)
    lines = lines.split()
    return lines
