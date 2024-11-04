import datetime
import matplotlib.pyplot as plt

def convert_timestamp(timestamp):
    """Converts a Unix timestamp to a human-readable date and time string."""
    try:
        return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    except (TypeError, ValueError) as e:
        return f"Error converting timestamp: {e}"

def plot_timestamps(unix_timestamps):
    """Plots timestamps relative to the first timestamp in the list."""

    # Convert Unix timestamps to datetime objects
    human_readable_dates = [datetime.datetime.fromtimestamp(ts) for ts in unix_timestamps]

    # Calculate elapsed time in hours from the first timestamp
    elapsed_hours = [(ts - unix_timestamps[0]) / 3600 for ts in unix_timestamps]

    # Extract hours from the human-readable dates for histogram
    hours = [dt.hour for dt in human_readable_dates]

    # Plot the converted times as a function of hours from the first timestamp
    plt.figure(figsize=(10, 6))
    plt.plot(elapsed_hours, human_readable_dates, marker='o', linestyle='-', color='b')
    plt.xlabel('Hours from First Timestamp')
    plt.ylabel('Human-Readable Time (YYYY-MM-DD HH:MM:SS)')
    plt.title('Converted Times as a Function of Hours from the First Timestamp')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Plot a histogram showing the distribution of timestamps across different hours
    plt.figure(figsize=(10, 6))
    plt.hist(hours, bins=range(0, 25), edgecolor='black', alpha=0.7)
    plt.xlabel('Hour of the Day')
    plt.ylabel('Number of Timestamps')
    plt.title('Histogram of Timestamps by Hour')
    plt.grid(True)
    plt.xticks(range(0, 24))
    plt.show()

def main():
    # Input your Unix timestamps here (leave this empty for new analysis)
    unix_timestamps = []

    # Check if there are timestamps to process
    if not unix_timestamps:
        print("No timestamps entered. Please update the unix_timestamps list.")
    else:
        plot_timestamps(unix_timestamps)

if __name__ == "__main__":
    main()
