import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

os.makedirs("graphs", exist_ok=True)
plt.rcParams.update({"figure.facecolor": "white", "font.size": 10.5})

# --- Graph 1: Edge vs Cloud Cluster Placement Diagram ---
fig, ax = plt.subplots(figsize=(11, 5.2))
ax.set_xlim(0, 11)
ax.set_ylim(0, 5.5)
ax.axis("off")
ax.set_title("Edge vs Cloud Microservice Placement on 3-Node Kind Cluster (edge-cloud)",
             fontsize=13, fontweight="bold", pad=12)

def draw_box(x, y, w, h, title, body, fc, ec):
    box = mpatches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.12", facecolor=fc, edgecolor=ec, linewidth=2)
    ax.add_patch(box)
    ax.text(x + w/2, y + h - 0.35, title, ha="center", va="top", fontweight="bold", fontsize=11, color="#1d3557")
    ax.text(x + w/2, y + h/2 - 0.25, body, ha="center", va="center", fontsize=9.5, color="#222222")

# Control plane
draw_box(0.4, 1.8, 2.8, 2.7, "edge-cloud-control-plane",
         "Role: control-plane\nK8s v1.37.0\n\nTaint: control-plane\n(No user pods)",
         "#edf2f4", "#457b9d")

# Edge worker
draw_box(3.9, 1.8, 3.1, 2.7, "edge-cloud-worker",
         "Label: node-type=edge\n\n[edge-deployment Pod]\nIP: 10.244.1.2 | Status: Running\n\"Hello from the EDGE microservice\"",
         "#e8f5e9", "#2a9d8f")

# Cloud worker
draw_box(7.6, 1.8, 3.1, 2.7, "edge-cloud-worker2",
         "Label: node-type=cloud\n\n[cloud-deployment Pod]\nIP: 10.244.2.2 | Status: Running\n\"Hello from the CLOUD microservice\"",
         "#fff3e0", "#e76f51")

# Services at bottom
draw_box(3.9, 0.3, 3.1, 1.0, "edge-service (ClusterIP)",
         "10.96.101.104:80 -> 5678", "#d8f3dc", "#2a9d8f")
draw_box(7.6, 0.3, 3.1, 1.0, "cloud-service (ClusterIP)",
         "10.96.34.49:80 -> 5678", "#ffe5d9", "#e76f51")

# Arrows
ax.annotate("", xy=(5.45, 1.75), xytext=(5.45, 1.35), arrowprops=dict(arrowstyle="->", lw=2, color="#2a9d8f"))
ax.annotate("", xy=(9.15, 1.75), xytext=(9.15, 1.35), arrowprops=dict(arrowstyle="->", lw=2, color="#e76f51"))

plt.tight_layout()
plt.savefig("graphs/01_edge_cloud_architecture.png", dpi=150)
plt.close()

# --- Graph 2: Step 6 nodeSelector Strict Enforcement State Chart ---
fig, ax = plt.subplots(figsize=(10, 4.5))
phases = [
    "Step 3–4:\nInitial Deploy\n(edge + cloud labeled)",
    "Step 6.1–6.2:\nRemoved node-type=edge\n& Deleted Edge Pod",
    "Step 6.3:\nRestored node-type=edge\nLabel"
]
edge_running  = [1, 0, 1]
edge_pending  = [0, 1, 0]
cloud_running = [1, 1, 1]

x = range(len(phases))
w = 0.25
ax.bar([i - w for i in x], edge_running, w, label="edge-deployment: Running", color="#2a9d8f")
ax.bar([i for i in x], edge_pending, w, label="edge-deployment: Pending (FailedScheduling)", color="#e63946")
ax.bar([i + w for i in x], cloud_running, w, label="cloud-deployment: Running (Unaffected)", color="#457b9d")

ax.set_xticks(list(x))
ax.set_xticklabels(phases)
ax.set_yticks([0, 1])
ax.set_yticklabels(["0 Pods", "1 Pod"])
ax.set_ylim(0, 1.35)
ax.set_title("Strict nodeSelector Enforcement: Pod State Across Label Changes", fontsize=12.5, fontweight="bold")
ax.grid(axis="y", alpha=0.35)
ax.legend(loc="upper right")

ax.annotate("FailedScheduling:\n2 node(s) didn't match\nnodeSelector", xy=(1, 1.02), xytext=(1, 1.15),
            ha="center", fontsize=8.5, fontweight="bold", color="#b5171e")

plt.tight_layout()
plt.savefig("graphs/02_nodeselector_lifecycle.png", dpi=150)
plt.close()

print("Generated 2 graphs in graphs/!")
