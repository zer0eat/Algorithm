# 부분수열의합2_BOJ1208

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import itertools

# input 받기
N, S = map(int, input().split())                    # N 수열의 크기 / S 부분 수열의 합
lst = list(map(int, input().split()))               # 수열을 list로 input 받고
lst1 = lst[:N//2]                                   # input 받은 수열의 앞부분 반을 lst1로 저장
lst2 = lst[N//2:]                                   # input 받은 수열의 뒷부분 반을 lst2로 저장

tmp1 = []                                           # lst1의 부분집합의 합을 저장할 리스트 생성
tmp2 = []                                           # lst2의 부분집합의 합을 저장할 리스트 생성

for i in range(len(lst1)+1):                        # lst1의 크기만큼 반복해서
    for j in itertools.combinations(lst1, i):       # lst1의 부분집합을 구하고
        tmp1.append(sum(j))                         # 부분집합의 합을 tmp1에 저장한다
tmp1.sort()                                         # tmp1을 오름차순으로 정렬한다

for i in range(len(lst2)+1):                        # lst2의 크기만큼 반복해서
    for j in itertools.combinations(lst2, i):       # lst2의 부분집합을 구하고
        tmp2.append(sum(j))                         # 부분집합의 합을 tmp2에 저장한다
tmp2.sort(reverse=True)                             # tmp2를 내림차순으로 정렬한다

ans = 0                                             # 정답을 저장할 변수 생성
t1 = 0                                              # tmp1의 포인터 변수 생성
t2 = 0                                              # tmp2의 포인터 변수 생성
while t1 < len(tmp1) and t2 < len(tmp2):            # t1의 포인터와 t2의 포인터가 모두 해당 부분집합의 합 리스트보다 커질 때까지 반복해서
    if tmp1[t1] + tmp2[t2] == S:                    # 두 부분집합의 합이 S라면
        ans1 = 1                                    # tmp1[t1]과 같은 원소의 개수를 저장할 변수 생성
        for i in range(t1+1, len(tmp1)):            # t1포인터 부터 tmp1 끝까지 반복해서
            if tmp1[t1] == tmp1[i]:                 # tmp1[t1]와 같은 원소가 나오면
                ans1 += 1                           # ans1에 1을 추가한다
            else:                                   # tmp1[t1]와 다른 원소가 나오면
                break                               # for문을 break
        ans2 = 1                                    # tmp2[t2]과 같은 원소의 개수를 저장할 변수 생성
        for j in range(t2+1, len(tmp2)):            # t2포인터 부터 tmp2 끝까지 반복해서
            if tmp2[t2] == tmp2[j]:                 # tmp2[t2]와 같은 원소가 나오면
                ans2 += 1                           # ans2에 1을 추가한다
            else:                                   # tmp2[t2]와 다른 원소가 나오면
                break                               # for문을 break
        ans += (ans1 * ans2)                        # ans에 부분집합의 수인 ans1 * ans2를 더해준다
        t1 += ans1                                  # t1 포인터를 ans1만큼 이동한다
        t2 += ans2                                  # t2 포인터를 ans2만큼 이동한다
    elif tmp1[t1] + tmp2[t2] < S:                   # 두 부분집합의 합이 S보다 작다면
        t1 += 1                                     # tmp1의 포인터를 한 칸 이동한다
    elif tmp1[t1] + tmp2[t2] > S:                   # 두 부분집합의 합이 S보다 크다면
        t2 += 1                                     # tmp2의 포인터를 한 칸 이동한다

if S == 0:                                          # S가 0이라면
    ans -= 1                                        # 공집합인 경우 1을 빼주고
print(ans)                                          # 부분집합의 개수를 출력한다