# 수이어가기_BOJ2635

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(input())                            # 첫번째 수
i = 1                                       # 두번째 수
maxV = 0                                    # 규칙에 따라 만들 수 있는 최대 개수
maxlst = []                                 # 규칙에 따라 만들 수 있는 최대 개수의 요소를 담은 리스트
while i <= N:                               # i를 N까지 반복할 때
    s = 0                                   # s 더해야 할 값을 불러오는 인덱스
    e = 1                                   # e 빼야할 값을 불러오는 인덱스
    lst = [N, i]                            # 시작과 그 다음 요소를 리스트에 담고 시작
    while lst[s] - lst[e] >= 0:             # 앞의 요소와 뒤의 요소의 차가 0 이상일 때
        lst.append(lst[s] - lst[e])         # 그 값을 리스트에 append
        s += 1                              # 시작값을 한칸 뒤로 이동
        e += 1                              # 빼주는 값을 한칸 뒤로 이동
    else:                                   # 반복이 끝나면
        i += 1                              # 두번째 값을 하나 올려주고
        if maxV < len(lst):                 # 최대 개수가 나온경우는 저장을 해준다
            maxV = len(lst)
            maxlst = lst

print(maxV)
print(*maxlst)

