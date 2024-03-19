# 팰린드롬_BOJ8892

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                                        # 테스트 케이스를 input 받고
for t in range(T):                                      # 테스트 케이스를 반복해서
    K = int(input())                                    # 단어의 수를 input 받고
    ans = 0                                             # 정답을 저장할 변수를 생성한다
    words = [input().strip() for _ in range(K)]         # 단어를 input 받아 리스트에 저장하고
    for i in range(K):                                  # 저장된 단어를 반복하고
        for j in range(K):                              # 저장된 단어를 반복해서
            if i != j:                                  # i와 j가 다른 단어라면
                word = words[i] + words[j]              # 두 단어의 합을 word에 저장하고
                for w in range(len(word)//2):           # 합한 단어의 앞부분을 반복해서
                    if word[w] == word[len(word)-w-1]:  # 앞뒤가 같다면
                        pass                            # pass하고
                    else:                               # 다르다면
                        break                           # for문을 break한다
                else:                                   # 모든 단어가 같아 팰린드롬이라면
                    ans = word                          # ans에 정답을 저장한다
    else:                                               # 단어의 조합이 끝났다면
        if ans:                                         # ans에 저장된 단어가 있으면
            print(ans)                                  # 해당 단어를 출력하고
        else:                                           # 저장된 단어가 없다면
            print(0)                                    # 0을 출력한다