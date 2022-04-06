from collections import defaultdict
N, M, K = list(map(int, input().split()))
land = [[5 for _ in range(N)] for _ in range(N)]
land_refill = [list(map(int, input().split())) for _ in range(N)]
trees = [list(map(int, input().split())) for _ in range(M)]
trees_map = defaultdict(list)
trees_map.keys()
dx = [-1, -1, -1, 0,  0, 1, 1, 1]
dy = [-1, 0, 1, -1,  1, -1, 0, 1]

for i in range(len(trees)):
    if (trees[i][0], trees[i][1]) in trees_map.keys():
        trees_map[(trees[i][0], trees[i][1])].append(trees[i][2])
    else:
        trees_map[(trees[i][0], trees[i][1])] = [trees[i][2]]
trees_map

for i in range(K):
    trees_map_key = list(trees_map.keys())
    trees_map_values = list(trees_map.values())
    dead_trees = []
    for j in range(len(trees_map)):
        trees_map[trees_map_key[j]].sort()

        for k in range(len(trees_map[trees_map_key[j]])):

            if land[trees_map_key[j][0]-1][trees_map_key[j][1]-1] >= trees_map[trees_map_key[j]][k]:
                land[trees_map_key[j][0]-1][trees_map_key[j][1]-1] -= trees_map[trees_map_key[j]][k]
                trees_map[trees_map_key[j]][k] += 1
            else:
                dead_trees.append([trees_map_key[j][0], trees_map_key[j][1], trees_map[trees_map_key[j]][k:]])
                trees_map[trees_map_key[j]] = trees_map[trees_map_key[j]][:k]
    for j in range(len(dead_trees)):
        land[dead_trees[j][0]][dead_trees[j][1]] += sum(dead_trees[j][2]//2)

    trees_map_key = list(trees_map.keys())
    trees_map_values = list(trees_map.values())
    for j in range(len(trees_map)):
        for k in range(len(trees_map[trees_map_key[j]])):
            if trees_map_values[k][0] % 5 == 0:
                for _ in range(8):
                    nx = trees_map_key[k][0] + dx[_]
                    ny = trees_map_key[k][1] + dy[_]
                    if 1 > nx or N < nx or 1 > ny or N < ny: continue
                    trees_map[nx,ny].append(1) 
                    
    for j in range(N):
        for k in range(N):
            land[j][k] += land_refill[j][k]
    print('#'*10)
    print(land)
    print('#'*10)

tree_cnt = 0    
for i in range(len(trees_map)):
    tree_cnt += len(list(trees_map.values())[i])

print(tree_cnt, trees_map)