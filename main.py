from utils.process import Process
from utils.metrics import print_algorithm_info, calculate_metrics
from utils.visualization import draw_gantt_chart
from algorithms.fcfs import fcfs
from algorithms.prio import priority_scheduling
from algorithms.rr import round_robin
from algorithms.edf import earliest_deadline_first
from algorithms.srtf import srtf
def get_processes(priority=False, edf=False):
    processes = []
    n = int(input("Enter the number of processes: "))

    for i in range(1, n + 1):
        at = int(input(f"Enter Arrival Time for Process {i} (default 0): ") or 0)
        bt = int(input(f"Enter Burst Time for Process {i}: "))
        
        priority_val = None
        if priority:
            priority_val = int(input(f"Enter Priority for Process {i} (lower is higher priority): "))

        deadline = None
        if edf:
            deadline = int(input(f"Enter Deadline for Process {i}: "))

        processes.append(Process(i, at, bt, priority_val, deadline))
    
    return processes

def main():
    algo = input("Choose Scheduling Algorithm (FCFS, SJF, SRTF, RR, EDF, PRIO, PRIOP): ").strip().upper()

    if algo == "EDF":
        processes = get_processes(edf=True)
    elif algo in ["PRIO", "PRIOP"]:
        processes = get_processes(priority=True)
    else:
        processes = get_processes()

    print_algorithm_info(algo)

    if algo == "FCFS":
        result, timeline = fcfs(processes)
    elif algo == "SJF":
        result, timeline = sjf(processes)
    elif algo == "SRTF":
        result, timeline = srtf(processes)
    elif algo == "RR":
        quantum = int(input("Enter time quantum: "))
        result, timeline = round_robin(processes, quantum)
    elif algo == "EDF":
        result, timeline = earliest_deadline_first(processes)
    elif algo == "PRIO":
        result, timeline = priority_scheduling(processes, preemptive=False)
    elif algo == "PRIOP":
        result, timeline = preemptive_priority_scheduling(processes)
    else:
        print("Invalid choice!")
        return

    calculate_metrics(result, timeline)
    draw_gantt_chart(timeline)

if __name__ == "__main__":
    main()