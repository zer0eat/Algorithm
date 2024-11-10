# Football Scoring_BOJ24736

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A = list(map(int, input().split())) # A팀의 득점을 input 받고
B = list(map(int, input().split())) # B팀의 득점을 input 받고
totalA, totalB = 0, 0               # 점수를 저장할 변수를 생성한다
totalA += A[0]*6                    # A팀의 터치다운 점수를 더하고
totalA += A[1]*3                    # A팀의 필드골 점수를 더하고
totalA += A[2]*2                    # A팀의 안전 점수를 더하고
totalA += A[3]*1                    # A팀의 포인트 애프터 점수를 더하고
totalA += A[4]*2                    # A팀의 2점전환 점수를 더한다
totalB += B[0]*6                    # B팀의 터치다운 점수를 더하고
totalB += B[1]*3                    # B팀의 필드골 점수를 더하고
totalB += B[2]*2                    # B팀의 안전 점수를 더하고
totalB += B[3]*1                    # B팀의 포인트 애프터 점수를 더하고
totalB += B[4]*2                    # B팀의 2점전환 점수를 더한다
print(totalA, totalB)               # A, B팀의 점수를 출력한다