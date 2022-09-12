# 손익분기점_BOJ1712

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
arr = list(map(int, input().split())) # 고정비용, 가변비용, 판매비용이 적혀있는 리스트를 받고

n = 1   # n에 1을 저장한 후

# 팔수록 손해가 쌓이면 -1을 출력하고
if (arr[0]+(arr[1]*n)) - (arr[2]*n) <= (arr[0]+(arr[1]*(n+1))) - (arr[2]*(n+1)):
    print(-1)
# 팔수록 이익이 생기면 고정비용을 (판매비용 - 가변비용)으로 나누어 정수부분만 받은 뒤 1을 더한 값을 출력한다(최초 순이익이 생기는 개수)
elif (arr[0]+(arr[1]*n)) - (arr[2]*n) > (arr[0]+(arr[1]*(n+1))) - (arr[2]*(n+1)):
    n = 1 + arr[0] // ((arr[0]+(arr[1]*n)) - (arr[2]*n) - (arr[0]+(arr[1]*(n+1))) + (arr[2]*(n+1)))
    print(n)