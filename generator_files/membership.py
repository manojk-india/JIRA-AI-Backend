import csv

headers=[
    "name",
    "L1_Board",
    "L2_Board",
    "L3_Board",
]

board_data = [
    ["Alice", "CDF","DIS","Transaction Processing"],
    ["Bob", "CDF","DIS","Transaction Processing"],
    ["Rishika", "CDF","DIS","Transaction Processing"],
    ["Hari", "CDF","DIS","Transaction Processing"],
    ["Apoorva", "CDF","DIS","Transaction Processing"],
    ["Apoorva", "ESBNF","DIS","Transaction Processing"],
    ["David", "ESBNF","DIS","Transaction Processing"],
    ["Pavithra", "ESBNF","DIS","Transaction Processing"],
    ["Alok", "ESBNF","DIS","Transaction Processing"],
    ["Peter", "ESBNF","DIS","Transaction Processing"],
]


with open("generated_files/members.csv",mode="w") as file:
    writer=csv.writer(file)
    writer.writerow(headers)
    writer.writerows(board_data)


    