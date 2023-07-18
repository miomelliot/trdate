import re
import datetime as dt

class TransFormDate():

    def __init__(self):
        self._year = dt.datetime.now().year
        self._month = dt.datetime.now().month
        self._day = dt.datetime.now().day
        self._hour = "00"
        self._minute = "00"
        self._second = "00"
        self._list_array = None

    def __str__(self):
        return f"{self._list_array}"

    def stringLines(self, string):
        string = ' '.join(string)
        return string

    def splitLines(self, lines):
        lines = re.sub(r"[:-]", " ", lines)
        lines = lines.split()
        self._list_array = lines

    def Definition_of_the_year(self):
        if re.search(r"\d{4}", self._list_array, re.IGNORECASE):
            print((re.search(r"\d{4}", self._list_array, re.IGNORECASE)).group(0))

    def yearLinesTime(self):
        for i, item in enumerate(self._list_array):
            if re.search(r"^год$", item):
                self._year = f"20{self._list_array[i-1]}" if len(f"20{self._list_array[i-1]}") == 4 else dt.datetime.now().year
                if len(f"{self._list_array[i-1]}") == 4 and str(self._list_array[i-1])[:2] == "20":
                    self._year = f"{self._list_array[i-1]}" if len(f"{self._list_array[i-1]}") == 4 else dt.datetime.now().year
                self._list_array[i] = f"{self._year}YY"
                return
            elif re.search(r"^20[0-9]{2}$", item, re.IGNORECASE):
                self._list_array[i] = f"{self._year}YY"
                return

    def monthLinesTime(self):
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
        for i, item in enumerate(self._list_array):
            if item in dict_month:
                self._list_array[i] = f"{dict_month[item]}MM"
                self.month = dict_month[item]
                if i != 0 and self._list_array[i-1].isdigit():
                    self.day = self._list_array[i-1]
                    self._list_array[i-1] = f"{self._list_array[i-1]}DD"
                    return
            elif re.search(r"^вчера", item, re.IGNORECASE):
                yesterday = dt.datetime.now() - dt.timedelta(days=1)
                month_date = yesterday.strftime("%m")
                day_date = yesterday.strftime("%d")
                self._list_array[i] = f"{month_date}MM {day_date}DD"
                self.month = month_date
                self.day = day_date
                return
            elif re.search(r"позавчера", item, re.IGNORECASE):
                day_before_yesterday = dt.datetime.now() - dt.timedelta(days=2)
                month_date = day_before_yesterday.strftime("%m")
                day_date = day_before_yesterday.strftime("%d")
                self._list_array[i] = f"{month_date}MM {day_date}DD"
                self.month = month_date
                self.day = day_date
                return
        return
    
if __name__ == '__main__':
    date = TransFormDate()
    date.splitLines('2023 06 08')
    date.yearLinesTime()
    date.monthLinesTime()
    print(date)
    print()