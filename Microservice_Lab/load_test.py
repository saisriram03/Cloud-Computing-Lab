import urllib.request
import time
from concurrent.futures import ThreadPoolExecutor, as_completed


URL = "http://localhost:8003/orders/1"

WORKLOADS = [1, 2, 4, 8, 16]
REQUESTS_PER_WORKLOAD = 20


def send_request():
    start = time.perf_counter()

    try:
        with urllib.request.urlopen(URL, timeout=10) as response:
            response.read()
            status = response.status

        end = time.perf_counter()

        return {
            "success": status == 200,
            "time": end - start
        }

    except Exception:
        end = time.perf_counter()

        return {
            "success": False,
            "time": end - start
        }


print("=" * 60)
print("MICROSERVICE LOAD TEST")
print("=" * 60)
print(f"Target API: {URL}")
print(f"Requests per workload: {REQUESTS_PER_WORKLOAD}")
print()


for concurrency in WORKLOADS:

    print("-" * 60)
    print(f"Workload: {concurrency} concurrent requests")

    results = []

    start_total = time.perf_counter()

    with ThreadPoolExecutor(max_workers=concurrency) as executor:

        futures = [
            executor.submit(send_request)
            for _ in range(REQUESTS_PER_WORKLOAD)
        ]

        for future in as_completed(futures):
            results.append(future.result())

    end_total = time.perf_counter()

    total_time = end_total - start_total

    successful = sum(1 for r in results if r["success"])
    failed = len(results) - successful

    average_response_time = (
        sum(r["time"] for r in results) / len(results)
    )

    throughput = len(results) / total_time

    print(f"Concurrent Requests : {concurrency}")
    print(f"Total Requests      : {len(results)}")
    print(f"Successful Requests : {successful}")
    print(f"Failed Requests     : {failed}")
    print(f"Average Response    : {average_response_time:.4f} seconds")
    print(f"Total Test Time     : {total_time:.4f} seconds")
    print(f"Throughput          : {throughput:.2f} requests/sec")


print()
print("=" * 60)
print("LOAD TEST COMPLETED")
print("=" * 60)