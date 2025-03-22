import heapq
from utils.process import Process

def priority_scheduling(processes, preemptive=False):
    processes.sort(key=lambda p: p.arrival_time)
    ready_queue = []
    timeline = []
    time, index, completed = 0, 0, 0

    while completed < len(processes):
        while index < len(processes) and processes[index].arrival_time <= time:
            heapq.heappush(ready_queue, (processes[index].priority, processes[index].pid, processes[index]))
            index += 1

        if ready_queue:
            _, _, p = heapq.heappop(ready_queue)

            if p.start_time == -1:
                p.start_time = time
                p.response_time = time - p.arrival_time

            if preemptive:
                time += 1
                p.remaining_time -= 1
                timeline.append((p.pid, 1))

                if p.remaining_time > 0:
                    heapq.heappush(ready_queue, (p.priority, p.pid, p))
                else:
                    p.completion_time = time
                    p.turnaround_time = p.completion_time - p.arrival_time
                    p.waiting_time = p.turnaround_time - p.burst_time
                    completed += 1
            else:
                time += p.burst_time
                p.completion_time = time
                p.turnaround_time = p.completion_time - p.arrival_time
                p.waiting_time = p.turnaround_time - p.burst_time
                timeline.append((p.pid, p.burst_time))
                completed += 1
        else:
            timeline.append(("Idle", 1))
            time += 1

    return processes, timeline