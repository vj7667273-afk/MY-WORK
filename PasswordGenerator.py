#importing the random module
import random

#a function that will generate a password of length (n) and return it
def Generatepassword(n):
    #defining the list of choices of characters
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"
    password = ""

    for i in range(n):
        #randomly selecting one character and appending it to the resultant password string
        password += random.choice(characters)

    #finally returning the randomly generated password
    return password

if __name__ == "__main__":
    n = 12
    password = Generatepassword(n)
    print("A randomly selected password is:", password)
