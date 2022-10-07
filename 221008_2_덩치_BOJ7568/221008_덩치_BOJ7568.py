# 덩치_BOJ7568

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(sys.stdin.readline())                                           # N 전체 사람의 수
ans = []                                                                # 사람의 몸무게와 키를 저장할 빈리스트 생성
for _ in range(N):                                                      # 전체사람의 수만큼 반복해서
    ans.append(list(map(int, sys.stdin.readline().split())))            # [몸무게, 키]를 ans리스트에 append

rank = []                                                               # 등수를 저장할 빈리스트 생성
for a1 in range(len(ans)):                                              # 전체사람의 목록을 반복하고
    cnt = 1                                                             # 등수를 저장할 변수를 생성하고
    for a2 in range(len(ans)):                                          # 전체사람의 목록을 반복할 때
        if a1 != a2:                                                    # 같은 두 대상을 비교하지 않을 때
            if ans[a1][0] < ans[a2][0] and ans[a1][1] < ans[a2][1]:     # 기준이 되는 사람보다 비교대상이 키와 몸무게가 모두 클 경우에
                cnt += 1                                                # cnt에 1을 추가하고
    else:                                                               # 반복이 끝났으면
        rank.append(cnt)                                                # rank리스트에 랭킹을 append 한다
print(*rank)