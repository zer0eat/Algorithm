# 자작나무가 없소~_BOJ31496

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, S = input().split()              # 아이템의 수와 아이템 이름을 input받고
ans = 0                             # 정답을 저장할 변수를 생성하다
for n in range(int(N)):             # 아이템의 수를 반복해서
    item, M = input().split()       # 아이템과 개수를 input받고
    item = list(item.split('_'))    # 아이템의 이름을 _ 기준으로 나눠서
    for i in item:                  # 아이템의 이름을 반복해서
        if S == i:                  # S가 포함된 아이템이라면
            ans += int(M)           # 개수를 정답에 추가하고
            break                   # for문을 break한다
print(ans)                          # 사라진 아이템의 수를 출력한다