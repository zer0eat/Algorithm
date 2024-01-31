# 수들의 합 8_BOJ25332

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 수열의 길이를 input 받고
lstA = list(map(int, input().split()))  # A 수열을 리스트로 input 받고
lstB = list(map(int, input().split()))  # B 수열을 리스트롤 input 받는다
dic = dict()                            # 두 수의 차를 저장할 딕셔너리를 생성한다
sumA = 0                                # A 리스트의 합을 저장할 변수를 생성하고
sumB = 0                                # B 리스트의 합을 저장할 변수를 생성한다
dic[0] = 1                              # 두 리스트의 차가 0이 되는 값을 1로 저장하고
ans = 0                                 # 정답을 저장할 변수를 생성한다
for i in range(N):                      # 수열의 길이를 반복해서
    sumA += lstA[i]                     # sumA에 i번째 원소를 더하고
    sumB += lstB[i]                     # sumB에 i번째 원소를 더한 후
    if dic.get(sumA-sumB) != None:      # 두 수의 차만큼 차이가 있던 경우가 있었다면
        ans += dic[sumA-sumB]           # 두 수의 차만큼 있던 앞선 경우만큼 합이 같게 만들 수 있으므로 ans에 추가하고
        dic[sumA-sumB] += 1             # 두 수의 차를 key인 원소에 value를 1 추가한다
    else:                               # 두 수의 차만큼 차이가 있던 경우가 처음이라면
        dic[sumA-sumB] = 1              # 두 수의 차를 key로 value를 1로 원소를 생성한다
print(ans)                              # 두 수열의 합이 같아지는 경우의 수를 출력한다