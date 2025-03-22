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

    # Sort processes by arrival time to handle arrivals correctly
    processes.sort(key=lambda p: p.arrival_time)
    time = 0
    timeline = []
    queue = deque()
    index = 0
    n = len(processes)

    # Assign tickets based on priority (higher priority = lower number = more tickets)
    # If no priority is provided, assume equal tickets (e.g., 100 tickets each)
    total_tickets = 0
    ticket_mapping = {}
    for p in processes:
        tickets = p.priority if p.priority is not None else 100  # Default 100 tickets if no priority
        tickets = max(1, 1000 - tickets * 100)  # Convert priority to tickets (lower priority value = more tickets)
        ticket_mapping[p.pid] = (total_tickets, total_tickets + tickets - 1)  # Range of tickets for this process
        total_tickets += tickets

    while index < n or queue:
        # Add arriving processes to the queue
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
                break  # No more processes to schedule

        # Perform the lottery: pick a random ticket
        winning_ticket = random.randint(0, total_tickets - 1)
        winner = None
        for p in queue:
            start, end = ticket_mapping[p.pid]
            if start <= winning_ticket <= end:
                winner = p
                break

        # Remove the winner from the queue to process it
        queue.remove(winner)

        if winner.start_time == -1:
            winner.start_time = time
            winner.response_time = time - winner.arrival_time

        # Execute for quantum or remaining time, whichever is smaller
        exec_time = min(winner.remaining_time, quantum)
        time += exec_time
        winner.remaining_time -= exec_time
        timeline.append((winner.pid, exec_time))

        # Add back to queue if not finished
        if winner.remaining_time > 0:
            queue.append(winner)
        else:
            winner.completion_time = time
            winner.turnaround_time = winner.completion_time - winner.arrival_time
            winner.waiting_time = winner.turnaround_time - winner.burst_time

    return processes, timeline