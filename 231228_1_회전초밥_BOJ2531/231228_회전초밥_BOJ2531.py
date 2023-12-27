# 회전초밥_BOJ2531

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, D, K, C = map(int, input().split())      # N 회전 초밥 벨트에 놓인 접시의 수 / D 초밥의 가짓수 / K 연속해서 먹는 접시의 수 / C 쿠폰 번호를 input 받고
chobab = [int(input()) for i in range(N)]   # 초밥의 종류를 input 받아 리스트로 저장한다
ans = 0                                     # 먹을 수 있는 초밥의 종류를 셀 변수를 생성하고
for i in range(N):                          # 연속해서 K개 먹을 때 가장 먼저 먹는 초밥을 반복해서
    if i+K > N:                             # K번째 먹는 초밥이 마지막 초밥보다 크다면
        lst = chobab[i:]+chobab[:i+K-N]     # i번째 초밥부터 끝까지와 처음부터 i+K-N번째 초밥까지 먹을 수 있으므로 리스트에 저장하고
    else:                                   # K번째 먹는 초밥이 마지막 초밥보다 작거나 같다면
        lst = chobab[i: i+K]                # i번째부터 K개의 초밥을 리스트에 저장한다
    eat = len(set(lst+[C]))                 # 리스트의 초밥과 서비스 초밥을 set에 담은 후 길이를 구해 먹을 수 있는 종류를 eat에 저장하고
    if eat == K+1:                          # eat이 K+1개라면
        print(K+1)                          # 최댓값이 되므로 K+1로 출력하고
        quit()                              # 종료한다
    elif eat > ans:                         # eat이 최댓값이 아닌경우 ans보다 크다면
        ans = eat                           # ans를 eat으로 저장한다
print(ans)                                  # 먹을 수 있는 초밥의 가짓수를 출력한다