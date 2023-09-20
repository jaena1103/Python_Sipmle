# 컬렉션 타입
#  - 변수 하나에 값을 여러개 저장
#  - 실질적으로 변수에 컬렉션 1개가 저장
#  - **리스트(List), *튜플(Tuple), **딕트(Dictionary), 세트(Set)

# 1.리스트(List)  ex: 기차
#  - 시퀀스 자료형(연속 된 값 저장)
#  - index 사용(Slicing 가능)
#  - [] 사용
#  - 정렬 가능
#  - mutable(생성 된 후 변경 가능)
#  - packing과 unpacking 가능
#  - 멤버함수: append(), extend(), insert(), remove(), pop(), index(), sorted(), 등등
# * 2차원 리스트는 표(table)과 동일한 형태

list_a = [1, 2, 3]                       #3칸
list_b = []                              #1칸
list_c = ["chosun", 5, 3.14, [1, 2, 3]]  #4칸
# ^1차원리스트                  ^2차원리스트
# c에서 배열같은 느낌 요것은 c에 없는 내용 알아두쇼잉

#packing and unpacking
list_d = ["A", "B", "C"]  # packing 리스트를 대괄호로 묶어남
a, b, c = ["A", "B", "C"] # unpacking 처음보는 것 a가 A로 순서대로 담김

# a = list_d[0]
# b = list_d[1]     ->  c랑 java에서 이렇게 씀 파이썬은 위에처럼
# c = list_d[2]

# append(값) : 리스트의 맨 마지막에 값을 추가
a = [1, 2, 3]
a.append(4)
print(a)
# insert(인덱스, 값) : 리스트의 원하는 인덱스에 값을 추가
b = [1, 2, 3]
b.insert(1, 9)
print(b)

# extend(리스트) : 리스트와 리스트를 병합
a = [1, 2, 3]
b = [3, 4, 5]
# a.extend(b)
# print(a)
c = a+b
print(c)
# append는 병합아니라 추가여서 안된데

# remove(값) : 리스트 내 원소를 값으로 삭제
# pow(인덱스) : 리스트 내 원소를 인덱스로 삭제
abc = [1, 2, 3, 4, 5]
abc.remove(3) # 3이라는 값
print(abc)
e = abc.pop(0)  # 0번 인덱스
print(abc)
print(e)   # -> 선택사항 담고싶음 담기

# index() : ()안의 값의 인덱스를 출력
a = ["A", "B"]
print(a.index("B"))

# sort() and sorted() : 리스트 안의 원소들을 정렬
#  - sort() : 원본값 자체를 정렬(원본값 상실)  쓰지마삼
#  - sorted() : 원본값을 복제해서 정렬(원본값 유지)  이거 쓰기
a = [95, 1, 3, 55, 27, 45]
b = sorted(a)  # 디포트: 오름차순
c = sorted(a, reverse=True)  # 내림차순
print(a)
print(b)
print(c)
