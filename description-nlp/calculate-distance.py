import numpy as np
import pandas as pd
import textdistance as td
import json


def calculate(DATA_FILE, DEL, FUNC, SAMPLE_SIZE, SAVE_FILE, USE_COLS):

    [KEY, VALUE] = USE_COLS

    data = pd.read_csv(DATA_FILE, delimiter=DEL, usecols=USE_COLS)
    data = data.dropna()

    jd = {}
    sample_data = data[:SAMPLE_SIZE]

    for item in sample_data.iterrows():
        title = item[1][KEY]
        jd[title] = {}

    for item in sample_data.iterrows():
        title = item[1][KEY]
        desc = item[1][VALUE]

        for item1 in sample_data.iterrows():
            title1 = item1[1][KEY]
            desc1 = item1[1][VALUE]

            if title1 in jd[title].keys():
                # print("Key Present.")
                continue

            if title == title1:
                jd[title][title1] = jd[title1][title] = -1
                # print("Set value as -1")
                continue

            jd[title][title1] = jd[title1][title] = FUNC(desc, desc1)

    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        f.write(json.dumps(jd))



""""
DATA_FILE = ".\\..\\data\\imdb-title-cast-rating-desc.tsv"
DEL = "\t"
FUNC = td.jaccard
SAMPLE_SIZE = 100
SAVE_FILE = "jd-check.json"
USE_COLS = [KEY, VALUE] = ["title","description"]

calculate(
    DATA_FILE=".\\..\\data\\imdb-title-cast-rating-desc.tsv",
    DEL="\t",
    FUNC=td.jaccard,
    SAMPLE_SIZE=100,
    SAVE_FILE="jd-check.json",
    USE_COLS=["title", "description"],
)

"""