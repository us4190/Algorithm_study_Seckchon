import math

def solution(n, stations, w):
    prev = 1
    disConnected = []
    for station in stations:
        front = station - w
        if front > prev:
            disConnected.append([prev, front-1])
        prev = station + w + 1
    if prev <= n:
        disConnected.append([prev, n])
    
    count = 0
    for section in disConnected:
        length = section[1] - section[0] + 1
        count += math.ceil(length / (1 + 2*w))
        
    return count