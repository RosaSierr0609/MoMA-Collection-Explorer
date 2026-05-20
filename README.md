# MoMA Collection Explorer

Un dashboard interactivo que explora la colección permanente del **Museum of Modern Art (MoMA)** de Nueva York — artistas, orígenes, técnicas y las décadas que dieron forma a uno de los museos más icónicos del mundo.

---

## Sobre el proyecto

El objetivo fue conectar un dataset real a una base de datos en la nube, limpiar y transformar los datos, realizar un análisis exploratorio y construir un dashboard interactivo con Streamlit.

---

## Fuente de datos

Los datasets utilizados en este proyecto están publicados por el **Museum of Modern Art (MoMA)** y están disponibles en el [repositorio de GitHub del MoMA](https://github.com/MuseumofModernArt/collection).

- **Dataset de obras:** 160.435 registros con título, artista, fecha, técnica, dimensiones y fecha de adquisición
- **Dataset de artistas:** 15.905 registros con nombre, nacionalidad, género, año de nacimiento y año de fallecimiento

Ambos datasets están bajo licencia [CC0 1.0 Universal de Dominio Público](https://creativecommons.org/publicdomain/zero/1.0/).

> Este proyecto utiliza los datos de la colección del MoMA "tal como están" con fines de investigación y educación.
> Gran parte de la información no está completa y no ha sido aprobada por los conservadores del MoMA.
> Este proyecto no está respaldado ni afiliado al MoMA.
> Las imágenes no están incluidas en el dataset. Para obtener licencias de imágenes, contacta con
> [Art Resource](http://www.artres.com/) (Norteamérica) o
> [Scala Archives](http://www.scalarchives.com/) (fuera de Norteamérica).

---

## Estructura del dashboard

La app está organizada como una visita al museo, con cuatro salas para explorar:

| Sala | Descripción |
|---|---|
| 🏛️ Entrance Hall | Cifras clave, primera y última adquisición |
| 🌍 Hall of Origins | Mapa mundial de artistas por país de origen |
| 🖼️ Techniques Hall | Treemap de técnicas artísticas en la colección |
| 🔍 The Collection | Busca y filtra obras por artista, década o año |

---

## Tecnologías utilizadas

- **Python** — procesamiento y análisis de datos
- **Pandas** — limpieza y transformación de datos
- **TiDB Cloud** — base de datos en la nube compatible con MySQL
- **Plotly Express** — visualizaciones interactivas
- **Streamlit** — framework de aplicaciones web

---

## Pipeline de datos

1. **SQL** — Tablas creadas en TiDB Cloud (`Artists` como tabla padre, `Artworks` como tabla hija con Foreign Key)
2. **Carga de datos** — CSVs limpiados y subidos mediante `mysql-connector-python` en lotes de 1.000 filas
3. **Preprocesamiento** — Valores nulos tratados, tipos de datos corregidos, fechas parseadas con `pd.to_datetime`
4. **Ingeniería de características** — Nuevas columnas creadas: `MediumCategory` (clasificador de técnicas), `CreditLineCategory` (tipo de adquisición), `Year`, `YearAcquired`, `Decade`, `Country`
5. **EDA** — Análisis univariante y bivariante con Plotly sobre género, nacionalidad, técnicas y tendencias temporales
6. **Exportación** — DataFrame analítico final guardado como `.pkl` para carga rápida en Streamlit

---

## Estructura del proyecto

```
├── app.py                    # Aplicación Streamlit
├── Dataset_MoMa.pkl          # DataFrame analítico (caché local)
├── MoMa_Proyect.ipynb        # Notebook completo del proyecto:
│   ├── SQL queries            #   - Creación de tablas y carga en TiDB Cloud
│   ├── Preprocesamiento       #   - Limpieza, tratamiento de nulos, conversión de tipos
│   ├── Ingeniería de features #   - Nuevas columnas: MediumCategory, CreditLineCategory, Year, Decade, Country
│   └── EDA                    #   - Análisis univariante, bivariante y conclusiones
├── credenciales.py            # Credenciales de la base de datos (no incluido en el repo)
├── logo_MoMA.png              # Logo del MoMA
└── README.md
```

---

## Conclusiones principales

1. **Ludwig Mies van der Rohe domina la colección.** El arquitecto es el artista más representado en el dataset, con una influencia significativa en la distribución temporal de adquisiciones y en el peso de ciertas técnicas.

2. **La colección refleja un fuerte desequilibrio de género.** Las artistas femeninas son una minoría, siendo Louise Bourgeois la más representada. Se observa una tendencia positiva a partir de los años 90.

3. **Las donaciones son el principal método de adquisición.** Más del 60% de las obras entraron en la colección como regalos, lo que refleja una cultura de mecenazgo muy arraigada.

---

## Cómo ejecutarlo en local

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/moma-collection-explorer.git
cd moma-collection-explorer

# Crear y activar el entorno virtual
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows

# Instalar dependencias
pip install streamlit pandas plotly mysql-connector-python

# Ejecutar la app
streamlit run app.py
```

> **Nota:** El archivo `credenciales.py` no está incluido en el repositorio. La app carga los datos desde el archivo `.pkl` local y no requiere conexión a la base de datos para funcionar.

---

## Atribución

Este proyecto utiliza datos del dataset de la colección del MoMA. El MoMA solicita que se reconozca y atribuya activamente su autoría siempre que sea posible. Si utilizas el dataset para una publicación, cítalo usando el identificador de objeto digital disponible en el [repositorio de GitHub del MoMA](https://github.com/MuseumofModernArt/collection).

---

## Demo en vivo

👉 [Ver en Streamlit Cloud](https://moma-collection-explorer-jgskyfvzd6enbjzrcj86je.streamlit.app)
