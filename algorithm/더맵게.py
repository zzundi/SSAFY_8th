from collections import deque

def solution(scoville, K):
    cnt = 0
    scoville = deque(scoville.sort())
    n_s = deque([])
    while True:
        if len(n_s) >= 2:
            if scoville[1] < n_s[0]:
                m1 = scoville.popleft()
                m2 = scoville.popleft()
            elif scoville[1] > n_s[0] and scoville[0] < n_s[0]:
                m1 = scoville.popleft()
                m2 = n_s.popleft()
            elif scoville[1] > n_s[0] and scoville[0] > n_s[0] and scoville[0] < n_s[1]:
                m1 = n_s.popleft()
                m2 = scoville.popleft()
            else:
                m1 = n_s.popleft()
                m2 = n_s.popleft()
        elif len(n_s) == 1:
            if scoville[1] < n_s[0]:
                m1 = scoville.popleft()
                m2 = scoville.popleft()
            elif scoville[1] > n_s[0] and scoville[0] < n_s[0]:
                m1 = scoville.popleft()
                m2 = n_s.popleft()
            else:
                m1 = n_s.popleft()
                m2 = scoville.popleft()
        else:
            m1 = scoville.popleft()
            m2 = scoville.popleft()
            
        if m1 >= K:
            break
        if m1+m2*2 < K:
            n_s.append(m1+m2*2)
        cnt +=1
        if len(scoville) < 2:
            if scoville[0] < K:
                cnt = -1
            break
    return cnt

solution([1,2,3,9,10,12], 7)