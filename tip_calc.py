#Author: Richard Ward

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = d.strip("$")
    y = round(float(d), 1)
    print(y)
    return y

def percent_to_float(p):
    p = float(p.strip("%"))
    z = float(100)
    w = float(p / z)
    print (w)
    return w

main()