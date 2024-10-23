import requests
import csv
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# Function to check page speed
def check_page_speed(url):
    try:
        # Start the timer
        start_time = time.time()

        # Fetch the page
        response = requests.get(url, timeout=10)  # Set a 10-second timeout for requests
        response.raise_for_status()  # Check if request was successful

        # Stop the timer
        load_time = time.time() - start_time

        return {"URL": url, "Load Time (seconds)": load_time}

    except requests.exceptions.RequestException as e:
        return {"URL": url, "Load Time (seconds)": "Error: " + str(e)}

# Function to read URLs from a CSV file, check their page speed, and write results to another CSV file
def check_urls_from_csv(input_csv, output_csv, max_workers=10):
    results = []

    # Read URLs from the input CSV
    with open(input_csv, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        url_list = [row[0] for row in reader]

    # Use ThreadPoolExecutor to process URLs concurrently
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(check_page_speed, url): url for url in url_list}

        # Collect the results as they complete
        for future in as_completed(futures):
            result = future.result()
            results.append(result)

    # Write results to a new CSV file
    with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["URL", "Load Time (seconds)"])
        writer.writeheader()
        writer.writerows(results)

    print(f"Results have been saved to {output_csv}")

# Example usage
input_csv = "url_list.csv"   # Input CSV file with URLs
output_csv = "page_speed_results.csv"  # Output CSV file to store the results
max_workers = 10  # Number of threads to use (you can adjust this based on your system's capabilities)

check_urls_from_csv(input_csv, output_csv, max_workers)
