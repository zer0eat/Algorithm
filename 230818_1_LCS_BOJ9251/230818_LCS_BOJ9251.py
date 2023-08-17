# LCS_BOJ9251

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
word1 = input().strip()                                         # 첫번째 문자열을 input 받고
word2 = input().strip()                                         # 두번째 문자열을 input 받은 후
w1 = len(word1)+1                                               # 첫번째 문자열의 길이에 1을 더한 변수를 생성하고
w2 = len(word2)+1                                               # 두번째 문자열의 길이에 1을 더한 변수를 생성한다
lst = [[0] * w2 for _ in range(w1)]                             # w2열 w1행의 행렬을 생성하고
for i in range(1, w1):                                          # 1부터 첫번째 문자열의 길이만큼 반복하고
    for j in range(1, w2):                                      # 1부터 두번째 문자열의 길이만큼 반복해서
        if word1[i-1] == word2[j-1]:                            # i번째 첫번째 문자와 j번째 두번째 문자가 같다면
            lst[i][j] = lst[i-1][j-1] + 1                       # i행 j열의 원소에 이전까지 개수에서 1 더한 값을 저장한다
        else:                                                   # i번째 첫번째 문자와 j번째 두번째 문자가 다르다면
            lst[i][j] = max(lst[i-1][j], lst[i][j-1])           # i번째 첫번째 문자와 j-1번째 두번째 문자까지의 최대 길이와 i-1번째 첫번째 문자와 j번째 두번째 문자까지의 최대 길이 중 더 큰 값을 저장한다
print(lst[w1-1][w2-1])                                          # 부분 수열 중 가장 긴 문자열의 길이를 출력한다