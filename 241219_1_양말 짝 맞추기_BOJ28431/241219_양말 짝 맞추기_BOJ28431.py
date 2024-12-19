# 양말 짝 맞추기_BOJ28431

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
dic = dict()            # 딕셔너리를 생성하고
for n in range(5):      # 5개의 양말을 반복해서
    a = int(input())    # 양말을 input 받고
    if dic.get(a):      # 한짝이 있다면
        dic[a] = 0      # 해당 양말을 pair 처리하고
    else:               # 한짝이 없다면
        dic[a] = 1      # 양말 한짝을 추가한다
for d in dic:           # 양말 딕셔너리를 반복해서
    if dic[d] == 1:     # 한짝만 남아싿면
        print(d)        # 남은 양말을 출력한다