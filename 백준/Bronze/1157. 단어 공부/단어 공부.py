import sys
from collections import Counter

word = input()
word = word.upper() # 대소문자 구분 없다했으니 대문자로 변환 -> 리스트는 upper X
word = list(word) # 먼저 소문자로 변환하고 list 형태로 바꿈

count = Counter(word) # 단어와 단어 개수가 딕셔너리로 반환됨

max_count = max(count.values()) # 최대 빈도수 
max_words = [k for k, v in count.items() if v==max_count] # 빈도수 가진 문자 찾기

if len(max_words) > 1:
    print("?")
else:
    print(max_words[0])