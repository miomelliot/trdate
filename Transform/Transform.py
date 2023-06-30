import re 
import datetime

# YYYY-MM-DD HH24:MI:SS
class Transform():
    def __init__(self):
        self.year = datetime.datetime.now().year
        self.month = datetime.datetime.now().month
        self.day = datetime.datetime.now().day
        self.hour = "00"
        self.minute = "00"
        self.second = "00"
        
    def splitLines(self, lines):
        lines = re.sub(r":", " ", lines)
        lines = lines.split()
        return lines
    
    # MM and DD formats
    def monthLinesTime(self, list_raw):
        dict_month = {
            "января" : "1",
            "февраля" : "2",
            "марта" : "3",
            "апреля" : "4",
            "мая" : "5",
            "июня" : "6",
            "июля" : "7",
            "августа" : "8",
            "сентября" : "9",
            "октября" : "10",
            "ноября" : "11",
            "декабря" : "12"
        }
        list_array = self.splitLines(list_raw)
        for i, item in enumerate(list_array):
            if item in dict_month:
                list_array[i] = f"{dict_month[item]}MM"
                self.month = dict_month[item]
                if i != 0:    
                    self.day = list_array[i-1]
                    list_array[i-1] = f"{list_array[i-1]}DD"
        return list_array
        
        
    def hourLines(self, list_raw):
        list_array = self.splitLines(list_raw)
        for i, item in enumerate(list_array):
            if re.search(r"^час$", item):
                list_array[i] = "1HH"
                self.hour = list_array[i]
                return list_array
            elif re.search(r"час", item) and re.search(r"[0-9]", list_array[i - 1], re.IGNORECASE) and not re.search(r"дня|вечер|ноч", list_array[i + 1]):
                if int(list_array[i - 1]) < 24:
                    self.hour = list_array[i-1]
                    list_array[i-1] = f"{list_array[i-1]}HH"
                    return list_array
            elif list_array[-1] != item and re.search(r"дня|вечер|ноч", list_array[i + 1]):
                if int(list_array[i - 1]) in (9, 10, 11):
                    list_array[i - 1] = int(list_array[i - 1]) + 12
                elif int(list_array[i - 1]) == 12:
                    list_array[i - 1] = int(list_array[i - 1]) - 12
                self.hour = list_array[i-1]
                list_array[i-1] = f"{list_array[i-1]}HH"
                return list_array
        
    
    def get_date_list(self, list):
        self.monthLinesTime(list)
        self.hourLines(list)
        date_string = f"{self.year}-{self.month}-{self.day} {self.hour}:{self.minute}:{self.second}"
        date_format = "%Y-%m-%d %H:%M:%S"
        print(datetime.datetime.strptime(date_string, date_format))



if __name__ == '__main__':
    t = Transform()
    t.get_date_list("Вчера в 13:44")