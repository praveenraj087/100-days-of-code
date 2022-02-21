import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = data["Primary Fur Color"]
fur_color_unique = fur_color.value_counts()
fur_df = pd.DataFrame(fur_color_unique)
fur_df.to_csv("squirrel_count.csv")
fur_clr = pd.read_csv("squirrel_count.csv")
print(fur_clr)
