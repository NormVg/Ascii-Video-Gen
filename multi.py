import threading
from concurrent.futures import ThreadPoolExecutor

# Function that simulates processing an item
def process_item(item):
    print(f"Processing: {item}")
    # Simulate a task (e.g., computation or I/O)
    # You can replace this with actual work (e.g., file download, API call, etc.)
    import time
    time.sleep(2)  # Simulating some work by sleeping for 2 seconds
    print(f"Completed: {item}")
    return f"Result of {item}"

def process_all_items(items):
    # Use ThreadPoolExecutor to manage threads
    with ThreadPoolExecutor() as executor:
        # Submit tasks to the executor and collect the results
        results = list(executor.map(process_item, items))
    
    print("All tasks completed!")
    return results

# List of items to process
items = [1, 2, 3, 4, 5]

# Call the function to process all items
final_results = process_all_items(items)
print(final_results)
