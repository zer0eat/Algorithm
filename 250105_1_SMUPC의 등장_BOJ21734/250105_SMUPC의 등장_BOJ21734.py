# SMUPC의 등장_BOJ21734

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
word = list(input().strip())            # 문자를 input 받고
for w in word:                          # 문자를 반복해서
    aski = ord(w)                       # 문자를 아스키코드로 변환해서
    num1, aski = aski//100, aski%100    # 아스키코드의 백의 자리를 구하고
    num2, num3 = aski//10, aski%10      # 아스키코드의 십과 일의 자리를 구해서
    print(w*(num1+num2+num3))           # 문자를 아스키코드 각 자리의 합만큼 출력한다