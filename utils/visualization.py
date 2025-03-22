import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def draw_gantt_chart(timeline):
    # Set Seaborn style for better aesthetics
    sns.set_style("whitegrid")  # Use a clean white grid background
    sns.set_context("notebook", font_scale=1.2)  # Adjust font size for readability

    # Create a figure with a larger size for better visibility
    plt.figure(figsize=(12, 3), dpi=100)

    # Define a color palette using Seaborn
    palette = sns.color_palette("husl", 10)  # Use the 'husl' palette for distinct, vibrant colors
    colors = {}
    start = 0

    for pid, duration in timeline:
        # Assign colors: "Idle" gets gray, processes get a color from the palette
        if pid not in colors:
            if isinstance(pid, str) and pid.lower() == "idle":
                colors[pid] = sns.color_palette("Greys", 1)[0]  # Gray for Idle
            else:
                # Cycle through the palette for processes
                colors[pid] = palette[pid % len(palette)]

        # Draw the bar for the process
        plt.barh(y=0, width=duration, left=start, height=0.6, align='center',
                 color=colors[pid], edgecolor="black", linewidth=1.2)

        # Add text label in the center of the bar
        display_name = f"P{pid}" if isinstance(pid, int) else "Idle"
        # Determine text color based on luminance of the bar color for readability
        luminance = 0.299 * colors[pid][0] + 0.587 * colors[pid][1] + 0.114 * colors[pid][2]
        text_color = 'white' if luminance < 0.5 else 'black'

        plt.text(start + duration / 2, 0, display_name, ha='center', va='center',
                 color=text_color, fontsize=10, fontweight='bold')

        start += duration

    # Customize the plot
    plt.xlabel("Time", fontsize=12, labelpad=10)
    plt.ylabel("Processes", fontsize=12, labelpad=10)
    plt.title("Gantt Chart", fontsize=14, pad=15)

    # Set x-axis ticks to show time progression
    plt.xticks(range(start + 1), fontsize=10)
    plt.yticks([])  # Hide y-axis ticks since we only have one row

    # Add a grid for better readability
    plt.grid(True, axis='x', linestyle='--', alpha=0.7)

    # Adjust layout to prevent clipping
    plt.tight_layout()

    # Show the plot
    plt.show()