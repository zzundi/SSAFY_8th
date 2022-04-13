t = int(input())
for _ in range(t):
    N, M = map(int, input().split())
    books = [False] * N
    requests = []
    for i in range(M):
        requests.append(list(map(int, input().split())))
    requests.sort(key=lambda x: x[1])
    cnt = 0
    while requests:
        a, b = requests.pop(0)
        for i in range(a-1, b):
            if not books[i]:
                cnt += 1
                books[i] = True
                break
    print(cnt)