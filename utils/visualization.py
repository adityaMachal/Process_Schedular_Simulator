import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def draw_gantt_chart(timeline):
    
    sns.set_style("whitegrid")  
    sns.set_context("notebook", font_scale=1.2) 

  
    plt.figure(figsize=(12, 3), dpi=100)

  
    palette = sns.color_palette("husl", 10) 
    colors = {}
    start = 0

    for pid, duration in timeline:
       
        if pid not in colors:
            if isinstance(pid, str) and pid.lower() == "idle":
                colors[pid] = sns.color_palette("Greys", 1)[0]  
            else:
              
                colors[pid] = palette[pid % len(palette)]

      
        plt.barh(y=0, width=duration, left=start, height=0.6, align='center',
                 color=colors[pid], edgecolor="black", linewidth=1.2)

    
        display_name = f"P{pid}" if isinstance(pid, int) else "Idle"
       
        luminance = 0.299 * colors[pid][0] + 0.587 * colors[pid][1] + 0.114 * colors[pid][2]
        text_color = 'white' if luminance < 0.5 else 'black'

        plt.text(start + duration / 2, 0, display_name, ha='center', va='center',
                 color=text_color, fontsize=10, fontweight='bold')

        start += duration

    
    plt.xlabel("Time", fontsize=12, labelpad=10)
    plt.ylabel("Processes", fontsize=12, labelpad=10)
    plt.title("Gantt Chart", fontsize=14, pad=15)

   
    plt.xticks(range(start + 1), fontsize=10)
    plt.yticks([])  

    
    plt.grid(True, axis='x', linestyle='--', alpha=0.7)

  
    plt.tight_layout()

  
    plt.show()