# Hashing_BOJ15829

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
L = int(sys.stdin.readline())               # 문자열의 길이
arr = sys.stdin.readline().rstrip()         # 문자열을 리스트로 input

r = 31                                      # M과 서로소인 특정 숫자를 31로 지정
M = 1234567891                              # r과 서로소인 특정 숫자를 1234567891로 지정

# 문자를 숫자로 치환하기 위한 딕셔너리 생성
alphabet = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8, 'i' : 9, 'j' : 10, 'k' : 11, 'l' : 12, 'm' : 13, 'n' : 14, 'o' : 15, 'p' : 16, 'q' : 17, 'r' : 18, 's' : 19, 't' : 20, 'u' : 21, 'v' : 22, 'w' : 23, 'x' : 24, 'y' : 25, 'z' : 26}
tmp = 0                                     # 해시를 저장할 변수
for n in range(L):                          # 문자열의 길이만큼 반복해서
    tmp += alphabet.get(arr[n]) * (r**n)    # 해당 문자에 해당하는 숫자에 현재 항의 번호를 제곱한 값을 곱한 값을 tmp에 더한다
else:                                       # 반복을 마쳤다면 M으로 나눈 나머지를 출력
    print(tmp % M)