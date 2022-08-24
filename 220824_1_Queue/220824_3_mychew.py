def mychew(N):
    mc = N
    people = 0
    while mc > 0:
        people += 1
        mc = mc - people
    return people + mc

print(mychew(1000000))

