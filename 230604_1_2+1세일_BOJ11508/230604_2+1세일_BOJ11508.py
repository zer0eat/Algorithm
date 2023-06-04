# 2+1세일_BOJ11508

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                    # 유제품의 수를 input 받고
lst = []                            # 유제품의 가격을 저장할 리스트를 생성하고
for _ in range(N):                  # 유제품의 수를 반복해서
    dairyProduct = int(input())     # 유제품의 가격을 input 받은 후
    lst.append(dairyProduct)        # lst에 유제품의 가격을 append한다
lst.sort(reverse=True)              # 유제품의 가격을 내림차순으로 정렬하고
ans = 0                             # 총 비용을 저장할 변수를 생성한다
for i in range(1, N+1):             # 유제품의 수를 반복해서
    if i % 3 == 0:                  # 3의 배수인 경우에는
        pass                        # 패스하고
    else:                           # 3의 배수가 아닌 경우에는
        ans += lst[i-1]             # ans에 비용을 더한다
print(ans)                          # 유제품을 구입하기 위한 총 비용을 출력한다