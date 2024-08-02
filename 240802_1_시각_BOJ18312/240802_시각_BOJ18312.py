# 시각_BOJ18312

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, K = map(int, input().split())                # N 시와 K 들어가는 수를 input 받고
ans = 0                                         # 정답을 저장할 변수를 생성하고
for n in range(N+1):                            # 시를 세고
    if n < 10:                                  # 시가 한자리라면
        n *= 10                                 # 시에 0을 붙여주고
    for m in range(60):                         # 분을 세고
        if m < 10:                              # 분이 한자리라면
            m *= 10                             # 분에 0을 붙여주고
        for k in range(60):                     # 초를 세고
            if k < 10:                          # 초가 한자리라면
                k *= 10                         # 초에 0을 붙여준다
            if str(K) in str(n)+str(m)+str(k):  # K가 해당 시간에 들어간다면
                ans += 1                        # 정답을 하나 추가하고
print(ans)                                      # K가 포함되는 시간을 출력한다