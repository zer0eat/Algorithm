# k번째 수_BOJ11004

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, K = map(int, input().split())        # N 숫자의 개수 / K N개의 수 중 찾고자 하는 순번을 input 받고
lst = list(map(int, input().split()))   # N개의 숫자를 input 받아 리스트로 저장하고
lst.sort()                              # 오름차순으로 정렬하고
print(lst[K-1])                         # K번째 수를 출력한다