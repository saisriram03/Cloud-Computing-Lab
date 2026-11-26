
# ☁️🚀 CLOUD COMPUTING LAB 🚀☁️

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00C6FF,25:0072FF,50:7B2FFF,75:FF00C8,100:FF6B00&height=220&section=header&text=CLOUD%20COMPUTING%20LAB&fontSize=46&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=VIRTUALIZATION%20%7C%20DOCKER%20%7C%20KUBERNETES%20%7C%20MICROSERVICES&descAlignY=58&descSize=16" width="100%"/>

### 👨‍💻 **SAI SRI RAM**

**B.Tech — Computer Science (Artificial Intelligence)**  
**KLE Technological University, Hubballi**

<br>

![Cloud](https://img.shields.io/badge/☁️_Cloud_Computing-0072FF?style=for-the-badge)
![Virtualization](https://img.shields.io/badge/🖥️_Virtualization-7B2FFF?style=for-the-badge)
![Docker](https://img.shields.io/badge/🐳_Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/🐍_Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/🌶️_Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![FastAPI](https://img.shields.io/badge/⚡_FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Kubernetes](https://img.shields.io/badge/☸️_Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![Terraform](https://img.shields.io/badge/🏗️_Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)
![Microservices](https://img.shields.io/badge/🧩_Microservices-FF00C8?style=for-the-badge)

</div>

---

# 🌌 CLOUD COMPUTING LAB

> ### ☁️ A complete practical journey from **Virtualization → Containerization → Microservices → Kubernetes → Edge Computing → Infrastructure Automation**

This repository contains the practical implementations, experiments, evaluations, and projects completed as part of the **Cloud Computing Laboratory**.

The repository explores modern cloud computing concepts through hands-on implementations involving virtualization, Docker, distributed systems, Kubernetes orchestration, edge computing, microservices, and Terraform-based infrastructure automation.

The work is organized into **7 major experiments and projects**.

---

# 📂 REPOSITORY STRUCTURE

```text
Cloud-Computing-Lab/
│
├── EXP-1/
│   └── Virtualization Performance
│
├── EXPERIMENT 2/
│   └── Docker Containerization
│
├── Eval 1/
│   └── Microservice_Lab/
│
├── PRIORITY-POD-SCHEDULING-CC-EVAL2-main/
│   └── Kubernetes Priority-Based Pod Scheduling
│
├── edge-vs-cloud-k8s-main/
│   └── Edge vs Cloud Computing using Kubernetes
│
├── microservice-project-main/
│   └── Microservices Project
│
├── terraform-multiple-containers-main/
│   └── Terraform Multiple Container Deployment
│
└── README.md
```

---

# 🖥️ EXPERIMENT 1 — VIRTUALIZATION PERFORMANCE

## 🎯 Objective

To understand virtualization technologies and evaluate the performance of different virtualization environments.

## 🔍 Overview

Virtualization allows multiple virtual machines to operate on a single physical system by sharing hardware resources.

This experiment focuses on understanding and comparing virtualization platforms based on their resource utilization and performance.

## 🧪 Key Concepts

- Virtual Machines (VMs)
- Hypervisors
- CPU Virtualization
- Memory Management
- Resource Allocation
- Virtual Machine Performance
- Infrastructure Virtualization

## 🏆 Performance Observation

**Proxmox VE performed better** in the conducted performance comparison.

---

# 🐳 EXPERIMENT 2 — DOCKER CONTAINERIZATION

## 🎯 Objective

To understand containerization and deploy a Flask application using Docker.

## 🔍 Overview

Docker is a containerization platform that packages applications and their dependencies into lightweight, portable containers.

Containers provide application isolation and simplify deployment across different environments.

## ⚙️ Technologies Used

| Technology | Purpose |
|---|---|
| Docker | Containerization |
| Python | Application Development |
| Flask | Web Application Framework |
| Dockerfile | Container Image Configuration |
| Docker Image | Application Packaging |
| Docker Container | Application Execution |

## 🔄 Implementation Workflow

```text
       🐍 FLASK APPLICATION
                |
                ↓
            DOCKERFILE
                |
                ↓
        BUILD DOCKER IMAGE
                |
                ↓
        CREATE CONTAINER
                |
                ↓
        RUN FLASK APPLICATION
                |
                ↓
        🌐 ACCESS APPLICATION
```

## 🏆 Result

The Flask application was successfully containerized and executed using Docker.

---

# 🧩 EXPERIMENT 3 — MICROSERVICE LAB

## 🎯 Objective

To understand and implement a distributed application using microservices architecture and evaluate its performance.

## 🔍 Overview

Microservices architecture divides an application into smaller, independent services. Each service handles a specific responsibility and communicates with other services through APIs.

## 🧪 Key Concepts

- Microservices Architecture
- Distributed Systems
- API Communication
- Service Independence
- Scalability
- Fault Isolation
- Performance Testing

## 📈 Performance Results

| Metric | Observed Result |
|---|---:|
| Successful Requests | 100% |
| Maximum Throughput | 153.54 req/s |

## 🏆 Result

The distributed application successfully handled the tested requests, achieving 100% successful requests and a maximum recorded throughput of 153.54 requests per second.

---

# ☸️ EXPERIMENT 4 — PRIORITY-BASED POD SCHEDULING

## 🎯 Objective

To implement priority-based pod scheduling in Kubernetes and understand how Kubernetes schedules workloads based on their priority.

## 🔍 Overview

Kubernetes is a container orchestration platform that automates container deployment, scaling, and management.

Priority-based scheduling allows important workloads to receive scheduling preference over lower-priority workloads.

## 🧪 Key Concepts

- Kubernetes Architecture
- Pods and Nodes
- Priority Classes
- Pod Scheduling
- Preemption
- Resource Allocation
- Container Orchestration

## ⚙️ Technologies Used

- Kubernetes
- Minikube
- Docker
- kubectl
- YAML Configuration

## 🔄 Implementation Workflow

```text
          KUBERNETES CLUSTER
                  |
                  ↓
          CREATE PRIORITY CLASSES
                  |
          ┌───────┼───────┐
          ↓       ↓       ↓
         LOW    MEDIUM   HIGH
       PRIORITY PRIORITY PRIORITY
          |       |       |
          └───────┼───────┘
                  |
                  ↓
           KUBERNETES SCHEDULER
                  |
                  ↓
          PRIORITY-BASED SCHEDULING
                  |
                  ↓
            POD DEPLOYMENT
```

## 🏆 Result

Implemented Kubernetes PriorityClasses and tested pod scheduling behavior using different priority levels.

---

# 🌐 EXPERIMENT 5 — EDGE VS CLOUD COMPUTING USING KUBERNETES

## 🎯 Objective

To understand and implement edge and cloud computing environments using Kubernetes.

## 🔍 Overview

Edge computing processes data closer to its source, reducing latency and network dependency.

Cloud computing provides centralized infrastructure with scalable computing and storage resources.

This project explores how Kubernetes can be used to manage workloads across edge and cloud environments.

## 🧪 Key Concepts

- Edge Computing
- Cloud Computing
- Kubernetes
- Distributed Infrastructure
- Workload Deployment
- Node Management
- Resource Allocation
- Container Orchestration

## 🔄 Architecture

```text
             APPLICATION REQUEST
                     |
                     ↓
              KUBERNETES
                     |
             ┌───────┴───────┐
             ↓               ↓
        EDGE NODE         CLOUD NODE
             |               |
       LOW-LATENCY       CENTRALIZED
       PROCESSING        PROCESSING
             |               |
             └───────┬───────┘
                     |
                     ↓
               APPLICATION
                 RESPONSE
```

## 🏆 Result

Explored Kubernetes-based edge and cloud workload deployment and the differences between edge and centralized cloud processing.

---

# 🧩 EXPERIMENT 6 — MICROSERVICES PROJECT

## 🎯 Objective

To develop and understand an application using microservices architecture.

## 🔍 Overview

A microservices-based application separates its functionality into independent services that communicate through APIs.

Each service can be developed, tested, maintained, and deployed independently.

## 🧪 Key Concepts

- Microservices Architecture
- Service Communication
- REST APIs
- Independent Deployment
- Distributed Applications
- Scalability
- Service Management

## 🔄 Architecture Workflow

```text
                👤 CLIENT
                    |
                    ↓
              API REQUEST
                    |
                    ↓
             APPLICATION
                    |
          ┌─────────┼─────────┐
          ↓         ↓         ↓
       SERVICE   SERVICE   SERVICE
          1         2         3
          |         |         |
          └─────────┼─────────┘
                    |
                    ↓
              API RESPONSE
                    |
                    ↓
                👤 CLIENT
```

## 🏆 Result

Explored the development and organization of applications using independent microservices and distributed communication.

---

# 🏗️ EXPERIMENT 7 — TERRAFORM MULTIPLE CONTAINERS

## 🎯 Objective

To understand Infrastructure as Code (IaC) and automate the creation and management of multiple containers using Terraform.

## 🔍 Overview

Terraform is an Infrastructure as Code tool that allows infrastructure resources to be defined, configured, and managed using declarative configuration files.

It simplifies infrastructure provisioning and makes deployments repeatable.

## 🧪 Key Concepts

- Infrastructure as Code (IaC)
- Terraform
- Container Management
- Infrastructure Provisioning
- Declarative Configuration
- Resource Management
- Automated Deployment

## ⚙️ Technologies Used

- Terraform
- Docker
- Container Images
- HCL Configuration Language

## 🔄 Implementation Workflow

```text
           TERRAFORM CONFIGURATION
                     |
                     ↓
               TERRAFORM INIT
                     |
                     ↓
               TERRAFORM PLAN
                     |
                     ↓
              TERRAFORM APPLY
                     |
                     ↓
              DOCKER PROVIDER
                     |
             ┌───────┼───────┐
             ↓       ↓       ↓
         CONTAINER CONTAINER CONTAINER
             1       2       3
             |       |       |
             └───────┼───────┘
                     |
                     ↓
           MULTIPLE CONTAINERS
               SUCCESSFULLY
                PROVISIONED
```

## 🏆 Result

Explored Terraform-based infrastructure provisioning and the automated management of multiple Docker containers.

---

# 🛠️ TECHNOLOGIES & TOOLS

<div align="center">

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)
![Proxmox](https://img.shields.io/badge/Proxmox-E57000?style=for-the-badge&logo=proxmox&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

</div>

---

# 🎓 LEARNING OUTCOMES

Through these experiments and projects, the following concepts were explored:

1. Understanding virtualization and hypervisor technologies.
2. Comparing virtualization environments based on performance.
3. Containerizing applications using Docker.
4. Deploying Flask applications inside containers.
5. Understanding distributed systems and microservices.
6. Implementing priority-based pod scheduling in Kubernetes.
7. Exploring edge and cloud computing environments.
8. Understanding container orchestration and workload management.
9. Developing applications using microservices architecture.
10. Automating infrastructure provisioning using Terraform.
11. Understanding scalability, resource allocation, and deployment.

---

# 📊 CLOUD COMPUTING JOURNEY

<div align="center">

| # | Practical Area | Technology |
|:---:|---|---|
| 01 | Virtualization Performance | Proxmox VE |
| 02 | Containerization | Docker |
| 03 | Distributed Microservices | Python / Flask / FastAPI |
| 04 | Priority-Based Scheduling | Kubernetes |
| 05 | Edge vs Cloud Computing | Kubernetes |
| 06 | Microservices Project | Microservices |
| 07 | Infrastructure Automation | Terraform |

</div>

---

# 👨‍💻 ABOUT ME

### **SAI SRI RAM**

**B.Tech — Computer Science (Artificial Intelligence)**  
**KLE Technological University, Hubballi**

Interested in Cloud Computing, Artificial Intelligence, Distributed Systems, Backend Development, Kubernetes, and Emerging Technologies.

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-saisriram03-181717?style=for-the-badge&logo=github)](https://github.com/saisriram03)

[![Repository](https://img.shields.io/badge/Cloud_Computing_Lab-Explore_Repository-0072FF?style=for-the-badge&logo=github)](https://github.com/saisriram03/Cloud-Computing-Lab)

<br>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00C6FF,25:0072FF,50:7B2FFF,75:FF00C8,100:FF6B00&height=120&section=footer" width="100%"/>

### ☁️ LEARN • BUILD • DEPLOY • SCALE 🚀

**THANK YOU FOR VISITING!**

</div>
