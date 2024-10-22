def is_yesr_leap(year):
    if (year % 4 == 0):
        print("год: " + str(year) + " True")
    else:
        print("год: " + str(year) + " False")
is_yesr_leap(int(input("Введите год: ")))
