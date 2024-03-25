monate = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    datum = input("Date: ")

    try:
        if "/" in datum:
            month, day, year = datum.split("/")
            if (int(month) >=1 and int(month) <=12 and int(day) >=1 and int(day) <=31):
                break

    except ValueError:
        try:
            old_month, old_day, old_year = datum.split(" ")
            for i in range(len(monate)):
                if old_month == monate[i]:
                    month = i+1

            day = old_day.replace(",", "")
            if (int(month) >=1 and int(month) <=12 and int(day) >=1 and int(day) <=31):
                break

            if not old_day.endswith(","):
                continue
        except:
            print()
            pass

print(f"{int(year)}-{int(month):02}-{int(day):02}", end="")