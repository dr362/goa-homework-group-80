# 1) კომენტარებით ახსენით რას აკეთებს conditional statements

#conditional statements - ნიშნავს პირობით მოქმედებებს

# 2)შექმენით კოდი რომელის დაპრინტავს "adult" როცა ასაკი იქნება 18 წელზე მეტი, თუ 13 წელსა და 18 წელს შორისაა დაპრინტოს "teen", ხოლო ყველა სხვა შემთხვევაში დაპრინტოს "child"
age = 17
if age > 18:
    print("adult")
elif age > 13 and age < 18:
    print("teen")
else:
    print("child")

# 3)შექმენით ცვლადი name და age, თუ სახელი უდრის გიორგის და 18 წელზე მეტისაა დაპრინტოს adult giorgi, თუ 18 წელზე ნაკლებისაა დაპრინტოს "not adult giorgi", და თუ საერთოდ არ ქვია გიორგი დაპრინტოს 'not giorgi" (indented if-else)

name = "giorgi"
age = 21
if name == "giorgi" and age > 18:
    print("Adult giorgi")
    if age < 18:
        print("not adult giorgi")
else:
    print("Not Giorgi")

# 4)შექმენით ორი ინტეჯერის შემცველი ცვლადი, თუ პირველი ცვლადი უნაშთოდ იყოფა მეორეზე დაპრინტე True სხვა შემთხვევაში კი False

num1 = 10
num2 = 2
if num1 % num2 == 0:
    print(True)
else:
    print(False)

# 5)მომხმარებელს შემოატანინე მისი საყვარელი ფილმი და სახელი, თუ მისი სახელი ავთოა მაშინ დაპრინტე "you are avto" , თუ ლევანი ქვია და მისი საყვარელი ფილმია ტიტანიკი, დაპრინტე "Levani loves titanic" ყველა სხვა შემთხვევაში დაპრინტე "someone likes other film" (indented if-else)
name = input("Please enter your name: ")
film = input("Please enter your fav film: ")
if name == "avto":
    print("you are avto")
elif name == "levani" and film == "titanic":
    print("Levani loves titanic")
else:
    print("someone likes other film")