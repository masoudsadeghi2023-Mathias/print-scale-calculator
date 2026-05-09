import streamlit as st

# --- Language dictionary ---
LANG = {
    "fa": {
        "title": "📏 ابزار محاسبه مقیاس دقیق برای چاپ",
        "desc": "اندازه یک بخش از تصویر و همان بخش روی کاغذ را وارد کن.",
        "image_part": "اندازه بخش روی تصویر (سانتی‌متر)",
        "print_part": "اندازه همان بخش روی کاغذ (سانتی‌متر)",
        "current_dim": "Width یا Height فعلی در Image Size (سانتی‌متر)",
        "scale": "🔹 نسبت مقیاس:",
        "new_dim": "🔹 مقدار جدید برای Width/Height:",
        "info": "این مقدار را در Photoshop → Image Size وارد کن.",
        "warning": "لطفاً هر سه مقدار را وارد کن."
    },
    "en": {
        "title": "📏 Accurate Print Scale Calculator",
        "desc": "Enter the size of a section on the image and the same section on the print.",
        "image_part": "Image section size (cm)",
        "print_part": "Printed section size (cm)",
        "current_dim": "Current Width/Height in Image Size (cm)",
        "scale": "🔹 Scale factor:",
        "new_dim": "🔹 New Width/Height:",
        "info": "Enter this value in Photoshop → Image Size.",
        "warning": "Please enter all three values."
    },
    "sv": {
        "title": "📏 Noggrann skalberäkning för utskrift",
        "desc": "Ange storleken på en del av bilden och samma del på utskriften.",
        "image_part": "Bildsektionens storlek (cm)",
        "print_part": "Utskriftssektionens storlek (cm)",
        "current_dim": "Nuvarande bredd/höjd i Image Size (cm)",
        "scale": "🔹 Skalningsfaktor:",
        "new_dim": "🔹 Ny bredd/höjd:",
        "info": "Ange detta värde i Photoshop → Image Size.",
        "warning": "Vänligen fyll i alla tre värden."
    }
}

# --- Flags ---
FLAGS = {
    "fa": "🇮🇷 فارسی",
    "en": "🇬🇧 English",
    "sv": "🇸🇪 Svenska"
}

# --- Default language ---
if "lang" not in st.session_state:
    st.session_state.lang = "fa"

# --- Horizontal language buttons ---
col1, col2, col3 = st.columns(3)

with col1:
    if st.button(FLAGS["fa"]):
        st.session_state.lang = "fa"

with col2:
    if st.button(FLAGS["en"]):
        st.session_state.lang = "en"

with col3:
    if st.button(FLAGS["sv"]):
        st.session_state.lang = "sv"

# --- Active language ---
lang = st.session_state.lang
T = LANG[lang]

# --- UI ---
st.title(T["title"])
st.write(T["desc"])

image_part = st.number_input(T["image_part"], min_value=0.0, step=0.01)
print_part = st.number_input(T["print_part"], min_value=0.0, step=0.01)
current_dimension = st.number_input(T["current_dim"], min_value=0.0, step=0.01)

if image_part > 0 and print_part > 0 and current_dimension > 0:
    scale_factor = print_part / image_part
    new_dimension = current_dimension * scale_factor

    st.success(f"{T['scale']} **{scale_factor:.3f}**")
    st.success(f"{T['new_dim']} **{new_dimension:.2f} cm**")

    st.info(T["info"])
else:
    st.warning(T["warning"])
