import sys

A = int(input())
B = int(input())
C = int(input())

num = []

result = list(map(int, str(A * B * C))) # 숫자를 문자열로 바꾸고 문자열의 각 문자를 다시 정수로 반환후 리스트(배열) 만들기

for _ in range(10):
   num.append(0) # 0~9까지 리스트 초기화

for _ in range(10):
   
    if 0 in result:
      num[0] += 1
      result.remove(0)

    elif 1 in result:
      num[1] += 1
      result.remove(1)
    
    elif 2 in result:
      num[2] += 1
      result.remove(2)
    
    elif 3 in result:
      num[3] += 1
      result.remove(3)

    elif 4 in result:
      num[4] += 1
      result.remove(4)

    elif 5 in result:
      num[5] += 1
      result.remove(5)

    elif 6 in result:
      num[6] += 1
      result.remove(6)

    elif 7 in result:
      num[7] += 1
      result.remove(7)

    elif 8 in result:
      num[8] += 1
      result.remove(8)

    elif 9 in result:
      num[9] += 1
      result.remove(9)
    
for i in num:
  print(i)