
# Automated Data Analysis Report

## Introduction
This is an automated analysis of the dataset, providing summary statistics, visualizations, and insights from the data.

## Dataset Overview
- **Rows**: 10000
- **Columns**: 23
- **Missing Values**:
book_id                         0
goodreads_book_id               0
best_book_id                    0
work_id                         0
books_count                     0
isbn                          700
isbn13                        585
authors                         0
original_publication_year      21
original_title                585
title                           0
language_code                1084
average_rating                  0
ratings_count                   0
work_ratings_count              0
work_text_reviews_count         0
ratings_1                       0
ratings_2                       0
ratings_3                       0
ratings_4                       0
ratings_5                       0
image_url                       0
small_image_url                 0

## Summary Statistics
|                           |   count |   unique | top                                                                                      |   freq |            mean |              std |            min |             25% |              50% |             75% |              max |
|:--------------------------|--------:|---------:|:-----------------------------------------------------------------------------------------|-------:|----------------:|-----------------:|---------------:|----------------:|-----------------:|----------------:|-----------------:|
| book_id                   |   10000 |      nan | nan                                                                                      |    nan |  5000.5         |   2886.9         |     1          |  2500.75        |   5000.5         |  7500.25        |  10000           |
| goodreads_book_id         |   10000 |      nan | nan                                                                                      |    nan |     5.2647e+06  |      7.57546e+06 |     1          | 46275.8         | 394966           |     9.38223e+06 |      3.32886e+07 |
| best_book_id              |   10000 |      nan | nan                                                                                      |    nan |     5.47121e+06 |      7.82733e+06 |     1          | 47911.8         | 425124           |     9.63611e+06 |      3.55342e+07 |
| work_id                   |   10000 |      nan | nan                                                                                      |    nan |     8.64618e+06 |      1.17511e+07 |    87          |     1.00884e+06 |      2.71952e+06 |     1.45177e+07 |      5.63996e+07 |
| books_count               |   10000 |      nan | nan                                                                                      |    nan |    75.7127      |    170.471       |     1          |    23           |     40           |    67           |   3455           |
| isbn                      |    9300 |     9300 | 439023483                                                                                |      1 |   nan           |    nan           |   nan          |   nan           |    nan           |   nan           |    nan           |
| isbn13                    |    9415 |      nan | nan                                                                                      |    nan |     9.75504e+12 |      4.42862e+11 |     1.9517e+08 |     9.78032e+12 |      9.78045e+12 |     9.78083e+12 |      9.79001e+12 |
| authors                   |   10000 |     4664 | Stephen King                                                                             |     60 |   nan           |    nan           |   nan          |   nan           |    nan           |   nan           |    nan           |
| original_publication_year |    9979 |      nan | nan                                                                                      |    nan |  1981.99        |    152.577       | -1750          |  1990           |   2004           |  2011           |   2017           |
| original_title            |    9415 |     9274 |                                                                                          |      5 |   nan           |    nan           |   nan          |   nan           |    nan           |   nan           |    nan           |
| title                     |   10000 |     9964 | Selected Poems                                                                           |      4 |   nan           |    nan           |   nan          |   nan           |    nan           |   nan           |    nan           |
| language_code             |    8916 |       25 | eng                                                                                      |   6341 |   nan           |    nan           |   nan          |   nan           |    nan           |   nan           |    nan           |
| average_rating            |   10000 |      nan | nan                                                                                      |    nan |     4.00219     |      0.254427    |     2.47       |     3.85        |      4.02        |     4.18        |      4.82        |
| ratings_count             |   10000 |      nan | nan                                                                                      |    nan | 54001.2         | 157370           |  2716          | 13568.8         |  21155.5         | 41053.5         |      4.78065e+06 |
| work_ratings_count        |   10000 |      nan | nan                                                                                      |    nan | 59687.3         | 167804           |  5510          | 15438.8         |  23832.5         | 45915           |      4.94236e+06 |
| work_text_reviews_count   |   10000 |      nan | nan                                                                                      |    nan |  2919.96        |   6124.38        |     3          |   694           |   1402           |  2744.25        | 155254           |
| ratings_1                 |   10000 |      nan | nan                                                                                      |    nan |  1345.04        |   6635.63        |    11          |   196           |    391           |   885           | 456191           |
| ratings_2                 |   10000 |      nan | nan                                                                                      |    nan |  3110.89        |   9717.12        |    30          |   656           |   1163           |  2353.25        | 436802           |
| ratings_3                 |   10000 |      nan | nan                                                                                      |    nan | 11475.9         |  28546.4         |   323          |  3112           |   4894           |  9287           | 793319           |
| ratings_4                 |   10000 |      nan | nan                                                                                      |    nan | 19965.7         |  51447.4         |   750          |  5405.75        |   8269.5         | 16023.5         |      1.4813e+06  |
| ratings_5                 |   10000 |      nan | nan                                                                                      |    nan | 23789.8         |  79768.9         |   754          |  5334           |   8836           | 17304.5         |      3.01154e+06 |
| image_url                 |   10000 |     6669 | https://s.gr-assets.com/assets/nophoto/book/111x148-bcc042a9c91a29c1d680899eff700a03.png |   3332 |   nan           |    nan           |   nan          |   nan           |    nan           |   nan           |    nan           |
| small_image_url           |   10000 |     6669 | https://s.gr-assets.com/assets/nophoto/book/50x75-a91bf249278a81aabab721ef782c4a74.png   |   3332 |   nan           |    nan           |   nan          |   nan           |    nan           |   nan           |    nan           |

## Key Insights
Based on the dataset summary provided, here are some insights and observations regarding the book data:

### 1. **Missing Values**
- **ISBN and ISBN13**: A significant number of missing values are present in the `isbn` (700 missing) and `isbn13` (585 missing) columns. This could indicate that a number of books lack standard identifiers, which might affect searchability and categorization.
- **Original Publication Year**: There are 21 missing values for `original_publication_year`. This could be important for analyzing trends over time, especially in the context of newer versus older titles.
- **Original Title**: The `original_title` column has 585 missing values, which could impact the understanding of the book's identity, especially if different editions or translations exist.

### 2. **Language Code**
- There are 1,084 missing values in the `language_code` column, indicating a potential lack of language information for a substantial number of books. This could hinder the ability to segment analysis by language, which is crucial for understanding readership demographics.

### 3. **Ratings Analysis**
- **Average Ratings**: The average ratings range from approximately 3.57 (e.g., *Twilight*) to 4.44 (e.g., *Harry Potter and the Philosopher's Stone*). The average ratings suggest a generally high level of reader satisfaction, particularly for popular series.
- **Distribution of Ratings**: The dataset provides detailed ratings distribution (ratings_1 to ratings_5). For instance, *The Hunger Games* has a high count of 5-star ratings (2,706,317), indicating that a substantial portion of readers rated it highly.
- **Outliers in Ratings**: Books like *Twilight* show a high count of 1-star ratings (456,191), suggesting polarized opinions, while other books may have a more balanced distribution of ratings.

### 4. **Trends Over Time**
- **Publication Years**: Analyzing the `original_publication_year` could provide insights into trends in book popularity over time. For example, books published in the last two decades might show higher ratings and reviews due to increased readership and accessibility through platforms like Goodreads.
  
### 5. **Authors and Popularity**
- Popular authors like J.K. Rowling and Suzanne Collins appear multiple times and have books with high ratings and reviews. This indicates their significant impact on contemporary literature and reader engagement.
- The authors' diversity in genres and styles could be explored to understand how different styles resonate with readers.

### 6. **Visual Insights**
- **Image URLs**: The presence of `image_url` and `small_image_url` columns suggests that visual appeal plays a role in attracting readers. Analyzing the click-through rates or engagement on these images could add another layer to understanding book popularity.

### 7. **Book Counts**
- The `books_count` column indicates the number of editions or formats available for each book. For example, *Harry Potter and the Philosopher's Stone* has a high `books_count` of 491, which could signify its various editions, translations, and formats (e.g., paperback, hardcover, eBook).

### 8. **Overall Reader Engagement**
- The `ratings_count` and `work_ratings_count` columns provide insight into reader engagement. Books with millions of ratings (e.g., *The Hunger Games* with 4,780,653) indicate a strong reader base, likely due to successful marketing, adaptations (such as movies), or cultural relevance.

### Conclusion
The dataset reveals a rich landscape of literary engagement, with high reader satisfaction and varied opinions on certain titles. However, the presence of missing data in critical columns like ISBN and language code suggests gaps that could be explored further for a comprehensive analysis. Identifying trends in publication years alongside author popularity and ratings can provide valuable insights into the changing dynamics of reader preferences over time

## Visualizations
### Correlation Matrix
![Correlation Matrix](correlation_matrix.png)

### Distributions
![book_id Distribution](book_id_distribution.png)
![goodreads_book_id Distribution](goodreads_book_id_distribution.png)
![best_book_id Distribution](best_book_id_distribution.png)
![work_id Distribution](work_id_distribution.png)
![books_count Distribution](books_count_distribution.png)
![isbn13 Distribution](isbn13_distribution.png)
![original_publication_year Distribution](original_publication_year_distribution.png)
![average_rating Distribution](average_rating_distribution.png)
![ratings_count Distribution](ratings_count_distribution.png)
![work_ratings_count Distribution](work_ratings_count_distribution.png)
![work_text_reviews_count Distribution](work_text_reviews_count_distribution.png)
![ratings_1 Distribution](ratings_1_distribution.png)
![ratings_2 Distribution](ratings_2_distribution.png)
![ratings_3 Distribution](ratings_3_distribution.png)
![ratings_4 Distribution](ratings_4_distribution.png)
![ratings_5 Distribution](ratings_5_distribution.png)
