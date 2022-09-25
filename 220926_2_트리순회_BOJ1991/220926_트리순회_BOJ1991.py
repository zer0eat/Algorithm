# 트리순회_BOJ1991

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# 전위 순회를 위한 함수
def preorder(A):
    global ans1
    if A != '':                                         # ''이 아닐때
        ans1 += num_str[A]                              # ans1에 A에 해당하는 알파벳을 넣고
        preorder(ch1[A])                                # 왼쪽 자식을 탐색하고
        preorder(ch2[A])                                # 오른쪽 자식을 탐색한다

# 중위 순회를 위한 함수
def inorder(A):
    global ans2
    if A != '':                                         # ''이 아닐때
        inorder(ch1[A])                                 # 왼쪽 자식을 탐색하고
        ans2 += num_str[A]                              # ans2에 A에 해당하는 알파벳을 넣고
        inorder(ch2[A])                                 # 오른쪽 자식을 탐색한다

# 후위 순회를 위한 함수
def postorder(A):
    global ans3
    if A != '':                                         # ''이 아닐때
        postorder(ch1[A])                               # 왼쪽 자식을 탐색하고
        postorder(ch2[A])                               # 오른쪽 자식을 탐색하고
        ans3 += num_str[A]                              # ans3에 A에 해당하는 알파벳을 넣는다

# input 받기
N = int(input())                                        # 이진트리의 노드의 개수

# 알파벳에 대응하는 숫자와 반대의 딕셔너리 생성
str_num = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25}
num_str = {v:k for k,v in str_num.items()}

ch1 = [''] * (N + 1)                                    # 왼쪽 자식의 인덱스를 저장할 리스트를 만들고
ch2 = [''] * (N + 1)                                    # 오른쪽 자식의 인덱스를 저장할 리스트를 만든다

for n in range(N):                                      # 노드의 숫자만큼 반복 했을 때
    a, b, c = input().split()                           # a는 부모노드 b는 왼쪽자식노드 c는 오른쪽자식노드이다
    if b != '.':                                        # b가 ''이 아닐때
        ch1[str_num[a]] = str_num[b]                    # ch1에 인덱스가 a인 요소에 b를 저장한다
    if c != '.':                                        # c가 ''이 아닐때
        ch2[str_num[a]] = str_num[c]                    # ch2에 인덱스가 a인 요소에 c를 저장한다

ans1 = ''                                               # 전위순회의 답을 저장할 변수
ans2 = ''                                               # 중위순회의 답을 저장할 변수
ans3 = ''                                               # 후위순회의 답을 저장할 변수

preorder(0)                                             # 전위순회를 A부터 시작한다
inorder(0)                                              # 중위순회를 A부터 시작한다
postorder(0)                                            # 후위순회를 A부터 시작한다

print(ans1)
print(ans2)
print(ans3)