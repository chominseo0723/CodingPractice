import sys

# 공백으로 구분된 여러 정수를 리스트로 입력받기 
line = list(map(int, input().split())) 

N = line[0] # 사람 수
K = line[1] # K번째 사람 제거

people = list(range(1, N+1)) # 1~N 까지 사람 리스트 생성
box = [] # 최종 출력 박스 
idx = 0 # 처음 인덱스 

while len(people): # line 의 원소 개수만큼 출력
    idx = (idx+K-1) % len(people) # K-1 번째 인덱스
    box.append(people.pop(idx))

# ", ".join(map(str, box)) : box 의 모든 원소에 str() 적용 -> join 은 문자열만 가능하므로
# 그 문자열 리스트를 ㅣ", " 로 이어붙인다.
print("<"+", ".join(map(str, box))+">")
