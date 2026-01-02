# 1)უყურეთ ჩანაწერს ხელმეორედ (აუცილებლად!)

# 2)შექმენით 8 ცვლადი სადაც შეინახავთ ყველა შესაძლო ლოგიკური ოპერატორის მაგალითს (4 ცალი or / 4 ცალი and)
first = True
second = False
third = True
fourth = False
fifth = True
sixth = False
seventh = True
eightth = False

#or
print(first or fourth)
print(fourth or second)
print(first or third)
print(second or first)
#and
print(fifth and sixth)
print(fifth and seventh)
print(sixth and eightth)
print(eightth and fifth)
# 3)მომხმარებელს შემოატანინეთ მისი სახელი, შემოატანინეთ მისი ასაკი, ასევე სიმაღლე და შეამოწმეთ თუ მომხმარებლის ასაკი მეტია 18 და მისი სახელი უდრის თქვენს სახელს და ასევე მისი სიმაღლე მეტია 1.80-ზე

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
size = float(input("Please enter your size: "))
print(age >= 18  and name == "Alexandre" and size >= 1.80)


# 4)მომხმარებელს შემოატანინეთ ორი რიცხვი (num1 და num2) და გაიგეთ რა იქნება ნაშთი, პირველი რიცხვის მეორეზე გაყოფის შემდეგ

num1 = int(input("Please enter your number: "))
num2 = int(input("Please enter your number: "))
print(num1 / num2)

# 5)მომხმარებელს შემოატანინეთ მისი ასაკი და გაიგეთ არის თუ არა ის ლუწი (იყოფა თუ არა ზუსტად 2ზე) ანუ გვრჩება თუ არა ნაშთი ნული, ორზე გაყოფის შედეგად

age = int(input("Please enter your age"))

if age // 2 == 0:
    print("congrats your age can divide by 2")