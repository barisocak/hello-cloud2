from flask import Flask
import os
import psycopg2

app = Flask(__name__)

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://kullanici:sifre@host:port/veritabani"
)

def connect_db():
    return psycopg2.connect(DATABASE_URL)

@app.route("/")
def index():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS ziyaretciler (id SERIAL PRIMARY KEY, isim TEXT)")
    conn.commit()

    cur.execute("INSERT INTO ziyaretciler (isim) VALUES ('Bulut Bilişim')")
    conn.commit()

    cur.execute("SELECT isim FROM ziyaretciler ORDER BY id DESC LIMIT 1")
    son_isim = cur.fetchone()[0]

    cur.close()
    conn.close()

    return f"Merhaba Bulut! Son kayıt: {son_isim}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

