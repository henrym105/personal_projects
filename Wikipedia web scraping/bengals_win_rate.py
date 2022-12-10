import pandas as pd

# URL for Cincinnati Bengals win data on Wikipedia
url = 'https://en.wikipedia.org/wiki/List_of_Cincinnati_Bengals_seasons'

# Read data from table on website into pandas DataFrame
df = pd.read_html(url).DataFrame

print(df.head(20))
print(df.columns)
# Extract win data from DataFrame and print


# wins = df['W']
# print(wins)
