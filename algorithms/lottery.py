from utils.process import Process
import random
from collections import deque

def lottery_scheduling(processes, quantum=2):
    """
    Lottery Scheduling Algorithm:
    - Each process is assigned a number of tickets based on priority (higher priority = more tickets).
    - A random lottery determines which process runs next for a fixed quantum.
    - Processes with more tickets have a higher chance of being selected.
    """
    if quantum <= 0:
        print("Quantum must be greater than 0. Setting default to 2.")
        quantum = 2

    
    processes.sort(key=lambda p: p.arrival_time)
    time = 0
    timeline = []
    queue = deque()
    index = 0
    n = len(processes)

    
    total_tickets = 0
    ticket_mapping = {}
    for p in processes:
        tickets = p.priority if p.priority is not None else 100  
        tickets = max(1, 1000 - tickets * 100) 
        ticket_mapping[p.pid] = (total_tickets, total_tickets + tickets - 1) 
        total_tickets += tickets

    while index < n or queue:
        
        while index < n and processes[index].arrival_time <= time:
            queue.append(processes[index])
            index += 1

        if not queue:
            if index < n:
                idle_time = processes[index].arrival_time - time
                timeline.append(("Idle", idle_time))
                time += idle_time
                continue
            else:
                break  
        winning_ticket = random.randint(0, total_tickets - 1)
        winner = None
        for p in queue:
            start, end = ticket_mapping[p.pid]
            if start <= winning_ticket <= end:
                winner = p
                break

        queue.remove(winner)

        if winner.start_time == -1:
            winner.start_time = time
            winner.response_time = time - winner.arrival_time

        
        exec_time = min(winner.remaining_time, quantum)
        time += exec_time
        winner.remaining_time -= exec_time
        timeline.append((winner.pid, exec_time))

        if winner.remaining_time > 0:
            queue.append(winner)
        else:
            winner.completion_time = time
            winner.turnaround_time = winner.completion_time - winner.arrival_time
            winner.waiting_time = winner.turnaround_time - winner.burst_time

    return processes, timeline