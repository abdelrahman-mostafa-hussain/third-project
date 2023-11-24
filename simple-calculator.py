def operation()->None:
    print("This is the operation of this calculator:")
    print("1- addition arithmetic")
    print("2- subtraction arothmetic")
    print("3- multiplication arithmetic")
    print("4- division arithmetic")
    print("5- quit the calculator")

def addition(num1,num2)->float:
    return num1+num2

def subtraction(num1,num2)->float:
    return num1-num2

def multiplication(num1,num2)->float:
    return num1*num2

def division(num1,num2)->float:
    return num1/num2

def main():
    while True:
        num1=float(input("Enter the first number: "))
        num2=float(input("Enter the second number: "))
        operation()
        arith_Opera=int(input("Enter the number of operation arithmetic you want: "))
        if arith_Opera == 5:
            print("Thank to use my simple calculator")
            break
        while True:
            if arith_Opera == 1:
                sum=addition(num1,num2)
                print("the sum of two number you input is",sum)
                break
            elif arith_Opera == 2:
                sub=subtraction(num1,num2)
                print("the subtract of two number you input is",sub)
                break
            elif arith_Opera == 3:
                multi=multiplication(num1,num2)
                print("the subtract of two number you input is",multi)
                break
            elif arith_Opera == 4:
                if num2 == 0:
                    print("the subtract of two number you input is unknown number")
                    break
                else:
                    div=division(num1,num2)
                    print("the subtract of two number you input is",div)
                    break
            else:
                arith_Opera=int(input("invalid number please enter valid one: "))
                continue
        print("let's try another round")

if __name__=="__main__":
    main()