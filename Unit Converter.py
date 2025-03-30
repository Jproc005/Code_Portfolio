def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(pounds):
    return pounds / 2.20462

def yen_to_usd(yen):
    return yen * 0.0067

def usd_to_yen(usd):
    return usd * 149.8449

def unit_converter():
    print("Welcome to the Unit Converter!")
    print("Choose a category:")
    print("1. Temperature")
    print("2. Length")
    print("3. Weight")
    print("4. Currency")

    choice = input("Enter 1, 2, 3, or 4: ")

    if choice == "1":
        temp = float(input("Enter the temperature: "))
        unit = input("Convert from (C/F): ").strip().upper()
        if unit == "C":
            print(f"{temp}°C is {celsius_to_fahrenheit(temp):.2f}°F")
        elif unit == "F":
            print(f"{temp}°F is {fahrenheit_to_celsius(temp):.2f}°C")
        else:
            print("Invalid unit!")

    elif choice == "2":
        length = float(input("Enter the length: "))
        unit = input("Convert from (M/FT): ").strip().upper()
        if unit == "M":
            print(f"{length} meters is {meters_to_feet(length):.2f} feet")
        elif unit == "FT":
            print(f"{length} feet is {feet_to_meters(length):.2f} meters")
        else:
            print("Invalid unit!")

    elif choice == "3":
        weight = float(input("Enter the weight: "))
        unit = input("Convert from (kg/lb): ").strip().upper()
        if unit == "KG":
            print(f"{weight} kg is {kg_to_pounds(weight):.2f} pounds")
        elif unit == "LB":
            print(f"{weight} pounds is {pounds_to_kg(weight):.2f} kg")
        else:
            print("Invalid unit!")

    elif choice == "4":
        Currency = float(input("Enter the amount: "))
        unit = input("Convert from (yen/usd): ").strip().lower()
        if unit == "yen":
            print(f"{Currency} yen is {yen_to_usd(Currency):.2f} usd")
        elif unit == "usd":
            print(f"{Currency} usd is {usd_to_yen(Currency):.2f} yen")
        else:
            print("Invalid unit!")

    else:
        print("Invalid choice!")

# Run the converter
unit_converter()
