import re
import datetime as dt

# YYYY-MM-DD HH24:MI:SS


class Transform():
    def __init__(self):
        self.year = dt.datetime.now().year
        self.month = dt.datetime.now().month
        self.day = dt.datetime.now().day
        self.hour = "00"
        self.minute = "00"
        self.second = "00"

    # .join
    def stringLinse(self, string):
        string = ' '.join(string)
        return string
    
    # split
    def splitLines(self, lines):
        lines = re.sub(r"[:-]", " ", lines)
        lines = lines.split()
        return lines

    # YYYY format
    def yearLines(self, lines):
        list_array = self.splitLines(lines)
        for i, item in enumerate(list_array):
            if re.search(r"^год$", item):
                self.year = f"20{list_array[i-1]}" if len(
                    f"20{list_array[i-1]}") == 4 else dt.datetime.now().year
                if len(f"{list_array[i-1]}") == 4 and str(list_array[i-1])[:2] == "20":
                    self.year = f"{list_array[i-1]}" if len(
                        f"{list_array[i-1]}") == 4 else dt.datetime.now().year
                list_array[i] = f"{self.year}YY"
                return self.stringLinse(list_array)

    # MM and DD formats
    def monthLinesTime(self, list_raw):
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
        list_array = self.splitLines(list_raw)
        for i, item in enumerate(list_array):
            if item in dict_month:
                list_array[i] = f"{dict_month[item]}MM"
                self.month = dict_month[item]
                if i != 0:
                    self.day = list_array[i-1]
                    list_array[i-1] = f"{list_array[i-1]}DD"
        return self.stringLinse(list_array)

    # HH format
    def hourLines(self, list_raw):
        list_array = self.splitLines(list_raw)
        for i, item in enumerate(list_array):
            if re.search(r"^час$", item):
                list_array[i] = "1HH"
                self.hour = list_array[i]
                return self.stringLinse(list_array)
            elif re.search(r"час", item) and re.search(r"[0-9]", list_array[i - 1], re.IGNORECASE) and not re.search(r"дня|вечер|ноч", list_array[i + 1]):
                if int(list_array[i - 1]) < 24:
                    self.hour = list_array[i-1]
                    list_array[i-1] = f"{list_array[i-1]}HH"
                    return self.stringLinse(list_array)
            elif list_array[-1] != item and re.search(r"дня|вечер|ноч", list_array[i + 1]):
                try:
                    if int(list_array[i - 1]) in (9, 10, 11):
                        list_array[i - 1] = int(list_array[i - 1]) + 12
                    elif int(list_array[i - 1]) == 12:
                        list_array[i - 1] = int(list_array[i - 1]) - 12
                except ValueError:
                    if int(list_array[i]) in (9, 10, 11):
                        list_array[i] = int(list_array[i]) + 12
                    elif int(list_array[i]) == 12:
                        list_array[i] = int(list_array[i]) - 12
                self.hour = list_array[i]
                list_array[i-1] = f"{list_array[i]}HH"
                return self.stringLinse(list_array)
            # elif re.search(r"пол", item, re.IGNORECASE):
            #     if len(list_array) >= i + 1:
            #         if int(list_array[i + 1]) in (9, 10, 11):
            #             list_array[i + 1] = int(list_array[i + 1]) + 12
            #         elif int(list_array[i + 1]) == 12:
            #             list_array[i + 1] = int(list_array[i + 1]) - 12
            #         self.hour = list_array[i+1]
            #         list_array[i+1] = f"{list_array[i+1]}HH"

    
    def get_date_list(self, list, flags=None):
        self.yearLines(list)
        self.monthLinesTime(list)
        self.hourLines(list)
        date_string = f"{self.year}-{self.month}-{self.day} {self.hour}:{self.minute}:{self.second}"
        date_format = "%Y-%m-%d %H:%M:%S"
        parsed_date = dt.datetime.strptime(date_string, date_format)

        # Получение текущей даты
        now = dt.datetime.now()

        if flags is not None:
            if "p" in flags and parsed_date > now:
                parsed_date = now
            elif "r" in flags and parsed_date.date() > now.date():
                parsed_date = now
        elif parsed_date > now:
            print("Ошибка: указанная дата не может быть больше текущей даты без установленного флага.")
            return


if __name__ == '__main__':
    t = Transform()
    t.get_date_list("5 мая 2024 год 17 51")
