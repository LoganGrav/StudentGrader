import warnings
warnings.simplefilter(action='ignore', category=FutureWarning) #I kept getting "FutureWarnings" so I added this to ingore them
import pandas as pd #imporpanda for data frame and cswv reading

df = pd.read_csv('Ten_Students_Scores.csv') #read data and store in df


for index, row in df.iterrows():    #iterate through each row
    Score = float(row[3]) * 0.2     #add wieght to each score
    Score = Score + float(row[4]) * 0.2
    Score = Score + float(row[5]) * 0.3
    Score = Score + float(row[6]) * 0.3
    df.loc[index, "Grade"] = Score  #add the score to row 8
    if Score >= 90:                 #set letter grade
        df.loc[index, "Letter Grade"] = "A"
    elif Score >= 80:
        df.loc[index, "Letter Grade"] = "B"
    elif Score >= 70:
        df.loc[index, "Letter Grade"] = "C"
    else:
        df.loc[index, "Letter Grade"] = "D"

df.to_csv('Ten_Students_Grades.csv', index=False)   #save data frame



