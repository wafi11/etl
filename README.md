# 📰 News ETL Pipeline

Scraping berita dari Detik.com, cleaning data, dan menyimpannya ke DuckDB — lalu di-expose via Flask API.

---

## 🏗️ Struktur Project

```
etl/
├── scrapper/
│   └── detik_com.py     # Scraping artikel dari detik.com
├── transform/
│   └── detik_com.py     # Cleaning & normalisasi data
├── db/
│   └── db.py            # Koneksi & operasi DuckDB
├── data/                # Output CSV sementara
├── main.py              # Entry point pipeline
├── makefile             # Shortcut command
└── .gitignore
```

---

## ⚙️ Flow Pipeline

```
Scraping (requests + BeautifulSoup)
    ↓
Transform (pandas + regex)
    ↓
Load (DuckDB)
    ↓
API (Flask) — coming soon
```

---

## 🚀 Quick Start

**1. Clone & setup environment**

```bash
git clone <repo-url>
cd etl
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**2. Jalanin pipeline**

```bash
make run
# atau
python main.py
```

---

## 🛠️ Tech Stack

| Tool                     | Fungsi                       |
| ------------------------ | ---------------------------- |
| Python                   | Bahasa utama                 |
| requests + BeautifulSoup | Scraping HTML                |
| pandas                   | Cleaning & transformasi data |
| DuckDB                   | Database analitik lokal      |
| Flask                    | REST API (coming soon)       |

---

## 📦 Schema Database

```sql
CREATE TABLE articles (
    id           BIGINT PRIMARY KEY,
    title        VARCHAR,
    url          VARCHAR UNIQUE,
    source       VARCHAR,
    published_at TIMESTAMP,
    scraped_at   TIMESTAMP
);
```

---

## 📊 Contoh Output

```
                                               title        source        published_at
KPK Ungkap Ketum PP Japto Dapat Jatah Bulanan...  news    2026-03-11 21:16:00
Iran Menolak Tampil di Piala Dunia 2026!           sport   2026-03-11 19:45:00
Ancang-ancang Serangan Baru, AS Minta Warga Pe...  news    2026-03-11 20:22:00
```

---

## 📌 Roadmap

- [x] Scraper Detik.com
- [x] Transform & cleaning
- [x] Load ke DuckDB
- [ ] Flask REST API
- [ ] Scheduler (cron / Airflow)
- [ ] Full Text Search

---

> Made by [Wafi](https://github.com/wafi11) — Fullstack Developer & Data Engineer
