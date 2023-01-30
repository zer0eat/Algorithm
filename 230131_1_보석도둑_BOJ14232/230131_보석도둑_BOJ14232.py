# 보석도둑_BOJ14232

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
jewelry = int(sys.stdin.readline().strip())     # 들 수 있는 보석의 무게를 input 받고

ans = []                                        # 낱개의 보석의 무게를 저장할 빈 리스트를 생성하고
num = 2                                         # 공약수를 통해 보석의 무게를 측정하기 위한 변수 생성
while num*num <= jewelry:                       # jewelry가 num의 제곱보다 크다면 반복해서 (num보다 작은 소수는 모두 계산을 했고 제곱근보다 커지면 더이상 나눌 수 없으므로)
    if jewelry % num == 0:                      # jewelry가 num으로 나누어 떨어진다면
        jewelry //= num                         # jewelry를 num으로 나누고
        ans.append(num)                         # ans에 num을 append한다
    else:                                       # num으로 나누어 떨어지지 않는다면
        num += 1                                # num에 1을 추가한다
else:                                           # while문이 끝났다면
    ans.append(jewelry)                         # jewelry를 ans에 append하고
    print(len(ans))                             # ans의 개수를 출력
    print(*ans)                                 # ans를 출력