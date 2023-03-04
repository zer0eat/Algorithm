# 멘토와멘티_BOJ26265

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                        # N 멘토와 멘티의 수
name = [list(input().split()) for _ in range(N)]        # 멘토와 멘티의 이름을 리스트로 input 받아 리스트로 저장
name = sorted(name, key=lambda n:(n[1]), reverse=True)  # 멘티의 이름을 내림차순으로 정렬하고
name = sorted(name, key=lambda n:(n[0]))                # 멘토의 이름을 오름차순으로 정렬해서
for n in name:                                          # name 리스트를 반복해서
    print(*n)                                           # 멘토와 멘티를 출력한다