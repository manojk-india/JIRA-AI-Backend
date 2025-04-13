import pandas as pd

# Load the dataset
df = pd.read_csv("generated_files/output.csv")

# Filter issues assigned to Alok in Sprint 8
alok_issues = df[(df['assignee'] == 'Alok') & (df['sprint'] == 'Sprint 8')]
total_story_points_alok = alok_issues['story_points'].sum()

# Filter issues assigned to Apoorva in Sprint 8
apoorva_issues = df[(df['assignee'] == 'Apoorva') & (df['sprint'] == 'Sprint 8')]
total_story_points_apoorva = apoorva_issues['story_points'].sum()

# Save results to a text file
with open("generated_files/output.txt", "w") as f:
    f.write(f"Total story points assigned to Alok in Sprint 8: {total_story_points_alok}\n")
    f.write(f"Total story points assigned to Apoorva in Sprint 8: {total_story_points_apoorva}\n")
