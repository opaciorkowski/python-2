num1 = input("podaj pierwsza liczbe\n")
num2 = input("podaj druga liczbe\n")
operator = input("podaj typ operacji (+, -, /, *, **)\n")
match operator:
    case "+":
        print(float(num1)+float(num2))
    case "-":
        print(float(num1)-float(num2))
    case "/":
        if num2 == '0':
            print("nie mozna dzielic przez 0!")
            exit()
        print(float(num1)/float(num2))
    case "*":
        print(float(num1)*float(num2))
    case "**":
        print(float(num1)**float(num2))
    case _:
        print("niepoprawna operacja")
