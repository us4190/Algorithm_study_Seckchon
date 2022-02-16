class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_dict = {}
        n_car = len(position)
        for i in range(n_car):
            car_dict[position[i]] = speed[i]
        position.sort(reverse=True)
        
        count = n_car
        for i in range(n_car):
            if self.isFleet(position, car_dict, target, i):
                count -= 1
        return count
            
        
    def isFleet(self, position, car_dict, target, i):
        if i == 0:
            return False
        p1 = position[i]
        p2 = position[i-1]
        dist1 = target - p1
        dist2 = target - p2
        v1 = car_dict[p1]
        v2 = car_dict[p2]
        if dist1/v1 <= dist2/v2:
            position[i] = position[i-1]
            return True
        return False
        