# 2, 4, 6, 8_BOJ34509

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
ans = 10                                    # 정답을 저장할 변수를 생성하고
while 1:                                    # break가 나올때까지 반복해서
    if ans > 9:                             # 숫자가 두자리 이상인 경우
        tmp = int(str(ans)[::-1])           # 숫자를 뒤집어서
        if tmp % 4 == 0:                    # 뒤집은 숫자가 4의 배수라면
            tmp = list(map(int, str(ans)))  # 각 자리 숫자를 리스트로 만들어서
            if sum(tmp) % 6 == 0:           # 숫자의 합이 6의 배수라면
                if '8' not in str(ans):     # 숫자에 8이 들어가는지 확인해서
                    print(ans)              # 정답을 출력하고
                    break                   # while문을 종료한다
    ans += 1                                # 다음수를 검색하기 위해 1 추가한다