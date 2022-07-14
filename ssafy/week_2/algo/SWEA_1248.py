'''
문제링크:
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15PTkqAPYCFAYD&categoryId=AV15PTkqAPYCFAYD&categoryType=CODE&problemTitle=1248&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1




'''

T = int(input())
for t in range(T):
    N, _, A, B = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    tri_map = {}
    for i in range(0,len(nums),2):
        if nums[i] not in list(tri_map.keys()):
            tri_map[nums[i]] = [nums[i+1]]
        else:
            tri_map[nums[i]].append(nums[i+1])
    tri_list = list(tri_map.items())
    top_A = set()
    top_B = set()
    while True:
        for k, v in tri_list:
            if A in v:
                top_A.add(k)
                A = k
            if B in v:
                top_B.add(k)
                B = k
        if top_B & top_A:
            break
    top_t = list(top_A & top_B)
    top = max(top_A & top_B)
    sub_tris = 1
    for _ in range(N):
        for k, v in tri_list:
            if k in top_t:
                sub_tris += len(v)
                top_t.remove(k)
                top_t.extend(v)
    print(f'#{t+1} {top} {sub_tris}')



    

