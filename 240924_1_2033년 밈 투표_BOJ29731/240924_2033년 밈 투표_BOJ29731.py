# 2033년 밈 투표_BOJ29731

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
promise = {'Never gonna give you up' : 1,                   # 공약을 딕셔너리로 저장하고
           'Never gonna let you down' : 1,
           'Never gonna run around and desert you' : 1,
           'Never gonna make you cry' : 1,
           'Never gonna say goodbye' : 1,
           'Never gonna tell a lie and hurt you' : 1,
           'Never gonna stop' : 1}
N = int(input())                                            # 공약의 수를 input받고
for n in range(N):                                          # 공약의 수를 반복해서
    speak = input().strip()                                 # 공약을 input 받고
    if promise.get(speak):                                  # 해당 공약이 존재하면
        pass                                                # pass하고
    else:                                                   # 해당 공약이 존재하지 않으면
        print('Yes')                                        # Yes를 출력하고
        quit()                                              # 종료한다
else:                                                       # 모든 공약이 존재하면
    print('No')                                             # No를 출력한다