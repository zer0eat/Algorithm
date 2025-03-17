# 피갤컵_BOJ33612

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())    # N번째 피갤컵을 input 받고
cup = {
    1: [2024, 8],
    2: [2025, 3],
    3: [2025, 10],
    4: [2026, 5],
    5: [2026, 12]
}                   # 피갤컵 개최 일자 딕셔너리를 생성해서
print(*cup[N])      # N번째 피갤컵 날짜를 출력한다다