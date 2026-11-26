<#
.SYNOPSIS
    Reproducible Kubernetes Priority Scheduling & Preemption Experiment.
.DESCRIPTION
    Creates custom PriorityClasses, saturates node memory with low-priority pods,
    verifies preemption with a high-priority pod, verifies non-preempting behavior
    (preemptionPolicy: Never), and proves priority-based scheduling queue ordering.
#>

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$Manifests = Join-Path $Root "manifests"
$Results = Join-Path $Root "results"
New-Item -ItemType Directory -Force -Path $Results | Out-Null

Write-Host "[1/6] Capturing cluster baseline..." -ForegroundColor Cyan
kubectl get nodes -o wide | Out-File "$Results\01-cluster-baseline.txt"

Write-Host "[2/6] Creating namespace and PriorityClasses..." -ForegroundColor Cyan
kubectl apply -f "$Manifests\01-namespace.yaml"
kubectl apply -f "$Manifests\02-priority-classes.yaml"
kubectl get priorityclasses | Tee-Object "$Results\02-priority-classes.txt"

Write-Host "[3/6] Deploying low-priority workload (3 x 2Gi memory)..." -ForegroundColor Cyan
kubectl apply -f "$Manifests\03-low-priority-workload.yaml"
kubectl rollout status deployment/low-priority-workload -n priority-demo --timeout=60s
kubectl get pods -n priority-demo -o custom-columns=NAME:.metadata.name,STATUS:.status.phase,PRIORITY-CLASS:.spec.priorityClassName,PRIORITY:.spec.priority,NODE:.spec.nodeName | Tee-Object "$Results\03-low-priority-running.txt"

Write-Host "[4/6] Deploying high-priority pod (triggers preemption)..." -ForegroundColor Cyan
kubectl apply -f "$Manifests\04-high-priority-pod.yaml"
kubectl wait --for=condition=Ready pod/high-priority-critical-pod -n priority-demo --timeout=60s
kubectl get events -n priority-demo --sort-by='.lastTimestamp' | Tee-Object "$Results\04-preemption-events.txt"

Write-Host "[5/6] Deploying high-priority non-preempting pod (preemptionPolicy: Never)..." -ForegroundColor Cyan
kubectl apply -f "$Manifests\05-non-preempting-pod.yaml"
Start-Sleep -Seconds 3
kubectl describe pod high-priority-non-preempting-pod -n priority-demo | Tee-Object "$Results\05-non-preempting-test.txt"

Write-Host "[6/6] Verifying priority queue ordering by freeing resources..." -ForegroundColor Cyan
kubectl delete pod high-priority-critical-pod -n priority-demo --wait=true
kubectl wait --for=condition=Ready pod/high-priority-non-preempting-pod -n priority-demo --timeout=60s
kubectl get pods -n priority-demo -o custom-columns=NAME:.metadata.name,STATUS:.status.phase,PRIORITY-CLASS:.spec.priorityClassName,PRIORITY:.spec.priority,NODE:.spec.nodeName | Tee-Object "$Results\06-queue-ordering-test.txt"

Write-Host "Experiment complete! Cleaning up..." -ForegroundColor Green
kubectl delete -f "$Manifests\01-namespace.yaml" --wait=false
kubectl delete -f "$Manifests\02-priority-classes.yaml"
