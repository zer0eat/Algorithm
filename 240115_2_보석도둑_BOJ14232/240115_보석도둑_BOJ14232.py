# 보석도둑_BOJ14232

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
K = int(input())            # 보석의 무게를 input 받고
ans = []                    # 훔쳐올 보석의 무게을 저장할 리스트를 생성한 후
prime = 2                   # 보석의 무게를 갖는 변수를 생성한다
while prime*prime <= K:     # prime이 K의 제곱근이 보다 커질때까지 반복해서
    if K % prime == 0:      # K가 prime으로 나누어 떨어지면
        K //= prime         # K를 prime으로 나누고
        ans.append(prime)   # 보석의 무게에 prime을 추가한다
    else:                   # K가 prime으로 나누어 떨어지지 않는다면
        prime += 1          # prime을 1 추가해서 다음으로 넘어간다
else:                       # prime이 K의 제곱근보다 커졌다면
    ans.append(K)           # 남은 K를 보석의 무게에 추가하고
    print(len(ans))         # 보석의 개수를 출력하고
    print(*ans)             # 보석의 무게를 오름차순으로 출력한다