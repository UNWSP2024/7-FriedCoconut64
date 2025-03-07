def main():
    all_entered_values = []
    while True:
        year_data = int(input("Please input a year:"))
        state_data = input("Please input a state:")
        pop_data = int(input("Please input total population for your state for that year:"))
        my_list = ([year_data, state_data, pop_data])
        all_entered_values.append(my_list)
        x = input("Would you like to enter more data? (Type Y):")
        if x != "Y":
            break

    year_to_sum = int(input("What year would you like to see the total population from?:"))
    total_pop = sum_population_for_year(all_entered_values, year_to_sum)
    print("Total population for", year_to_sum, "is", total_pop)



def sum_population_for_year(all_entered_values, year_to_sum):
    total = 0
    for row in all_entered_values:
        if row[0] == year_to_sum:
            total += row[2]
    return total

if __name__ == '__main__':
    main()

# Program #3, Donovan Thompson 3/5/2025
