import matplotlib.pyplot as plt
import numpy as np

def draw_gantt_chart(timeline):
    plt.figure(figsize=(10, 2))
    colors = {}
    start = 0

    for pid, duration in timeline:
        if pid not in colors:
            if isinstance(pid, str) and pid.lower() == "idle":
                colors[pid] = np.array([0.5, 0.5, 0.5])  # Gray for Idle
            else:
                colors[pid] = np.random.rand(3,)  # Random color for processes

        plt.barh(0, duration, left=start, height=0.5, align='center',
                 color=colors[pid], edgecolor="black")

        text_color = 'black' if np.array_equal(colors[pid], np.array([0.5, 0.5, 0.5])) else 'white'
        display_name = f"P{pid}" if isinstance(pid, int) else "Idle"

        plt.text(start + duration / 2, 0, display_name, ha='center', va='center',
                 color=text_color, fontsize=10, fontweight='bold')

        start += duration

    plt.xlabel("Time")
    plt.ylabel("Processes")
    plt.title("Gantt Chart")
    plt.xticks(range(start + 1))
    plt.show()