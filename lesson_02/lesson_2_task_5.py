month = int(input("Введите месяц "))
def month_to_season(month):
    if 1 <= month <= 2 or month == 12:
        print("Зима")
    elif 3 <= month <= 5:
        print("Весна")
    elif 6 <= month <=8:
        print("Лето")
    elif 9 <= month <= 11:
        print("Осень")
    else: print("Некорректный месяц")
month_to_season(month)