# 엘리스 트랙 매칭_BOJ31428

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                # 학생의 수를 input 받고
track = list(input().split())   # 학생별 선택한 트랙을 리스트로 저장해서
alice = input().strip()         # 앨리스의 트랙을 input 받고
print(track.count(alice))       # 앨리스와 같은 트랙을 선택한 사람의 수를 출력한다