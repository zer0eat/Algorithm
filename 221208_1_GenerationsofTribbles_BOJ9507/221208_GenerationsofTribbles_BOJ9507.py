# Generations of Tribbles_BOJ9507

# import.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(sys.stdin.readline())               # 테스트 케이스
ans = []                                    # n번째 꿍 피보나치 수를 저장하기 위한 리스트 생성
for t in range(T):                          # 테스트 케이스를 반복해서
    ans.append(int(sys.stdin.readline()))   # 꿍 피보나치수 인덱스를 input 받아 ans에 append

ggong_fibonaci = [1, 1, 2, 4]               # 0부터 3까지 꿍 피보나치 수를 저장한 리스트를 생성하고

for a in range(4, max(ans)+1):              # 4부터 ans에 담긴 최대 값까지 반복해서
    ggong_fibonaci.append(ggong_fibonaci[a-1] + ggong_fibonaci[a-2] + ggong_fibonaci[a-3] + ggong_fibonaci[a-4])  # 4부터 꿍 피보나치수를 구해 리스트에 append

for n in ans:                               # ans를 반복해서
    print(ggong_fibonaci[n])                # 해당 숫자의 꿍피보나치수를 출력한다
