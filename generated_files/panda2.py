
```python
#code start
import pandas as pd

# Load the dataset
df = pd.read_csv("generated_files/output.csv")

# Step 1: Filter issues by CDF board
cdf_issues = df[df["board"] == "CDF"]

# Step 2: Filter completed sprints and sort by end date
completed_sprints = cdf_issues[cdf_issues["sprint_state"] == "Completed"]
completed_sprints = completed_sprints.sort_values("sprint_end_date", ascending=False)

# Get last two completed sprints
last_two_completed_sprints = completed_sprints["sprint"].unique()[:2]

# Step 3: Calculate average story points for completed sprints
avg_story_points = (
    completed_sprints[completed_sprints["sprint"].isin(last_two_completed_sprints)]
    .groupby("sprint")["story_points"]
    .sum()
    .mean()
)

# Step 4: Filter future sprints and sort by start date
future_sprints = cdf_issues[cdf_issues["sprint_state"] == "Future"]
future_sprints = future_sprints.sort_values("sprint_start_date")

# Get next two future sprints
next_two_future_sprints = future_sprints["sprint"].unique()[:2]

# Step 5: Calculate total story points for each future sprint
future_sprint_points = (
    future_sprints[future_sprints["sprint"].isin(next_two_future_sprints)]
    .groupby("sprint")["story_points"]
    .sum()
)

# Step 6: Compare future sprint story points with average
results = []
for sprint, points in future_sprint_points.items():
    if points >= avg_story_points - 5 and points <= avg_story_points + 5:
        status = "Okay Utilization"
    elif points < avg_story_points - 5:
        status = "Underutilized"
    else:
        status = "Overutilized"
    
    results.append({"Sprint": sprint, "Story Points": points, "Status": status})

# Save results to output.txt
with open("generated_files/output.txt", "w") as f:
    f.write("User Query: Calculate the average story points from the last 2 completed sprints in the CDF board, then compare the total story points of the next 2 future sprints (one at a time) with this average, and classify each future sprint as 'Underutilized', 'Okay Utilization', or 'Overutilized'\n\n")
    f.write(f"Average Story Points from Last Two Completed Sprints: {avg_story_points}\n\n")
    for result in results:
        f.write(f"Sprint: {result['Sprint']}, Story Points: {result['Story Points']}, Status: {result['Status']}\n")
#code end
```
