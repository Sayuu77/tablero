import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Configuración de la página
st.set_page_config(
    page_title="Tablero de Dibujo Creativo",
    page_icon="🎨",
    layout="wide"
)

# Estilos CSS con tema pastel
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    .main-title {
        font-size: 3rem;
        text-align: center;
        color: #6c5ce7;
        margin-bottom: 1rem;
        font-weight: 700;
        text-shadow: 2px 2px 4px rgba(108, 92, 231, 0.2);
    }
    
    .subtitle {
        text-align: center;
        color: #a29bfe;
        margin-bottom: 2rem;
        font-size: 1.2rem;
        font-weight: 300;
    }
    
    .sidebar-content {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 20px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 2px solid #ffeaa7;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
    }
    
    .canvas-container {
        background: white;
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem;
        border: 3px solid #fd79a8;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
        text-align: center;
    }
    
    .stSlider > div > div {
        background: linear-gradient(90deg, #74b9ff, #a29bfe);
    }
    
    .stSelectbox > div > div {
        background: white;
        border: 2px solid #ffeaa7;
        border-radius: 12px;
    }
    
    .stColorPicker > div > div {
        border: 2px solid #dfe6e9;
        border-radius: 12px;
    }
    
    .property-title {
        color: #6c5ce7;
        font-weight: 600;
        margin-bottom: 0.5rem;
        font-size: 1.1rem;
    }
    
    .dimension-display {
        background: linear-gradient(135deg, #74b9ff, #a29bfe);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 10px;
        text-align: center;
        margin: 0.5rem 0;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# Título principal
st.markdown('<div class="main-title">🎨 Tablero de Dibujo Creativo</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Libera tu creatividad con esta herramienta de dibujo interactiva</div>', unsafe_allow_html=True)

# Layout principal
col1, col2 = st.columns([1, 2])

with col1:
    with st.sidebar:
        st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
        st.markdown("### ⚙️ Propiedades del Tablero")
        
        # Dimensiones del canvas
        st.markdown('<div class="property-title">📐 Dimensiones del Tablero</div>', unsafe_allow_html=True)
        canvas_width = st.slider("**Ancho del tablero**", 300, 700, 500, 50)
        canvas_height = st.slider("**Alto del tablero**", 200, 600, 300, 50)
        
        # Mostrar dimensiones actuales
        st.markdown(f'<div class="dimension-display">Tamaño actual: {canvas_width} × {canvas_height}</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
        st.markdown("### 🖌️ Herramientas de Dibujo")
        
        # Modo de dibujo
        st.markdown('<div class="property-title">🔧 Herramienta de Dibujo</div>', unsafe_allow_html=True)
        drawing_mode = st.selectbox(
            "Selecciona la herramienta:",
            ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
            label_visibility="collapsed"
        )
        
        # Grosor del trazo
        st.markdown('<div class="property-title">📏 Ancho de Línea</div>', unsafe_allow_html=True)
        stroke_width = st.slider('Selecciona el grosor del trazo', 1, 30, 15, label_visibility="collapsed")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
        st.markdown("### 🎨 Paleta de Colores")
        
        # Color del trazo
        st.markdown('<div class="property-title">✏️ Color del Trazo</div>', unsafe_allow_html=True)
        stroke_color = st.color_picker("Elige el color para dibujar", "#6C5CE7", label_visibility="collapsed")
        
        # Color de fondo
        st.markdown('<div class="property-title">🏞️ Color de Fondo</div>', unsafe_allow_html=True)
        bg_color = st.color_picker("Elige el color de fondo", "#FFFFFF", label_visibility="collapsed")
        
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="canvas-container">', unsafe_allow_html=True)
    st.markdown("### 🎨 Tu Lienzo Creativo")
    
    # Canvas de dibujo
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color=bg_color,
        height=canvas_height,
        width=canvas_width,
        drawing_mode=drawing_mode,
        key=f"canvas_{canvas_width}_{canvas_height}",
        display_toolbar=True
    )
    
    # Información adicional debajo del canvas
    col_info1, col_info2, col_info3 = st.columns(3)
    with col_info1:
        st.metric("Herramienta Actual", drawing_mode.capitalize())
    with col_info2:
        st.metric("Grosor del Trazo", stroke_width)
    with col_info3:
        st.metric("Tamaño", f"{canvas_width}×{canvas_height}")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer decorativo
st.markdown("""
<div style="text-align: center; color: #a29bfe; margin-top: 3rem; padding: 2rem;">
    <p style="font-size: 0.9rem;">✨ Creado con amor para artistas digitales ✨</p>
</div>
""", unsafe_allow_html=True)
