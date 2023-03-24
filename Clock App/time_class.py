class MyTime:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.fix()

    def add_second(self):
        self.second += 1
        self.fix()

        
    def sub_second(self):
        self.second -= 1
        self.fix()

    def show(self):
        print(self.hour, ':', self.minute, ':', self.second)

    def sum(self, other):
        s_new = self.second + other.second
        m_new = self.minute + other.minute
        h_new = self.hour + other.hour
        result = MyTime(h_new, m_new, s_new)
        return result

    def equal(self, other):
        s_new = self.second - other.second
        m_new = self.minute - other.minute
        h_new = self.hour - other.hour
        if s_new == 0 and m_new == 0 and h_new == 0:
            return True
        else:
            return False

    def toString(self):
        return f'{self.hour}:{self.minute}:{self.second}'

    def sub(self, other):
        s_new = self.second - other.second
        m_new = self.minute - other.minute
        h_new = self.hour - other.hour
        result = MyTime(h_new, m_new, s_new)
        return result

    @staticmethod
    def convert_second_to_time(second):
        x = MyTime(0, 0, second)
        return x


    def convert_time_to_second(self):
        second = (self.hour * 60 + self.minute) * 60 + self.second
        return second
        
    def convert_GMT_to_Tehran(self):
        Tehran = Time(3, 30, 0)
        x = Time.sum(self, Tehran)
        return x
 
    def fix(self):
        while self.second >= 60:
            self.second -= 60
            self.minute += 1

        while self.minute >= 60:
            self.minute -= 60
            self.hour += 1

        while self.hour >= 24:
            self.hour -= 24

        while self.second < 0:
            self.second += 60
            self.minute -= 1

        while self.minute < 0:
            self.minute += 60
            self.hour -= 1
            
        while self.hour < 0:
            self.hour += 24

# t1 = Time(3, 15, 20)
# t1.show()

# t2 = Time(3, 15, 22)
# t2.show()

# t3 = t1.sub(t2)
# t3.show()

# t4 = Time(1, 1, 1)
# # t4 = t4.convert_second_to_time(60*60*2 + 60*23 + 56)
# # print(t4.convert_time_to_second())
# t5 = t4.convert_GMT_to_Tehran()
# t5.show()

# t6 = Time.convert_second_to_time(60*60*2 + 60*23 + 56)
# t6.show()
