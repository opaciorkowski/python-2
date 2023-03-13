a = "Python 2023"
b = "Python 2023"
c = "Python 2023"
print(a==b)
print(b==c)
print("a "+hex(id(a)), type(a))
print("b "+hex(id(b)), type(b))
print("c "+hex(id(c)), type(c))

print("punkt 3")
c = "Java 11"
print(a==b)
print(b==c)
print("a "+hex(id(a)), type(a))
print("b "+hex(id(b)), type(b))
print("c "+hex(id(c)), type(c))
#########################################
num1 = input("podaj pierwsza liczbe\n")
num2 = input("podaj druga liczbe\n")
operator = input("podaj typ operacji (+, -, /, *, **)\n")
match operator:
    case "+":
        print(float(num1)+float(num2))
    case "-":
        print(float(num1)-float(num2))
    case "/":
        print(float(num1)/float(num2))
    case "*":
        print(float(num1)*float(num2))
    case "**":
        print(float(num1)**float(num2))
    case _:
        print("niepoprawna operacja")

#########################################
##uzyj dictionary
question0 = input("Jak masz na imię oraz nazwisko?")
question1 = input("Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie:")
question2 = input("W jakich okolicznościach czytasz książki najczęściej?")
question3 = input("Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?")
question4 = input("Po książki w jakiej formie sięgasz najczęściej?")
question5 = input("Ile książek czytasz średnio w ciągu roku?")
question6 = input("Jak często średnio czytasz książki?")
question7 = input("Po jakie gatunki książek sięgasz najczęściej?")

print("pytanie: Jak masz na imię oraz nazwisko?")
print("odpowiedz ", question0)
print("pytanie: Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie:")
print("odpowiedz ", question1)
print("pytanie: W jakich okolicznościach czytasz książki najczęściej?")
print("odpowiedz ", question2)
print("pytanie: Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?")
print("odpowiedz ", question3)
print("pytanie: Po książki w jakiej formie sięgasz najczęściej?")
print("odpowiedz ", question4)
print("pytanie: Ile książek czytasz średnio w ciągu roku?")
print("odpowiedz ", question5)
print("pytanie: Jak często średnio czytasz książki?")
print("odpowiedz ", question6)
print("pytanie: Po jakie gatunki książek sięgasz najczęściej?")
print("odpowiedz ", question7)
