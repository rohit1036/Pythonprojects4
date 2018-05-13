def calulator(num1,num2):
    '''
    1.The first line contains the sum of the two numbers.
    2. The second line contains the difference of the two numbers (first - second).
    3. The third line contains the product of the two numbers.
    4.The fourth line contain integer division of two numbers .
    5. The fifth line contain float division of two numbers .
    '''

    print("Sum of two numbers: ", num1 + num2)
    print("Difference of two numbers: ", num1 - num2)
    print("Product of two numbers: ",num1*num2)
    print("Floor Division: ",num1//num2)
    print("Float Division: ",num1/num2)

if __name__=='__main__':
    try:
        print("User input !, Enter two integer values seprated by space:")
        num1,num2=(input("Enter numbers:").split())
        num1=int(num1)
        num2=int(num2)
    except (ValueError,Exception) as msg:
        print("Error massage: {}".format(msg))
    else:
        calulator(num1,num2)
    finally:
        print("done!")
    print(calulator.__doc__)
