# 단어의개수_BOJ1152

# input.txt
import sys
sys.stdin = open('input.txt')

# input 받기
arr = input().split()   # 문자열을 띄어쓰기 단위로 input 받아
print(len(arr))         # 단어를 세어 출력한다