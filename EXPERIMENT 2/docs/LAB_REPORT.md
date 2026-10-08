# 🧪 Cloud Computing Laboratory — Experiment 2
## Dockerized Python Flask Application

---

## 1. 🎯 Aim

To package a simple Python Flask web application into a Docker image and run it locally in a Docker container using Docker Desktop.

---

## 2. ✅ Objectives

1. Verify Docker installation and run the Docker `hello-world` test image.
2. Create a Flask application and record its dependency.
3. Build a Docker image from a Dockerfile.
4. Run the application container with a host-to-container port mapping.
5. Verify the Docker image, container, and application response.

---

## 3. 🖥️ Requirements

- Windows computer with Docker Desktop installed and running
- Windows PowerShell
- Python application source and Dockerfile
- Web browser for testing `http://localhost:5000`

---

## 4. 🧰 Software Used

| Software / Technology | Use |
|---|---|
| Windows | Operating system |
| PowerShell | Terminal used for commands |
| Docker Desktop | Local Docker environment |
| Docker | Image build and container lifecycle commands |
| Python 3.12 slim image | Container base image |
| Flask | Python web framework |
| Web browser | Accessing the local application |

---

## 5. 📁 Project Structure

```text
EXPT-2 CC/
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
├── LICENSE
└── docs/
    ├── LAB_REPORT.md
    └── screenshots/
        ├── 01_Docker_Version_Verification.png
        ├── 02_Docker_Hello_World_Test.png
        ├── 03_Creating_Docker_Project_Directory.png
        ├── 04_Flask_Application_app_py.png
        ├── 05_Python_Requirements_File.png
        ├── 06_Dockerfile_Creation.png
        ├── 07_Verifying_Project_Files.png
        ├── 08_Docker_Image_Build.png
        ├── 09_Docker_Image_Verification.png
        ├── 10_Docker_Container_Status.png
        ├── 11_Docker_Container_Running.png
        └── 12_Flask_Application_Browser_Output.png
```

---

## 6. 💻 Implementation

The application defines a Flask route at `/`. When requested, it returns:

```text
Hello! My first Docker application is running.
```

The server listens on `0.0.0.0:5000`, making it accessible through the container's published port.

The project used during the experiment was located at:

```text
C:\Users\Asus\OneDrive\Desktop\docker-python-app
```

---

## 7. 🐳 Dockerfile

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
```

### Explanation

The Dockerfile:
- selects the Python base image,
- sets `/app` as the working directory,
- copies the dependency list and application code,
- installs Flask,
- documents port `5000`,
- starts the Flask application when the container runs.

---

## 8. 🧾 Commands Executed

```powershell
docker --version
docker run hello-world

cd "$HOME\OneDrive\Desktop"
mkdir docker-python-app
cd docker-python-app
pwd
dir

docker build -t my-python-app .
docker images
docker run -d -p 5000:5000 --name my-python-container my-python-app
docker ps
docker ps -a
docker start my-python-container
```

The browser test used:

```text
http://localhost:5000
```

---

## 9. ⚠️ Troubleshooting

### 9.1 Desktop Path

The Desktop directory was under OneDrive, so the experiment navigated with:

```powershell
cd "$HOME\OneDrive\Desktop"
```

rather than the assumed:

```text
C:\Users\Asus\Desktop
```

### 9.2 Container Name Already in Use

An existing `my-python-container` was present.

It was checked with:

```powershell
docker ps -a
```

and started with:

```powershell
docker start my-python-container
```

The existing container was reused instead of creating a duplicate.

---

## 10. ✅ Verification

- `docker images` lists locally available images, including `my-python-app` after a successful build.
- `docker ps` lists running containers and their published ports.
- `docker ps -a` lists all containers, including stopped containers.
- The running container showed the port mapping `0.0.0.0:5000->5000/tcp`.
- The Flask response was verified through the browser at `http://localhost:5000`.

---

## 11. 🌐 Output

The browser displayed:

> **Hello! My first Docker application is running.**

The running container was identified as:

```text
my-python-container
```

with port mapping:

```text
0.0.0.0:5000 -> 5000/tcp
```

---

## 12. 🖼️ Experiment Evidence

| No. | Evidence |
|---:|---|
| 01 | Docker Version Verification |
| 02 | Docker Hello World Test |
| 03 | Creating Docker Project Directory |
| 04 | Flask Application (`app.py`) |
| 05 | Python Requirements File |
| 06 | Dockerfile Creation |
| 07 | Verifying Project Files |
| 08 | Docker Image Build |
| 09 | Docker Image Verification |
| 10 | Docker Container Status |
| 11 | Docker Container Running |
| 12 | Flask Application Browser Output |

All 12 original evidence screenshots are included in the `docs/screenshots/` folder.

---

## 13. 🧠 Learning Outcomes

The experiment demonstrated:
- how a Dockerfile is used to build an image,
- how a container is run from that image,
- how port publishing makes the Flask service available to a browser,
- the difference between an image and a container,
- the use of `docker ps` and `docker ps -a` to check container state,
- why Flask listens on `0.0.0.0` inside a container,
- and basic Docker troubleshooting.

---

## 14. 🏁 Conclusion

The Flask application was successfully built into a Docker image and run locally in a container. Port `5000` was mapped to the host, and the expected response was accessed through `localhost` in a browser.

---

## 15. 🚀 Future Scope

Possible extensions include:

- Docker Compose
- Docker Hub publishing
- CI/CD
- Kubernetes deployment
- Cloud deployment
- Container health checks
- Running behind a production WSGI server

> These are future possibilities and were not performed as part of this experiment.

