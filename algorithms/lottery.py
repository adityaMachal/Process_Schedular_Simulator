from utils.process import Process
import random
from collections import deque

def lottery_scheduling(processes):
    """
    Non-Preemptive Lottery Scheduling Algorithm (With User-Provided Tickets):
    - Each process has a user-specified number of tickets.
    - A random lottery selects the next process from the ready queue.
    - The selected process runs to completion without interruption.
    - Processes with more tickets have a higher chance of being selected.
    """
    # Sort processes by arrival time to process arrivals in order
    processes.sort(key=lambda p: p.arrival_time)
    time = 0
    timeline = []
    queue = deque()
    index = 0
    n = len(processes)

    # Use the user-provided ticket counts
    ticket_counts = {}
    for p in processes:
        if p.tickets is None or p.tickets < 1:
            raise ValueError(f"Process {p.pid} must have a positive number of tickets for Lottery Scheduling.")
        ticket_counts[p.pid] = p.tickets

    # Main scheduling loop
    while index < n or queue:
        # Add all processes that have arrived by the current time to the queue
        while index < n and processes[index].arrival_time <= time:
            queue.append(processes[index])
            index += 1

        # If queue is empty, CPU is idle until the next process arrives
        if not queue:
            if index < n:
                idle_time = processes[index].arrival_time - time
                timeline.append(("Idle", idle_time))
                time += idle_time
                continue
            else:
                break  # No more processes to schedule

        # Perform lottery to select the next process
        total_tickets = sum(ticket_counts[p.pid] for p in queue)
        winning_ticket = random.randint(0, total_tickets - 1)
        cumulative = 0
        winner = None
        for p in queue:
            tickets = ticket_counts[p.pid]
            cumulative += tickets
            if winning_ticket < cumulative:
                winner = p
                break

        # Remove the winner from the queue to execute it
        queue.remove(winner)

        # Set start and response time if this is the process's first execution
        if winner.start_time == -1:
            winner.start_time = time
            winner.response_time = time - winner.arrival_time

        # Run the process to completion (non-preemptive)
        exec_time = winner.remaining_time
        time += exec_time
        winner.remaining_time -= exec_time
        timeline.append((winner.pid, exec_time))

        # Update process metrics
        winner.completion_time = time
        winner.turnaround_time = winner.completion_time - winner.arrival_time
        winner.waiting_time = winner.turnaround_time - winner.burst_time

    return processes, timeline