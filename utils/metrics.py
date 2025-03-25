from tabulate import tabulate

def print_algorithm_info(algo):
    descriptions = {
        "FCFS": "First Come, First Serve (FCFS) executes processes in order of arrival.",
        "SJF": "Shortest Job First (SJF) selects the process with the smallest burst time first.",
        "SRTF": "Shortest Remaining Time First (SRTF) is a preemptive version of SJF.",
        "RR": "Round Robin (RR) gives each process a fixed time slice (quantum).",
        "EDF": "Earliest Deadline First (EDF) prioritizes processes with the closest deadlines.",
        "PRIO": "Priority Scheduling (Non-Preemptive) runs the highest priority available process.",
        "PRIOP": "Priority Scheduling (Preemptive) allows priority-based preemption.",
        "LOTTERY": "Non-Preemptive Lottery Scheduling uses user-provided tickets for each process; a random draw determines which process runs to completion."
    }
    print("\n" + "="*40)
    print(f"  {algo} Scheduling Algorithm")
    print("="*40)
    print(descriptions.get(algo, "Invalid Algorithm"))
    print("="*40 + "\n")

def print_process_table(processes, algo=""):
   
    sorted_processes = sorted(processes, key=lambda p: p.pid)
    
   
    if algo == "LOTTERY":
       
        table = [[
            p.pid, p.arrival_time, p.burst_time, p.tickets,
            p.completion_time, p.turnaround_time, p.waiting_time, p.response_time
        ] for p in sorted_processes]
        headers = ["PID", "AT", "BT", "Tickets", "CT", "TAT", "WT", "RT"]
    else:
    
        table = [[
            p.pid, p.arrival_time, p.burst_time, p.priority if p.priority is not None else "-",
            p.completion_time, p.turnaround_time, p.waiting_time, p.response_time
        ] for p in sorted_processes]
        headers = ["PID", "AT", "BT", "Priority", "CT", "TAT", "WT", "RT"]

    print("\nProcess Details:\n")
    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))

def calculate_metrics(processes, timeline, algo=""):
    print_process_table(processes, algo)
    
    avg_tat = sum(p.turnaround_time for p in processes) / len(processes)
    avg_wt = sum(p.waiting_time for p in processes) / len(processes)
    avg_rt = sum(p.response_time for p in processes) / len(processes)
    throughput = len(processes) / max(p.completion_time for p in processes)

    print("\n" + "="*30)
    print(f"Metrics Summary")
    print("="*30)
    print(f"Average Turnaround Time  : {avg_tat:.2f}")
    print(f"Average Waiting Time     : {avg_wt:.2f}")
    print(f"Average Response Time    : {avg_rt:.2f}")
    print(f"Throughput               : {throughput:.2f} processes/unit time")
    print("="*30 + "\n")