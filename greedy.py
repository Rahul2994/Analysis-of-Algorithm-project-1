import random
import time
import matplotlib.pyplot as plt
from dataclasses import dataclass

@dataclass
class Surgery:
    id: str
    start: int
    end: int
    surgeon: str
    equipment: tuple = ()

def greedy_or_schedule(surgeries, R):
    surgeries_sorted = sorted(surgeries, key=lambda s: s.end)
    rooms = [{'last_end': -10**9, 'jobs': []} for _ in range(R)]
    surgeon_last_end = {}
    equipment_last_end = {}
    for s in surgeries_sorted:
        for r in range(R):
            if s.start >= rooms[r]['last_end']:
                sl = surgeon_last_end.get(s.surgeon, -10**9)
                if s.start >= sl:
                    ok = True
                    for eq in s.equipment:
                        if s.start < equipment_last_end.get(eq, -10**9):
                            ok = False
                            break
                    if not ok: continue
                    rooms[r]['jobs'].append(s)
                    rooms[r]['last_end'] = s.end
                    surgeon_last_end[s.surgeon] = s.end
                    for eq in s.equipment:
                        equipment_last_end[eq] = s.end
                    break
    return rooms

# ---------------------
# Experimental Running Time + Utilization + Scheduled Count
# ---------------------
sizes = [50, 100, 200, 400, 800]  # number of surgeries
R = 5  # number of rooms

times = []
scheduled_counts = []
room_utilizations = []

for N in sizes:
    # Generate random surgeries
    surgeries = []
    for i in range(N):
        start = random.randint(0, 20)
        end = start + random.randint(1, 4)
        surgeon = f"Dr.{random.randint(1,10)}"
        equipment = (f"E{random.randint(1,5)}",)
        surgeries.append(Surgery(f"S{i+1}", start, end, surgeon, equipment))
    
    # Measure running time
    t0 = time.time()
    rooms = greedy_or_schedule(surgeries, R)
    t1 = time.time()
    times.append(t1 - t0)
    
    # Total scheduled surgeries
    total_scheduled = sum(len(r['jobs']) for r in rooms)
    scheduled_counts.append(total_scheduled)
    
    # Room utilization: busy time / total possible time
    max_time = max((s.end for s in surgeries), default=0)
    total_busy = sum(sum(s.end - s.start for s in r['jobs']) for r in rooms)
    room_utilizations.append(total_busy / (R * max_time) if max_time > 0 else 0)

# ---------------------
# Plot Running Time
# ---------------------
plt.figure(figsize=(6,4))
plt.plot(sizes, times, marker='o', color='blue')
plt.xlabel("Number of Surgeries (N)")
plt.ylabel("Running Time (seconds)")
plt.title("Greedy OR Scheduling Algorithm Running Time")
plt.grid(True)
plt.tight_layout()
plt.savefig("greedy_running_time.png")
plt.show()

# ---------------------
# Plot Scheduled Surgeries
# ---------------------
plt.figure(figsize=(6,4))
plt.plot(sizes, scheduled_counts, marker='s', color='green')
plt.xlabel("Number of Surgeries (N)")
plt.ylabel("Scheduled Surgeries")
plt.title("Number of Surgeries Scheduled by Greedy Algorithm")
plt.grid(True)
plt.tight_layout()
plt.savefig("greedy_scheduled_count.png")
plt.show()

# ---------------------
# Plot Room Utilization
# ---------------------
plt.figure(figsize=(6,4))
plt.plot(sizes, room_utilizations, marker='^', color='red')
plt.xlabel("Number of Surgeries (N)")
plt.ylabel("Room Utilization")
plt.title("Room Utilization vs Number of Surgeries")
plt.grid(True)
plt.tight_layout()
plt.savefig("greedy_room_utilization.png")
plt.show()
