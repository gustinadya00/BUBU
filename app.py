import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Pesan untuk Bubu",
    page_icon="💌",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -----------------------------
# Demo configuration
# -----------------------------
DEMO_PASSWORD = "bubu1106"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Comic+Neue:wght@400;700&family=Patrick+Hand&display=swap');

html, body, [class*="css"] {
    font-family: 'Comic Neue', 'Trebuchet MS', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(255,255,255,.8) 0 2px, transparent 3px),
        radial-gradient(circle at 90% 30%, rgba(255,255,255,.65) 0 2px, transparent 3px),
        linear-gradient(135deg, #fff7cf 0%, #dff6ff 48%, #ffe4ee 100%);
}

.main .block-container {
    max-width: 1120px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.comic-title {
    font-family: 'Patrick Hand', cursive;
    font-size: clamp(3rem, 7vw, 6rem);
    line-height: .85;
    text-align: center;
    color: #153b5b;
    text-shadow: 4px 4px 0 #fff, 7px 7px 0 #f4c542;
    margin: .3rem 0 1rem;
}

.comic-subtitle {
    text-align: center;
    font-size: 1.15rem;
    color: #234;
    margin-bottom: 2rem;
}

.panel {
    background: rgba(255,255,255,.88);
    border: 3px solid #183b56;
    border-radius: 20px;
    box-shadow: 8px 8px 0 #183b56;
    padding: 1.4rem;
    margin: 1rem 0 1.5rem;
}

.stButton > button {
    border: 3px solid #183b56 !important;
    border-radius: 14px !important;
    box-shadow: 4px 4px 0 #183b56 !important;
    font-family: 'Comic Neue', sans-serif !important;
    font-weight: 700 !important;
    background: #ffd84d !important;
    color: #183b56 !important;
}

.stButton > button:hover {
    transform: translate(-2px, -2px);
    box-shadow: 6px 6px 0 #183b56 !important;
}

.envelope-wrap {
    text-align: center;
    padding: 2rem 1rem;
}

.envelope {
    position: relative;
    display: inline-flex;
    width: 300px;
    height: 205px;
    align-items: center;
    justify-content: center;
    margin: 1rem auto;
    background: #f4c542;
    border: 4px solid #183b56;
    border-radius: 12px;
    box-shadow: 10px 10px 0 #183b56;
    transform: rotate(-1deg);
}

.envelope:before {
    content: "";
    position: absolute;
    inset: 0;
    border-radius: 8px;
    background: linear-gradient(145deg, transparent 49%, #d89e25 50% 52%, transparent 53%);
}

.envelope:after {
    content: "💌";
    position: absolute;
    font-size: 4.2rem;
    background: #fff;
    border: 3px solid #183b56;
    border-radius: 50%;
    width: 92px;
    height: 92px;
    display: grid;
    place-items: center;
    z-index: 2;
}

.envelope-label {
    position: absolute;
    bottom: 12px;
    left: 0;
    right: 0;
    z-index: 3;
    font-weight: 700;
    color: #183b56;
}

.stTextArea textarea, .stTextInput input {
    border: 2px solid #183b56 !important;
    border-radius: 12px !important;
    background: #fffdf3 !important;
}

.badge {
    display: inline-block;
    padding: .35rem .8rem;
    border: 2px solid #183b56;
    border-radius: 999px;
    background: #fff;
    font-weight: 700;
    margin: .2rem;
}

.card {
    background: #fff;
    border: 3px solid #183b56;
    border-radius: 16px;
    padding: 1.1rem;
    height: 100%;
    box-shadow: 5px 5px 0 #183b56;
}

.card h3 {
    margin-top: 0;
    color: #153b5b;
}

.confidential {
    text-align: center;
    color: #9b2335;
    font-weight: 700;
    letter-spacing: .08em;
}

.speech {
    position: relative;
    background: #fff;
    border: 3px solid #183b56;
    border-radius: 20px;
    padding: 1.2rem;
    box-shadow: 6px 6px 0 #183b56;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Session state
# -----------------------------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "letter" not in st.session_state:
    st.session_state.letter = ""

# -----------------------------
# Login / confidentiality
# -----------------------------
if not st.session_state.authenticated:
    st.markdown('<div class="confidential">🔒 CONFIDENTIAL • NDUT × BUBU ONLY</div>', unsafe_allow_html=True)
    st.markdown('<div class="comic-title">Pesan untuk Bubu</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="comic-subtitle">📁 CASE FILE: HATI-HATI, ADA PESAN RAHASIA DI DALAMNYA!</div>',
        unsafe_allow_html=True,
    )

    st.markdown("""
    <div class="panel">
        <h2>🕵️‍♀️ Restricted Area</h2>
        <p>Website ini adalah ruang kecil milik <b>Ndut & Bubu</b>.
        Masukkan password untuk membuka case file.</p>
        <p>💡 Demo password: <code>bubu1106</code></p>
    </div>
    """, unsafe_allow_html=True)

    password = st.text_input("🔑 Password", type="password", placeholder="Masukkan password rahasia...")
    if st.button("🔓 Buka Case File", use_container_width=True):
        if password == DEMO_PASSWORD:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("🚨 ACCESS DENIED — password belum tepat.")
    st.stop()

# -----------------------------
# Sidebar navigation
# -----------------------------
with st.sidebar:
    st.markdown("### 📂 CASE #BUBU")
    page = st.radio(
        "Pilih halaman",
        ["💌 Surat Rahasia", "🗺️ Memory Map", "🎯 Mission Board", "📜 Case Notes"],
    )
    st.divider()
    st.caption("🔒 Confidential — Ndut & Bubu only")
    if st.button("🔐 Lock website"):
        st.session_state.authenticated = False
        st.rerun()

# -----------------------------
# Landing / Letter page
# -----------------------------
if page == "💌 Surat Rahasia":
    st.markdown('<div class="confidential">🔒 CONFIDENTIAL • TOP SECRET LOVE LETTER</div>', unsafe_allow_html=True)
    st.markdown('<div class="comic-title">Pesan untuk Bubu</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="comic-subtitle">Sebuah amplop. Sebuah pesan. Sebuah Bubu yang harus membukanya. 💛</div>',
        unsafe_allow_html=True,
    )

    st.markdown("""
    <div class="envelope-wrap">
        <div class="envelope">
            <div class="envelope-label">CLICK BELOW TO OPEN THE CASE ✉️</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("✉️ Buka Amplop", use_container_width=True):
        st.session_state.envelope_open = True

    if st.session_state.get("envelope_open", False):
        st.markdown("""
        <div class="panel">
            <h2>💌 SURAT TERBUKA!</h2>
            <p>Dear Bubu,</p>
            <p>Ini adalah tempat Ndut bisa meninggalkan pesan kecil,
            surat panjang, atau random thoughts yang tiba-tiba muncul jam 2 pagi.</p>
            <p>✍️ Sekarang giliranmu membaca atau menulis sesuatu.</p>
        </div>
        """, unsafe_allow_html=True)

        letter = st.text_area(
            "📝 Tulis pesan rahasia untuk Bubu",
            value=st.session_state.letter,
            height=240,
            placeholder="Dear Bubu...\n\nHari ini aku mau bilang...",
        )
        if st.button("💛 Simpan Pesan", use_container_width=True):
            st.session_state.letter = letter
            st.success("💌 Pesan tersimpan di sesi demo ini!")

        if st.session_state.letter:
            st.markdown(
                f'<div class="speech"><b>📨 Pesan tersimpan:</b><br><br>{st.session_state.letter.replace(chr(10), "<br>")}</div>',
                unsafe_allow_html=True,
            )

# -----------------------------
# Memory Map
# -----------------------------
elif page == "🗺️ Memory Map":
    st.markdown('<div class="comic-title">Memory Map</div>', unsafe_allow_html=True)
    st.markdown('<div class="comic-subtitle">📍 Beberapa titik kecil dalam perjalanan Ndut × Bubu</div>', unsafe_allow_html=True)

    memories = [
        ("📌 CASE 001", "First Chapter", "Awal mula cerita. Dua orang yang akhirnya memutuskan untuk saling mengenal lebih jauh."),
        ("📌 CASE 002", "The Little Things", "Perhatian kecil, obrolan panjang, dan hal-hal random yang ternyata jadi memorable."),
        ("📌 CASE 003", "Team Us", "Bukan tentang selalu sempurna, tapi tentang selalu mencoba menyelesaikan sesuatu bersama."),
    ]

    cols = st.columns(3)
    for col, (tag, title, text) in zip(cols, memories):
        with col:
            st.markdown(
                f'<div class="card"><span class="badge">{tag}</span><h3>{title}</h3><p>{text}</p></div>',
                unsafe_allow_html=True,
            )

    st.write("")
    st.markdown("""
    <div class="panel">
        <h2>🧭 Next Destination</h2>
        <p>Tambahkan foto, tanggal, tempat, atau inside joke kalian di sini.
        Pada versi produksi, halaman ini bisa dikembangkan menjadi timeline interaktif.</p>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# Mission Board
# -----------------------------
elif page == "🎯 Mission Board":
    st.markdown('<div class="comic-title">Mission Board</div>', unsafe_allow_html=True)
    st.markdown('<div class="comic-subtitle">🎯 Side quests untuk Ndut & Bubu</div>', unsafe_allow_html=True)

    missions = [
        "🍜 Makan sesuatu yang belum pernah dicoba",
        "🎬 Movie night tanpa debat film lebih dari 10 menit",
        "📸 Ambil satu foto absurd bersama",
        "💬 Deep talk sampai lupa waktu",
        "🌙 Jalan malam dan cari tempat baru",
    ]

    st.markdown('<div class="panel"><h2>ACTIVE MISSIONS</h2></div>', unsafe_allow_html=True)
    for i, mission in enumerate(missions):
        done = st.checkbox(mission, key=f"mission_{i}")
        if done:
            st.caption("✅ Mission cleared!")

# -----------------------------
# Case Notes
# -----------------------------
else:
    st.markdown('<div class="comic-title">Case Notes</div>', unsafe_allow_html=True)
    st.markdown('<div class="comic-subtitle">📜 Catatan rahasia dari markas Ndut × Bubu</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="panel">
        <h2>🕵️ Confidentiality Notice</h2>
        <p><b>Prototype warning:</b> password di contoh ini hanya demonstrasi UI.
        Untuk deployment nyata, password jangan ditulis langsung di source code.
        Gunakan Streamlit Secrets dan autentikasi yang benar.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h3>📅 Case opened</h3>
        <p>11 June 2026</p>
        <h3>👥 Authorized agents</h3>
        <p>Ndut & Bubu</p>
        <h3>🗃️ Current status</h3>
        <p>ACTIVE — proceeding with affection.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.caption(f"Pesan untuk Bubu • Prototype • {datetime.now().strftime('%d %B %Y')}")
