# 수강신청_BOJ13414

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
K, L = map(int, input().split())                        # K 수강 가능 인원 / L 대기 목록의 길이를 input 받는다
click = dict()                                          # 수강신청을 시도한 학번을 저장할 딕셔너리를 생성하고
for i in range(1, L+1):                                 # 1부터 L까지 반복해서
    click[input().strip()] = i                          # 학번을 key로 클릭 순서를 value로 생성한다
click = sorted(click.items(), key=lambda x : x[1])      # 클릭 순서를 오름차순으로 정렬하고
K = min(len(click), K)                                  # 수강 가능 인원과 대기 목록의 번호 중 작은 값으로 K에 저장하고
for i in range(K):                                      # K를 반복해서
    print(click[i][0])                                  # 수강신청에 성공한 인원의 학번을 출력한다