import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Veritabanı bağlantısı
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()


# Tablo oluşturma
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS sleep_data
                  (date text, hours int)''')

# Verileri tabloya ekleme
while True:
    date = input("Tarih (YYYY-MM-DD): ")
    if not date:
        break
    hours = int(input("Kaç saat uyudun: "))
    cursor.execute("INSERT INTO sleep_data (date, hours) VALUES (?, ?)", (date, hours))

    # Değişiklikleri kaydetme
    conn.commit()

# Verileri okuma
df = pd.read_sql_query("SELECT * from sleep_data", conn)

# Grafik oluşturma
sns.lineplot(data=df, x='date', y='hours', marker='o')

# Grafik başlığı ve eksen etiketleri ekleme
plt.title('Uyku Düzeni')
plt.xlabel('Tarih')
plt.ylabel('Uyku Saati')

# Grafiği ekranda gösterme
plt.show()

# Veritabanı bağlantısını kapatma
conn.close()
