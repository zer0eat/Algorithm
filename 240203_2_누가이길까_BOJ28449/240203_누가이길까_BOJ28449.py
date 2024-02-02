# 누가 이길까_BOJ28449

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

# input 받기
N, M = map(int, input().split())                # N HI 팀의 인원수 / M ARC 팀의 인원 수 input 받고
HI = list(map(int, input().split()))            # HI팀의 코딩 실력을 리스트로 input 받고
ARC = list(map(int, input().split()))           # ARC팀의 코딩 실력을 리스트로 input 받고
ARC.sort()                                      # ARC를 오름차순으로 정렬한다
ans = [0, 0, 0]                                 # 정답을 저장할 리스트를 생성하고
for h in HI:                                    # HI의 코딩실력을 반복해서
    midL = bisect_left(ARC, h)                  # ARC에서 h보다 낮은 인덱스를 저장하고
    midR = bisect_right(ARC, h)                 # ARC에서 h보다 높은 인덱스를 저장한다
    if midL == midR:                            # midL과 midR이 같다면 같은 수가 없으므로
        ans[0] += midL                          # 승리횟수와
        ans[1] += len(ARC)-midL                 # 패배 횟수를 저장하고
    else:                                       # midL과 midR이 다르다면
        if midL < len(ARC) and ARC[midL] != h:  # midL이 인덱스 안에 있고 h가 아니라면
            midL += 1                           # midL을 오른쪽으로 한칸 이동하고
        if midR == len(ARC) or ARC[midR] != h:  # midR이 인덱스 안에 있고 h가 아니라면
            midR -= 1                           # midR을 왼쪽으로 한칸 이동한다
        if midL <= midR:                        # midL이 midR보다 같거나 작다면
            ans[2] += (midR-midL+1)             # 무승부 횟수를 더해주고
            ans[0] += midL                      # 승리 횟수를 더해주고
            ans[1] += len(ARC)-midR-1           # 패배 횟수를 더해준다
        else:                                   # midL이 midR보다 크다면 모든 경우 승리하므로
            ans[0] += midL                      # 승리횟수를 저장한다
print(*ans)                                     # HI팀 참가자의 승리 횟수, ARC팀 참가자의 승리 횟수, 무승부 횟수를 공백으로 구분하여 출력한다
