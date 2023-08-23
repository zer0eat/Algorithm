# 인사성 밝은 곰곰이_BOJ25192

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 채팅방의 기록을 input 받고
ans = 0                                 # 이모티콘 사용 횟수를 저장할 변수를 생성한다
for i in range(N):                      # 채팅방의 기록을 반복해서
    tmp = input().strip()               # 채팅방의 기록을 input 받고
    if tmp == 'ENTER':                  # 채팅방의 기록이 ENTER라면
        gomgom = dict()                 # 이모티콘 사용 내용을 저장할 딕셔너리를 생성한다
    else:                               # 만약 ENTER가 아니라면
        if gomgom.get(tmp) == None:     # 사용자가 이모티콘을 사용한 기록이 있는지 확인하여 기록이 없다면
            gomgom[tmp] = 1             # 이모티콘 사용 기록을 남기고
            ans += 1                    # 사용 횟수를 1 추가한다
print(ans)                              # 모든 기록을 탐색한 후 곰곰티콘이 사용된 횟수를 출력한다