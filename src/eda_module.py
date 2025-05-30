import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import re

def analyze_headline_length(df, column='headline'):
    df['headline_length'] = df[column].astype(str).apply(len)
    print("\nHeadline Length Statistics:")
    print(df['headline_length'].describe())

def articles_per_publisher(df, column='publisher'):
    print("\nArticle Counts Per Publisher:")
    print(df[column].value_counts())
    df[column].value_counts().plot(kind='barh', figsize=(10, 6), title="Articles Per Publisher")
    plt.xlabel("Number of Articles")
    plt.ylabel("Publisher")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()

def analyze_publication_dates(df, date_col='date'):
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    print("\nPublication Date Range:", df[date_col].min(), "to", df[date_col].max())
    df.set_index(date_col).resample('D').size().plot(figsize=(12, 4), title="Articles Published Over Time")
    plt.xlabel("Date")
    plt.ylabel("Number of Articles")
    plt.tight_layout()
    plt.show()

def perform_topic_modeling(df, column='headline', num_topics=5):
    print("\nPerforming Topic Modeling...")
    vectorizer = CountVectorizer(stop_words='english', max_df=0.9, min_df=2)
    X = vectorizer.fit_transform(df[column].astype(str))
    lda = LatentDirichletAllocation(n_components=num_topics, random_state=42)
    lda.fit(X)
    feature_names = vectorizer.get_feature_names_out()
    for topic_idx, topic in enumerate(lda.components_):
        top_keywords = [feature_names[i] for i in topic.argsort()[-10:]]
        print(f"\nTopic #{topic_idx + 1}: {', '.join(top_keywords)}")

def plot_publication_frequency(df, date_col='date'):
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    daily_counts = df.groupby(df[date_col].dt.date).size()
    plt.figure(figsize=(12, 4))
    daily_counts.plot()
    plt.title("Daily Publication Frequency")
    plt.xlabel("Date")
    plt.ylabel("Number of Articles")
    plt.tight_layout()
    plt.show()

def analyze_publishing_times(df, date_col='date'):
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    df['hour'] = df[date_col].dt.hour
    print("\nPublishing Frequency by Hour:")
    df['hour'].value_counts().sort_index().plot(kind='bar', figsize=(10, 4))
    plt.xlabel("Hour of Day")
    plt.ylabel("Number of Articles")
    plt.title("Publishing Times")
    plt.tight_layout()
    plt.show()

def analyze_publishers(df, publisher_col='publisher'):
    print("\nTop 10 Publishers:")
    print(df[publisher_col].value_counts().head(10))

def analyze_publisher_domains(df, publisher_col='publisher'):
    df['domain'] = df[publisher_col].astype(str).apply(lambda x: re.search(r'@([\w\.-]+)', x).group(1) if '@' in x else None)
    domain_counts = df['domain'].value_counts().dropna().head(10)
    print("\nTop Email Domains (if applicable):")
    print(domain_counts)
    domain_counts.plot(kind='barh', figsize=(8, 5), title="Top Publisher Email Domains")
    plt.xlabel("Number of Articles")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()

def plot_wordcloud(df, text_column='headline'):
    text_data = " ".join(df[text_column].dropna().astype(str).tolist())
    wordcloud = WordCloud(width=800, height=400, background_color='white', stopwords=STOPWORDS).generate(text_data)
    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title("Word Cloud of Headlines")
    plt.show()

def filter_by_recent_days(df, date_column='date', days=30):
    df[date_column] = pd.to_datetime(df[date_column], errors='coerce')
    recent_date_threshold = pd.Timestamp.today() - pd.Timedelta(days=days)
    filtered_df = df[df[date_column] >= recent_date_threshold]
    print(f"\nFiltered data to last {days} days: {len(filtered_df)} rows")
    return filtered_df

def export_to_csv(df, filename="eda_results.csv"):
    df.to_csv(filename, index=False)
    print(f"Exported EDA results to {filename}")

def export_to_excel(df, filename="eda_results.xlsx"):
    df.to_excel(filename, index=False)
    print(f"Exported EDA results to {filename}")

def run_full_eda(df):
    analyze_headline_length(df)
    articles_per_publisher(df)
    analyze_publication_dates(df)
    perform_topic_modeling(df)
    plot_publication_frequency(df)
    analyze_publishing_times(df)
    analyze_publishers(df)
    analyze_publisher_domains(df)
    plot_wordcloud(df)
    recent_df = filter_by_recent_days(df, days=30)
    export_to_csv(recent_df, "recent_headlines.csv")
    export_to_excel(recent_df, "recent_headlines.xlsx")
