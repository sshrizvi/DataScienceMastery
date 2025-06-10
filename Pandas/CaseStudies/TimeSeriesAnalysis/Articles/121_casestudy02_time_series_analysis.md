# <picture><source srcset="https://pandas.pydata.org/static/img/pandas_mark_white.svg" type="image/webp"><img src="https://pandas.pydata.org/static/img/pandas_mark_white.svg" width="32" height="32"></picture> Pandas for Data Science

> [!TIP]  
> Link to Previous Article  
> 🡸 [MultiIndex Series and DataFrames](../../Pandas/Articles/119_multiindex_series_and_dataframes.md)

## Time Series Analysis on Google Stock Data

> [!IMPORTANT]  
> Link to Related Notebooks of this article for practical implementation.
> [Notebooks](../Notebooks/)  
> Link to Related Data of this article for practical implementation.
> [Data](../Data/)  


### 1. Project Overview  
This case study is a **hands‑on time‑series analysis of Alphabet (GOOG) daily price data from 2004‑08‑19 through 2024‑12‑17**.  
It demonstrates a full workflow—from raw CSV ingestion to feature engineering, statistical profiling, resampling, and rich visualisation—implemented in a single Jupyter notebook. 

### 2. Data & Dependencies  
| Item | Details |
|------|---------|
| **Dataset** | `GoogleStockData2004To2024.csv` (Kaggle download)  |
| **Key libraries** | `pandas`, `numpy`, `matplotlib` |
| **Notebook name** | `CaseStudy 02 : Google Stock Data Analysis` |

#### Data Variable Description
| Variable  | Description |
|-----------|-------------|
| date      | Date |
| open      | The price at market open. |
| high      | The highest price for that day. |
| low       | The lowest price for that day. |
| close     | The price at market close, adjusted for splits. |
| adj_close | The closing price after adjustments for all applicable splits and dividend distributions. Data is adjusted using appropriate split and dividend multipliers, adhering to Center for Research in Security Prices (CRSP) standards. |
| volume    | The number of shares traded on that day. |


### 3. Workflow Summary  

| Step | What Happens | Key Code / Output |
|------|--------------|-------------------|
| **Data prep** | Convert `Date` column → `datetime64`, set as index for fast slicing.  | Enables queries like `df.loc['2022']` |
| **Enrich features** | Adds `month_name`, `weekday_name`, `Quarter` plus **Daily, Log, % and Intraday returns**.  &  | Creates four return metrics for later stats |
| **Data validity check** | Confirms `High ≥ Open/Close ≥ Low` for every row—no anomalies found.  | Data passes all rules |
| **Exploratory slicing** | Examples: Independence‑Day snapshot across years, full‑year slices, partial indexing.  |
| **Visualisations** | Single‑series plots (Open, Close, High, Low), 2×2 dashboard, and dynamic helper functions:<br>`visualize_quarter_values()` & `visualize_year_quarter_values()` for any column/quarter. ,  |
| **Return statistics** | `display_return_stats()` summarises mean, st‑dev, min, max, skew & kurtosis for each return measure. Example output: mean daily return ≈ **0.10 %**, σ ≈ 1.9 %.  |
| **Comprehensive panel** | `plot_return_analysis()` produces a 6‑panel figure (price path, daily/log returns, their distributions & 30‑day annualised volatility).  |
| **Resampling** | Down‑sample to quarter/month/year means and up‑sample to 6‑hour intervals with spline interpolation.  &  |
| **Smoothing & shift** | Rolling window (10‑day) smoothing and `shift()` examples for lag features.  |

### 4. Notable Findings  

* **Positive drift:** Average daily arithmetic return ≈ **0.10 %** with positive skew (≈ 0.62) indicating a long right tail.   
* **Volatility clusters:** 30‑day rolling σ shows spikes during 2008‑09 and 2020 market shocks, calming post‑2023.   
* **Seasonality cues:** Quick functions reveal quarter‑on‑quarter acceleration in closing prices since 2020, visible in `visualize_quarter_values()` plots.   

### 5. Next Steps & Ideas  

* Extend feature set with **technical indicators** (SMA, RSI, MACD).  
* Apply **ARIMA / Prophet** forecasting on logarithmic returns.  
* Compare Google with peer tech stocks for **pair‑wise correlation & beta**.  
* Deploy notebook as an **interactive dashboard (e.g., Streamlit)**.


> [!TIP]  
> Link to Next Article  
> 🡺 []()