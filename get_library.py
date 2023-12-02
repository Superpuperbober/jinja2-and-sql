from jinja2  import Environment, FileSystemLoader
import sqlite3
from store_model import get_genre, get_request

 #то что мы будем кидать в запрос
GENRE_ID = 2
MAX_PRICE = 600
MIN_PRICE = 300
conn = sqlite3.connect("store.sqlite")

with open("store.db", "r", encoding ='utf-8-sig') as f:
    script = f.read()

conn.executescript(script)

df_request = get_request(conn, MIN_PRICE,MAX_PRICE,GENRE_ID)
df_genre = get_genre(conn)

conn.close()

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('templ.html')

result_html = template.render(
    df_request = df_request,
    df_genre = df_genre,
    min_price = MIN_PRICE,
    max_price = MAX_PRICE,
    genre_id = GENRE_ID,
)

with open('result.html', 'w', encoding ='utf-8-sig') as f:
    print(result_html, file=f)