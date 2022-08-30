# 간단한 압축풀기_1946

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())                                                    # 테스트 케이스
for t in range(T):                                                  # 테스트 케이스만큼 반복
    N = int(input())                                                # 테스트 케이스 번호
    arr = [list(input().split()) for _ in range(N)]                 # 압축 정보를 리스트로 저장

    zip = ''                                                        # 압축해제한 문자열을 저장할 변수
    for a in arr:                                                   # 압축된 정보를 하나씩 반복할 때
        zip += a[0] * int(a[1])                                     # 문자열을 숫자만큼 zip에 저장

    print(f'#{t+1}')                                                # 테스트 번호를 출력하고
    for z in range(0, len(zip), 10):                                # 10개씩 끊어서 출력한다
        print(zip[z:10+z])