#gravity

# input을 텍스트로 받기
import sys
sys.stdin = open('input.txt')

#lst에 input.txt를 리스트로 저장
lst = list(map(int, input().split()))

# 원소활용
# for i in lst:
#     value = i

# index 활용
res = 0 # 결과물
for idx in range(len(lst)):
    value = lst[idx]

# 나보다 오른쪽에 있는 박스 수 세기
    cnt = 0
    for right_idx in range(idx+1, len(lst)):
        if value > lst[right_idx]:
            cnt += 1
    if cnt > res:
        res = cnt

print(res)