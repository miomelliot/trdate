import re
import datetime as dt


class TransFormDate():
    """
    Класс TransFormDate предназначен для работы с датами.

    Methods
    -------
    `stringLines`(self, string: List[str]) -> str:
        Объединяет строки в переданном списке `string` в одну строку, разделяя пробелами.

    `splitLines`(self, lines: str) -> List[str]:
        Метод выполняет разделение строк и возвращает список слов.

    `yearLines`(self) -> None:
        Метод выполняет обработку списка и замену элементов с указанием года.

    `monthLines`(self) -> None:
        Метод обрабатывает список `self.list_array`, заменяя месяца на числовой формат и добавляя метки 'MM' и 'DD' для месяца и дня соответственно.

    `hourLines`(self) -> None:
        Метод для обработки списка строк и определения времени в формате часов и минут.

    `minuteLines`(self) -> None:
        Ищет строки, начинающиеся с 'минут' в списке `list_array` и выполняет определенные действия.

    `get_d`(self) -> datetime:
        Возвращает объект `datetime`, полученный из атрибутов `year`, `month`, `day`, `hour`, `minute` и `second`.

    `get_date_list`(self, line: str) -> List[datetime]:
        Метод для получения списка дат из строки `line` и обработки их.
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
        """
        Объединяет строки в переданном списке `string` в одну строку, разделяя пробелами.

        Parameters
        ----------
        `string` : `list[str]`
            Список строк, которые нужно объединить.

        Returns
        -------
        `str`
            Объединенная строка.

        Example
        -------
        >>> obj = MyClass()
        >>> lines = ['Hello', 'world!']
        >>> obj.stringLines(lines)
        'Hello world!'
        """
        string = ' '.join(string)
        return string

    def splitLines(self, lines):
        """
        Метод выполняет разделение строк и возвращает список слов.

        Parameters
        ----------
        lines : str
            Строка, которую необходимо разделить.

        Returns
        -------
        list
            Список слов, полученных после разделения строки.

        Example
        -------
        >>> transform_date = TransFormDate()
        >>> example_line = "Пример строки: для разделения"
        >>> result = transform_date.splitLines(example_line)
        >>> print(result)
        ['Пример', 'строки', 'для', 'разделения']
        """
        lines = re.sub(r"[:-]", " ", lines)
        lines = lines.split()
        return lines

    def yearLines(self):
        """
        Метод выполняет обработку списка и замену элементов с указанием года.

        Returns
        -------
        `list`
            Список с обработанными элементами, включающими год.

        Example
        -------
        >>> transform_date = TransFormDate()
        >>> transform_date.list_array = ['элемент', 'год', '20', 'YY']
        >>> result = transform_date.yearLines()
        >>> print(result)
        ['элемент', '2020YY', '20YY']
        """
        for i, item in enumerate(self.list_array):
            if re.search(r"^год$", item):
                self.year = f"20{self.list_array[i-1]}" if len(
                    f"20{self.list_array[i-1]}") == 4 else dt.datetime.now().year
                self.list_array[i-1] = f"{self.list_array[i-1]}YY"
                if len(f"{self.list_array[i-1]}") == 4 and str(self.list_array[i-1])[:2] == "20":
                    self.year = f"{self.list_array[i-1]}" if len(
                        f"{self.list_array[i-1]}") == 4 else dt.datetime.now().year
                self.list_array[i] = f"{self.year}YY"
                return self.list_array
            elif re.search(r"^20[0-9]{2}$", item, re.IGNORECASE):
                self.list_array[i] = f"{self.year}YY"
                return self.list_array

    def monthLines(self):
        """
        Метод обрабатывает список `self.list_array`, заменяя месяца на числовой формат и добавляя метки '`MM`' и '`DD`' для месяца и дня соответственно.

        Returns
        -------
        `list`
            Список строк, где месяцы заменены на числовой формат и добавлены метки '`MM`' и '`DD`'.

        Example
        -------
        >>> transform_date = TransFormDate()
        >>> transform_date.list_array = ["января", "какой-то текст", "февраля", "еще текст", "декабря"]
        >>> result = transform_date.monthLines()
        >>> print(result)
        ['1MM', 'какой-то текст', '2MM', 'еще текст', '12MM']
        """
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
        """
        Метод для обработки списка строк и определения времени в формате часов и минут.

        Returns
        -------
        `list`
            Список строк после обработки, где определены временные значения.

        Example
        -------
        >>> transform_date = TransFormDate()
        >>> example_list = ["15", "часов"]
        >>> result = transform_date.hourLines(example_list)
        >>> print(result)
        ['15HH', 'часов']
        """
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
                        self.list_array[i -
                                        1] = int(self.list_array[i - 1]) + 12
                    elif int(self.list_array[i - 1]) == 12:
                        self.list_array[i -
                                        1] = int(self.list_array[i - 1]) - 12
                    elif re.search(r"дня|вечер", self.list_array[i + 1]) and int(self.list_array[i - 1]) < 12:
                        self.list_array[i -
                                        1] = int(self.list_array[i - 1]) + 12
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
            elif re.search(r"^(0?[1-9]|1[0-9]|2[0-3])$", item, re.IGNORECASE) and len(self.list_array) == i+2 and re.search(r"^минут", self.list_array[i+1], re.IGNORECASE) == None:
                self.hour = self.list_array[i]
                self.list_array[i] = f"{self.list_array[i]}HH"
                if re.search(r"^(0?[1-9]|[1-5][0-9]|59)$", self.list_array[i+1], re.IGNORECASE):
                    self.minute = self.list_array[i+1]
                    self.list_array[i+1] = f"{self.list_array[i+1]}MI"
                return self.list_array
            elif re.search(r"пол", item, re.IGNORECASE):
                if len(self.list_array) >= i + 1:
                    if int(self.list_array[i + 1]) in (9, 10, 11):
                        self.list_array[i +
                                        1] = int(self.list_array[i + 1]) + 12
                    elif int(self.list_array[i + 1]) == 12:
                        self.list_array[i +
                                        1] = int(self.list_array[i + 1]) - 12
                    self.hour = self.list_array[i+1]
                    self.list_array[i+1] = f"{self.list_array[i+1]}HH"
                    return self.list_array
            elif re.search(r"^(0?[1-9]|1[0-9]|2[0-3])$", item, re.IGNORECASE):
                if len(self.list_array) > i + 2 and re.search(r"^\d{2}$", self.list_array[i + 1], re.IGNORECASE):
                    self.hour = self.list_array[i]
                    self.list_array[i] = f"{self.list_array[i]}HH"
                    self.minute = self.list_array[i+1]
                    self.list_array[i+1] = f"{self.list_array[i+1]}MI"
                    return self.list_array
                elif re.search(r"^минут", self.list_array[i+1], re.IGNORECASE) == None:
                    self.hour = self.list_array[i]
                    self.list_array[i] = f"{self.list_array[i]}HH"
                    return self.list_array

    def minuteLines(self):
        """
        Ищет строки, начинающиеся с 'минут' в списке `list_array` и выполняет определенные действия.

        Returns
        -------
        `List[str]` or `None`
            Список `list_array` с изменениями, либо `None`, если условия не выполнены.

        Example
        -------
        >>> transform_date = TransFormDate()
        >>> transform_date.list_array = ["10", "минут"]
        >>> result = transform_date.minuteLines()
        >>> print(result)
        ['10MI', 'минут']
        """
        for i, item in enumerate(self.list_array):
            if re.search(r"^минут", item, re.IGNORECASE):
                if re.search(r"^(0?[1-9]|[1-5][0-9]|59)$", self.list_array[i-1], re.IGNORECASE):
                    self.minute = self.list_array[i-1]
                    self.list_array[i-1] = f"{self.list_array[i-1]}MI"
                    return self.list_array

    def get_d(self):
        """
        Возвращает объект `datetime`, полученный из атрибутов `year`, `month`, `day`, `hour`, `minute` и `second`.

        Returns
        -------
        `dt.datetime`
            Объект `datetime`, представляющий дату и время, соответствующие атрибутам класса.
        """
        date_string = f"{self.year}-{self.month}-{self.day} {self.hour}:{self.minute}:{self.second}"
        date_format = "%Y-%m-%d %H:%M:%S"
        parsed_date = dt.datetime.strptime(date_string, date_format)
        return parsed_date

    def get_date_list(self, line):
        """
        Метод для получения списка дат из строки `line` и обработки их.

        Parameters
        ----------
        line : str
            Строка, содержащая даты в определенном формате.

        Returns
        -------
        None

        Example
        -------
        >>> transform_date = TransFormDate()
        >>> line = "2023-07-21, 2023-07-22, 2023-07-23"
        >>> transform_date.get_date_list(line)
        2023-07-21
        2023-07-22
        2023-07-23
        """
        self.list_array = self.splitLines(line)
        self.yearLines()
        self.monthLines()
        self.hourLines()
        self.minuteLines()

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
    ds.get_date_list("6 часов утра 34 минуты")
    print(ds)
