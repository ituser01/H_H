print("*입장료 프로그램*")

while True:
    age = int(input("나이를 입력하세요:"))
    if age >= 0 and age <= 3:
        print("요금은 무료입니다.")
    elif age >= 4 and age <= 13:
        print("요금은 2000원 입니다.")
    elif age >= 14 and age <= 18:
        print("요금은 3000원 입니다.")
    elif age >= 19 and age <= 65:
        print("요금은 5000원 입니다.")
    else:
        print("66세 이상는 무료입니다.")


