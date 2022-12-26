# N과M10_BOJ15664

# input.txt 열기
import sys
sys.stdin = open('input.txt')

def NM():
    if len(ans) == M:                           # ans 리스트에 M개의 요소가 들어있다면
        A = len(ans2)                           # 중복을 확인할 빈 set의 개수를 A에 저장하고
        tmp = ans[:]                            # tmp에 ans를 저장하고
        tmp.sort()                              # 오름차순으로 sort 한다
        ans2.add(tuple(tmp[:]))                 # ans2 set에 tmp를 add 한 후
        if A != len(ans2):                      # 개수가 바뀌었다면 중복이 아니므로
            print(*tmp)                         # tmp를 출력하고
        return                                  # 리턴한다
    for i in range(len(lst)):                   # lst의 인덱스를 반복해서
        if i not in idx:                        # idx 리스트에 i가 없을 경우에
            ans.append(lst[i])                  # ans에 lst[i]를 append하고
            idx.append(i)                       # idx에 i를 append 하고
            NM()                                # NM 함수를 실행하고
            ans.pop()                           # ans에서 lst[i]를 pop한다
            idx.pop()                           # idx에서 i를 pop한다

# input 받기
N, M = map(int, sys.stdin.readline().split())   # N 수열의 개수 / M 중복 없이 고를 개수

lst = list(map(int, sys.stdin.readline().split()))  # input 받은 수열을 lst에 저장한다
lst.sort()                                      # lst를 오름차순으로 정렬한 후

ans = []                                        # 정답을 저장할 빈 리스트 생성
ans2 = set()                                    # 중복을 확인할 빈 set 생성
idx = []                                        # 인덱스 중복을 확인할 빈 리스트 생성

NM()                                            # NM 함수 실행