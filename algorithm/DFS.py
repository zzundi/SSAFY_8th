graph = dict()
 
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']


def dfs(graph, start_node):

    ## 기본은 항상 두개의 리스트를 별도로 관리해주는것
    need_visited, visited = list(), list()

    ## 시작 노드 설정하기
    need_visited.append(start_node)

    ## 만약 아직 방문이 필요한 노드가 있다면
    while need_visited:

        ## 그 중에서 가장 마지막 데이터를 추출(스택 구조 활용)
        node = need_visited.pop()

        ## 만약 그 노드가 방문한 목록에 없다면
        if node not in visited:

            ##  방문한 목록에 추가하기
            visited.append(node)

            ## 그 노드에 연결된 노드를
            need_visited.extend(graph[node])
    return visited

def dfs_recursive(graph, start, visited = []):
   
    ## 데이터를 추가하는 명령어 / 재귀 실시!
    visited.append(start)

    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node, visited)
    return visited


n = int(input())
map_list = {}
for i in range(n):
    row_list = []
    row_list.append(list(map(int, input())))
    for j in range(n):
        map_list[(i, j)] = row_list[j]

print(map_list)

