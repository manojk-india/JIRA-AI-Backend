import pandas as pd

members_df = pd.read_csv('generated_files/members.csv')

# Query parameters
x_board = 'x'  # Replace with the actual board name

# Step 1: Get members of x board from members.csv
members_of_x_board = members_df[members_df['Board'] == x_board]['name'].tolist()

if not members_of_x_board:
    print("No members found for board: " + x_board)
else:
    print("Members of " + x_board + " board: " + str(members_of_x_board))

pto_df = pd.read_csv('generated_files/PTO.csv')

# Step 2: Calculate total leave days for each member of x board
leave_data_x_board = pto_df[pto_df['name'].isin(members_of_x_board)][['name', 'total_days', 'sprint']]

if leave_data_x_board.empty:
    print("No leave data found for members of " + x_board + " board.")
else:
    print("Leave data for members of " + x_board + " board:")
    print(leave_data_x_board)
