# TV Show Recommendation Program

## Database

- [IMDB Dataset](https://imdb.com/interfaces)
    - **title.basics.tsv.gz**


## Progress

- [x] Find distance between all genres.
- [x] Create correlational matrix for the dataset.
    - [ ] Pearson's
    - [ ] Kendall's
    - [x] Spearman's
- [ ] NLP for the descriptions of each title against every title:
    - [ ] Tf-Idf - Scikit Learn
    - [ ] Tf-Idf - Tensorflow
    - [ ] Soft/ Cosine similarity
    - [x] Jaccard Index
    - [ ] Sorensen-Dice coefficient
- [ ] Add options to reorder the recommendations based on:
    - Genre
    - Cast
    - Director