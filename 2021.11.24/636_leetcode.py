class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        new_logs = []
        answer = [0] * n
        for log in logs:
            new_log = log.split(':')
            new_log[0] = int(new_log[0])
            new_log[2] = int(new_log[2])
            new_logs.append(new_log)
        
        prev_time = 0
        for log in new_logs:
            curr_func, s, curr_time = log
            if not stack:
                stack.append([curr_func, 0])
                prev_time = curr_time
            
            if s == "start":
                stack[-1][1] += curr_time - prev_time
                stack.append([curr_func, 0])
                prev_time = curr_time
            else:
                ended_func, ended_time = stack.pop()
                ended_time += curr_time - prev_time + 1
                prev_time = curr_time + 1
                answer[ended_func] += ended_time
                
        return answer
                