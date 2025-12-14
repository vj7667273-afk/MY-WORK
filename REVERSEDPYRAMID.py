#FUNCTION TO PRINT A HALF REVERSED PYRAMID PATTERN
def half_pyramid(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
              print("* ",end="")
        print("\r")

#EXAMPLE:PRINT A HALF REVERSED PYRAMID PATTERN
n=5
half_pyramid(n)