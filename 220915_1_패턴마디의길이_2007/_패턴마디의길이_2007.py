# 패턴마디의길이_2007

# input.txt
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())                                    # 테스트 케이스
for t in range(T):                                  # 테스트 케이스를 반복할 때
    message = input()                               # 문자열을 input 받고

    tmp = message[0]                                # 첫번째 문자열을 저장한 변수를 생성한 후

    for i in range(1, len(message)):                # 2번째글자 부터 반복하며 같은 문자열을 찾는다
        if tmp == message[i : i + len(tmp)]:        # tmp에 담긴 문자열과 현재부터 tmp 길이만큼 비교했을 때 같다면
            print(f'#{t+1}', len(tmp))              # 문자열의 길이를 출력하고 반복문을 종료한다
            break
        else:                                       # tmp에 담긴 문자열과 현재부터 tmp 길이만큼 비교했을 때 다르다면
            tmp += message[i]                       # i번째 문자를 tmp에 저장하고 넘어간다


