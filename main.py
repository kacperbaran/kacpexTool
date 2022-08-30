import pandas as pd 

links = (
    "/Users/kacper/Documents/development/python/kacpexTool/py scipt/1.xlsx", 
    "/Users/kacper/Documents/development/python/kacpexTool/py scipt/2.xlsx",
    "/Users/kacper/Documents/development/python/kacpexTool/py scipt/3.xlsx"
)

needed_columns = [2, 7, 10, 15, 37, 44, 62, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86]

appended_data = []
for country in links:
    data = pd.read_excel(country, skiprows= 13, usecols=needed_columns)
    print(data.shape)
    appended_data.append(data)
df = pd.concat(appended_data)

dfTitle = pd.read_excel(links[1], skiprows=12, nrows=1, usecols=needed_columns)
print(dfTitle.shape)

df = pd.concat([dfTitle, df])
df.to_excel("testowy.xlsx", header= False, index= False)
