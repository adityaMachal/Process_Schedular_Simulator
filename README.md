# Scheduling Algorithms Simulator

This project simulates various CPU scheduling algorithms, including FCFS, SJF, SRTF, RR, EDF, Priority Scheduling (both preemptive and non-preemptive), Lottery Scheduling, and Multilevel Queue (MLQ) Scheduling. It provides detailed performance metrics and a visually appealing Gantt chart to illustrate process execution.

## Features
- Supports 9 scheduling algorithms:
  - **FCFS**: First Come, First Serve
  - **SJF**: Shortest Job First (non-preemptive)
  - **SRTF**: Shortest Remaining Time First (preemptive)
  - **RR**: Round Robin
  - **EDF**: Earliest Deadline First
  - **PRIO**: Priority Scheduling (non-preemptive)
  - **PRIOP**: Priority Scheduling (preemptive)
  - **LOTTERY**: Lottery Scheduling (probabilistic, ticket-based)
  - **MLQ**: Multilevel Queue Scheduling (priority-based queues with configurable algorithms)
- Calculates key metrics: Turnaround Time, Waiting Time, Response Time, and Throughput
- Visualizes execution with a Gantt chart using Matplotlib and Seaborn for enhanced aesthetics

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/scheduling_algorithms.git
   cd scheduling_algorithms