# 분해합_BOJ2231

# input.txt
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(input())                    # 생성자를 알고 싶은 분해합을 input 받음

n = 1                               # 생성자를 n이라고 생각하고 분해합을 검사하기 위해 변수 생성
while 1:                            # break까지 반복할 때
    sum = 0                         # 분해합을 저장할 변수를 생성하고
    sum += n                        # n 자신을 sum에 더한다
    a = n                           # n을 a에 저장하고
    a = list(str(a))                # a를 str로 바꿔 list에 저장한다
    for i in a:                     # 바꾼 리스트를 순회하며
        sum += int(i)               # 각자리의 숫자를 sum에 더한다
    if n > N:                       # 만약 분해합보다 생성자가 커진다면
        print(0)                    # 0을출력하고
        break                       # break
    elif N == sum:                  # 생성자를 찾았다면
        print(n)                    # 생성자를 출력한 후
        break                       # break
    else:                           # 아직 찾고 있는 중이라면
        n += 1                      # 다음 숫자가 생성자인지 알아보기 위해 n에 1을 추가한다

