print('........vot eligibilty test........')
age=int(input("please enter the  age="));
if age >=18 and  age <= 99:
    print("you are eligible")
    print('......thank you.....')
elif age>= 100 :
    print("you are not eligible")
else:print("you are  not eligible")
age1= int(input("please enter the correct age="))
if age1 == age:
    print("you are eligible")
elif age1 >=18 and  age1 <= 99:
    print("you are eligible")
elif age1>=100:
    print("you are not eligible")
else :
    print("you are not eligible")
print('..........thank you...........')