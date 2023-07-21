from ..code.main import TransFormDate
import datetime as dt

def test_get_date_list():
    ds = TransFormDate()
    ds.get_date_list("3 июля 23 год 23 59")
    assert str(ds) == "['3DD', '7MM', '23YY', '2023YY', '23HH', '59MI']"
    
def test_yearLines():
    ds = TransFormDate("20 1000 23 год")
    ds.yearLines()
    assert str(ds) == "['20', '1000', '23YY', '2023YY']"

def test_monthLines():
    ds = TransFormDate("2 числа")
    ds.monthLines()
    assert str(ds) == "['2DD', 'числа']"
    
def test_hourLines():
    ds = TransFormDate("час")
    ds.hourLines()
    assert str(ds) == "['1HH']"

def test_minuteLines():
    ds = TransFormDate("в 12 минут")
    ds.minuteLines()
    assert str(ds) == "['в', '12MI', 'минут']"
    
def test_get_d():
    ds = TransFormDate()
    ds.get_d()
    date = dt.datetime.now().strftime("%Y %m %d %H %M %S").split()
    assert str(ds) == str(date)