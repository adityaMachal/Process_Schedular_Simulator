from .prio import priority_scheduling

def preemptive_priority_scheduling(processes):
    return priority_scheduling(processes, preemptive=True)