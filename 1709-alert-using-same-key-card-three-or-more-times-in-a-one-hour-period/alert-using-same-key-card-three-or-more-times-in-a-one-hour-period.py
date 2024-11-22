from collections import defaultdict
from typing import List

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        # Helper function to convert time in HH:MM format to total minutes since midnight
        def time_to_minutes(time):
            hours, minutes = map(int, time.split(":"))  # Split time into hours and minutes
            return hours * 60 + minutes  # Convert hours to minutes and add

        # Dictionary to store the list of times (in minutes) for each worker
        worker_times = defaultdict(list)

        # Populate worker_times with each worker's access times in minutes
        for name, time in zip(keyName, keyTime):
            worker_times[name].append(time_to_minutes(time))

        # Set to store names of workers who triggered alerts
        alerts = set()

        # Check for alerts for each worker
        for name, times in worker_times.items():
            times.sort()  # Sort the access times for each worker
            for i in range(len(times) - 2):  # Loop through times to find any 3 within 1 hour
                if times[i + 2] - times[i] <= 60:  # Check if the 3rd time is within 1 hour of the 1st
                    alerts.add(name)  # Add worker to alerts
                    break  # No need to check further for this worker

        # Return the list of names sorted alphabetically
        return sorted(alerts)

# Time Complexity (TC):
# O(N log N) - Sorting access times for each worker dominates, where N is the total number of keycard uses.

# Space Complexity (SC):
# O(U + N) - U for the dictionary of worker times (unique workers), and N for the access times stored.
