# 1) კომენტარის სახით ახსენი რა არის input და output

#input - რაღაცის ტექსტით შეტანა
#output - input-ის შედეგი

# 2)პრინტის საშუალებით გამოიტანე input  და output 2-2 მაგალითი

an_input = input("Enter your name")
print(an_input)

another_input = input("Enter your age")
print(int(another_input))

# 3)მომხმარებელს შემოატანინე მისი საყვარელი საჭმელი და გამოიტანე ის

fav_Food = input("Your favourite food is... ")
print(fav_Food)

# 4)მომხმარებელს შემოატანინე მისი სახელი და დაპრინტე "hello (მისი სახელი)"

name = input("Please enter your name: ")
print("Hello " + name)

# 5)შექმენი ცვლადი num სადაც შეინახავ რიცხვს სტრინგის სახით, შემდეგ მომხმარებელს შემოატანინე რაიმე რიცხვი და გამოიტანე მათი ჯამი

integer = 10
string = "5"

print(int(string) + integer)

# 6)კომენტარის სახით ახსენი რატომ გამოაქვს ამ კოდს ერორი:
# var = input("enter your age")
# print(var + 3)

#აქ ერორი იმის გამო არის რომ სტრინგს ვერ ვუმატებთ ინტეჯერს ამისთვის საჭიროა რომ ვარ ცვლადი ვაქციოთ ინტეჯერად

#7)მომხმარებელს შემოატანინეთ ორი რიცხვი და გამოიტანეთ პირველ რიცხვში რამდენჯერ მოთავსდება მეორე რიცხვი

num1 = 10
num2 = 5
print(num1 // num2)