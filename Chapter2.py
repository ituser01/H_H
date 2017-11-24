\n "문자열 삽입"
\n "a=','"
\n "a.join('abcd)"
\n "'a,b,c,d'"

\n "문자열 바꾸기(replace)"
\n "a="Life is too short"
\n "a.replace("Life","your leg")
\n "your leg is too short"

\n "문자열 나누기(split)"
\n "a='Life is too short'"
\n "a.split() <공백기준으로 문자열 나눔>"
\n "['Life','is','too','short']"
\n "[a='a:b:c:d']"
\n "a.split(':') <: 기호를 기준으로 문자열 나눔>"
\n "['a','b','c','d']"

\n "리스트형 구조에서 쓰이는 함수"
\n "a=[1,2,3,['a','b','c']]"
\n "a[0]=1"
\n "a[-1]=['a','b','c']"
\n "a[3]=[a'a,'b','c']"

\n "a='12345'
\n "a[0:2]=12 처음부터 2번째까지의 값을 모두 나타낸다."
\n "a=[1,2,3,4,5]"
\n "b=a[:2] 처음부터 a[1]까지 *python은 0부터 숫자를 세는 것과 리스트들 안에 숫자들을
\n "c=a[2:] a[2]부터 끝까지    세는 것과 혼돈하면 안된다.
\n "b=[1,2] c=[3,4,5]"

\n "중첩된 리스트에서 슬라이싱하기"
\n "a=[1,2,3,['a','b','c'],4,5]"
\n "a[2:5]=[3,['a','b','c'],4]"
\n "a[3][:2]=['a','b']"

\n "리스트 반복하기(*)"
\n "a=[1,2,3]"
\n "a*3=[1,2,3,1,2,3,1,2,3]"

\n "리스트에서 하나의 값 수정하기"
\n "a=[1,2,3]"
\n "a[2]=4"
\n "a=[1,2,4]"

\n "del 함수 이용해서 리스트 요소 삭제하기"
\n "a=[1,'c',4]"
\n "del a[1]"
\n "a = [1,4]"

\n "리스트에 요소 추가하기"
\n "a=[1,2,3]"
\n "a.append(4)"
\n "a=[1,2,3,4]"

\n "a.append([5,6])"
\n "a=[1,2,3,4,[5,6])"

\n "리스트 정렬(sort)"
\n "a=[1,4,3,2]"
\n "a.sort()"
\n "a=[1,2,3,4]"

\n "리스트 뒤집기(reverse)"
\n "a=['a','c','b']"
\n "a.reverse()"
\n "a=['b','c','a']"

\n "리스트에 요소 삽입(insert)"
\n "a=[1,2,3]"
\n "a.insert(0,4)" a[0] 위치에 4를 삽입
\n "[4,1,2,3]"

\n "리스트 요소 제거(remove)"
\n "a=[1,2,3,1,2,3]"
\n "a.remove(3)" < 중복으로 '3'이 있어도 제일 처음 요소만 사라짐
\n "a=[1,2,1,2,3]"

\n "리스트요소 끄집어내기(pop)"
\n "a=[1,2,3]"
\n "a.pop()"
\n "a=[1,2]"

\n "리스트 확장(expend)"
\n "a=[1,2,3]"
\n "a.extemd([4,5])"
\n "a=[1,2,3,4,5]"

\n "딕셔너리 기본틀"
\n "dic={'name':'pey','phone':'01012345678','birth':'1118'}
\n "key='name','phone','birth'"

\n "집합 자료형"
\n "s1=set([1,2,3])"
\n "s1={1,2,3}

\n "s1=set([1,2,3,4,5,6])"
\n "s2=set([4,5,6,7,8,9])"
\n "교집합"
\n "s1&s2= {4,5,6}"
\n "s1.intersection(s2) ={4,5,6}
\n "합집합"
\n "s1|s2"
\n "{1,2,3,4,5,6,7,8,9}
\n "si.union(s2)={1,2,3,4,5,6,7,8,9}
\n "차집합"
\n "s1-s2"
\n "{1,2,3}"
\n "s2-s1"
\n "{8,9,7}"
\n "s1.difference(s2)"
\n "{1,2,3}
\n "s2.difference(s1)"
\n "{8,9,7}"
-------------"연 습 문 제"--------------
pin = "881120-1068234"
print(pin[:6])
print(pin[7:])

pin = "881120-1068234"
print(pin[7])

a=[1,3,5,4,2]
a.sort()
a.reverse()
print(a)

a=['Life','is','too','short']
result=" ".join(a)
print(result)

a=(1,2,3)
a=a+(4,)
print(a)

a={'A':90,'B':80,'C':70}
result =a.pop('B')
print(a)
print(result)

a=[1,1,1,2,2,3,3,3,4,4,5]
aset=set(a)
b=list(aset)
print(b)
