# 1) კომენტარის სახით ახსენით რა არის control flow და algorithm

#control flow - მასალა სადაც შედის ბევრი მნიშვნელოვანი რამ
#algorithm - თანმიმდევრული მასალა

# 2) ახსენი რას აკეთებენ % და // ოპერატორები და მოიყვანე 2-2 მაგალითი

#% - არ მახსოვს
print(5 % 10)
print(20 % 5)
#// - ისეთი გაყოფა რომელიც გეუბნება რა რიცხვი რამდენჯერ თავსდება
print(10 // 5)
print( 20 // 5)


# 3)შექმენით ორი ცვლადი, ერთში შეინახი რიცხვი 1-20, მეორეში რაიმე სახელი. შექმენით კოდი რომელიც დააბრუნებს True, როცა პირველი ცვლადი იქნება 15-ზე მეტი, ხოლო მეორე ცვლადში იქნება თქვენი სახელი

age = int(input("Please enter your age: "))
name = input("Please enter your name: ")
print(age >= 15 and name == "alexandre")

# 4) მომხმარებელს შემოატანინეთ მისი ასაკი და სახელი, შემოუშვით საიტზე თუ ის იქნება 18 წელზე მეტის ან მისი სახელი იქნება "Andrew"

Age = int(input("please enter your age: "))
Name = input("Please eneter your name: ")
print(age >= 18 or name == "Andrew")

# 5)რას გამოიტანს შემდეგი კოდები:
# num = 17
# print(num>18 or 2>1)
#True

# age = 18
# print(Age >= 18 and 10==10)
#True

# random = "saba"
# print("saba"==random or 17%2==0)
#False