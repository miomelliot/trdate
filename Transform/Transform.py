import re 

# YYYY-MM-DD HH24:MI:SS
class Transform() :
    def __init__(self) :
        self.year = ""
        self.month = ""
        self.day = ""
        self.hour = ""
        self.minute = ""
        
    def splitLines(self, lines):
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
                    list_array[i-1] = f"{list_array[i-1]}DD"
                    self.day = list_array[i-1]
        return list_array
        
        
    def hourLines(self, list_raw):
        list_array = self.splitLines(list_raw)
        for i, item in enumerate(list_array):
            if re.search(r"^час$", item):
                list_array[i] = "1HH"
                self.hour = list_array[i]
            elif re.search(r"час", item) and re.search(r"[0-9]", list_array[i - 1], re.IGNORECASE) :
                
                print(1)
        return list_array
                
                
if __name__ == '__main__':
    transform = Transform()
    print(transform.monthLinesTime("5 мая в 7 часов утра"))