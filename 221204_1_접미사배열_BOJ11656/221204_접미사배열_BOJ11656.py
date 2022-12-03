# 접미사배열_BOJ11656

# import.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = input()                 # 문자열을 input 받고

ans = []                    # 접미사를 저장할 리스트를 생성한 뒤
for n in range(len(N)):     # 문자열의 길이만큼 반복해서
    ans.append(N[n:])       # 접미사를 ans리스트에 append

ans.sort()                  # 사전 순으로 오름차순 정렬하고
for a in ans:               # ans를 반복해서
    print(a)                # 정답을 출력한다


