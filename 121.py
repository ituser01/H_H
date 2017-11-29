pocket=['cellphone''money']
card=1
if 'money' in pocket:    print("일반 택시를 타고 가라")
elif card:                print("모범 택시를 타고 가라")
else:                     print("걸어가라")

treeHit=0
while treeHit < 10:
    treeHit= treeHit+1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
       print("나무 넘어 갑니다.")