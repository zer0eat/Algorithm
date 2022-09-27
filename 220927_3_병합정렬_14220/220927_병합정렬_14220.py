# 병합정렬_14220

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# 분할정복
def mergesort(lst):
    if len(lst) == 1:                       # 리스트의 길이가 1이면
        return lst                          # lst를 리턴한다
    middle = len(lst)//2                    # 중간 값을 len(lst)//2 로 잡고
    left = lst[:middle]                     # 왼쪽을 처음부터 middle 전까지
    right = lst[middle:]                    # 오른쪽을 middle부터 끝까지로 잘라준다
    left = mergesort(left)                  # 왼쪽만 다시 mergesort 돌리고
    right = mergesort(right)                # 오른쪽만 다시 mergesort 돌린다
    return merge(left, right)               # 두 리스트를 merge 하는 함수에 넣는다

def merge(left, right):
    global cnt                              # 오른쪽 리스트의 끝이 왼쪽리스트의 끝보다 작을 경우 더해줄 변수 불러옴
    result = []                             #
    if left[-1] > right[-1]:                # 왼쪽리스트 끝과 오른쪽리스트 끝을 비교해서 왼쪽이 더크면
        cnt += 1                            # cnt에 1을 추가한다
    left = left[::-1]                       # left에 리스트를 뒤집어서 다시 저장해주고
    right = right[::-1]                     # right에 리스트를 뒤집어서 다시 저장해준다
    while left or right:                    # left와 right 둘중하나가 빌때까지 반복해서
        if left and right:                  # 만약 left와 right가 둘다 있으면
            if left[-1] <= right[-1]:       # left의 맨뒤의 요소와 right의 맨뒤의 요소를 비교해서 left가 더 작거나 같으면
                result.append(left.pop())   # result에 left를 pop해서 넣는다
            else:                           # right가 더 작다면
                result.append(right.pop())  # result에 right를 pop해서 넣는다
        elif left:                          # 만약 left만 요소가 들어 있다면
            result.extend(left[::-1])       # 남아있는 요소를 뒤집어서 result에 extend 한다
            break                           # while문 break
        elif right:                         # 만약 right만 요소가 들어 있다면
            result.extend(right[::-1])      # 남아있는 요소를 뒤집어서 result에 extend 한다
            break                           # while문 break
    return result                           # 결과를 return 한다

# input 받기
T = int(input())                            # 테스트 케이스
for t in range(T):                          # 테스트 케이스를 반복할 때
    N = int(input())                        # 정수의 개수
    L = list(map(int, input().split()))     # N개의 정수를 L에 리스트 형태로 받음
    cnt = 0                                 # 병합할 때 오른쪽 마지막 요소가 왼쪽 마지막 요소보다 큰 경우에 더할 변수
    L = mergesort(L)                        # L에 mergesort 결과를 저장한다
    print(f'#{t+1}', L[N//2], cnt)