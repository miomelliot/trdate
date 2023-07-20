import datetime as dt
from ..code.date_utils import yearLines, monthLines, hourLines, get_d


def test_year_lines():
    """
    Determines a year from converted oral speech.
    Take into account the presence of speech distortion

    Определяет год из преобразованной устной речи.
    Принять во внимание наличие искажения речи
    """
    year_list = ['2023', '11', '24', '10']
    year_answer = ['2023YY', '11', '24', '10']
    assert yearLines(year_list) == year_answer

    year_list = ['20', '1000', '23', '11', '24', '10']
    year_answer = ['20YY', '2023YY', '23YY', '11', '24', '10']
    assert yearLines(year_list) == year_answer


def test_monthLines():

    list_array = ["3", "июля", "23", "год"]
    expected_output = ["3DD", "7MM", "23", "год"]
    assert monthLines(list_array) == expected_output

    yesterday = dt.datetime.now() - dt.timedelta(days=1)
    month_date = yesterday.strftime("%m")
    day_date = yesterday.strftime("%d")
    list_array = ["вчера"]
    expected_output = [f'{month_date}MM {day_date}DD']
    assert monthLines(list_array) == expected_output

    day_before_yesterday = dt.datetime.now() - dt.timedelta(days=2)
    month_date = day_before_yesterday.strftime("%m")
    day_date = day_before_yesterday.strftime("%d")
    list_array = ["позавчера"]
    expected_output = [f'{month_date}MM {day_date}DD']
    assert monthLines(list_array) == expected_output


def test_hourLines():
    list_array = ["час"]
    expected_output = ["1HH"]
    assert hourLines(list_array) == expected_output

    list_array = ["12", "часов"]
    expected_output = ["12HH", "часов"]
    assert hourLines(list_array) == expected_output

    list_array = ["9", "часов", "вечера"]
    expected_output = ["21HH", "часов", "вечера"]
    assert hourLines(list_array) == expected_output

    list_array = ["17", "часов"]
    expected_output = ["17HH", "часов"]
    assert hourLines(list_array) == expected_output

    # list_array = ["12", "15"]
    # expected_output = ["12HH", "15MI"]
    # assert hourLines(list_array) == expected_output


def test_get_d():
    year = "2022"
    month = "10"
    day = "15"
    hour = "12"
    minute = "30"
    second = "00"
    expected_output = dt.datetime(2022, 10, 15, 12, 30, 0)
    assert get_d(year, month, day, hour, minute, second) == expected_output
