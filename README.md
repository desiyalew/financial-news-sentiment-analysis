# 📊 Predicting Price Moves with News Sentiment

This project investigates the relationship between financial news sentiment and stock price movements. Conducted as part of Tenx Platform Week 1 with Nova Financial Solutions, the project applies Natural Language Processing (NLP), time-series analytics, and technical indicators to derive actionable insights from financial news data.

---

## 🧠 Project Objective

To enhance Nova Financial Solutions' predictive analytics by:
- Performing sentiment analysis on financial news headlines.
- Correlating sentiment with stock price movements.
- Recommending data-driven trading strategies.

---

## 📁 Dataset Overview

**Financial News and Stock Price Integration Dataset (FNSPID)**  
Fields:
- `headline` - News article title.
- `url` - Article source link.
- `publisher` - News source.
- `date` - Publication date and time (UTC-4).
- `stock` - Ticker symbol (e.g., AAPL, TSLA).

Combined with OHLCV stock price data.

---

## 📌 Key Tasks

### 1. Exploratory Data Analysis (EDA)
- Analyzed headline lengths, article frequency by publisher.
- Identified publishing trends over time.
- Performed keyword analysis and topic modeling (LDA).

### 2. Sentiment Analysis
- Tools: `TextBlob`, `NLTK`
- Classified headlines as Positive, Neutral, or Negative.
- Aggregated daily sentiment per stock.

### 3. Technical Analysis
- Tools: `TA-Lib`, `pynance`
- Calculated indicators: SMA, EMA, RSI, MACD
- Visualized indicator trends alongside price changes.

### 4. Correlation Analysis
- Aligned news and stock price dates.
- Computed daily returns.
- Used Pearson correlation to assess sentiment-return relationships.

---

## 📈 Insights & Recommendations

- Publishers like Bloomberg had stronger influence on stock movement.
- Early morning sentiment scores showed predictive value for daily returns.
- Suggested Strategy: Sentiment-based momentum trading with caution on volatility.

---

## 🛠 Tools & Environment

- **Languages**: Python (Jupyter, Scripts)
- **Libraries**: pandas, nltk, TextBlob, matplotlib, TA-Lib, pynance
- **Version Control**: Git + GitHub
- **CI/CD**: GitHub Actions
- **Structure**:
├── notebooks/
├── src/
├── tests/
├── .github/workflows/
├── README.md
└── requirements.txt

---

## 🚧 Challenges Faced

- Handling timezones in financial data alignment.
- Sentiment model limitations with financial jargon.
- Addressed using preprocessing and smoothing techniques.

---

## 🔮 Future Work

- Implement FinBERT for domain-specific sentiment analysis.
- Explore intraday data and news lag effects.
- Expand feature engineering for multi-day predictive modeling.

---

## 📎 Resources

- [TextBlob](https://textblob.readthedocs.io/en/dev/)
- [TA-Lib Python](https://github.com/ta-lib/ta-lib-python)
- [PyNance](https://github.com/mqandil/pynance)
- [Investopedia](https://www.investopedia.com/terms/s/stockmarket.asp)

---