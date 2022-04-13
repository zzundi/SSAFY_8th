n = int(input())
coins_row = [input() for _ in range(n)]
coins_col = ['a'*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        coins_col[i][j] = coins_row[j][i]
print(coins_col)
print(coins_row)
# row_max = 0
# row_max_idx = 0
# col_max = 0
# col_max_idx = 0
# for i in range(n):
#     if coins_row[i].count('T') > row_max:
#         row_max = coins_row[i].count('T')
#         row_max_idx = i
#     if coins_col[i].count('T') > col_max:
#         col_max = coins_col[i].count('T')
#         col_max_idx = i
# if col_max > row_max:
#     coins_col[col_max_idx].