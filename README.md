# MoMA Collection Explorer

An interactive data dashboard that explores the permanent collection of the **Museum of Modern Art (MoMA)** in New York — artists, origins, techniques, and the decades that shaped one of the world's most iconic museums.

---

## About the Project

This project was built as the final project for the Business Intelligence module of a Data Analytics bootcamp. The goal was to connect a real-world dataset to a cloud database, clean and transform the data, perform an exploratory data analysis, and build an interactive Streamlit dashboard.

---

## Data Source

The datasets used in this project are published by the **Museum of Modern Art (MoMA)** and are available at the [MoMA GitHub repository](https://github.com/MuseumofModernArt/collection).

- **Artworks dataset:** 160,435 records with title, artist, date, medium, dimensions and acquisition date
- **Artists dataset:** 15,905 records with name, nationality, gender, birth and death year

Both datasets are licensed under [CC0 1.0 Universal Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/).

> This project uses the MoMA collection data "as is" for research and educational purposes.
> Much of the information is not complete and has not been curatorially approved by MoMA.
> This project is not endorsed by or affiliated with MoMA.
> Images are not included in the dataset. To license images please contact
> [Art Resource](http://www.artres.com/) (North America) or
> [Scala Archives](http://www.scalarchives.com/) (outside North America).

---

## Dashboard Structure

The app is organized as a museum visit, with four rooms to explore:

| Room | Description |
|---|---|
| 🏛️ Entrance Hall | Key figures, first and last acquisitions |
| 🌍 Hall of Origins | World map of artists by country of origin |
| 🖼️ Techniques Hall | Treemap of artistic techniques in the collection |
| 🔍 The Collection | Search and filter artworks by artist, decade or year |

---

## Tech Stack

- **Python** — data processing and analysis
- **Pandas** — data cleaning and transformation
- **TiDB Cloud** — cloud MySQL-compatible database
- **Plotly Express** — interactive visualizations
- **Streamlit** — web application framework

---

## Data Pipeline

1. **SQL** — Tables created in TiDB Cloud (`Artists` as parent, `Artworks` as child with Foreign Key)
2. **Data upload** — CSVs cleaned and uploaded via `mysql-connector-python` in batches of 1000 rows
3. **Preprocessing** — Null values handled, data types corrected, dates parsed with `pd.to_datetime`
4. **Feature engineering** — New columns created: `MediumCategory` (technique classifier), `CreditLineCategory` (acquisition type), `Year`, `YearAcquired`, `Decade`, `Country`
5. **EDA** — Univariate and bivariate analysis with Plotly, covering gender, nationality, techniques and temporal trends
6. **Export** — Final analytical DataFrame saved as `.pkl` for fast loading in Streamlit

---

## Project Structure

```
├── app.py                    # Streamlit application
├── Dataset_MoMa.pkl          # Analytical DataFrame (local cache)
├── MoMa_Proyect.ipynb        # Full project notebook:
│   ├── SQL queries            #   - Table creation and data upload to TiDB Cloud
│   ├── Data preprocessing     #   - Cleaning, null handling, type conversion
│   ├── Feature engineering    #   - New columns: MediumCategory, CreditLineCategory, Year, Decade, Country
│   └── EDA                    #   - Univariate, bivariate analysis and key findings
├── credenciales.py            # Database credentials (not included in repo)
└── README.md
```

---

## Key Findings

1. **Ludwig Mies van der Rohe dominates the collection.** The architect is the most represented artist in the dataset, significantly influencing the temporal distribution of acquisitions and the weight of certain techniques.

2. **The collection reflects a strong gender imbalance.** Female artists are a minority, with Louise Bourgeois as the most represented. A positive trend is observed from the 1990s onwards.

3. **Donations are the primary acquisition method.** Over 60% of works entered the collection as gifts, reflecting a deeply rooted culture of patronage.

---

## How to Run Locally

```bash
# Clone the repository
git clone https://github.com/your-username/moma-collection-explorer.git
cd moma-collection-explorer

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows

# Install dependencies
pip install streamlit pandas plotly mysql-connector-python

# Run the app
streamlit run app.py
```

> **Note:** The `credenciales.py` file is not included in the repository. The app loads data from the local `.pkl` file and does not require a database connection to run.

---

## Attribution

This project uses data from the MoMA collection dataset. MoMA requests that you actively acknowledge and give attribution to MoMA wherever possible. If you use the dataset for a publication, please cite it using the digital object identifier provided in the [MoMA GitHub repository](https://github.com/MuseumofModernArt/collection).

---

## Live Demo

👉 [View on Streamlit Cloud](https://moma-collection-explorer-jgskyfvzd6enbjzrcj86je.streamlit.app)
