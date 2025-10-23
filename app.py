import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Configuración minimalista
st.set_page_config(
    page_title="Tablero de Dibujo",
    page_icon="🎨",
    layout="centered"
)

# Estilos CSS minimalistas con un solo color
st.markdown("""
<style>
    .stApp {
        background-color: #fafafa;
    }
    
    .title {
        font-size: 2rem;
        text-align: center;
        color: #4A4A4A;
        margin-bottom: 0.5rem;
        font-weight: 400;
        letter-spacing: -0.5px;
    }
    
    .subtitle {
        text-align: center;
        color: #7A7A7A;
        margin-bottom: 2rem;
        font-size: 1rem;
        font-weight: 300;
    }
    .section-title {
        color: #ffffff;
        font-weight: 500;
        margin-bottom: 0.8rem;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# Títulos
st.markdown('<div class="title">Tablero para dibujo</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Dibuja libremente con las herramientas disponibles</div>', unsafe_allow_html=True)

# Layout principal
col1, col2 = st.columns([1, 2])

with col1:
    with st.sidebar:
        st.markdown("#### Propiedades del Tablero")
        
        # Dimensiones del tablero
        st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Dimensiones del Tablero</div>', unsafe_allow_html=True)
        canvas_width = st.slider("Ancho del tablero", 300, 700, 500, 50)
        canvas_height = st.slider("Alto del tablero", 200, 600, 300, 50)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Herramientas
        st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Configuración de Dibujo</div>', unsafe_allow_html=True)
        drawing_mode = st.selectbox(
            "Herramienta de Dibujo:",
            ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
        )
        stroke_width = st.slider('Selecciona el ancho de línea', 1, 30, 15)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Colores
        st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Colores</div>', unsafe_allow_html=True)
        stroke_color = st.color_picker("Color de trazo", "#000000")
        bg_color = st.color_picker("Color de fondo", "#FFFFFF")
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    # Canvas de dibujo (EXACTAMENTE como en el código original)
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color=bg_color,
        height=canvas_height,
        width=canvas_width,
        drawing_mode=drawing_mode,
        key=f"canvas_{canvas_width}_{canvas_height}",
    )
