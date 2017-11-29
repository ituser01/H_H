visit = 0
free = 3
event = 5
print("입장료 프로그램")
while True:
    age=int(input("나이를 입력하세요 :"))
    if age >= 0 and age <= 3:
        print("귀하의 등급은 [유아]이며, 요금은 무료입니다.")
    elif age >= 4 and age <= 13:
        print("귀하의 등급은 [어린이]이며, 요금은 2000원 입니다.")
    elif age >= 14 and age <= 18:
        print("귀하의 등급은 [청소년]이며 , 요금은 3000원 입니다.")
    elif age >= 19 and age <= 59:
        print("귀하의 등급은 [성인]이며, 요금은 5000원 입니다.")
    else age >= 60 and age <= 65:
        print("귀하의 등급은 [성인]이며, 요금은 5000원 입니다.")