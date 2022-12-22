# N과M5_BOJ15654

# import.txt 열기
import sys
sys.stdin = open('input.txt')

def NM():
    if len(ans) == M:                           # ans 리스트에 M개의 요소가 들어있다면
        print(*ans)                             # ans를 출력하고
        return                                  # return한다
    for i in range(len(lst)):                   # lst를 반복해서
        if lst[i] not in ans:                   # ans에 lst[i]가 없을 때
            ans.append(lst[i])                  # ans에 lst[i]를 append하고
            NM()                                # NM 함수를 실행하고
            ans.pop()                           # ans에서 lst[i]를 pop한다


# input 받기
N, M = map(int, sys.stdin.readline().split())   # N 수열의 개수 / M 중복 없이 고를 개수

lst = list(map(int, sys.stdin.readline().split()))  # input 받은 수열을 lst에 저장한다
lst.sort()                                      # lst를 오름차순으로 정렬한 후

ans = []                                        # 정답을 저장할 빈 리스트 생성

NM()                                            # NM 함수 실행