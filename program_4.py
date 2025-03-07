import math
def main():
    coordinate_list = []
    coordinate_1 = []
    coordinate_2 = []

    try:
        x1 = float(input("Please enter an x coordinate:"))
        y1 = float(input("Please enter a y coordinate:"))
        z1 = float(input("Please enter a z coordinate:"))
    except ValueError:
        print("Error, input must be a number")
        main()
        return
    coordinate_1.append((x1, y1, z1))

    try:
        x2 = float(input("Please enter another x coordinate:"))
        y2 = float(input("Please enter another y coordinate:"))
        z2 = float(input("Please enter another z coordinate:"))
    except ValueError:
        print("Error, input must be a number and have a decimal point")
        main()
        return

    coordinate_2.append((x2,y2,z2))
    coordinate_list.append(coordinate_1)
    coordinate_list.append(coordinate_2)
    distance = calculate_distance(coordinate_1[0], coordinate_2[0])
    print("The distance between your two points is", distance)


def calculate_distance(position_1, position_2):
    x1, y1, z1 = position_1
    x2, y2, z2 = position_2

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z1 - z2) ** 2)
    return distance

if __name__ == '__main__':
    main()

# Program #4, Donovan Thompson 3/6/2025
