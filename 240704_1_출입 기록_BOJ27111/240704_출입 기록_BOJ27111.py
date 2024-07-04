# 출입 기록_BOJ27111

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 출입 기록의 수를 input 받고
ans = 0                                 # 정답을 저장할 변수를 생성한다
dic = dict()                            # 출입기록을 작성할 딕셔너리를 생성하고
for n in range(N):                      # 출입기록을 반복해서
    a, b = map(int, input().split())    # a 출입하는 사람 번호와 b 출입 여부를 input 받고
    if b == 1:                          # 부대에 들어왔다면
        if dic.get(a) == 1:             # a번 사람이 출입 상태라면
            ans += 1                    # 지난 출입이 누락이 되었으므로 누락 개수를 추가한다
        else:                           # a번 사람이 출입하지 않았다면
            dic[a] = 1                  # 출입상태로 기록한다
    else:                               # 부대에서 나갔다면
        if dic.get(a) == 1:             # a번 사람이 출입 상태라면
            dic[a] = 0                  # 나간 상태로 기록한다
        else:                           # a번 사람이 출입 상태가 아니라면
            ans += 1                    # 지난 나간 기록이 누락이 되었으므로 누락 개수를 추가한다
for d in dic:                           # 출입 기록을 반복해서
    if dic[d] == 1:                     # d번 사람이 나간 기록이 없다면
        ans += 1                        # 누락된 기록을 추가한다
print(ans)                              # 누락된 출입 기록의 최소 개수를 출력한다