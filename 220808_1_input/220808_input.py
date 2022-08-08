# 숫자 하나 받기
import sys
sys.stdin = open('input1.txt')

arr = int(input())
print(arr)

# 리스트로 받기
import sys
sys.stdin = open('input2.txt')

arr = list(map(int, input().split()))
print(arr)

#변수로 받기
import sys
sys.stdin = open('input2.txt')

a, b, c = map(int, input().split())
print(a, b, c)

#매트리스 받기
import sys
sys.stdin = open('input3.txt')

n, m = map(int,input().split())
lst=[]
for i in range(n):
    tmp = list(map(int,input().split()))
    lst.append(tmp)
print(lst)

#매트리스 받기 2
import sys
sys.stdin = open('input3.txt')

n, m = map(int,input().split())
lst = [list(map(int, input().split()))for i in range(n)]
print(lst)

#매트리스 연속 받기
import sys
sys.stdin = open('input4.txt')

t = int(input())
for case in range(1, 1+t):
    n, m = map(int, input().split())
    lst = [list(map(int, input().split()))for i in range(n)]
    print(case)
    print(lst)
