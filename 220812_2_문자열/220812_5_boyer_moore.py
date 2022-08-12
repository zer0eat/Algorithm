# Boyer moore
# T : target / P : pattern

def pre_process(P):

    M = len(P)

    # skip 배열 대신 딕셔너리
    PI = dict()

    # (M - i - 1)만큼 스킵하지만
    # 마지막 index를 제외한 이유 : 마지막 index가 matching이 되었는데 실패했으면 M만큼 skip해야 하기 때문(즉, 포함되지 않은 char랑 같은 취급)
    # 여기서 사용하지 않는 문자들은 .get method의 default값 사용
    for i in range(M-1):
        PI[P[i]] = M - (1 + i)
    return PI


def boyer_moore(T, P):
    PI = pre_process(P)

    M = len(P)

    # text 순회에 대한 index
    i = 0

    while i <= len(T) - M:
        # skip 잘 되고있나 확인
        # print(i)

        #
        # M번째 인덱스
        j = M - 1
        # 비교를 시작할 위치 (현재위치 + M번째 인덱스)
        k = (i) + (M - 1)

        # 비교할 j가 남아있고, text와 pattern이 같으면 1씩 줄여 비교
        while j >= 0 and P[j] == T[k]:
            j -= 1
            k -= 1

        # 비교 성공
        if j == -1:
            pos = i
            return pos

        # i를 비교를 시작할 위치 (초반의 k)에 해당하는 문자( T[i + M - 1] )
        # 해당 문자의 skip 테이블의 크기( PI[T[i + M - 1]] )만큼 스킵

        i += PI.get(T[i + M - 1], M)

		# 실패할 경우 -1 반환
    return -1