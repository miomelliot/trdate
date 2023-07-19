import re
import datetime as dt

def yearLines(list_array):
    """Находим год"""
    for i, item in enumerate(list_array):
        if re.search(r"^год$", item):
            year = f"20{list_array[i-1]}" if len(f"20{list_array[i-1]}") == 4 else dt.datetime.now().year
            list_array[i-1] = f"{list_array[i-1]}YY"
            if len(f"{list_array[i-1]}") == 4 and str(list_array[i-1])[:2] == "20":
                year = f"{list_array[i-1]}" if len(f"{list_array[i-1]}") == 4 else dt.datetime.now().year
            list_array[i] = f"{year}YY"
            return list_array
        elif re.search(r"^20[0-9]{2}$", item, re.IGNORECASE):
            list_array[i] = f"{year}YY"
            return list_array

def monthLines(list_array):
    """Находим месяц и дату"""
    dict_month = {
        "января": "1",
        "февраля": "2",
        "марта": "3",
        "апреля": "4",
        "мая": "5",
        "июня": "6",
        "июля": "7",
        "августа": "8",
        "сентября": "9",
        "октября": "10",
        "ноября": "11",
        "декабря": "12"
    }
    for i, item in enumerate(list_array):
        if item in dict_month:
            list_array[i] = f"{dict_month[item]}MM"
            month = dict_month[item]
            if i != 0:
                day = list_array[i-1]
                list_array[i-1] = f"{list_array[i-1]}DD"
                return list_array
        elif re.search(r"^вчера", item, re.IGNORECASE):
            yesterday = dt.datetime.now() - dt.timedelta(days=1)
            month_date = yesterday.strftime("%m")
            day_date = yesterday.strftime("%d")
            list_array[i] = f"{month_date}MM {day_date}DD"
            month = month_date
            day = day_date
            return list_array
        elif re.search(r"позавчера", item, re.IGNORECASE):
            day_before_yesterday = dt.datetime.now() - dt.timedelta(days=2)
            month_date = day_before_yesterday.strftime("%m")
            day_date = day_before_yesterday.strftime("%d")
            list_array[i] = f"{month_date}MM {day_date}DD"
            month = month_date
            day = day_date
            return list_array
    return list_array

def hourLines(list_array):
    for i, item in enumerate(list_array):
        if re.search(r"^час$", item):
            hour = list_array[i]
            list_array[i] = "1HH"
            return list_array
        elif re.search(r"час", item) and re.search(r"[0-9]", list_array[i - 1], re.IGNORECASE) and not re.search(r"дня|вечер|ноч", list_array[i + 1]):
            if int(list_array[i - 1]) < 24:
                hour = list_array[i-1]
                list_array[i-1] = f"{list_array[i-1]}HH"
                return list_array
        elif re.search(r"^полдень$", item):
            hour = "12"
            list_array[i] = "12HH"
            return list_array
        elif list_array[-1] != item and re.search(r"дня|вечер|ноч", list_array[i + 1]):
            try:
                if int(list_array[i - 1]) in (9, 10, 11):
                    list_array[i - 1] = int(list_array[i - 1]) + 12
                elif int(list_array[i - 1]) == 12:
                    list_array[i - 1] = int(list_array[i - 1]) - 12
                elif re.search(r"дня|вечер", list_array[i + 1]) and int(list_array[i - 1]) < 12:
                    list_array[i - 1] = int(list_array[i - 1]) + 12
            except ValueError:
                if int(list_array[i]) in (9, 10, 11):
                    list_array[i] = int(list_array[i]) + 12
                elif int(list_array[i]) == 12:
                    list_array[i] = int(list_array[i]) - 12
                elif re.search(r"дня|вечер", list_array[i]):
                    list_array[i] = int(list_array[i]) + 12
            hour = list_array[i-1]
            list_array[i-1] = f"{list_array[i-1]}HH"
            return list_array
        elif re.search(r"^(0?[1-9]|1[0-9]|2[0-3])$", item, re.IGNORECASE) and len(list_array) == i+2:
            hour = list_array[i]
            list_array[i] = f"{list_array[i]}HH"
            if re.search(r"^(0?[1-9]|[1-5][0-9]|59)$", list_array[i+1], re.IGNORECASE):
                minute = list_array[i+1]
                list_array[i+1] = f"{list_array[i+1]}MI"
            return list_array
        elif re.search(r"пол", item, re.IGNORECASE):
            if len(list_array) >= i + 1:
                if int(list_array[i + 1]) in (9, 10, 11):
                    list_array[i + 1] = int(list_array[i + 1]) + 12
                elif int(list_array[i + 1]) == 12:
                    list_array[i + 1] = int(list_array[i + 1]) - 12
                hour =list_array[i+1]
                list_array[i+1] = f"{list_array[i+1]}HH"
        elif re.search(r"^\d{2}$", item, re.IGNORECASE):
            if len(list_array) > i + 2 and re.search(r"^\d{2}$", list_array[i + 1], re.IGNORECASE):
                hour =list_array[i]
                list_array[i] = f"{list_array[i]}HH"
                minute = list_array[i+1]
                list_array[i+1] = f"{list_array[i+1]}MI"
                return list_array
            else:
                hour =list_array[i]
                list_array[i] = f"{list_array[i]}HH"
                return list_array
            
def get_d(year, month, day, hour, minute, second):
    date_string = f"{year}-{month}-{day} {hour}:{minute}:{second}"
    date_format = "%Y-%m-%d %H:%M:%S"
    parsed_date = dt.datetime.strptime(date_string, date_format)
    return parsed_date