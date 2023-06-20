# 이진검색트리_BOJ5639

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# input 받기
lst = []                                # input 데이터를 저장할 리스트 생성
while 1:                                # break가 나올때까지 반복해서
    try:                                # input 받을 데이터가 있다면
        lst.append(int(input()))        # 이진 검색 트리를 전위 순회한 순서를 lst에 append
    except:                             # 더 이상 input 받을 데이터가 없어 예외가 발생했다면
        break                           # whlie문을 break

def postorder(start, end):
    if start > end:                     # 트리의 시작점보다 끝점이 더 작다면
        return                          # 함수를 return
    for i in range(start+1, end+1):     # 1번 인덱스부터 끝까지 반복해서
        if lst[start] < lst[i]:         # 시작 인덱스의 숫자보다 큰수가 나오면
            mid = i                     # 해당 인덱스를 mid에 저장하고
            break                       # for문을 break
    else:                               # 작은수가 없다면 루트 오른쪽은 숫자가 없으므로
        mid = end + 1                   # mid를 end + 1로 자장
    postorder(start+1, mid-1)           # 루트 왼쪽에 있는 수를 후위순회하기 위해 (루트 다음수부터, 왼쪽 끝 수)
    postorder(mid, end)                 # 루트 오른쪽에 있는 수를 후위순회하기 위해 (mid부터, 끝까지)
    print(lst[start])                   # 후위 순회를 모두 마친 후 루트를 출력한다

postorder(0, len(lst)-1)                # 후위순회를 할 트리의 시작점과 끝점을 넣어 찾는다
