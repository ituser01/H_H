print("*입장료 프로그램*")

while True:
    age = int(input("나이를 입력하세요:"))
    if age >= 0 and age <= 3:
        print("귀하의 등급은 [유아]이며, 요금은 무료입니다.")
        print("감사합니다. 티켓을 발행합니다.")
    elif age >= 4 and age <= 13:
        print("귀하의 등급은 [어린이]이며, 요금은 2000원 입니다.")
        money = int(input("요금 유형을 선택하세요. (1:현금, 2:공원 전용 신용카드]"))
        if money ==1:
            print("1.현금")
            pay = int(input("요금을 입력하세요:"))
            if pay == 2000:
                print("감사합니다. 티켓을 발행합니다.")
            elif pay > 2000:
                print("감사합니다. 티켓을 발행하고 거스름돈 %d원을 반환합니다." % (pay -2000))
            elif pay < 2000:
                print("%d원 모자랍니다. 입력하신 요금을 반환합니다." % (pay -2000))
        elif money ==2:
             print("2.공원 전용 신용카드")
             print("10%할인되어 1800원 결제되었습니다. 감사합니다.티켓을 발행합니다.")
    elif age >= 14 and age <= 18:
        print("귀하의 등급은 [청소년]이며 , 요금은 3000원 입니다.")
        money = int(input("요금 유형을 선택하세요. (1:현금, 2:공원 전용 신용카드]"))
        if money == 1:
            print("1.현금")
            pay = int(input("요금을 입력하세요:"))
            if pay == 3000:
                print("감사합니다. 티켓을 발행합니다.")
            elif pay > 3000:
                print("감사합니다. 티켓을 발행하고 거스름돈 %d원을 반환합니다." % (pay - 3000))
            elif pay < 3000:
                print("%d원 모자랍니다. 입력하신 요금을 반환합니다." % (pay - 3000))
        elif money == 2:
            print("2.공원 전용 신용카드")
            print("10%할인되어 2700원 결제되었습니다. 감사합니다.티켓을 발행합니다.")
    elif age >= 19 and age <= 59:
         print("귀하의 등급은 [성인]이며, 요금은 5000원 입니다.")
         money = int(input("요금 유형을 선택하세요. (1:현금, 2:공원 전용 신용카드]"))
         if money == 1:
             print("1.현금")
             pay = int(input("요금을 입력하세요:"))
             if pay == 5000:
                 print("감사합니다. 티켓을 발행합니다.")
             elif pay > 5000:
                 print("감사합니다. 티켓을 발행하고 거스름돈 %d원을 반환합니다." % (pay - 5000))
             elif pay < 5000:
                 print("%d원 모자랍니다. 입력하신 요금을 반환합니다." % (pay - 5000))
         elif money == 2:
             print("2.공원 전용 신용카드")
             print("10%할인되어 4500원 결제되었습니다. 감사합니다.티켓을 발행합니다.")
    elif age >= 60 and age <= 65:
        print("귀하의 등급은 [성인]이며, 요금은 5000원 입니다.")
        money = int(input("요금 유형을 선택하세요. (1:현금, 2:공원 전용 신용카드]"))
        if money == 1:
            print("1.현금")
            pay = int(input("요금을 입력하세요:"))
            if pay == 5000:
                print("감사합니다. 티켓을 발행합니다.")
            elif pay > 5000:
                print("감사합니다. 티켓을 발행하고 거스름돈 %d원을 반환합니다." % (pay - 5000))
            elif pay < 5000:
                print("%d원 모자랍니다. 입력하신 요금을 반환합니다." % (pay - 5000))
        elif money == 2:
            print("2.공원 전용 신용카드")
            print("15%할인되어 4250원 결제되었습니다. 감사합니다.티켓을 발행합니다.")
    else:
          print("귀하의 등급은 [노인]이며, 요금은 무료입니다.")
          print("감사합니다. 티켓을 발행합니다.")