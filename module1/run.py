import pandas as pd
import jordan as j

df = pd.DataFrame({'Name':['Jordan','Ireland'],'Age':[24,25]})
df = df.append({'Name':'Test'}, ignore_index=True)
df = df.append({'Name':'Not Test'}, ignore_index=True)

j.null_check(df)