import threading
import requests
import time
from queue import Queue

# List of URLs to download (as examples, replace with actual URLs)
URLS = [
    "https://example.com/file1.jpg",
    "https://example.com/file2.jpg",
    "https://example.com/file3.jpg"
]

# Shared resource: a list to keep track of downloaded files
downloaded_files = []
download_lock = threading.Lock()

# Function to download a single file
def download_file(url, file_queue):
    try:
        print(f"Starting download of {url}")
        response = requests.get(url)
        file_name = url.split("/")[-1]
        
        # Simulate file saving
        with open(file_name, "wb") as file:
            file.write(response.content)
        
        with download_lock:
            downloaded_files.append(file_name)
        
        print(f"Finished downloading {file_name}")
        file_queue.put(file_name)  # Queue the file for processing
    except Exception as e:
        print(f"Error downloading {url}: {e}")

# Function to process a downloaded file
def process_file(file_queue):
    while not file_queue.empty():
        file_name = file_queue.get()
        print(f"Processing {file_name}...")
        time.sleep(2)  # Simulate file processing
        print(f"Finished processing {file_name}")

# Multi-threaded download function
def multi_threaded_download(urls):
    threads = []
    file_queue = Queue()

    for url in urls:
        thread = threading.Thread(target=download_file, args=(url, file_queue))
        thread.start()
        threads.append(thread)
    
    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Now start processing files concurrently
    process_threads = []
    for _ in range(len(urls)):
        thread = threading.Thread(target=process_file, args=(file_queue,))
        thread.start()
        process_threads.append(thread)
    
    # Wait for processing threads to finish
    for thread in process_threads:
        thread.join()

# Single-threaded download function for comparison
def single_threaded_download(urls):
    file_queue = Queue()

    for url in urls:
        download_file(url, file_queue)

    # Process files sequentially after downloading
    process_file(file_queue)

if __name__ == "__main__":
    print("Starting single-threaded download and processing...")
    start_time = time.time()
    single_threaded_download(URLS)
    single_duration = time.time() - start_time
    print(f"Single-threaded time: {single_duration:.2f} seconds\n")

    print("Starting multi-threaded download and processing...")
    downloaded_files.clear()  # Clear the list for fresh run
    start_time = time.time()
    multi_threaded_download(URLS)
    multi_duration = time.time() - start_time
    print(f"Multi-threaded time: {multi_duration:.2f} seconds\n")

    print(f"Performance improvement: {single_duration / multi_duration:.2f}x")
