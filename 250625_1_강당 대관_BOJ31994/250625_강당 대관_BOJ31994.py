# 강당 대관_BOJ31994

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
ans = ''                        # 정답을 저장할 변수를 생성하고
people = 0                      # 최대 인원을 저장할 변수를 생성한다
for n in range(7):              # 7개의 강의를 반복해서
    A, B = input().split()      # 강의명과 신청자수를 input받고
    if people < int(B):         # 최대 신청자 수가 나왔다면
        ans = A                 # 강의명을 저장하고
        people = int(B)         # 최대 신청자수를 갱신한다
print(ans)                      # 강당을 대관해줄 강의를 출력한다