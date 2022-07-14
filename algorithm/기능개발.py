import math

progresses = [93, 30, 55]
speeds = [1, 30, 5]
answer = []
    
while len(progresses) > 0:
    complete = 0
    need_p = 100 - progresses[0]
    need_d = math.ceil(need_p / speeds[0])
    for j in range(len(progresses)):
        progresses[j] = progresses[j] + speeds[j]*need_d
    while progresses[0] >= 100:
        progresses.pop(0)
        speeds.pop(0)
        complete += 1

    answer.append(complete)
print(answer)