def main():
    try:
        number_first=int(input("\nEnter first number: "))
    except:
         print("invailed input")
         main()
         
    print("\n select operator")
    print("+ : addition")
    print("- : subtraction")
    print("* : multplication")
    print("/ : divison")

    operator=input("\nEnter operator: ")
    if operator =='+':
        print("\n")
    elif operator == '-':
        print("\n")
    elif operator =='*':
        print("\n")
    elif operator =='/':
        print("\n")
    else:
        print("invailed operator selected")
        main()
    try:
        number_second=int(input("Enter second number: "))
    except:
         print("invailed input")
         main()
         
    if operator =='+':
            print("the answer is: ",number_first + number_second)
            main()
    elif operator == '-':
         print("the answer is: ",number_first - number_second)
         main()
    elif operator =='*':
         print("the answer is:",number_first * number_second)
         main
    elif operator =='/':
         if number_second != 0:
              print("the answer is:",number_first / number_second)
              main()
         else:
             print("infinite Error: Division by zero!")
             main()
    return
main()