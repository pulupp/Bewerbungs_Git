amount_to_pay = 50

accepted_coin = [0, 1, 2, 5, 10, 25]


print("Amount due: 50")

while amount_to_pay > 0:
    to_pay = int(input("Insert coin: "))

    if to_pay in accepted_coin and to_pay <= amount_to_pay:
        amount_to_pay -= to_pay
        if amount_to_pay > 0:
          print(f"Amount Due: {amount_to_pay}")

    elif to_pay == 50:
         print(f"Amount Due: {amount_to_pay}")

    elif to_pay > amount_to_pay:
              change_owed = to_pay - amount_to_pay
              amount_to_pay = 0
              print(f"Change Owed: {change_owed}")

if amount_to_pay == 0:
     print("Change Owed: 0")

change_owed = 0