# Робинзон Крузо_BOJ27219

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())
print('V'*(N//5), end='')   # N을 5로 나눌 수 있는 만큼 V를 출력하고
print('I'*(N%5))            # N을 5로 나눈 나머지큼 I를 출력한다