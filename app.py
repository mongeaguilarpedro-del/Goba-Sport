import base64
from datetime import datetime
import os
import sqlite3
import streamlit as st


# Función para cargar imagen local como fondo en CSS
def get_base64_image(image_path):
  if os.path.exists(image_path):
    with open(image_path, "rb") as img_file:
      return base64.b64encode(img_file.read()).decode()
  return None


# Buscador de logo
logo_encontrado = None
try:
  for archivo in os.listdir("."):
    if archivo.lower().startswith("logo"):
      logo_encontrado = archivo
      break
except Exception:
  pass

# Configuración de página
st.set_page_config(
    page_title="GOBA Sport",
    page_icon=logo_encontrado if logo_encontrado else "🏆",
    layout="wide",
)

# Carga de fondo local o fallback web con un estadio de fútbol profesional muy llamativo
bg_base64 = get_base64_image("fondo_estadio.jpg")
if not bg_base64:
  bg_base64 = get_base64_image("fondo_estadio.png")

if bg_base64:
  bg_css = f"data:image/jpg;base64,{bg_base64}"
else:
  # Fondo de estadio de alta calidad y impacto visual
  bg_css = "https://images.unsplash.com/photo-1518063319789-7217e6adc85e?q=80&w=1920&auto=format&fit=crop"

# Estilos CSS avanzados con tipografía Inter y el fondo deportivo
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Inter', sans-serif;
    }}

    .stApp {{
        background-color: #0d1117;
        background-image: linear-gradient(rgba(13, 17, 23, 0.82), rgba(13, 17, 23, 0.90)), 
                          url('{bg_css}');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #e6edf3;
    }}
    
    section[data-testid="stSidebar"] {{
        background-color: #161b22;
        border-right: 1px solid #30363d;
    }}

    div[data-testid="stVerticalBlock"] > div[style*="border"] {{
        background-color: rgba(22, 27, 34, 0.85) !important;
        border: 1px solid #30363d !important;
        border-radius: 10px !important;
        box-shadow: 0 8px 16px rgba(0,0,0,0.6);
    }}

    .stButton button {{
        border-radius: 8px;
        font-weight: 600;
        letter-spacing: 0.3px;
        transition: all 0.3s ease;
    }}
    
    .stButton button:hover {{
        border-color: #238636;
        color: #238636;
        transform: translateY(-1px);
    }}
    
    .stTextInput input, .stSelectbox select, .stNumberInput input {{
        background-color: #161b22 !important;
        border-color: #30363d !important;
        color: #e6edf3 !important;
        border-radius: 6px !important;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)


# Función para inicializar base de datos
def init_db():
  conn = sqlite3.connect("indumentaria_clubes.db")
  cursor = conn.cursor()
  cursor.execute("""
        CREATE TABLE IF NOT EXISTS clubes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            contacto TEXT
        )
    """)
  cursor.execute("""
        CREATE TABLE IF NOT EXISTS pedidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            club_id INTEGER,
            tipo_prenda TEXT,
            cantidad INTEGER,
            talle TEXT,
            estado TEXT,
            fecha TEXT,
            precio_total REAL DEFAULT 0,
            monto_pagado REAL DEFAULT 0,
            FOREIGN KEY(club_id) REFERENCES clubes(id)
        )
    """)
  conn.commit()
  conn.close()


init_db()

# Encabezado
col_head1, col_head2 = st.columns([3, 1])
with col_head1:
  st.title("GOBA Sport")
  st.caption(
      "🏆 Indumentaria Deportiva Profesional para Clubes e Instituciones"
  )

if logo_encontrado:
  st.sidebar.image(logo_encontrado, use_container_width=True)
else:
  st.sidebar.warning("⚠️ No se encontró un archivo de logo.")

st.sidebar.markdown("---")

# Menú de navegación simplificado
menu = [
    "⭐ Catálogo y Guía de Pedidos",
    "🛡️ Registrar Club",
    "📋 Cargar Nuevo Pedido",
    "📈 Mis Pedidos y Seguimiento",
]
choice = st.sidebar.selectbox("Menú de Navegación", menu)
st.sidebar.markdown("---")

# Número de WhatsApp configurado: 3533-680073
telefono_contacto = "5493533680073"
mensaje_wa = "Hola! Te escribo desde GOBA Sport para consultar un pedido..."
link_whatsapp = (
    f"https://wa.me/{telefono_contacto}?text={mensaje_wa.replace(' ', '%20')}"
)

st.sidebar.markdown("### 💬 Soporte del Taller")
st.sidebar.markdown(
    f"""
    <a href="{link_whatsapp}" target="_blank" style="text-decoration: none;">
        <div style="
            background-color: #238636; 
            color: white; 
            padding: 10px 15px; 
            border-radius: 8px; 
            text-align: center; 
            font-weight: 600; 
            font-size: 14px;
            box-shadow: 0 4px 10px rgba(35, 134, 54, 0.3);">
            📲 Contactar por WhatsApp
        </div>
    </a>
    """,
    unsafe_allow_html=True,
)

st.sidebar.markdown("---")
st.sidebar.info("⚡ **GOBA Sport**\nCalidad y diseño para tu equipo.")

# ---------------------------------------------------------
# 0. CATÁLOGO
# ---------------------------------------------------------
if choice == "⭐ Catálogo y Guía de Pedidos":
  st.subheader("⭐ Bienvenid@s a GOBA Sport")
  st.markdown(
      "Conocé nuestra oferta de indumentaria deportiva personalizada y los"
      " pasos para encargar la ropa de tu club."
  )
  st.markdown("---")
  st.markdown("### 🥇 Líneas de Fabricación")

  col_cat1, col_cat2, col_cat3 = st.columns(3)
  with col_cat1:
    with st.container(border=True):
      st.markdown("#### 🎽 Equipaciones Oficiales")
      st.markdown(
          "- Camisetas Titulares y Suplentes\n- Shorts y Pantalones cortos\n-"
          " Medias y conjuntos de arquero\n- *Telas antitranspirantes"
          " Microfit.*"
      )
  with col_cat2:
    with st.container(border=True):
      st.markdown("#### 🧥 Abrigo y Entrenamiento")
      st.markdown(
          "- Camperas de frisa / Impermeables\n- Buzos deportivos de salida\n-"
          " Pantalones chupín y entrenamiento\n- *Acabados térmicos y de gran"
          " durabilidad.*"
      )
  with col_cat3:
    with st.container(border=True):
      st.markdown("#### ⚽ Accesorios y Equipo")
      st.markdown(
          "- Pecheras para entrenamiento\n- Indumentaria para cuerpo"
          " técnico\n- Banderines y bolsos personalizados"
      )

  st.markdown("---")
  st.markdown("### 📌 ¿Cómo hacer tu pedido en 3 pasos?")
  st.info(
      "**1. Registrá tu Club:** Ingresá en el menú lateral a **'Registrar"
      " Club'** para dar de alta la institución.\n\n"
      "**2. Cargar el Pedido:** Seleccioná las prendas, cantidades, curvas de"
      " talles y la fecha de entrega deseada en **'Cargar Nuevo"
      " Pedido'**.\n\n"
      "**3. Seguimiento e Impresión:** Consultá el estado en tiempo real de tu"
      " indumentaria y generá comprobantes por WhatsApp."
  )

# ---------------------------------------------------------
# 1. REGISTRAR CLUB
# ---------------------------------------------------------
elif choice == "🛡️ Registrar Club":
  st.subheader("🛡️ Registro de Nueva Institución Deportiva")
  st.markdown(
      "Agregá los datos del club para poder asignarle pedidos de indumentaria."
  )

  with st.form("form_club", border=True):
    nombre_club = st.text_input(
        "Nombre del Club / Institución (Ej: Club Atlético Talleres)"
    )
    contacto = st.text_input("Teléfono o Persona de Contacto")
    submitted = st.form_submit_button(
        "💾 Guardar Club", use_container_width=True
    )

    if submitted:
      if not nombre_club.strip():
        st.warning("⚠️ Por favor ingresá el nombre del club.")
      else:
        conn = sqlite3.connect("indumentaria_clubes.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO clubes (nombre, contacto) VALUES (?, ?)",
            (nombre_club.strip(), contacto.strip()),
        )
        conn.commit()
        conn.close()
        st.success(
            f"¡Club '{nombre_club}' registrado con éxito en la base de datos!"
        )

# ---------------------------------------------------------
# 2. CARGAR NUEVO PEDIDO
# ---------------------------------------------------------
elif choice == "📋 Cargar Nuevo Pedido":
  st.subheader("📋 Cargar Nuevo Pedido de Indumentaria")

  conn = sqlite3.connect("indumentaria_clubes.db")
  cursor = conn.cursor()
  cursor.execute("SELECT id, nombre FROM clubes")
  clubes = cursor.fetchall()
  conn.close()

  if not clubes:
    st.warning(
        "⚠️ Primero debes registrar un club en la sección 'Registrar Club'."
    )
  else:
    club_dict = {c[1]: c[0] for c in clubes}

    with st.form("form_pedido", border=True):
      col_a, col_b = st.columns(2)
      with col_a:
        club_seleccionado = st.selectbox(
            "🛡️ Seleccionar Club Deportivo", list(club_dict.keys())
        )
        tipo_prenda = st.selectbox(
            "👕 Tipo de Prenda",
            [
                "👕 Conjuntos deportivos",
                "👕 Remeras",
                "👖 Pantalones",
                "🧥 Camperas",
                "🧥 Buzos",
            ],
        )
        cantidad = st.number_input(
            "📦 Cantidad total de unidades", min_value=1, value=10
        )
        talle = st.selectbox(
            "📏 Curva de talles / Detalle",
            ["S - M - L - XL", "Infantiles", "Mixto"],
        )

      with col_b:
        fecha_entrega = st.date_input("📅 Fecha estimada requerida")
        precio_total = st.number_input(
            "💰 Presupuesto / Precio Total ($)",
            min_value=0.0,
            value=0.0,
            step=1000.0,
        )
        monto_pagado = st.number_input(
            "💵 Seña abonada ($)", min_value=0.0, value=0.0, step=1000.0
        )

      submitted_pedido = st.form_submit_button(
          "🚀 Confirmar y Registrar Pedido", use_container_width=True
      )

      if submitted_pedido:
        c_id = club_dict[club_seleccionado]
        conn = sqlite3.connect("indumentaria_clubes.db")
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO pedidos (club_id, tipo_prenda, cantidad, talle, estado, fecha, precio_total, monto_pagado) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                c_id,
                tipo_prenda,
                cantidad,
                talle,
                "Pendiente",
                str(fecha_entrega),
                precio_total,
                monto_pagado,
            ),
        )
        conn.commit()
        conn.close()
        st.success("¡Pedido registrado correctamente en el sistema!")

# ---------------------------------------------------------
# 3. VER, ACTUALIZAR Y CANCELAR PEDIDOS
# ---------------------------------------------------------
elif choice == "📈 Mis Pedidos y Seguimiento":
  st.subheader("📈 Panel de Seguimiento de Pedidos")

  conn = sqlite3.connect("indumentaria_clubes.db")
  cursor = conn.cursor()
  cursor.execute("""
        SELECT pedidos.id, clubes.nombre, pedidos.tipo_prenda, pedidos.cantidad, 
               pedidos.talle, pedidos.estado, pedidos.fecha, pedidos.precio_total, pedidos.monto_pagado
        FROM pedidos 
        JOIN clubes ON pedidos.club_id = clubes.id
        ORDER BY pedidos.fecha ASC
    """)
  pedidos = cursor.fetchall()
  conn.close()

  if not pedidos:
    st.info("📭 No hay pedidos cargados en el sistema todavía.")
  else:
    for p in pedidos:
      p_id, c_nombre, prenda, cant, talle, estado, fecha, p_total, p_pagado = p
      p_total = p_total or 0.0
      p_pagado = p_pagado or 0.0
      saldo = p_total - p_pagado

      with st.container(border=True):
        if estado == "Pendiente":
          icono_estado = "⏳"
        elif estado == "En producción":
          icono_estado = "⚙️"
        elif estado == "Listo para entrega":
          icono_estado = "📦"
        else:
          icono_estado = "✅"

        st.markdown(
            f"### 🔖 Pedido #{p_id} — **{c_nombre}** &nbsp;&nbsp;|&nbsp;&nbsp;"
            f" {icono_estado} *{estado}*"
        )

        col_m1, col_m2, col_m3, col_m4 = st.columns(4)
        col_m1.metric("Prenda", prenda)
        col_m2.metric("Cantidad", f"{cant} un. ({talle})")
        col_m3.metric("Entrega", fecha)
        col_m4.metric(
            "Saldo Pendiente",
            f"${saldo:,.2f}",
            delta=f"Total: ${p_total:,.2f}",
            delta_color="off",
        )

        st.markdown("---")
        col1, col2, col3 = st.columns([2, 2, 1])

        with col1:
          estados_lista = [
              "Pendiente",
              "En producción",
              "Listo para entrega",
              "Entregado",
          ]
          idx = estados_lista.index(estado) if estado in estados_lista else 0
          nuevo_estado = st.selectbox(
              "Cambiar Estado", estados_lista, index=idx, key=f"estado_{p_id}"
          )
          if st.button("🔄 Actualizar Estado", key=f"btn_{p_id}"):
            conn = sqlite3.connect("indumentaria_clubes.db")
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE pedidos SET estado = ? WHERE id = ?",
                (nuevo_estado, p_id),
            )
            conn.commit()
            conn.close()
            st.success(f"¡Pedido #{p_id} actualizado!")
            st.rerun()

        with col2:
          if st.button("📲 Generar Comprobante WhatsApp", key=f"comp_{p_id}"):
            texto_whatsapp = (
                f"👕 *GOBA SPORT - COMPROBANTE DE PEDIDO*\n"
                f"----------------------------------------\n"
                f"📌 *Pedido N°:* #{p_id}\n"
                f"🛡️ *Club:* {c_nombre}\n"
                f"👕 *Prenda:* {prenda}\n"
                f"📦 *Cantidad:* {cant} unidades ({talle})\n"
                f"📅 *Entrega estimada:* {fecha}\n"
                f"⚙️ *Estado:* {estado}\n"
                f"----------------------------------------\n"
                f"💰 *Costo Total:* ${p_total:,.2f}\n"
                f"💵 *Abonado:* ${p_pagado:,.2f}\n"
                f"💳 *Saldo Restante:* ${saldo:,.2f}\n"
                f"----------------------------------------\n"
                f"¡Gracias por confiar en GOBA Sport!"
            )
            st.text_area(
                "Texto listo para copiar:",
                texto_whatsapp,
                key=f"area_{p_id}",
                height=130,
            )

        with col3:
          st.write("")
          st.write("")
          if st.button("❌ Cancelar", key=f"del_{p_id}"):
            conn = sqlite3.connect("indumentaria_clubes.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM pedidos WHERE id = ?", (p_id,))
            conn.commit()
            conn.close()
            st.warning(f"Pedido #{p_id} eliminado.")
            st.rerun()