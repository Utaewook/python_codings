from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    if not cacheSize:
        return len(cities)*5

    for city in cities:
        city = str.lower(city)
        if city in cache:
            cache.remove(city)
            if len(cache) == cacheSize:
                cache.popleft()
            cache.append(city)
            answer += 1
        else:
            if len(cache) == cacheSize:
                cache.popleft()
            cache.append(city)
            answer += 5

    return answer