
from code.date_utils import yearLines, monthLines, dayLines, get_d

def test_year_lines():
    year_list_1 = ['2023', '11', '24', '10']
    year_list_2 = ['20', '1000', '23', '11', '24', '10']
    year_answer_1 = ['2023YY', '11', '24', '10']
    year_answer_2 = ['20', '2023YY', '23', '11', '24', '10']
    assert yearLines(year_list_1) == year_answer_1
    assert yearLines(year_list_2) == year_answer_2