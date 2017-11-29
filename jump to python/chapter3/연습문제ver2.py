print("*입장료 프로그램*")

while True:
    age = int(input("나이를 입력하세요:"))
    if age >= 0 and age <= 3:
        print("귀하의 등급은 [유아]이며, 요금은 무료입니다.")
        print("감사합니다. 티켓을 발행합니다.")
    elif age >= 4 and age <= 13:
        print("귀하의 등급은 [어린이]이며, 요금은 2000원 입니다.")
        pay = int(input("요금을 입력하세요:"))
        if pay == 2000:
                print("감사합니다. 티켓을 발행합니다.")
        elif pay > 2000:
                print("감사합니다. 티켓을 발행하고 거스름돈 %d를 반환합니다." % (pay -2000))
    elif age >= 14 and age <= 18:
         print("귀하의 등급은 [청소년]이며 , 요금은 3000원 입니다.")
         pay = int(input("요금을 입력하세요:"))
         if pay == 3000:
             print("감사합니다. 티켓을 발행합니다.")
         elif pay > 3000:
             print("감사합니다. 티켓을 발행하고 거스름돈 %원을 반환합니다." % (pay - 3000))
    elif age >= 19 and age <= 65:
        print("귀하의 등급은 [성인]이며, 요금은 5000원 입니다.")
        pay = int(input("요금을 입력하세요:"))
        if pay == 5000:
                print("감사합니다. 티켓을 발행합니다.")
        elif pay > 5000:
                print("감사합니다. 티켓을 발행하고 거스름돈 %d를 반환합니다." % (pay -5000))
    else:
          print("귀하의 등급은 [노인]이며, 요금은 무료입니다.")
          print("감사합니다. 티켓을 발행합니다.")