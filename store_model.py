import pandas as pd

def get_genre(conn):
    return pd.read_sql('''
        SELECT 
            genre_id,name_genre 
        FROM 
            genre 
    ''', conn)

def get_request(conn, min_price,max_price,genre_id):
    return pd.read_sql(f'''
        SELECT title AS Название, name_author AS Автор, price AS Цена
            FROM book
            JOIN author USING (author_id)
            JOIN genre USING (genre_id)
            WHERE price>={min_price} and price<={max_price} and genre_id = {genre_id}          
    ''', conn)


