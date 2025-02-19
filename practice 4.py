# practice 4
# print the pyramid pattern

print("hello there! please provide two numbers to our program.\n"
      "we would like to create something interesting.")

while True:
    print("")
    number1 = input("1/ please provide a number here: ")
    number2 = input("2/ please provide a number here: ")

    if number1.isdigit() and number2.isdigit():
        if int(number1) < int(number2):
            print("")
            for i in range(int(number1), int(number2) + 1):
                for j in range(int(number1), i + 1):
                    print(j, end=" ")
                print("")
            for n in range(int(number2) - 1, int(number1) - 1, -1):
                for m in range(int(number1), n + 1):
                    print(m, end=" ")
                print("")
            break
        elif number1 > number2:
            print("")
            print("the first number is bigger than the second number.\n"
                  "that is not acceptable. please try again.")
        else:
            print("")
            print("the first number is equal to the second number.\n"
                  "that is not acceptable. please try again.")
    else:
        print("")
        print("the inputs do not match the requirements.\n"
              "please try again")
