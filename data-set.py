import pandas as pd
import pingouin as pg
# Load Excel file into DataFrame
df = pd.read_excel('kalaniya-d.xlsx')
#Calculate Cronbach's alpha
alpha = pg. cronbach_alpha(data=df)
print (alpha)