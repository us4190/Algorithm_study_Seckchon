import collections

class Solution:    
    def customSortString(self, order: str, s: str) -> str:
        order_dict = collections.defaultdict(int)
        
        for i in range(len(order)):
            order_dict[order[i]] = i+1
        
        s_list = list(s)
        s_list.sort(key = lambda x : order_dict[x])
        return ''.join(s_list)
        