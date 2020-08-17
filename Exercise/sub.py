import math

class SubMain(object):

    def num(self):
        for i in range(10000):
            n = math.sqrt(i + 100)
            m = math.sqrt(i + 268)
            if n % 1 == 0 and m % 1 == 0:
                print(i)

    def date():
        cal = input('data: ')
        date = cal.split('-')

        year = int(date[0])
        month = int(date[1])
        day = int(date[2])

        month_arr = [0,31,28,31,30,31,30,31,31,30,31,30,31]

        num = 0

        for i in range(1, len(month_arr)):
            if month > i:
                num += month_arr[i]
            else:
                num += day
                break
        print(num)