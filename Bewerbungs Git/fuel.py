def main():
    input_fraction = input("Fraction: ")
    c = fraction(input_fraction)
    print(f"{c:.0%}")

def fraction(input_fraction):
    while True:
        try:
            a = input_fraction.split("/")
            if len(a) != 2:
                raise ValueError("Invalid input format. Please enter a fraction in the format 'numerator/denominator'.")
            numerator, denominator = map(int, a)
            if denominator == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            result = numerator / denominator * 100/100
            if 0 < result <= 99:
                return result
            elif result > 99:
                print("F")
                return result
            elif result < 1:
                print("E")
                return result
        except (ValueError, ZeroDivisionError) as e:
            print(e)
            input_fraction = input("Fraction: ")

main()