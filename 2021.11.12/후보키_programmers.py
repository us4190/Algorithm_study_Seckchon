from itertools import combinations

def solution(relation):
    idxList = [i for i in range(1,len(relation[0])+1)]
    size = len(relation)
    keyList = []
    
    one_count = 0
    removeList = []
    for i in idxList:
        col = [x[i-1] for x in relation]
        col_set = set(col)
        if len(col_set) == size:
            one_count += 1
            removeList.append(i)
            
    for i in removeList:
        idxList.remove(i)
    
    def helper(keySize):
        if keySize > len(idxList):
            return 0
        count = 0
        candidates = list(combinations(idxList, keySize))
        for cand in candidates:
            count_set = set()
            for r in range(len(relation)):
                new_key = tuple([])
                for c in cand:
                    new_key += tuple([relation[r][c-1]])
                count_set.add(new_key)
            if len(count_set) == size:
                isContain = False
                for key in keyList:
                    if aContainB(cand, key):
                        isContain = True
                if not isContain:
                    count += 1
                    keyList.append(cand)
        return count + helper(keySize+1)
        
    return helper(2) + one_count

def aContainB(a, b):
    isContain = True
    for i in b:
        if i not in a:
            return False
    return True