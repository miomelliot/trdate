from ..code.main import TransFormDate

def test_get_date_list():
    ds = TransFormDate()
    ds.get_date_list("3 июля 23 год 23 59")
    assert str(ds) == "['3DD', '7MM', '23YY', '2023YY', '23HH', '59MI']"