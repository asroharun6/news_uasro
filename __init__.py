import pandas as pd

def load_media_keywords():
    # Memuat data dari CSV yang berada dalam subfolder 'data'
    data_path = 'data/news_dictionary.csv'  # Sesuaikan path relatif ini
    df = pd.read_csv(data_path)
    return df['keyword'].tolist()  # Asumsi kolom yang berisi kata kunci adalah 'keyword'

media_keywords = load_media_keywords()  # Ini akan memuat kata kunci saat module diimport

def is_media(username):
    return any(keyword.lower() in username.lower() for keyword in media_keywords)
