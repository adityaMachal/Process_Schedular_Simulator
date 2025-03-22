from collections import deque
from utils.process import Process

def round_robin(processes, quantum=2):
    if quantum <= 0:
        print("Quantum must be greater than 0. Setting default to 2.")
        quantum = 2
    
    processes.sort(key=lambda p: p.arrival_time)
    time = 0
    timeline = []
    queue = deque()
    index = 0
    n = len(processes)
    
    while index < n or queue:
        if not queue and index < n:
            time = processes[index].arrival_time
            queue.append(processes[index])
            index += 1

        if queue:
            p = queue.popleft()
            
            if p.start_time == -1:
                p.start_time = time
                p.response_time = time - p.arrival_time

            exec_time = min(p.remaining_time, quantum)
            time += exec_time
            p.remaining_time -= exec_time
            timeline.append((p.pid, exec_time))

            while index < n and processes[index].arrival_time <= time:
                queue.append(processes[index])
                index += 1

            if p.remaining_time > 0:
                queue.append(p)
            else:
                p.completion_time = time
                p.turnaround_time = p.completion_time - p.arrival_time
                p.waiting_time = p.turnaround_time - p.burst_time

    return processes, timeline