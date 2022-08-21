# input을 텍스트로 받기
import sys
sys.stdin = open('gravity_input.txt')

#lst에 input.txt를 리스트로 저장
box = list(map(int, input().split()))

maxV = 0                                        # 박스의 최대 이동 값
for b in range(len(box)):                       # 박스의 원소를 반복할 때
    cnt = 0                                     # 박스가 이동한 칸의 수
    for c in range(len(box)-b):                 # 나를 포함한 이후의 박스를 반복할 때
        if box[b] > box[b + c]:                 # 나보다 작은 박스가 나올때만 카운트
            cnt += 1
    else:                                       # 반복이 끝나면
        if cnt > maxV:                          # 카운트가 maxV보다 크면 교체
            maxV = cnt

print(maxV)