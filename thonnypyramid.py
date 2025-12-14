#fUNCTION TO PRINT A HALF PYRAMID PATTERN
def half_pyramid(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("* ",end="")
        print("")
            
#EXAMPLE:PRINT A HALF PYRAMID WITH 5 ROWS
n = 5
half_pyramid(n)