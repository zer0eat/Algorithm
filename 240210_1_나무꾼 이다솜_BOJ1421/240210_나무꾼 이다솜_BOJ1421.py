# 나무꾼 이다솜_BOJ1421

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, C, W = map(int, input().split())         # N 나무의 개수 / C 나무를 자를 때 드는 비용 / W 나무 한 단위의 가격을 input 받고
woods = [int(input()) for _ in range(N)]    # 나무의 길이를 리스트로 input 받는다
ans = 0                                     # 정답을 저장할 변수를 생성하고
for l in range(1, max(woods)+1):            # 나무의 길이를 반복해서
    tmp = 0                                 # l 길이로 잘랐을 때 벌 수 있는 비용을 저장할 변수를 생성한다
    for w in woods:                         # 나무를 반복해서
        if w%l:                             # l 길이로 나누어 떨어지지 않는다면
            m = (w//l*l*W - w//l*C)         # 자른 나무의 개수에서 자른 비용을 뺀 값을 m에 저장한다
        else:                               # l 길이로 나누어 떨어진다면
            m = (w//l*l*W - (w//l-1)*C)     # 나누어 떨어지면 마지막 나무는 자를 필요가 없으므로 자른 비용에서 1을 뺀 값을 m에 저장한다
        if m > 0:                           # l로 잘랐을 때 이익이 0 초과라면
            tmp += m                        # tmp에 이익을 더해준다
    ans = max(ans, tmp)                     # 벌 수 있는 최대비용을 저장한다
print(ans)                                  # 벌 수 있는 돈의 최댓값을 출력한다