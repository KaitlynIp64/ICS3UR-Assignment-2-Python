#!/usr/bin/env python3

# Created by: Kaitlyn Ip
# Created on: Oct 2022
# This program calculates the area and perimeter of an equilateral triangle
#    with side inputted from the user

import math


def main():
    # this function calculates the area and perimeter of an equilateral triangle

    # input
    side_of_triangle = int(input("Enter the side of the equilateral triangle (mm): "))
    # process
    area_of_triangle = math.sqrt(3) / 4 * (math.pow(side_of_triangle, 2))
    perimeter_of_triangle = 3 * (side_of_triangle)

    # output
    print("")
    print("Area is {0} mm².".format(area_of_triangle))
    print("Perimeter is {0} mm.".format(perimeter_of_triangle))

    print("\nDone.")


if __name__ == "__main__":
    main()
