# 거짓말_BOJ1043

# input.txt 열기
import sys
sys.stdin = open('input.txt')

def find(ans):
    while ans:                                              # ans가 빌때까지 반복해서
        i = ans.pop()                                       # ans에서 번호를 하나 pop해서 i에 저장한 후
        known.append(i)                                     # known에 거짓말하면 안되는 친구의 번호를 append
        for q in range(len(num)-1, -1, -1):                 # num의 인덱스를 뒤에서부터 반복해서
            if i in num[q]:                                 # 친구 i가 num[q] 파티에 참석해 있다면 거짓말을 하면 안되는 파티가 되므로
                P = num.pop(q)                              # num에서 num[q]를 pop해서 P에 저장한 후
                for p in P:                                 # P를 반복해서
                    if p not in known:                      # known에 없는 친구의 번호가 나오면
                        ans.append(p)                       # ans에 append한다
    return                                                  # ans가 비었다면 함수를 return

# input 받기
N, M = map(int, sys.stdin.readline().split())               # N 친구의수 / M 파티의 수
num = []                                                    # 거짓말 파티를 저장할 빈 리스트 생성
known = list(map(int, sys.stdin.readline().split()))        # 거짓말인지 알고 있는 친구의 수와 친구의 번호를 input 받음
known.pop(0)                                                # 알고 있는 친구의 수를 list에서 pop

for _ in range(M):                                          # 파티의 수를 반복해서
    party = list(map(int, sys.stdin.readline().split()))    # 파티에 참석한 친구의 수와 친구의 번호를 input 받음
    party.pop(0)                                            # 알고 있는 친구의 수를 list에서 pop
    for i in party:                                         # 친구의 번호를 반복해서(1)
        if i in known:                                      # 해당친구가 거짓말인지 알고 있다면
            for j in party:                                 # 친구의 번호를 다시 반복해서(2)
                if j not in known:                          # 거짓말인지 모르는 친구라면
                    ans = [j]                               # ans에 친구 번호를 넣고 리스트를 생성한 후
                    find(ans)                               # find 함수를 통해 거짓말 할 수 없는 파티를 num에서 제외한다
            else:                                           # 반복이 끝났다면
                break                                       # (1)번의 친구의 번호를 반복하는 for문을 break
    else:                                                   # (1)의 반복을 모두 마쳤다면 거짓말 할 수 있는 파티이므로
        num.append(party)                                   # num에 party의 참석자 번호를 list 형태로 append

print(len(num))                                             # 거짓말 할 수 있는 파티의 수를 출력한다



