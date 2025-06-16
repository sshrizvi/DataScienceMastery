# <picture><source srcset="https://pandas.pydata.org/static/img/pandas_mark_white.svg" type="image/webp"><img src="https://pandas.pydata.org/static/img/pandas_mark_white.svg" width="32" height="32"></picture> Pandas for Data Science

> [!TIP]  
> Link to Previous Article  
> 🡸 [Time Series Analysis on Google Stock Data](../../TimeSeriesAnalysis/Articles/121_casestudy02_time_series_analysis.md)

## 🎬 IMDB Movie Reviews Analysis

> [!IMPORTANT]  
> Link to Related Notebooks of this article for practical implementation.
> [Notebooks](../Notebooks/)  
> Link to Related Data of this article for practical implementation.
> [Data](../Data/)  

This repository contains the full workflow and assets for my **NLP case‑study on 50 000 IMDB movie reviews**.  
The goal is to walk from raw HTML‑laden text to clean features that let us explore sentiment patterns visually
and feed future ML models.

### Environment

| Library | Purpose |
|---------|---------|
| `pandas`, `numpy` | Data Wrangling |
| `nltk`, `textblob` | Tokenisation & Linguistic Helpers |
| `wordcloud` | Text Visualisation |
| `matplotlib`, `seaborn` | Plotting |
| `scikit‑learn` | Vectorisation (`CountVectorizer`) & Dimensionality Reduction (`PCA`) |

Create the environment with:

```bash
pip install -r requirements.txt
```

*(See the `environment.yml` or `requirements.txt` for exact versions.)*

### Quick start

1. **Clone** the repo and `cd` into it.  
2. Place *IMDBMovieReviewsDataset.csv* inside `data/` (or let the notebook download from Kaggle).  
3. Launch the notebook:  

   ```bash
   jupyter notebook notebook/IMDB_Movie_Reviews_Analysis.ipynb
   ```

### Methodology

| Phase | Key steps |
|-------|-----------|
| **1. Loading** | Read the Kaggle CSV (`50 000` labelled reviews). |
| **2. Cleaning** | Lower‑casing, trimming, stripping HTML/URLs, expanding contractions, removing punctuation & special chars. |
| **3. Pre‑processing** | Tokenise with NLTK, drop English stop‑words, rejoin into a *processed_review* column. |
| **4. Feature engineering** | *Text length* (chars), *word count*, **uni/bi/tri‑grams** frequency tables. |
| **5. EDA** | Word‑clouds for positive vs. negative subsets to surface dominant terms. |
| **6. Vectorisation** | Bag‑of‑Words (top 5 000 tokens) via `CountVectorizer`. |
| **7. Projection** | 2‑D **PCA** scatter‑plot coloured by sentiment — quick sanity‑check of separability. |

### Results & insights

* Word‑clouds show positive reviews emphasise *story*, *character*, *time* whereas negatives highlight *movie*, *even*, *one* – indicating differing topical focuses.  
* PCA projection reveals partial clustering: positive and negative points form mixed but discernible regions, hinting that linear models plus richer features may achieve good separation.
* Feature tables (uni/bi/tri‑grams) ready the dataset for downstream classifiers (LogReg, SVM, BERT …), which are the logical next step.

> [!TIP]  
> Link to Next Article  
> 🡺 []()