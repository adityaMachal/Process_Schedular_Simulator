import heapq
from utils.process import Process

def srtf(processes):
    processes.sort(key=lambda p: p.arrival_time)
    ready_queue = []
    timeline = []
    time, index, completed = 0, 0, 0

    while completed < len(processes):
        while index < len(processes) and processes[index].arrival_time <= time:
            heapq.heappush(ready_queue, (processes[index].remaining_time, processes[index].pid, processes[index]))
            index += 1

        if ready_queue:
            _, _, p = heapq.heappop(ready_queue)
            if p.start_time == -1:
                p.start_time = time
                p.response_time = time - p.arrival_time

            p.remaining_time -= 1
            timeline.append((p.pid, 1))
            time += 1

            if p.remaining_time > 0:
                heapq.heappush(ready_queue, (p.remaining_time, p.pid, p))
            else:
                p.completion_time = time
                p.turnaround_time = p.completion_time - p.arrival_time
                p.waiting_time = p.turnaround_time - p.burst_time
                completed += 1
        else:
            timeline.append(("Idle", 1))
            time += 1

    return processes, timeline
