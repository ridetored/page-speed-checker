# page-speed-checker
This Python tool checks the page speed of multiple URLs using multi-threading for faster performance. It reads URLs from a CSV file, measures load times, and outputs the results in a new CSV file. Ideal for SEOs and developers to identify slow pages and optimize user experience and rankings.
# How It Works:
Reads URLs from a CSV file (url_list.csv).
Measures the page load time using requests and time libraries. It calculates how long it takes to get a response from the server.
Writes the results (URL and load time in seconds) to a new CSV file (page_speed_results.csv).
# Explanation:
Error Handling: The script catches errors such as timeouts, connection issues, and HTTP errors, and logs them in the CSV.
Timeout Setting: Each request has a timeout of 10 seconds to prevent the script from hanging on unresponsive websites.
# Benefits:
Easily measure page speed for multiple URLs in bulk using a CSV file.
Automated results stored in a downloadable CSV file, making it easy for SEOs and developers to review page load performance.
This tool helps you identify slow pages that may impact user experience and SEO rankings, enabling faster optimizations!
