s, N, K, r1, r2, c1, c2 = map(int, input().split())
practal_map = [[0] * (c2-c1+1) for _ in range(r2-r1+1)]


def query(r,c,s,x,y):
    if s==0:
        return None
    if   N**(s-1)*(N-K)//2 <= r < N**s - N**(s-1)*(N-K)//2 and N**(s-1)*(N-K)//2 <= c < N**s - N**(s-1)*(N-K)//2:
        practal_map[x-r1][y-c1] = 1
        return None
    else:
        query(r%(N**(s-1)),c%(N**(s-1)),s-1,x,y)

for x in range(r1,r2+1):
    for y in range(c1,c2+1):
        query(x,y,s,x,y)

print('\n'.join(''.join(str(x) for x in y)for y in practal_map))