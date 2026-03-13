# 1) შექმენით ინტეჯერების სია, ამოაგდე ბოლო ელემენტი და მის მაგივრად ჩასვი შენი საყვარელი რიცხვი
int_l = [1,10,20,30,40,50]
delete = int_l.pop(-1)
add = int_l.append(7)
print(int_l)
# 2)მომხმარებელს შემოატანინე მისი გვარი და გაარკვიე შეიცავს თუ არა მისი გვარი სტრინგ "shvili", ამის შესაბამისად დაპრინტე True ან False
surname = input("Please enter your surname: ")
if surname.find("shvili"):
    print(True)
else:
    print(False)
    
# 3)მომხმარებელს შემოატანინე რაიმე ინდექსი 1-5 და 10 ელემენტიან სიიდან ამოიღე ამ ინდექსზე მდგომი ელემენტი და სიის დასაწყისში ჩაამატე სტრინგი "change"
list_p = [10,5,60,103,500,605,403,809,300,1000]

int_i = int(input("Please enter your int: "))
if int_i > 5:
    print("INVALID INDEX")
elif int_i <= 5:
    pop = list_p.pop(int_i)
    add = list_p.insert(0,"change")
    print(list_p)
# 4)შექმენი 5 ელემენტიანი სტრინგების სია და გამოიტანე ყველა ელემენტი დიდი ასოებით
list_s = ["hi","hello","bye","goodbye","buh-bye"]
for i in list_s:
    print(i.upper)
# 5)მომხმარებელს შემოატანინე მისი საყვარელი კინო და რაიმე ასო, დაპრინტე True თუ ეს ასო ამ კინოს სახელშია, თუ არადა დაპრინტე False
fav_f = input("Please enter your fav movie: ")
letter = input("Please enter any letter: ")
if fav_f.find(letter):
    print(True)
else:
    print(False)