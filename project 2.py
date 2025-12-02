print("Welcome to the Pattern Generator and Number Analyzer!")

while True:
    print("Select an option : ")
    print("1.Generate a Pattern")
    print("2.Analyze a Range of Numbers")
    print("3.Exit")

    choice = int(input("Enter your choice :"))


    if choice == 1:
        n = int(input("Enter a number"))
        print("Pattern")
        for i in range(1,n+1):
            print("*"*i)
            
    elif choice == 2:
        start = int(input("Enter a Start number :"))
        End = int(input("Enter a End number :"))

        even = []
        odd = []
        total_sum = 0
        count = 0

        for n in range(start,End+1):
            if n%2==0:
                even.append(n)
            else:
                odd.append(n)

            total_sum += n
            count+=1
        print("\nEven number:",even)
        print("odd number:",odd)
        print("Total number :",count)
        print("sum:",total_sum)

    elif choice == 3:
        print("Exiting the program Goodbye!")
        break
             
    else:
        print("Invalid choice please try again correct choices")
