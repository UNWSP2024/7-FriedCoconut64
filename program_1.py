def main():
    month_names = ('January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November','December')
    print("Please enter total rainfall for each month")
    rain = (float(input("January:")), float(input("Febuary:")), float(input("March:")), float(input("April:")), float(input("May:")), float(input("June:")),
            float(input("July:")), float(input("August:")), float(input("September:")), float(input("October:")), float(input("November:")), float(input("December:")))
    max_rain = max(rain)
    min_rain = min(rain)
    print("Total Anual Rainfall is:",sum(rain), "inches")
    print("Average Rain per month is:", sum(rain)/12, "inches")
    most_rained = month_names[rain.index(max_rain)]
    least_rained = month_names[rain.index(min_rain)]
    print("The month with the most rain is:",most_rained)
    print("The month with the least rain is:", least_rained)


main()

# Program #1, Donovan Thompson 3/5/2025
