# A→B_BOJ16953

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
A, B = map(int, sys.stdin.readline().split())   # A 바뀌기 전의 값 / B 바뀌기 후의 값
cnt = 1                                         # A를 B로 바꾸는데 필요한 연산을 저장할 변수

while A <= B:                                   # A가 B보다 커질 때까지 반복해서
    if A == B:                                  # A와 B가 같다면
        print(cnt)                              # 연산의 수를 출력하고
        break                                   # while문을 break한다
    elif B % 10 == 1:                           # B의 일의 자리의 숫자가 1이라면
        B = B // 10                             # B를 일의 자리를 뺀 숫자로 저장한다
        cnt += 1                                # 연산의 수를 1을 추가한다
    elif B % 2 == 0:                            # B가 짝수라면
        B = B // 2                              # B를 2로 나눈 숫자로 저장한다
        cnt += 1                                # 연산의 수를 1을 추가한다
    else:                                       # 일의 자리의 숫자가 1이 아닌 홀수라면
        print(-1)                               # A를 B로 만들 수 없으므로 -1을 출력한다
        break                                   # while문을 break한다
else:                                           # A가 B보다 커져서 while이
    print(-1)                                   # A를 B로 만들 수 없으므로 -1을 출력한다