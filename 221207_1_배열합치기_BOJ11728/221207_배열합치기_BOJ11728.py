# 배열합치기_BOJ11728

# import.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N, M = map(int, sys.stdin.readline().split())           # N 첫번째 리스트의 숫자 개수 / M 두번째 리스트의 숫자 개수

ans1 = list(map(int, sys.stdin.readline().split()))     # 첫번째 배열의 내용을 리스트로 input 받고
ans2 = list(map(int, sys.stdin.readline().split()))     # 두번째 배열의 내용을 리스트로 input 받은 후

ans = ans1 + ans2                                       # 두 배열을 합친 후

ans.sort()                                              # 오름차순으로 정렬하고
print(*ans)                                             # 출력한다