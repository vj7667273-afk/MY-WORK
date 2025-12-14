#Function to print a half pyramid pattern
def half_pyramid(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("* ", end="")
        print("")

#example:print a half pyramid with 5 rows
n = 5
half_pyramid(n)
