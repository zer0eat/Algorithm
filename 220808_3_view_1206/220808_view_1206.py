# view_1206

# input.txt 받기
import sys
sys.stdin = open('input.txt')

#input.txt를 리스트로 저장하기
N = 10
for i in range(10):
    t = int(input())
    lst = list(map(int, input().split()))

    # 조망권 확인하기
    cnt = 0 # 조망권이 확보된 층 수
    for height in range(2,t-2):
        e = []
        if lst[height] - lst[height-2] > 0:
            e.append(lst[height] - lst[height-2])
            if lst[height] - lst[height-1] > 0:
                e.append(lst[height] - lst[height - 1])
                if lst[height] - lst[height + 1] > 0:
                    e.append(lst[height] - lst[height + 1])
                    if lst[height] - lst[height + 2] > 0:
                        e.append(lst[height] - lst[height + 2])
                        a = 255
                        for b in e:
                            if a > b:
                                a = b
                            else:
                                pass
                        cnt += a
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            pass
    print(f'#{i+1} {cnt}')


