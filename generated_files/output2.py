import pandas as pd
df = pd.read_csv("generated_files/output.csv")

# Get unique sprints and sort them
unique_sprints = sorted(df['sprint'].unique())

# Categorize sprints into previous, current, and future
previous_sprints = unique_sprints[:-2]  # Assuming at least two previous sprints
current_sprint = unique_sprints[-2] if len(unique_sprints) >= 2 else None
future_sprints = unique_sprints[-2:]

# Calculate average story points for previous sprints
previous_avg = df[df['sprint'].isin(previous_sprints)]['story_points'].mean()

# Calculate average for current sprint if it exists
current_avg = df[df['sprint'] == current_sprint]['story_points'].mean() if current_sprint else None

# Calculate average for future sprints and determine utilization
future_results = []
for sprint in future_sprints:
    sprint_avg = df[df['sprint'] == sprint]['story_points'].mean()
    if sprint_avg > previous_avg:
        utilization = "Over-Utilized"
    else:
        utilization = "Under-Utilized"
    future_results.append((sprint, sprint_avg, utilization))

# Prepare the output
output = f"User Query: Go to previous 2 sprints and calculate the avg story points assigned per sprint and then go to future 2 sprints and check whether its over utilized or underutilized by comparing it to average story points assigned in previous 2 sprints\n\n"
output += f"Previous 2 Sprints Average Story Points: {previous_avg:.2f}\n"
if current_avg is not None:
    output += f"Current Sprint Average Story Points: {current_avg:.2f}\n"
output += "\nFuture Sprints Utilization:\n"
for sprint, avg, status in future_results:
    output += f"Sprint: {sprint}, Average Story Points: {avg:.2f}, Status: {status}\n"

# Save to output.txt
with open("generated_files/output.txt", "w") as f:
    f.write(output)
