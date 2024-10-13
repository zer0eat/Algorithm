# 6174_BOJ9047

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                        # 테스트케이스를 input 받고
for t in range(T):                      # 테스트케이스를 반복해서
    num = input().strip()               # 숫자를 input 받고
    ans = 0                             # kaprekar 연산의 수를 저장할 변수를 생성한다
    while 1:                            # break가 나올 때까지 반복해서
        if num == '6174':               # num이 6174가 나오면
            break                       # while문을 종료한다
        tmp = list(num)                 # num을 리스트로 저장하고
        big, small = '', ''             # 큰수와 작은수를 저장할 변수를 생성하고
        tmp.sort()                      # tmp를 오름차순으로 정렬해서
        for p in tmp:                   # tmp를 반복해서
            small += p                  # 가장 작은 수를 만들어준후
        else:                           # for문을 마치면
            big = small[::-1]           # 가장 작은 수를 뒤집어 가장 큰 수를 저장한다
        num = str(int(big)-int(small))  # 큰수와 작은수의 차를 저장하고
        for n in range(4-len(num)):     # 4자리 이하라면 모자란만큼 반복해서
            num = '0'+num               # 앞에 0을 붙여준다
        ans += 1                        # 연산의 수를 1추가하고
    print(ans)                          # kaprekar연산의 수를 출력한다