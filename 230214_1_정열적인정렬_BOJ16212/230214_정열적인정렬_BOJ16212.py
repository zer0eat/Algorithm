# 정열적인정렬_BOJ16212

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(sys.stdin.readline().strip())               # 배열의 길이를 input 받고
lst = list(map(int, sys.stdin.readline().split()))  # 배열을 input 받아서
lst.sort()                                          # 배열을 오름차순으로 정렬해서
print(*lst)                                         # 정렬된 배열을 출력한다