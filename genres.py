import numpy as np
import pandas as pd

data = pd.read_table("tvs-data.tsv")
data = data[data["genres"]!="\\N"]
data.reset_index()

show_genres = list(data["genres"])

genres = ",".join(show_genres)
genres = genres.split(",")
genres = set(genres)

print(len(genres))
print(genres)
