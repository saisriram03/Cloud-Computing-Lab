# Experiment Observations: Kubernetes Priority Scheduling & Preemption

- **Date:** 2026-11-24
- **Cluster:** Docker Desktop Kubernetes (`desktop-control-plane`, Kubernetes `v1.36.1`, `containerd://2.3.1`)
- **Node Allocatable Resources:** `12 CPU`, `7979656Ki` (~7.61 GiB) Memory
- **Namespace:** `priority-demo`

---

## Summary of Observed Phases

| Phase | Action | Expected Behavior | Observed Result | Evidence File |
| :--- | :--- | :--- | :--- | :--- |
| **1. Baseline** | Inspect node capacity & allocated resources | Identify free memory headroom | `802Mi (10%)` memory allocated; `~6.8 GiB` free | [01-cluster-baseline.txt](./01-cluster-baseline.txt) |
| **2. PriorityClasses** | Apply 4 custom `PriorityClass` objects | Created with distinct values (`100`, `500`, `1000`) and policies | All 4 registered alongside built-in `system-*` classes | [02-priority-classes.txt](./02-priority-classes.txt) |
| **3. Saturate Node** | Deploy `low-priority-workload` (`3 × 2Gi` memory, priority `100`) | All 3 pods run, consuming most allocatable memory | All 3 pods `Running`; memory requests rose to `6946Mi (89%)` | [03-low-priority-running.txt](./03-low-priority-running.txt) |
| **4. Preemption** | Deploy `high-priority-critical-pod` (`2Gi` memory, priority `1000`, `PreemptLowerPriority`) | Scheduler evicts 1 low-priority pod to schedule the high-priority pod | `low-priority-workload-79b49d9fb4-l86jf` was **Preempted**; `high-priority-critical-pod` became **Running**; replacement low-priority pod `v722g` stayed **Pending** | [04-preemption-events.txt](./04-preemption-events.txt) |
| **5. Non-Preempting** | Deploy `high-priority-non-preempting-pod` (`2Gi` memory, priority `1000`, `Never`) | Pod does NOT evict running low-priority pods; remains `Pending` | Remained `Pending` with event: `preemption: not eligible due to preemptionPolicy=Never` | [05-non-preempting-test.txt](./05-non-preempting-test.txt) |
| **6. Queue Ordering** | Delete `high-priority-critical-pod` to free `2Gi` memory | Pending pod with priority `1000` (`high-priority-non-preempting-pod`) schedules ahead of older Pending pod with priority `100` (`v722g`) | `high-priority-non-preempting-pod` immediately transitioned to **Running** while `v722g` remained **Pending** | [06-queue-ordering-test.txt](./06-queue-ordering-test.txt) |

---

## Key Scheduler Events Captured

1. **Preemption Triggered:**
   ```text
   Warning  FailedScheduling  pod/high-priority-critical-pod              0/1 nodes are available: 1 Insufficient memory.
   Normal   Preempted         pod/low-priority-workload-79b49d9fb4-l86jf  Preempted by pod ec974bf3-a950-4e72-ae3f-e3eaa5611d1f on node desktop-control-plane
   Normal   Killing           pod/low-priority-workload-79b49d9fb4-l86jf  Stopping container worker
   Normal   Scheduled         pod/high-priority-critical-pod              Successfully assigned priority-demo/high-priority-critical-pod to desktop-control-plane
   ```

2. **Non-Preempting Policy Enforced:**
   ```text
   Warning  FailedScheduling  pod/high-priority-non-preempting-pod  0/1 nodes are available: 1 Insufficient memory. no new claims to deallocate, preemption: not eligible due to preemptionPolicy=Never.
   ```

3. **Priority Queue Ordering Enforced:**
   - `low-priority-workload-79b49d9fb4-v722g` (Priority `100`) entered the scheduling queue **18 seconds earlier** than `high-priority-non-preempting-pod` (Priority `1000`).
   - As soon as `2Gi` of memory became available, `kube-scheduler` selected `high-priority-non-preempting-pod` first.
