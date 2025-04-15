import csv

headers=[
    "name",
    "Board"
]

board_data = [
    ["Alice", "CDF"],
    ["Bob", "CDF"],
    ["Rishika", "CDF"],
    ["Hari", "CDF"],
    ["Apoorva", "CDF"],
    ["Apoorva", "ESBNF"],
    ["David", "ESBNF"],
    ["Pavithra", "ESBNF"],
    ["Alok", "ESBNF"],
    ["Peter", "ESBNF"],
]


with open("generated_files/members.csv",mode="w") as file:
    writer=csv.writer(file)
    writer.writerow(headers)
    writer.writerows(board_data)


    