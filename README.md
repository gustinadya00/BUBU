# 💌 Pesan untuk Bubu

Prototype website interaktif menggunakan **Python + Streamlit** dengan nuansa playful comic adventure.

## Struktur folder

```text
pesan_untuk_bubu/
├── app.py
├── requirements.txt
└── README.md
```

## Menjalankan secara lokal

Pastikan Python 3.10+ tersedia.

```bash
cd pesan_untuk_bubu
python -m venv .venv
```

Aktifkan environment:

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

Install dependency:

```bash
pip install -r requirements.txt
```

Jalankan:

```bash
streamlit run app.py
```

Browser biasanya terbuka otomatis di:

```text
http://localhost:8501
```

### Demo password

```text
bubu1106
```

## Deployment ke GitHub

1. Buat repository baru di GitHub, misalnya `pesan-untuk-bubu`.
2. Upload `app.py`, `requirements.txt`, dan `README.md`.
3. Atau gunakan Git:

```bash
git init
git add .
git commit -m "Initial Pesan untuk Bubu prototype"
git branch -M main
git remote add origin https://github.com/USERNAME/pesan-untuk-bubu.git
git push -u origin main
```

## Deployment ke Streamlit Community Cloud

1. Login ke Streamlit Community Cloud dengan akun GitHub.
2. Buat/deploy app baru.
3. Pilih repository GitHub `pesan-untuk-bubu`.
4. Branch: `main`.
5. Main file path: `app.py`.
6. Deploy.

## ⚠️ Tentang CONFIDENTIAL

Prototype ini memakai password hard-coded agar langsung bisa dicoba tanpa API key/database.

**Ini bukan security production-grade.** Siapa pun yang bisa melihat source repository dapat melihat password tersebut, dan aplikasi Streamlit publik pada dasarnya dapat diakses oleh siapa saja yang mengetahui URL.

Untuk versi yang benar-benar private, gunakan:
- repository GitHub private,
- Streamlit Secrets untuk menyimpan password,
- autentikasi yang lebih kuat,
- dan kontrol akses pada hosting.

Data surat pada prototype ini disimpan di `st.session_state`, sehingga **tidak menjadi database permanen** dan dapat hilang ketika sesi berakhir/restart.
