# 파일 완전 삭제_BOJ9243

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                    # 파일을 덮어씌울 횟수를 input 받고
before = list(input().strip())      # 기존 파일을 리스트로 input 받고
after = list(input().strip())       # 삭제 후 파일을 리스트로 input 받는다
if N % 2:                           # 덮어씌울 횟수가 홀수라면
    for i in range(len(before)):    # 파일의 원소를반복해서
        if before[i] == '1':        # 현재 1이라고 표시되어 있다면
            before[i] = '0'         # 0으로 바꿔주고
        else:                       # 현재 0이라고 표시되어 있다면
            before[i] = '1'         # 1로 바꿔준다
if before == after:                 # 파일이 삭제된 상태와 같아졌다면
    print("Deletion succeeded")     # 삭제 성공을 출력한다
else:                               # 파일이 삭제된 상태와 다르다면
    print("Deletion failed")        # 삭제 실패를 출력한다