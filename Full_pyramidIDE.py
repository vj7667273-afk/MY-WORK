#Full pyramid pattern in a python
def print_space(space):
    if space > 0:
        print(" ",end="")
        print_space(space - 1)  

def print_star(star):
    if star > 0:
        print("*",end="")
        print_star(star - 1)

def print_pyramid(n, current_row=1):
    if current_row > n:
        return

    spaces = n - current_row
    stars = 2 * current_row - 1

    # print spaces
    print_space(spaces)
 
    # print stars
    print_star(stars)

    # move to the next line for the next row
    print()

    # print the pyramid for the next row
    print_pyramid(n, current_row +1)

# set the number of rows for the pyramid
n = 5

# print the pyramid pattern
print_pyramid(n)


