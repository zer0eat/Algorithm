# 고냥이_BOJ16472

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                            # 인식할 수 있는 알파벳의 수를 input 받고
word = list(input().strip())                # 문자열을 리스트로 input 받는다
l = 0                                       # 왼쪽 끝을 가르킬 포인터를 생성하고
r = 0                                       # 오른쪽 끝을 가르킬 포인터를 생성한다
ans = 1                                     # 최장 길이를 저장할 변수를 생성하고
alphabet = [0]*26                           # 알파벳의 수를 저장할 리스트를 생성한 뒤
alphabet[ord(word[r])-97] = 1               # 문자열의 첫번째 알파벳을 하나 추가하고
cnt = 1                                     # 알파벳의 종류를 셀 변수를 생성한다
while l < len(word)-1:                      # 왼쪽포인터가 단어의 끝까지 갈때까지 반복해서
    if cnt <= N and r < len(word)-1:        # cnt가 N개 이하이고 오른쪽 포인터가 끝지점에 도달하지 않았다면
        r += 1                              # 오른쪽 포인터를 한칸 이동하고
        if alphabet[ord(word[r])-97] == 0:  # 오른쪽 포인터가 가르키는 알파벳이 없다면
            cnt += 1                        # cnt를 1개 추가하고
        alphabet[ord(word[r])-97] += 1      # 오른쪽 포인터가 가르키는 알파벳의 수를 하나 증가시킨다
    else:                                   # cnt가 N개보다 크거나 오른쪽 포인터가 끝지점이라면
        if alphabet[ord(word[l])-97] == 1:  # 왼쪽 포인터가 가르키는 알파벳이 한개 남았다면
            cnt -= 1                        # cnt를 1개 줄이고
        alphabet[ord(word[l])-97] -= 1      # 왼쪽 포인터가 가르키는 알파벳의 수를 하나 감소시킨 후
        l += 1                              # 왼쪽 포인터를 한칸 이동한다
    if cnt <= N:                            # 이동후 cnt가 N개 이하라면
        ans = max(ans, r-l+1)               # ans와 현재 문자열 길이 중 더 긴 값을 저장한다
print(ans)                                  # 번역기가 인식할 수 있는 문자열의 최대길이를 출력한다