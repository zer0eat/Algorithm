# Christmas Tree Adapter_BOJ32314

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
a = int(input())                    # 트리의 암페어를 input 받고
w, v = map(int, input().split())    # 어댑터의 와트와 볼트를 input 받는다
adapter = w/v                       # 어댑터의 암페어를 구하고
if a <= adapter:                    # 트리의 암페어보다 어댑터의 암페어가 같거나 크면
    print(1)                        # 1을 출력하고
else:                               # 그렇지 않으면
    print(0)                        # 0을 출력한다