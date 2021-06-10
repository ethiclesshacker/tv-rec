import numpy as np
import pandas as pd

data = pd.read_table("tvs-data.tsv")

show_genres = list(data["genres"])

genres = ",".join(show_genres)
genres = genres.replace("\\N,","")
genres = genres.split(",")
genres = set(genres)

print(len(genres))
print(genres)
