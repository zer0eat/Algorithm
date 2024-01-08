# 아이폰 9S_BOJ5883

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                            # 아이폰을 구매하려는 사람의 수를 input 받고
iphone = [int(input()) for i in range(N)]   # 구매하려는 아이폰의 용량을 리스트로 input 받는다
ans = 0                                     # 같은 용량을 원하는 사람의 연속 구간 길이를 저장할 변수를 생성하고
for i in range(N):                          # 아이폰을 구매하려는 사람의 수를 반복해서
    flag = 0                                # 줄에서 뺄 용량을 저장할 변수를 생성하고
    tmp = 1                                 # 연속된 사람의 수를 저장할 변수를 생성한다
    for j in range(i+1, N):                 # i번째 다음사람부터 반복해서
        if iphone[i] == iphone[j]:          # i번째 사람과 같은 용량을 구매하려고 한다면
            tmp += 1                        # 연속된 사람의 수를 더해주고
        elif not flag:                      # i번째 사람과 다른 용량을 사려는 사람이 나왔을 때 아직 뺸사람이 없다면
            flag = iphone[j]                # 뺄 사람의 용량을 flag에 저장한다
        elif flag == iphone[j]:             # i번째 사람과 다른 용량을 사려는 사람이 나왔을 때 뺸사람이 있는 경우 뺀사람과 j번째 사람의 용량이 같다면
            pass                            # pass한다
        else:                               # i번째 사람과 j번째 사람이 사려는 용량도 다르고 이미 뺀사람과 용량도 다르다면
            ans = max(ans, tmp)             # tmp와 ans 중 큰 값을 ans에 저장하고
            break                           # for문을 종료한다
    else:                                   # 마지막 사람까지 모두 확인했다면
        ans = max(ans, tmp)                 # tmp와 ans 중 큰 값을 ans에 저장한다
print(ans)                                  # 가장 길이가 긴 같은 용량을 원하는 사람의 연속 구간의 길이를 출력한다