# Lab Report: Dockerized Python Flask Application

**Course area:** Cloud Computing / Docker Laboratory
**Environment:** Windows, PowerShell, Docker Desktop

---

## 1. Title

Containerizing a Python Flask Web Application Using Docker

## 2. Aim

To containerize a simple Python Flask web application using Docker — writing a `Dockerfile`, building a Docker image, running it as a container, mapping the container's port to the host, and verifying that the application is accessible through a web browser.

## 3. Objectives

- Verify that Docker is correctly installed.
- Run the Docker Hello World container to confirm the installation.
- Write a minimal Flask web application.
- Define the application's Python dependency in `requirements.txt`.
- Write a `Dockerfile` describing how to build the application's image.
- Build a Docker image from the `Dockerfile`.
- Run a container from the built image with port mapping.
- Access and verify the application through a browser.
- Verify the image and container using Docker CLI commands.

## 4. Requirements

- A Windows machine with Docker Desktop installed and running.
- PowerShell as the command-line interface.
- Basic familiarity with Python and Flask.
- A text editor / IDE (Visual Studio Code was used) to write the application files.

## 5. Software Used

| Software | Version / Detail |
|---|---|
| Docker Desktop | Docker version 29.8.0, build 88096ef |
| Base image | python:3.12-slim |
| Python | 3.12 (via base image) |
| Flask | Installed via `requirements.txt` |
| OS | Windows |
| Shell | PowerShell |
| Editor | Visual Studio Code |

## 6. Project Structure

```
docker-python-app/
├── app.py
├── requirements.txt
└── Dockerfile
```

The project was created at:

```
C:\Users\Asus\OneDrive\Desktop\docker-python-app
```

## 7. Implementation

### 7.1 Application Code (`app.py`)

A minimal Flask application was written with a single route that returns a plain text message, running on host `0.0.0.0` and port `5000` so it is reachable from outside the container:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! My first Docker application is running."

app.run(host="0.0.0.0", port=5000)
```

### 7.2 Dependencies (`requirements.txt`)

```
flask
```

Flask is the only dependency required to run the application.

## 8. Dockerfile

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
```

**Explanation of each instruction:**

| Instruction | Purpose |
|---|---|
| `FROM python:3.12-slim` | Uses a lightweight official Python 3.12 image as the base |
| `WORKDIR /app` | Sets `/app` as the working directory inside the container |
| `COPY requirements.txt .` | Copies the dependency file into the image |
| `RUN pip install -r requirements.txt` | Installs Flask inside the image |
| `COPY app.py .` | Copies the application source code into the image |
| `EXPOSE 5000` | Documents that the container listens on port 5000 |
| `CMD ["python", "app.py"]` | Defines the command used to start the application when the container runs |

## 9. Commands Executed

**Verify Docker installation:**

```powershell
docker --version
```

**Test Docker installation:**

```powershell
docker run hello-world
```

**Navigate to Desktop and create the project directory:**

```powershell
cd "$HOME\OneDrive\Desktop"
mkdir docker-python-app
cd docker-python-app
pwd
```

**Verify project files:**

```powershell
dir
```

**Build the Docker image:**

```powershell
docker build -t my-python-app .
```

**Verify the Docker image:**

```powershell
docker images
```

**Run the container:**

```powershell
docker run -d -p 5000:5000 --name my-python-container my-python-app
```

**Handle the existing container (see Section 12 — Troubleshooting):**

```powershell
docker ps -a
docker start my-python-container
```

**Check running containers:**

```powershell
docker ps
```

**Access the application in a browser:**

```
http://localhost:5000
```

## 10. Screenshots / Evidence

All screenshots are stored in `docs/screenshots/` and referenced below.

| No. | File | Evidence Of |
|---|---|---|
| 1 | `01_Docker_Version_Verification.png` | `docker --version` output |
| 2 | `02_Docker_Hello_World_Test.png` | `docker run hello-world` output |
| 3 | `03_Creating_Docker_Project_Directory.png` | Project directory creation and navigation |
| 4 | `04_Flask_Application_app_py.png` | `app.py` source code |
| 5 | `05_Python_Requirements_File.png` | `requirements.txt` contents |
| 6 | `06_Dockerfile_Creation.png` | `Dockerfile` contents |
| 7 | `07_Verifying_Project_Files.png` | `dir` listing of project files |
| 8 | `08_Docker_Image_Build.png` | `docker build` execution and completion |
| 9 | `09_Docker_Image_Verification.png` | `docker images` output showing `my-python-app` |
| 10 | `10_Docker_Container_Status.png` | `docker ps` / `docker start my-python-container` |
| 11 | `11_Docker_Container_Running.png` | `docker ps` showing the running container and port mapping |
| 12 | `12_Flask_Application_Browser_Output.png` | Browser output at `http://localhost:5000` |

## 11. Output

Once the container was confirmed running with the correct port mapping (`0.0.0.0:5000->5000/tcp`), the application was accessed at `http://localhost:5000`. The browser displayed:

```
Hello! My first Docker application is running.
```

This confirms that the Flask application was correctly packaged, built into a Docker image, and served from within a running container.

## 12. Troubleshooting

**Issue 1 — Desktop path not found**

`C:\Users\Asus\Desktop` was not a valid path on this machine because the Desktop folder was redirected under OneDrive. This was resolved by using:

```powershell
cd "$HOME\OneDrive\Desktop"
```

**Issue 2 — Container name already in use**

When running:

```powershell
docker run -d -p 5000:5000 --name my-python-container my-python-app
```

Docker reported that the container name was already assigned to an existing container. This was not a failure of Docker — it simply meant that a container named `my-python-container` had already been created in an earlier run. Rather than removing it or creating a duplicate, the existing container was started directly:

```powershell
docker start my-python-container
```

The running state and port mapping were then confirmed with:

```powershell
docker ps
```

## 13. Learning Outcomes

- Understood the difference between a Docker **image** (a static, buildable template) and a **container** (a running instance of that image).
- Learned how to write a `Dockerfile` and understood the purpose of each instruction (`FROM`, `WORKDIR`, `COPY`, `RUN`, `EXPOSE`, `CMD`).
- Learned how port mapping (`-p host:container`) connects a containerized application to the host machine's network.
- Understood the Docker container lifecycle — created, running, stopped, and restarted — and the difference between `docker ps` and `docker ps -a`.
- Learned why a Flask app inside a container must bind to `0.0.0.0` rather than `127.0.0.1` to be reachable from outside the container.
- Practiced basic Docker CLI verification commands (`docker images`, `docker ps`, `docker ps -a`) to confirm each stage of the workflow.
- Learned that a container name conflict is expected behavior, not an error, and how to resolve it correctly using `docker start` instead of deleting and recreating the container.

## 14. Conclusion

This experiment successfully demonstrated containerizing a Python Flask application using Docker on Windows. Docker was verified and tested, a Flask application and its dependencies were defined, a `Dockerfile` was written, an image was built, and a container was run from that image with the correct port mapping. The application was verified as working by accessing `http://localhost:5000` in a browser and observing the expected response. All steps were carried out and verified locally using Docker Desktop, with no cloud or orchestration components involved.

## 15. Future Scope

The following extensions were **not** part of this experiment and are noted only as potential future work:

- Multi-container orchestration using Docker Compose
- Publishing the built image to Docker Hub
- Automating the build and deployment process with CI/CD
- Deploying the application to a Kubernetes cluster
- Deploying to a cloud platform (AWS, Azure, or GCP)
- Adding container health checks
- Replacing Flask's development server with a production WSGI server (e.g. Gunicorn)
