import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="MoMA Collection Explorer", layout="wide")

@st.cache_data
def cargar_datos():
    return pd.read_pickle("Dataset_MoMa.pkl")

df = cargar_datos()

st.sidebar.markdown("# MoMA")
st.sidebar.markdown("*Collection Explorer*")
st.sidebar.markdown("---")
st.sidebar.markdown("**Elige una sala para explorar la colección.**")
st.sidebar.markdown("---")

pagina = st.sidebar.radio(
    "",
    ["🏛️ Sala 1: Vestíbulo.", "🌍 Sala 2: Orígenes.", "🖼️ Sala 3: Técnicas.", "🔍 Sala 4: La Colección."]
)

if pagina == "🏛️ Sala 1: Vestíbulo.":
      
    st.title("🏛️ Sala 1: Vestíbulo.")
    st.markdown('Visión general de la colección de MoMA: Cifras claves y primera y última adquisición.')

    col1, col3 = st.columns(2) 
    col2, col4 = st.columns(2)

    col1.metric('Obras en exposición', df['Title'].nunique())
    col2.metric("Artistas", df["Artist"].nunique())
    col3.metric('Técnicas', df['Medium'].nunique())
    col4.metric('Nacionalidad', df['Nationality'].nunique())

    primera_obra = df.loc[df['DateAcquired'].idxmin(), 'Title']
    primera_fecha = df['DateAcquired'].min().strftime('%B %d, %Y')
      
    ultima_obra = df.loc[df['DateAcquired'].idxmax(), 'Title']
    ultima_fecha = df['DateAcquired'].max().strftime('%B %d, %Y')
      
    col_primera, col_ultima = st.columns(2)
      
    with col_primera:
        st.metric(label="Primera adquisión.", value=primera_obra)
        st.caption(f"*{primera_fecha}*")
    with col_ultima:
        st.metric(label="Última adquisión.", value=ultima_obra)
        st.caption(f"*{ultima_fecha}*")

df_filtrado = df.copy()
if pagina == "🌍 Sala 2: Orígenes.":
    nacionalidad_a_pais = {
    'American': 'United States',
    'French': 'France',
    'German': 'Germany',
    'British': 'United Kingdom',
    'Spanish': 'Spain',
    'Italian': 'Italy',
    'Japanese': 'Japan',
    'Russian': 'Russia',
    'Swiss': 'Switzerland',
    'Dutch': 'Netherlands',
    'Mexican': 'Mexico',
    'Belgian': 'Belgium',
    'Argentine': 'Argentina',
    'Austrian': 'Austria',
    'Brazilian': 'Brazil',
    'Canadian': 'Canada',
    'Colombian': 'Colombia',
    'Czech': 'Czech Republic',
    'Chilean': 'Chile',
    'Hungarian': 'Hungary',
    'Polish': 'Poland',
    'Danish': 'Denmark',
    'Venezuelan': 'Venezuela',
    'Ivorian': 'Ivory Coast',
    'South African': 'South Africa',
    'Chinese': 'China',
    'Swedish': 'Sweden',
    'Israeli': 'Israel',
    'Croatian': 'Croatia',
    'Trinidad and Tobagonian': 'Trinidad and Tobago',
    'Australian': 'Australia',
    'Indian': 'India',
    'Cuban': 'Cuba',
    'Finnish': 'Finland',
    'Serbian': 'Serbia',
    'Norwegian': 'Norway',
    'Portuguese': 'Portugal',
    'Peruvian': 'Peru',
    'Ukrainian': 'Ukraine',
    'Uruguayan': 'Uruguay',
    'Egyptian': 'Egypt',
    'Korean': 'South Korea',
    'Guatemalan': 'Guatemala',
    'Nigerian': 'Nigeria',
    'Romanian': 'Romania',
    'Slovak': 'Slovakia',
    'Puerto Rican': 'Puerto Rico',
    'Greek': 'Greece',
    'Latvian': 'Latvia',
    'Lebanese': 'Lebanon',
    'Sudanese': 'Sudan',
    'Costa Rican': 'Costa Rica',
    'Georgian': 'Georgia',
    'Slovenian': 'Slovenia',
    'Scottish': 'United Kingdom',
    'Icelandic': 'Iceland',
    'Turkish': 'Turkey',
    'Pakistani': 'Pakistan',
    'Thai': 'Thailand',
    'Luxembourger': 'Luxembourg',
    'Irish': 'Ireland',
    'Sri Lankan': 'Sri Lanka',
    'Iranian': 'Iran',
    'Haitian': 'Haiti',
    'Albanian': 'Albania',
    'Congolese': 'Democratic Republic of the Congo',
    'Malian': 'Mali',
    'Bosnian': 'Bosnia and Herzegovina',
    'Lithuanian': 'Lithuania',
    'Moroccan': 'Morocco',
    'Kenyan': 'Kenya',
    'Zimbabwean': 'Zimbabwe',
    'Tanzanian': 'Tanzania',
    'Cameroonian': 'Cameroon',
    'South Korean': 'South Korea',
    'Palestinian': 'Palestine',
    'Iraqi': 'Iraq',
    'Macedonian': 'North Macedonia',
    'Tunisian': 'Tunisia',
    'New Zealander': 'New Zealand',
    'Bulgarian': 'Bulgaria',
    'Ecuadorian': 'Ecuador',
    'Bangladeshi': 'Bangladesh',
    'Ghanaian': 'Ghana',
    'Vietnamese': 'Vietnam',
    'Cambodian': 'Cambodia',
    'Ethiopian': 'Ethiopia',
    'English': 'United Kingdom',
    'Emirati': 'United Arab Emirates',
    'Panamanian': 'Panama',
    'Bolivian': 'Bolivia',
    'Nicaraguan': 'Nicaragua',
    'Malaysian': 'Malaysia',
    'Uzbekistani': 'Uzbekistan',
    'Welsh': 'United Kingdom',
    'Bahamian': 'Bahamas',
    'Filipino': 'Philippines',
    'Senegalese': 'Senegal',
    'Taiwanese': 'Taiwan',
    'Czechoslovakian': 'Czech Republic',
    'Mozambican': 'Mozambique',
    'Salvadoran': 'El Salvador',
    'Indonesian': 'Indonesia',
    'Algerian': 'Algeria',
    'Beninese': 'Benin',
    'Estonian': 'Estonia',
    'Singaporean': 'Singapore',
    'Syrian': 'Syria',
    'Nepali': 'Nepal',
    'Paraguayan': 'Paraguay',
    'Azerbaijani': 'Azerbaijan',
    'Namibian': 'Namibia',
    'Jamaican': 'Jamaica',
    'Afghan': 'Afghanistan',
    'Ugandan': 'Uganda',
    'Catalan': 'Spain',
    'Yugoslavian': 'Serbia',
    'Persian': 'Iran',
    'Sierra Leonean': 'Sierra Leone',
    'Kuwaiti': 'Kuwait',
    'Burkinabé': 'Burkina Faso',
} 
    
    st.title("🌍 Sala 2: Orígenes.")
    st.markdown('Un mapa mundial de los artistas del MoMA: busca un artista y descubre su país de origen.')

    df_filtrado['Country'] = df_filtrado['Nationality'].map(nacionalidad_a_pais)
    col_filtro, col_info = st.columns(2)

    with col_filtro:
        artista = st.selectbox(
            "Busca un artista",
            options=['All Artists'] + sorted(df_filtrado['Artist'].unique().tolist())
        )

    with col_info:
        if artista != 'All Artists':
            pais = df_filtrado[df_filtrado['Artist'] == artista]['Country'].values[0]
            nacionalidad = df_filtrado[df_filtrado['Artist'] == artista]['Nationality'].values[0] 
            st.metric(label="Origen", value=pais)
            st.caption(f"Nacionalidad: {nacionalidad}")
    
    if artista == 'All Artists':
        datos_mapa = df_filtrado.dropna(subset=['Country']).groupby('Country')['Artist'].nunique().reset_index()
    else:
        datos_mapa = df_filtrado[df_filtrado['Artist'] == artista].dropna(subset=['Country']).groupby('Country')['Artist'].count().reset_index()

    if datos_mapa.empty:
        st.warning("Localización no encontrada.")
    else:
        fig = px.choropleth(
            datos_mapa,
            locations='Country',
            locationmode='country names',
            color='Artist',
            title='Artista por pais' if artista == 'All Artists' else f"{artista}'s Origin",
            color_continuous_scale=['#F5E6D3', '#C1440E']
        )
        fig.update_layout(height=600)
        st.plotly_chart(fig, use_container_width=True)

if pagina == "🖼️ Sala 3: Técnicas.":

    st.title("🖼️ Sala 3: Técnicas.")
    st.markdown('Visualización de las técnicas artísticas presentes en la colección.')

    medium_info = df.groupby('MediumCategory').agg(
        Artworks=('Title', 'count'),
        Artists=('Artist', 'nunique'),
        Top_Artist=('Artist', lambda x: x.value_counts().index[0])
    ).reset_index()

    fig = px.treemap(
        medium_info,
        path=['MediumCategory'],
        values='Artworks',
        title='Técnicas por artista',
        color='Artworks',
        color_continuous_scale=['#F5E6D3', '#C1440E'],
        hover_data={
            'Artists': True,
            'Top_Artist': True
        }
    )
    fig.update_layout(height=600)
    st.plotly_chart(fig, use_container_width=True)

if pagina == "🔍 Sala 4: La Colección.":
    
    st.title("🔍 Sala 4: La Colección.")
    st.markdown('Busca y filtra la colección por artista y década de adquisión.')

    col_f1, col_f2, col_f3 = st.columns(3)
    with col_f1:
        artista = st.selectbox(
            "Artista.",
            options=['All'] + sorted(df['Artist'].unique().tolist())
        )
    
    with col_f2:
        decade = st.selectbox(
            "Década.",
            options=['All'] + sorted(df['Decade'].dropna().unique().tolist())
        )
    
    with col_f3:
        year = st.selectbox(
            "Año.",
            options=['All'] + sorted(df['YearAcquired'].dropna().unique().tolist())
        )
    
    if artista != 'All':
        df_filtrado = df_filtrado[df_filtrado['Artist'] == artista]
    if decade != 'All':
        df_filtrado = df_filtrado[df_filtrado['Decade'] == decade]
    if year != 'All':
        df_filtrado = df_filtrado[df_filtrado['YearAcquired'] == year]
    
    st.markdown(f"**{len(df_filtrado)} artworks found**")
    st.dataframe(df_filtrado[['Title', 'Artist', 'Date', 'MediumCategory', 'Department', 'YearAcquired']])