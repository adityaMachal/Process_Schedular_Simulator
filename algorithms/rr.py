from collections import deque
from utils.process import Process  # Assuming a Process class exists

def round_robin(processes, quantum=2):
    # Ensure quantum is valid
    if quantum <= 0:
        print("Quantum must be greater than 0. Setting default to 2.")
        quantum = 2
    
    # Sort processes by arrival time
    processes.sort(key=lambda p: p.arrival_time)
    
    time = 0  # Current time
    timeline = []  # Gantt chart timeline
    queue = deque()  # Queue for ready processes
    index = 0  # Index to track unprocessed processes
    n = len(processes)
    
    while index < n or queue:
        # Add all processes that have arrived by the current time
        while index < n and processes[index].arrival_time <= time:
            queue.append(processes[index])
            index += 1
        
        # If queue is empty but processes remain, CPU is idle
        if not queue and index < n:
            next_arrival = processes[index].arrival_time
            idle_time = next_arrival - time
            timeline.append(("Idle", idle_time))
            time = next_arrival
            continue
        
        # If no more processes and queue is empty, exit
        if not queue:
            break
        
        # Process the next process in the queue
        p = queue.popleft()
        
        # Set start and response time if this is the first execution
        if p.start_time == -1:
            p.start_time = time
            p.response_time = time - p.arrival_time

        # Execute for quantum or remaining time, whichever is smaller
        exec_time = min(p.remaining_time, quantum)
        time += exec_time
        p.remaining_time -= exec_time
        timeline.append((p.pid, exec_time))
        
        # Add any new processes that arrived during execution
        while index < n and processes[index].arrival_time <= time:
            queue.append(processes[index])
            index += 1
        
        # If process isn't finished, put it back in the queue
        if p.remaining_time > 0:
            queue.append(p)
        else:
            # Process is complete, calculate metrics
            p.completion_time = time
            p.turnaround_time = p.completion_time - p.arrival_time
            p.waiting_time = p.turnaround_time - p.burst_time

    return processes, timeline