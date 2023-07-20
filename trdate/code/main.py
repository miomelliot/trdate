import re
import datetime as dt

class TransFormDate():
    
    """
    stringLines: `array` -> `json`
    
    splitLines: `lines` -> `array`:`str`
    
    """
    def __init__(self):
        self.year = dt.datetime.now().year
        self.month = dt.datetime.now().month
        self.day = dt.datetime.now().day
        self.hour = "00"
        self.minute = "00"
        self.second = "00"
        self.list_array = self.splitLines("сегодня")

    def __str__(self):
        return f"{self.list_array}"

    def stringLines(self, string):
        """преобразует в `json`"""
        string = ' '.join(string)
        return string

    def splitLines(self, lines):
        """преобразование `str` в `array:str`"""
        lines = re.sub(r"[:-]", " ", lines)
        lines = lines.split()
        return lines

    def yearLines(self):
        """Находим год"""
        for i, item in enumerate(self.list_array):
            if re.search(r"^год$", item):
                self.year = f"20{self.list_array[i-1]}" if len(f"20{self.list_array[i-1]}") == 4 else dt.datetime.now().year
                self.list_array[i-1] = f"{self.list_array[i-1]}YY"
                if len(f"{self.list_array[i-1]}") == 4 and str(self.list_array[i-1])[:2] == "20":
                    self.year = f"{self.list_array[i-1]}" if len(f"{self.list_array[i-1]}") == 4 else dt.datetime.now().year
                self.list_array[i] = f"{self.year}YY"
                return self.list_array
            elif re.search(r"^20[0-9]{2}$", item, re.IGNORECASE):
                self.list_array[i] = f"{self.year}YY"
                return self.list_array

    def monthLines(self):
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
        for i, item in enumerate(self.list_array):
            if item in dict_month:
                self.list_array[i] = f"{dict_month[item]}MM"
                self.month = dict_month[item]
                if i != 0:
                    self.day = self.list_array[i-1]
                    self.list_array[i-1] = f"{self.list_array[i-1]}DD"
                    return self.stringLines(self.list_array)
            elif re.search(r"^вчера", item, re.IGNORECASE):
                yesterday = dt.datetime.now() - dt.timedelta(days=1)
                month_date = yesterday.strftime("%m")
                day_date = yesterday.strftime("%d")
                self.list_array[i] = f"{month_date}MM {day_date}DD"
                self.month = month_date
                self.day = day_date
                return self.list_array
            elif re.search(r"позавчера", item, re.IGNORECASE):
                day_before_yesterday = dt.datetime.now() - dt.timedelta(days=2)
                month_date = day_before_yesterday.strftime("%m")
                day_date = day_before_yesterday.strftime("%d")
                self.list_array[i] = f"{month_date}MM {day_date}DD"
                self.month = month_date
                self.day = day_date
                return self.list_array
        return self.list_array

    def hourLines(self):
        for i, item in enumerate(self.list_array):
            if re.search(r"^час$", item):
                self.hour = self.list_array[i]
                self.list_array[i] = "1HH"
                return self.list_array
            elif re.search(r"час", item) and re.search(r"[0-9]", self.list_array[i - 1], re.IGNORECASE) and not re.search(r"дня|вечер|ноч", self.list_array[i + 1]):
                if int(self.list_array[i - 1]) < 24:
                    self.hour = self.list_array[i-1]
                    self.list_array[i-1] = f"{self.list_array[i-1]}HH"
                    return self.list_array
            elif re.search(r"^полдень$", item):
                self.hour = "12"
                self.list_array[i] = "12HH"
                return self.list_array
            elif self.list_array[-1] != item and re.search(r"дня|вечер|ноч", self.list_array[i + 1]):
                try:
                    if int(self.list_array[i - 1]) in (9, 10, 11):
                        self.list_array[i - 1] = int(self.list_array[i - 1]) + 12
                    elif int(self.list_array[i - 1]) == 12:
                        self.list_array[i - 1] = int(self.list_array[i - 1]) - 12
                    elif re.search(r"дня|вечер", self.list_array[i + 1]) and int(self.list_array[i - 1]) < 12:
                        self.list_array[i - 1] = int(self.list_array[i - 1]) + 12
                except ValueError:
                    if int(self.list_array[i]) in (9, 10, 11):
                        self.list_array[i] = int(self.list_array[i]) + 12
                    elif int(self.list_array[i]) == 12:
                       self.list_array[i] = int(self.list_array[i]) - 12
                    elif re.search(r"дня|вечер", self.list_array[i]):
                        self.list_array[i] = int(self.list_array[i]) + 12
                self.hour = self.list_array[i-1]
                self.list_array[i-1] = f"{self.list_array[i-1]}HH"
                return self.list_array
            elif re.search(r"^(0?[1-9]|1[0-9]|2[0-3])$", item, re.IGNORECASE) and len(self.list_array) == i+2:
                self.hour = self.list_array[i]
                self.list_array[i] = f"{self.list_array[i]}HH"
                if re.search(r"^(0?[1-9]|[1-5][0-9]|59)$", self.list_array[i+1], re.IGNORECASE):
                    self.minute = self.list_array[i+1]
                    self.list_array[i+1] = f"{self.list_array[i+1]}MI"
                return self.list_array
            elif re.search(r"пол", item, re.IGNORECASE):
                if len(self.list_array) >= i + 1:
                    if int(self.list_array[i + 1]) in (9, 10, 11):
                       self.list_array[i + 1] = int(self.list_array[i + 1]) + 12
                    elif int(self.list_array[i + 1]) == 12:
                       self.list_array[i + 1] = int(self.list_array[i + 1]) - 12
                    self.hour =self.list_array[i+1]
                    self.list_array[i+1] = f"{self.list_array[i+1]}HH"
            elif re.search(r"^\d{2}$", item, re.IGNORECASE):
                if len(self.list_array) > i + 2 and re.search(r"^\d{2}$", self.list_array[i + 1], re.IGNORECASE):
                    self.hour =self.list_array[i]
                    self.list_array[i] = f"{self.list_array[i]}HH"
                    self.minute = self.list_array[i+1]
                    self.list_array[i+1] = f"{self.list_array[i+1]}MI"
                    return self.list_array
                else:
                    self.hour =self.list_array[i]
                    self.list_array[i] = f"{self.list_array[i]}HH"
                    return self.list_array

    def get_d(self):
        date_string = f"{self.year}-{self.month}-{self.day} {self.hour}:{self.minute}:{self.second}"
        date_format = "%Y-%m-%d %H:%M:%S"
        parsed_date = dt.datetime.strptime(date_string, date_format)
        return parsed_date

    def get_date_list(self, line):
        self.list_array = self.splitLines(line)
        a = self.yearLines()
        b = self.monthLines()
        c = self.hourLines()
        
        parsed_date = self.get_d()

        # Получение текущей даты
        now = dt.datetime.now()

        if parsed_date > now:
            self.year = int(now.year) - 2
            parsed_date = self.get_d()
            print(parsed_date)
        else:
            print(parsed_date)


if __name__ == '__main__':
    ds = TransFormDate()
    ds.get_date_list("3 июля 23 год 23 59")
    print(ds)