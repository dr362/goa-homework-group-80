# 0) კომენტარის სახით ახსენი set-ის და tuple-ის მსგავსებები
#tuple,set ორივე უცვლელია
# 1)შექმენი 5 ელემენტიანი tuple და გაუკეთე სამ ცვლადში unpack ისე რომ მეორე ცვლადში 3 ელემენტიანი სია მიიღო
el = (1,0.1,"hi",True,False)
(i,*fsb,b) = el
print(el)
# 2)შექმენი სახელების სეტი და მომხმარებელს შემოატანინე თავისი სახელი, თუ ეს სახელი უკვე არის დაუპრინტე "ეს სახელი არის სეტში და აღარ დაემატება" სხვა შემთხვევაში კი ჩაამატეთ და დაუპრინტეთ
names = {"sandro","gio","deme","akaki"}
add = input("Please enter your name: ")
if add in names:
    print("ეს სახელი არის სეტში და აღარ დაემატება")
else:
    list(names)
    names.add(add)
    set(names)
print(names)

# 3)შექმენი tuple და ჩაამატე მასში ელემენტი
tup = (1,0.1,"hi",True,False)
listed = list(tup)
listed.append("bye")
print(listed)
