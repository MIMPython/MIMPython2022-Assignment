import pandas as pd
import numpy as np
import vn_fullname_generator as vnname

rows = 10
classList = ["K64", "K65", "K66", "K67"]
scoreList = np.arange(0, 10, 0.1)

namedata = [vnname.generate() for _ in range(rows)]
classdata = np.random.choice(classList, size = rows)
scoredata = np.random.choice(scoreList, size = rows)

data = pd.DataFrame({"name": namedata, 
                     "class": classdata, 
                     "score": scoredata})

print(data)

nStudent = []
meanScore = []
for item in classList:
    databyClass = data[data["class"] == item]
    nStudent.append(databyClass.shape[0])
    meanScore.append(round(np.mean(databyClass["score"].to_numpy()),2))
    
statisticData = pd.DataFrame({"class": classList, 
                              "nStudent": nStudent, 
                              "meanScore": meanScore})

print(statisticData)