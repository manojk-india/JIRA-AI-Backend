import pandas as pd
import random
from random import randint
from datetime import datetime

boards=["APS","DIS","TES"]

features = {
    "DIS-1":"RTB","DIS-2":"CTB","DIS-3":"RTB","DIS-4":"CTB",
    "DIS-5":"RTB","DIS-6":"CTB","DIS-7":"RTB",
    "TES-1":"CTB","TES-2":"RTB",
    "TES-3":"RTB","TES-4":"CTB",
    "APS-1":"CTB","APS-2":"RTB",
    "APS-3":"RTB","APS-4":"CTB"
}

data=[]
for i in features.keys():
    board=i[0:3]
    data.append({
        "key":i,
        "board":board,
        "summary":f"TASK {i[4]} for {board}",
        "description":f"Description for feature {i[4]} for {board}",
        "acceptance_criteria":f"Acceptance criteria for feature {i[4]} for {board}",
        "labels":features[i],
        "components":" ",
        "parent_link":" ",
        "requested_by":features[i],
        "estimate":" ",
        "due_date":" "
    })

    df=pd.DataFrame(data)
    df.to_csv("l2_board.csv",index=False)