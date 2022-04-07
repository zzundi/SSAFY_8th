hw = {}
p_hw = {}
score = 0
N = int(input())
for i in range(N):
    d, w = map(int, input().split())
    if d in hw.keys():
        hw[d].append(w)
    else:
        hw[d] = [w]
days = [max(hw.keys()) - i for i in range(max(hw.keys()))]
for i in days:
    if i+1 in days and i in hw.keys():
        p_hw[i] = hw[i] + p_hw[i+1]
    elif i+1 in days:
        p_hw[i] = p_hw[i+1]
    elif i in hw.keys():
        p_hw[i] = hw[i]
    if p_hw[i]:
        score += max(p_hw[i])
        p_hw[i].remove(max(p_hw[i]))
print(score)