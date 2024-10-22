# NFC West vs North_BOJ10170

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
print("NFC West       W   L  T")    # NFC 서부와 북부 디비전 순위를 출력한다
print("-----------------------")
print("Seattle        13  3  0")
print("San Francisco  12  4  0")
print("Arizona        10  6  0")
print("St. Louis      7   9  0")
print("")
print("NFC North      W   L  T")
print("-----------------------")
print("Green Bay      8   7  1")
print("Chicago        8   8  0")
print("Detroit        7   9  0")
print("Minnesota      5  10  1")