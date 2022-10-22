# 좌표압축_BOJ18870

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(sys.stdin.readline())                           # 좌표의 수
arr = list(map(int, sys.stdin.readline().split()))      # 좌표를 arr에 input
arrset = set(arr)                                       # arr을 set으로 변경해 중복을 없애준 후
arrset = list(arrset)                                   # 리스트로 다시 변경해서
arrset.sort()                                           # 오름차순으로 정렬해준다

arrdict = dict()                                        # 빈 딕셔너리를 생성하고
for i in range(len(arrset)):                            # arrset을 반복해서
    arrdict[arrset[i]] = i                              # 요소가 key 인덱스가 value가 되는 딕셔너리 생성

ans = []                                                # 정답을 저장할 리스트를 생성하고
for a in arr:                                           # arr을 반복해서
    ans.append(arrdict[a])                              # 해당 딕셔너리 값을 ans에 append

print(*ans)
