from utils.process import Process

def fcfs(processes):
    processes.sort(key=lambda p: p.arrival_time)
    time = 0
    timeline = []

    for p in processes:
        if time < p.arrival_time:
            timeline.append(("Idle", p.arrival_time - time))
            time = p.arrival_time

        p.start_time = time
        p.response_time = time - p.arrival_time
        time += p.burst_time
        p.completion_time = time
        p.turnaround_time = p.completion_time - p.arrival_time
        p.waiting_time = p.turnaround_time - p.burst_time
        timeline.append((p.pid, p.burst_time))

    return processes, timeline