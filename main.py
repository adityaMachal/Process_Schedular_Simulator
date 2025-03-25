from utils.process import Process
from utils.metrics import print_algorithm_info, calculate_metrics
from utils.visualization import draw_gantt_chart
from algorithms.fcfs import fcfs
from algorithms.sjf import sjf
from algorithms.srtf import srtf
from algorithms.rr import round_robin
from algorithms.edf import earliest_deadline_first
from algorithms.prio import priority_scheduling
from algorithms.priop import preemptive_priority_scheduling
from algorithms.lottery import lottery_scheduling

def get_processes(priority=False, edf=False, tickets=False):
    processes = []
    n = int(input("Enter the number of processes: "))

    for i in range(1, n + 1):
        at = int(input(f"Enter Arrival Time for Process {i} (default 0): ") or 0)
        bt = int(input(f"Enter Burst Time for Process {i}: "))
        
        priority_val = None
        if priority:
            priority_val = int(input(f"Enter Priority for Process {i} (lower is higher priority, press Enter to skip for Lottery): ") or None)

        deadline = None
        if edf:
            deadline = int(input(f"Enter Deadline for Process {i}: "))

        tickets_val = None
        if tickets:
            tickets_val = int(input(f"Enter number of tickets for Process {i}: "))

        processes.append(Process(i, at, bt, priority_val, deadline, tickets_val))
    
    return processes

def main():
    algo = input("Choose Scheduling Algorithm (FCFS, SJF, SRTF, RR, EDF, PRIO, PRIOP, LOTTERY): ").strip().upper()

    if algo == "EDF":
        processes = get_processes(edf=True)
    elif algo in ["PRIO", "PRIOP"]:
        processes = get_processes(priority=True)
    elif algo == "LOTTERY":
        processes = get_processes(tickets=True)
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
    elif algo == "LOTTERY":
        result, timeline = lottery_scheduling(processes)
    else:
        print("Invalid choice!")
        return

    calculate_metrics(result, timeline, algo)

   
    print("\nTimeline before drawing Gantt chart:", timeline)

  
    try:
        if timeline: 
            draw_gantt_chart(timeline)
        else:
            print("Cannot draw Gantt chart: Timeline is empty.")
    except Exception as e:
        print(f"Error drawing Gantt chart: {e}")

if __name__ == "__main__":
    main()