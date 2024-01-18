# 용액_BOJ2467

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                            # 용액의 수를 input 받고
solution = list(map(int, input().split()))  # 용액의 산/염기를 리스트로 input 받고
left = 0                                    # 왼쪽 용액을 가르킬 포인터를 만들고
right = N-1                                 # 오른쪽 용액을 가르킬 포인터를 만든다
ans = [2000000000, 0, 0]                    # 정답을 저장할 리스트를 생성한 후
while left < right:                         # 왼쪽이 오른쪽과 같아질 때까지 반복해서
    tmp = solution[left] + solution[right]  # 왼쪽과 오른쪽 용액을 더해 tmp에 저장한 후
    if abs(tmp) < ans[0]:                   # tmp의 절대 값이 제일 작은 경우
        ans[0] = abs(tmp)                   # ans[0]에 두 용액의 차를 저장하고
        ans[1] = solution[left]             # ans[1]에 왼쪽 용액의 농도를 저장하고
        ans[2] = solution[right]            # ans[2]에 오른쪽 용액의 농도를 저장한다
        if tmp > 0:                         # tmp의 절대 값이 양수인 경우
            right -= 1                      # 오른쪽의 포인터를 한칸 이동한다
        else:                               # tmp의 절대 값이 0보다 작거나 같은 경우
            left += 1                       # 왼쪽의 포인터를 한칸 이동한다
    elif tmp > 0:                           # tmp의 절대 값이 양수인 경우
        right -= 1                          # 오른쪽의 포인터를 한칸 이동한다
    else:                                   # tmp의 절대 값이 0보다 작거나 같은 경우
        left += 1                           # 왼쪽의 포인터를 한칸 이동한다
print(ans[1], ans[2])                       # 0에 가장 가까운 용액을 만들어내는 경우를 출력한다