"""
app.py — Streamlit Spam/Ham Classifier
Beautiful, interactive UI untuk mengklasifikasi pesan spam/ham
"""

import streamlit as st
import joblib
import re
import string
import nltk
from pathlib import Path
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# ── Page Config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="SpamShield · Detektor Spam",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ── Download NLTK resources ───────────────────────────────────────────────────
@st.cache_resource
def download_nltk():
    nltk.download("stopwords", quiet=True)
    nltk.download("punkt",     quiet=True)

download_nltk()

from nltk.corpus import stopwords

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* ─── Font Import ─────────────────────────── */
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;1,9..40,300&display=swap');

/* ─── Root Variables ──────────────────────── */
:root {
  --bg:      #0d0f14;
  --surface: #161920;
  --card:    #1c2030;
  --border:  #252a3a;
  --accent:  #4f6ef7;
  --green:   #22d3a0;
  --red:     #f75467;
  --yellow:  #f7c054;
  --text:    #e8eaf2;
  --muted:   #7a80a0;
  --radius:  14px;
}

/* ─── Global Reset ────────────────────────── */
*, *::before, *::after { box-sizing: border-box; }

html, body, .stApp {
  background: var(--bg) !important;
  color: var(--text) !important;
  font-family: 'DM Sans', sans-serif !important;
}

/* ─── Hide Streamlit chrome ───────────────── */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header { visibility: hidden; }

/* Tapi tetap tampilkan tombol toggle sidebar */
[data-testid="stSidebarCollapsedControl"],
[data-testid="collapsedControl"] {
  visibility: visible !important;
}.block-container { padding-top: 2.5rem !important; max-width: 800px; }

/* ─── Typography ──────────────────────────── */
h1, h2, h3 { font-family: 'Syne', sans-serif !important; }

/* ─── Hero headline ───────────────────────── */
.hero-title {
  font-family: 'Syne', sans-serif;
  font-size: clamp(2rem, 5vw, 3rem);
  font-weight: 800;
  line-height: 1.1;
  background: linear-gradient(135deg, #fff 30%, var(--accent));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 0.2rem;
}

.hero-sub {
  color: var(--muted);
  font-size: 1rem;
  font-weight: 300;
  letter-spacing: 0.02em;
  margin-bottom: 2.5rem;
}

/* ─── Pill badge ──────────────────────────── */
.badge {
  display: inline-flex; align-items: center; gap: 6px;
  padding: 4px 12px; border-radius: 99px;
  font-size: 0.72rem; font-weight: 600; letter-spacing: 0.06em;
  text-transform: uppercase;
}
.badge-accent { background: rgba(79,110,247,.15); color: var(--accent); border: 1px solid rgba(79,110,247,.3); }
.badge-green  { background: rgba(34,211,160,.12); color: var(--green);  border: 1px solid rgba(34,211,160,.3); }
.badge-red    { background: rgba(247, 84,103,.12); color: var(--red);   border: 1px solid rgba(247, 84,103,.3); }

/* ─── Card ────────────────────────────────── */
.card {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 1.4rem 1.6rem;
  margin-bottom: 1rem;
}

/* ─── Result card ─────────────────────────── */
.result-spam {
  background: linear-gradient(135deg, #1e0f12, #220e13);
  border: 1px solid rgba(247,84,103,.35);
  border-radius: var(--radius);
  padding: 1.6rem;
}
.result-ham {
  background: linear-gradient(135deg, #0c1d18, #0d2018);
  border: 1px solid rgba(34,211,160,.35);
  border-radius: var(--radius);
  padding: 1.6rem;
}
.result-label-spam {
  font-family: 'Syne', sans-serif;
  font-size: 2rem; font-weight: 800;
  color: var(--red);
}
.result-label-ham {
  font-family: 'Syne', sans-serif;
  font-size: 2rem; font-weight: 800;
  color: var(--green);
}
.result-conf {
  font-size: 0.88rem; color: var(--muted); margin-top: 0.25rem;
}
.result-msg {
  font-size: 0.9rem; color: var(--muted);
  font-style: italic; margin-top: 0.8rem;
  padding-left: 0.8rem;
  border-left: 2px solid var(--border);
}

/* ─── Textarea override ───────────────────── */
textarea {
  background: var(--surface) !important;
  color: var(--text) !important;
  border: 1px solid var(--border) !important;
  border-radius: 10px !important;
  font-family: 'DM Sans', sans-serif !important;
  font-size: 0.97rem !important;
  resize: vertical !important;
}
textarea:focus { border-color: var(--accent) !important; }

/* ─── Button ──────────────────────────────── */
.stButton > button {
  width: 100%; padding: 0.75rem 1rem;
  background: var(--accent) !important;
  color: #fff !important;
  border: none !important; border-radius: 10px !important;
  font-family: 'Syne', sans-serif !important;
  font-size: 1rem !important; font-weight: 600 !important;
  letter-spacing: 0.04em;
  transition: opacity .18s, transform .14s;
  cursor: pointer;
}
.stButton > button:hover { opacity: .88; transform: translateY(-1px); }
.stButton > button:active { transform: translateY(0px); }

/* ─── Example buttons styling ─────────────── */
.example-btn-spam > div > button {
  background: rgba(247,84,103,.15) !important;
  border: 1px solid rgba(247,84,103,.35) !important;
  color: #f75467 !important;
  font-size: 0.88rem !important;
  padding: 0.5rem 0.8rem !important;
}
.example-btn-spam > div > button:hover { background: rgba(247,84,103,.25) !important; }

.example-btn-ham > div > button {
  background: rgba(34,211,160,.12) !important;
  border: 1px solid rgba(34,211,160,.3) !important;
  color: #22d3a0 !important;
  font-size: 0.88rem !important;
  padding: 0.5rem 0.8rem !important;
}
.example-btn-ham > div > button:hover { background: rgba(34,211,160,.2) !important; }

/* ─── Expander ────────────────────────────── */
.streamlit-expanderHeader {
  background: var(--surface) !important;
  border: 1px solid var(--border) !important;
  border-radius: 10px !important;
  color: var(--muted) !important;
  font-size: 0.88rem !important;
}

/* ─── Divider ─────────────────────────────── */
hr { border-color: var(--border) !important; margin: 1.8rem 0 !important; }

/* ─── Scrollbar ───────────────────────────── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }

/* ─── Sidebar ─────────────────────────────── */
[data-testid="stSidebar"] {
  background: var(--surface) !important;
  border-right: 1px solid var(--border) !important;
}
[data-testid="stSidebar"] * { color: var(--text) !important; }

/* ─── Metric widgets ──────────────────────── */
[data-testid="metric-container"] {
  background: var(--card) !important;
  border: 1px solid var(--border) !important;
  border-radius: 10px !important;
  padding: 1rem !important;
}

/* ─── Columns gap ─────────────────────────── */
[data-testid="column"] { padding: 0 0.4rem !important; }

/* Paksa sidebar selalu terbuka */
[data-testid="stSidebar"] {
  transform: none !important;
  width: 21rem !important;
  min-width: 240px !important;
  display: block !important;
  visibility: visible !important;
}


</style>
""", unsafe_allow_html=True)


# ── Preprocessing ─────────────────────────────────────────────────────────────
def clean_text(text: str) -> str:
    text = str(text).lower()
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def remove_stopwords(text: str, language: str = 'indonesian') -> str:
    try:
        stop_words = set(stopwords.words(language))
    except OSError:
        stop_words = set(stopwords.words('english'))
    tokens = text.split()
    return ' '.join(w for w in tokens if w not in stop_words)

def preprocess(text: str) -> str:
    return remove_stopwords(clean_text(text))


# ── Load model ────────────────────────────────────────────────────────────────
@st.cache_resource
def load_model(path: str):
    p = Path(path)
    if not p.exists():
        return None
    return joblib.load(p)


# ── Prediction helper ─────────────────────────────────────────────────────────
def predict(model, text: str) -> dict:
    processed = preprocess(text)
    pred      = model.predict([processed])[0]
    proba     = model.predict_proba([processed])[0]
    classes   = model.classes_
    proba_dict = {c: round(float(p) * 100, 2) for c, p in zip(classes, proba)}
    return {
        "prediksi":    pred,
        "keyakinan":   proba_dict[pred],
        "probabilitas": proba_dict,
        "processed":   processed,
    }


# ── Gauge chart ───────────────────────────────────────────────────────────────
def gauge_chart(spam_pct: float):
    ham_pct = 100 - spam_pct
    color   = "#f75467" if spam_pct >= 50 else "#22d3a0"
    fig = go.Figure(go.Indicator(
        mode  = "gauge+number",
        value = spam_pct,
        number= {"suffix": "%", "font": {"size": 28, "color": color, "family": "Syne"}},
        gauge = {
            "axis": {"range": [0, 100], "tickcolor": "#7a80a0",
                     "tickfont": {"color": "#7a80a0", "size": 11}},
            "bar":  {"color": color, "thickness": 0.28},
            "bgcolor": "#1c2030",
            "borderwidth": 0,
            "steps": [
                {"range": [0, 40],   "color": "rgba(34,211,160,.08)"},
                {"range": [40, 60],  "color": "rgba(247,192,84,.08)"},
                {"range": [60, 100], "color": "rgba(247,84,103,.08)"},
            ],
            "threshold": {
                "line": {"color": color, "width": 3},
                "thickness": 0.8,
                "value": spam_pct,
            },
        },
        title = {"text": "Skor Spam", "font": {"size": 13, "color": "#7a80a0", "family": "DM Sans"}},
        domain= {"x": [0, 1], "y": [0, 1]},
    ))
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor ="rgba(0,0,0,0)",
        margin       = dict(t=30, b=0, l=20, r=20),
        height       = 200,
        font         = {"color": "#e8eaf2"},
    )
    return fig


# ── Probability bar chart ─────────────────────────────────────────────────────
def prob_bar(proba_dict: dict):
    labels = list(proba_dict.keys())
    values = list(proba_dict.values())
    colors = ["#22d3a0" if l == "ham" else "#f75467" for l in labels]
    fig = go.Figure(go.Bar(
        x=labels, y=values,
        marker_color=colors,
        text=[f"{v:.1f}%" for v in values],
        textposition="outside",
        textfont={"color": "#e8eaf2", "size": 13, "family": "Syne"},
        width=0.45,
    ))
    fig.update_layout(
        paper_bgcolor = "rgba(0,0,0,0)",
        plot_bgcolor  = "rgba(0,0,0,0)",
        xaxis = {"tickfont": {"color": "#e8eaf2", "size": 13}, "gridcolor": "#252a3a"},
        yaxis = {"range": [0, 110], "tickfont": {"color": "#7a80a0", "size": 11},
                 "gridcolor": "#252a3a", "ticksuffix": "%"},
        margin = dict(t=20, b=20, l=0, r=0),
        height = 200,
        showlegend = False,
    )
    return fig


# ══════════════════════════════════════════════════════════════════════════════
#  APP LAYOUT
# ══════════════════════════════════════════════════════════════════════════════

# ── Model path (hardcoded) ────────────────────────────────────────────────────
model_path = "models/spam_ham_model.pkl"

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <style>
    /* ══════════ CYBERPUNK SIDEBAR ══════════ */

    /* Scanline overlay */
    [data-testid="stSidebar"]::before {
      content: '';
      position: fixed; top: 0; left: 0;
      width: 280px; height: 100vh;
      background: repeating-linear-gradient(
        0deg,
        transparent,
        transparent 2px,
        rgba(0,255,200,.018) 2px,
        rgba(0,255,200,.018) 4px
      );
      pointer-events: none; z-index: 0;
    }

    /* Neon border kanan sidebar */
    [data-testid="stSidebar"] {
      border-right: 1px solid transparent !important;
      box-shadow:
        inset -1px 0 0 #00ffe1,
        inset -3px 0 20px rgba(0,255,225,.08),
        4px 0 30px rgba(0,255,225,.06) !important;
    }

    /* ── Section label ── */
    .sb-sec-label {
      font-size: .62rem; font-weight: 700; letter-spacing: .14em;
      text-transform: uppercase;
      color: #00ffe1;
      text-shadow: 0 0 8px rgba(0,255,225,.6), 0 0 20px rgba(0,255,225,.3);
      margin: 1rem 0 .45rem;
      display: flex; align-items: center; gap: 6px;
    }
    .sb-sec-label::after {
      content: '';
      flex: 1; height: 1px;
      background: linear-gradient(90deg, rgba(0,255,225,.4), transparent);
    }

    /* ── Mini cards ── */
    .sb-cards { display: grid; grid-template-columns: 1fr 1fr; gap: 5px; }
    .sb-mcard {
      background: linear-gradient(135deg, #0a0e1a, #0d1220);
      border: 1px solid rgba(0,255,225,.18);
      border-radius: 8px; padding: 8px 10px;
      position: relative; overflow: hidden;
      transition: border-color .2s;
    }
    .sb-mcard::before {
      content: '';
      position: absolute; top: 0; left: 0; right: 0; height: 1px;
      background: linear-gradient(90deg, transparent, rgba(0,255,225,.5), transparent);
    }
    .sb-mcard:hover { border-color: rgba(0,255,225,.45); }
    .sb-mcard-val {
      font-size: 1.15rem; font-weight: 700; color: #e8eaf2;
      font-family: 'Courier New', monospace;
    }
    .sb-mcard-lbl { font-size: .63rem; color: #4a6070; margin-top: 2px; line-height: 1.3; }

    /* ── Pipeline ── */
    .sb-pipe { display: flex; flex-direction: column; gap: 3px; }
    .sb-pipe-step {
      background: #080c16;
      border: 1px solid rgba(79,110,247,.25);
      border-left: 2px solid #4f6ef7;
      border-radius: 0 6px 6px 0;
      padding: 5px 10px;
      font-size: .7rem; color: #a0b0d0; font-weight: 500;
      box-shadow: inset 0 0 12px rgba(79,110,247,.05);
      position: relative;
    }
    .sb-pipe-step::before {
      content: '';
      position: absolute; left: -1px; top: 50%;
      transform: translateY(-50%);
      width: 2px; height: 60%;
      background: linear-gradient(180deg, transparent, #4f6ef7, transparent);
    }
    .sb-pipe-arrow {
      color: #4f6ef7; font-size: .65rem;
      padding-left: 12px; opacity: .6;
      text-shadow: 0 0 6px #4f6ef7;
    }

    /* ── Model rows ── */
    .sb-model-row {
      background: #080c16;
      border: 1px solid rgba(60,70,100,.5);
      border-radius: 8px; padding: 8px 10px; margin-bottom: 5px;
      position: relative; overflow: hidden;
      transition: all .2s;
    }
    .sb-model-row:hover {
      border-color: rgba(79,110,247,.4);
      box-shadow: 0 0 12px rgba(79,110,247,.08);
    }
    .sb-model-row.winner {
      border-color: rgba(0,255,225,.3) !important;
      background: linear-gradient(135deg, #080e14, #08140f);
      box-shadow: 0 0 20px rgba(0,255,225,.06), inset 0 0 20px rgba(0,255,225,.03) !important;
    }
    .sb-model-row.winner::after {
      content: '';
      position: absolute; top: 0; right: 0;
      width: 40%; height: 1px;
      background: linear-gradient(270deg, rgba(0,255,225,.5), transparent);
    }
    .sb-model-name { font-size: .78rem; font-weight: 700; color: #c8d4e8; }
    .sb-model-desc { font-size: .64rem; color: #4a5570; margin-top: 1px; }
    .sb-model-stats { display: flex; gap: 6px; margin-top: 6px; }
    .sb-stat {
      background: rgba(0,0,0,.4); border: 1px solid rgba(60,70,100,.4);
      border-radius: 5px; padding: 4px 8px; text-align: center;
    }
    .sb-stat-val { font-size: .74rem; font-weight: 700; color: #7a80a0; font-family: 'Courier New', monospace; }
    .sb-stat-val.win { color: #00ffe1; text-shadow: 0 0 6px rgba(0,255,225,.5); }
    .sb-badge {
      display: inline-flex; align-items: center; gap: 4px;
      font-size: .58rem; font-weight: 700;
      padding: 2px 7px; border-radius: 4px;
      background: rgba(0,255,225,.1); color: #00ffe1;
      border: 1px solid rgba(0,255,225,.3);
      letter-spacing: .06em; text-transform: uppercase;
      text-shadow: 0 0 6px rgba(0,255,225,.5);
      margin-bottom: 4px;
      animation: pulse-badge 2.5s ease-in-out infinite;
    }
    @keyframes pulse-badge {
      0%, 100% { box-shadow: 0 0 6px rgba(0,255,225,.2); }
      50% { box-shadow: 0 0 14px rgba(0,255,225,.45); }
    }

    /* ── TF-IDF config grid ── */
    .sb-config-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 5px; }
    .sb-config-item {
      background: #080c16;
      border: 1px solid rgba(60,70,100,.4);
      border-radius: 6px; padding: 6px 9px;
      position: relative;
    }
    .sb-config-key {
      font-size: .6rem; color: #3a4560;
      text-transform: uppercase; letter-spacing: .06em;
    }
    .sb-config-val {
      font-size: .82rem; font-weight: 700;
      color: #b060ff;
      text-shadow: 0 0 8px rgba(176,96,255,.4);
      font-family: 'Courier New', monospace;
      margin-top: 2px;
    }

    /* ── Performance rows ── */
    .sb-perf-block {
      background: #080c16; border: 1px solid rgba(60,70,100,.4);
      border-radius: 8px; padding: 2px 10px;
    }
    .sb-perf-row {
      display: flex; justify-content: space-between; align-items: center;
      padding: 6px 0; border-bottom: 1px solid rgba(30,40,60,.8);
      font-size: .72rem; color: #6070a0;
    }
    .sb-perf-row:last-child { border-bottom: none; }
    .sb-perf-val {
      font-weight: 700; color: #00ffe1;
      font-family: 'Courier New', monospace;
      text-shadow: 0 0 6px rgba(0,255,225,.45);
    }

    /* ── How it works ── */
    .sb-how {
      background: #080c16;
      border: 1px solid rgba(60,70,100,.35);
      border-left: 2px solid rgba(176,96,255,.5);
      border-radius: 0 8px 8px 0;
      padding: 9px 11px;
      font-size: .69rem; color: #6070a0; line-height: 1.7;
    }
    .sb-how em { color: #b060ff; font-style: normal; font-weight: 600; }

    /* ── Divider ── */
    .sb-divider {
      border: none;
      border-top: 1px solid rgba(0,255,225,.08);
      margin: .7rem 0;
    }

    /* ── GitHub btn ── */
    .sb-github-btn {
      display: flex; align-items: center; gap: 8px;
      background: linear-gradient(135deg, #080c16, #0a0e18);
      border: 1px solid rgba(0,255,225,.2);
      border-radius: 8px; padding: 8px 12px;
      font-size: .72rem; font-weight: 600; color: #7a90b0;
      text-decoration: none;
      transition: all .2s;
    }
    .sb-github-btn:hover {
      border-color: rgba(0,255,225,.5);
      color: #00ffe1;
      box-shadow: 0 0 12px rgba(0,255,225,.12);
      text-shadow: 0 0 8px rgba(0,255,225,.4);
    }

    /* ── Neon tag ── */
    .neon-tag {
      font-size: .58rem; font-weight: 700; letter-spacing: .1em;
      text-transform: uppercase;
      padding: 2px 8px; border-radius: 3px;
      display: inline-block; margin-bottom: .6rem;
    }
    .neon-tag-cyan {
      background: rgba(0,255,225,.08);
      border: 1px solid rgba(0,255,225,.25);
      color: #00ffe1;
      text-shadow: 0 0 8px rgba(0,255,225,.6);
    }
    .neon-tag-purple {
      background: rgba(176,96,255,.08);
      border: 1px solid rgba(176,96,255,.25);
      color: #b060ff;
      text-shadow: 0 0 8px rgba(176,96,255,.6);
    }

    /* ── Stat-bar mini ── */
    .sb-statbar { margin-top: 6px; }
    .sb-statbar-row { display: flex; align-items: center; gap: 6px; margin-bottom: 3px; }
    .sb-statbar-lbl { font-size: .6rem; color: #3a4560; width: 42px; flex-shrink: 0; }
    .sb-statbar-track {
      flex: 1; height: 3px; background: rgba(255,255,255,.04);
      border-radius: 2px; overflow: hidden;
    }
    .sb-statbar-fill {
      height: 100%; border-radius: 2px;
      background: linear-gradient(90deg, #4f6ef7, #00ffe1);
      box-shadow: 0 0 6px rgba(0,255,225,.4);
    }
    .sb-statbar-val { font-size: .6rem; color: #00ffe1; font-family: monospace; width: 38px; text-align: right; }

    </style>


    <!-- DATASET -->
    <div class="sb-sec-label">📦 Dataset</div>
    <div class="sb-cards">
      <div class="sb-mcard" style="grid-column:span 2">
        <div class="sb-mcard-val">3.762</div>
        <div class="sb-mcard-lbl">total pesan · dari 6.415 (setelah cleaning) · sumber Kaggle</div>
      </div>
      <div class="sb-mcard">
        <div class="sb-mcard-val" style="color:#f75467;text-shadow:0 0 8px rgba(247,84,103,.4)">1.942</div>
        <div class="sb-mcard-lbl">pesan spam</div>
      </div>
      <div class="sb-mcard">
        <div class="sb-mcard-val" style="color:#00ffe1;text-shadow:0 0 8px rgba(0,255,225,.4)">1.820</div>
        <div class="sb-mcard-lbl">pesan ham</div>
      </div>
    </div>

    <hr class="sb-divider">

    <!-- PREPROCESSING -->
    <div class="sb-sec-label">⚙️ Preprocessing Pipeline</div>
    <div class="sb-pipe">
      <div class="sb-pipe-step">Raw text</div>
      <div class="sb-pipe-arrow">▼</div>
      <div class="sb-pipe-step">Lowercase</div>
      <div class="sb-pipe-arrow">▼</div>
      <div class="sb-pipe-step">Hapus URL · angka · tanda baca</div>
      <div class="sb-pipe-arrow">▼</div>
      <div class="sb-pipe-step">Stopwords removal (NLTK Indo)</div>
      <div class="sb-pipe-arrow">▼</div>
      <div class="sb-pipe-step">Stemming</div>
    </div>

    <hr class="sb-divider">

    <!-- MODEL COMPARISON -->
    <div class="sb-sec-label">🤖 Model Comparison</div>

    <div class="sb-model-row">
      <div class="sb-model-name">Naive Bayes</div>
      <div class="sb-model-desc">Probabilistik · cepat · baseline</div>
      <div class="sb-model-stats">
        <div class="sb-stat"><div class="sb-stat-val">96.24%</div><div class="sb-mcard-lbl">CV F1</div></div>
        <div class="sb-stat"><div class="sb-stat-val">94.95%</div><div class="sb-mcard-lbl">Test Acc</div></div>
      </div>
      <div class="sb-statbar">
        <div class="sb-statbar-row">
          <div class="sb-statbar-lbl">F1</div>
          <div class="sb-statbar-track"><div class="sb-statbar-fill" style="width:96.24%;opacity:.45"></div></div>
          <div class="sb-statbar-val" style="opacity:.5">96.24</div>
        </div>
      </div>
    </div>

    <div class="sb-model-row">
      <div class="sb-model-name">Logistic Regression</div>
      <div class="sb-model-desc">Linear · interpretable · stabil</div>
      <div class="sb-model-stats">
        <div class="sb-stat"><div class="sb-stat-val">97.07%</div><div class="sb-mcard-lbl">CV F1</div></div>
        <div class="sb-stat"><div class="sb-stat-val">95.48%</div><div class="sb-mcard-lbl">Test Acc</div></div>
      </div>
      <div class="sb-statbar">
        <div class="sb-statbar-row">
          <div class="sb-statbar-lbl">F1</div>
          <div class="sb-statbar-track"><div class="sb-statbar-fill" style="width:97.07%;opacity:.6"></div></div>
          <div class="sb-statbar-val" style="opacity:.65">97.07</div>
        </div>
      </div>
    </div>

    <div class="sb-model-row winner">
      <div class="sb-badge">⚡ TERBAIK</div>
      <div class="sb-model-name">Linear SVM</div>
      <div class="sb-model-desc">Margin-based · high-dim · robust</div>
      <div class="sb-model-stats">
        <div class="sb-stat"><div class="sb-stat-val win">97.54%</div><div class="sb-mcard-lbl">CV F1</div></div>
        <div class="sb-stat"><div class="sb-stat-val win">95.75%</div><div class="sb-mcard-lbl">Test Acc</div></div>
      </div>
      <div class="sb-statbar">
        <div class="sb-statbar-row">
          <div class="sb-statbar-lbl">F1</div>
          <div class="sb-statbar-track"><div class="sb-statbar-fill" style="width:97.54%"></div></div>
          <div class="sb-statbar-val">97.54</div>
        </div>
      </div>
    </div>

    <hr class="sb-divider">

    <!-- TF-IDF CONFIG -->
    <div class="sb-sec-label">🔧 TF-IDF Config</div>
    <div class="neon-tag neon-tag-purple" style="margin-bottom:.4rem">vectorizer · params</div>
    <div class="sb-config-grid">
      <div class="sb-config-item"><div class="sb-config-key">max_features</div><div class="sb-config-val">10.000</div></div>
      <div class="sb-config-item"><div class="sb-config-key">ngram_range</div><div class="sb-config-val">(1, 2)</div></div>
      <div class="sb-config-item"><div class="sb-config-key">min_df</div><div class="sb-config-val">2</div></div>
      <div class="sb-config-item"><div class="sb-config-key">sublinear_tf</div><div class="sb-config-val">True</div></div>
    </div>

    <hr class="sb-divider">

    <!-- PERFORMA FINAL -->
    <div class="sb-sec-label">📈 Performa Final</div>
    <div class="sb-perf-block">
      <div class="sb-perf-row"><span>CV F1-Score (5-fold)</span><span class="sb-perf-val">97.54%</span></div>
      <div class="sb-perf-row"><span>Test Accuracy</span><span class="sb-perf-val">95.75%</span></div>
      <div class="sb-perf-row"><span>Precision (spam)</span><span class="sb-perf-val">96%</span></div>
      <div class="sb-perf-row"><span>Recall (spam)</span><span class="sb-perf-val">96%</span></div>
      <div class="sb-perf-row"><span>F1-Score (spam)</span><span class="sb-perf-val">96%</span></div>
    </div>

    <hr class="sb-divider">

    <!-- CARA KERJA -->
    <div class="sb-sec-label">💡 Cara Kerja</div>
    <div class="sb-how">
      SVM mencari <em>hyperplane</em> optimal yang memisahkan ruang vektor TF-IDF antara kelas spam dan ham.
      Unggul karena efektif pada data <em>sparse</em> berdimensi tinggi, lebih <em>robust</em> terhadap noise dibanding Naive Bayes,
      dan lebih stabil dari Logistic Regression untuk dataset teks besar.
    </div>

    <hr class="sb-divider">

    <!-- TIM PENGEMBANG -->
    <div class="sb-sec-label">👾 Tim Pengembang</div>

    <iv style="display:flex;flex-direction:column;gap:5px;">

      <div class="sb-team-card">
        <div class="sb-team-name" style="display: flex; justify-content: space-between; align-items: center;">
            <span>Zheka Baila Arkan</span>
            <span>⚡ ML Engineer</span>
        </div>      
      </div>

      <div class="sb-team-card">
        <div class="sb-team-name" style="display: flex; justify-content: space-between; align-items: center;">
              <span>Nabila Rohmatul Aulia</span>
              <span>🔧 Backend Developer</span>
        </div>      
      <div
          
      <div class="sb-team-card">
          <div class="sb-team-name" style="display: flex; justify-content: space-between; align-items: center;">
              <span>Refa Adinda Putri</span>
              <span>⚡ Data Engineer</span>
        </div>      
      <div

      <div class="sb-team-card">
        <div class="sb-team-name" style="display: flex; justify-content: space-between; align-items: center;">
              <span>Azri Zaki Mushodiq Kustiwa</span>
              <span>🛡️ QA</span>
        </div>  
      </div>
          

    <hr class="sb-divider">

    <!-- OUR REPO -->
    <div class="sb-sec-label">🔗 Our Repo</div>
    <a href="https://github.com/zhekabaila/spam-ham-classifier" target="_blank" class="sb-github-btn">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" style="flex-shrink:0;opacity:.7">
        <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z"/>
      </svg>
      zhekabaila/spam-ham-classifier
      <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="margin-left:auto;flex-shrink:0;opacity:.4">
        <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6M15 3h6v6M10 14L21 3"/>
      </svg>
    </a>
    """, unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="margin-bottom:.4rem">
  <span class="badge badge-accent">🛡️ Spam Detector · ML-Powered</span>
</div>
<div class="hero-title">SpamShield</div>
<div class="hero-sub">Klasifikasi pesan spam & ham secara instan dengan kecerdasan buatan</div>
""", unsafe_allow_html=True)

# ── Load model ────────────────────────────────────────────────────────────────
model = load_model(model_path)

if model is None:
    st.markdown("""
    <div class="card" style="border-color:rgba(247,84,103,.4); background:linear-gradient(135deg,#1e0f12,#220e13)">
      <p style="margin:0; color:#f75467; font-weight:600">⚠️ Model tidak ditemukan</p>
      <p style="margin:.4rem 0 0; color:#7a80a0; font-size:.88rem">
        Pastikan path model benar dan file <code>.pkl</code> tersedia.<br>
        Jalankan <strong>02_training.ipynb</strong> untuk melatih model terlebih dahulu.
      </p>
    </div>
    """, unsafe_allow_html=True)
    st.stop()
else:
    st.markdown("""
    <div style="display:flex;align-items:center;gap:8px;margin-bottom:1.2rem">
      <span class="badge badge-green">✓ Model siap</span>
      <span style="font-size:.8rem;color:#7a80a0">Linear SVM · TF-IDF</span>
    </div>
    """, unsafe_allow_html=True)

# ── Inject example texts via session state ────────────────────────────────────
if "input_text" not in st.session_state:
    st.session_state["input_text"] = ""

# ── Input label + Example buttons (centered, above textarea) ──────────────────
st.markdown("""
<p style='font-size:.9rem;color:#7a80a0;margin-bottom:.5rem'>✏️ Masukkan pesan yang ingin dicek</p>
""", unsafe_allow_html=True)

col_label, col_ex_spam, col_ex_ham = st.columns([3, 1.2, 1.2])
with col_label:
    st.markdown(
        "<p style='font-size:.78rem;color:#7a80a0;padding-top:.35rem;margin:0'>💡 Atau coba contoh:</p>",
        unsafe_allow_html=True,
    )
with col_ex_spam:
    st.markdown('<div class="example-btn-spam">', unsafe_allow_html=True)
    ex_spam = st.button("🚫 Contoh SPAM", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
with col_ex_ham:
    st.markdown('<div class="example-btn-ham">', unsafe_allow_html=True)
    ex_ham = st.button("✅ Contoh HAM", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

if ex_spam:
    st.session_state["input_text"] = (
        "SELAMAT! Anda terpilih sebagai pemenang undian berhadiah Rp 50.000.000! "
        "Klik link ini SEKARANG untuk klaim hadiah Anda sebelum kedaluwarsa: "
        "http://klaim-hadiah-gratis.xyz"
    )
if ex_ham:
    st.session_state["input_text"] = (
        "Hei, besok jadi ketemuan jam 3 sore di kafe dekat kantor? "
        "Aku sudah pesan meja. Kabarin ya kalau ada perubahan!"
    )

# ── Input area ────────────────────────────────────────────────────────────────
user_text = st.text_area(
    label       = "pesan",
    value       = st.session_state["input_text"],
    placeholder = "Ketik atau tempel pesan di sini...",
    height      = 130,
    label_visibility = "collapsed",
)

col_btn, col_clear = st.columns([4, 1])
with col_btn:
    check_clicked = st.button("🔍  Cek Pesan", use_container_width=True)
with col_clear:
    if st.button("✕ Hapus", use_container_width=True):
        st.session_state["input_text"] = ""
        st.rerun()

# ── Results ───────────────────────────────────────────────────────────────────
if check_clicked and user_text.strip():
    with st.spinner("Menganalisis pesan..."):
        result = predict(model, user_text)

    pred   = result["prediksi"]
    conf   = result["keyakinan"]
    proba  = result["probabilitas"]
    spam_p = proba.get("spam", 0)
    ham_p  = proba.get("ham",  0)

    is_spam = pred == "spam"
    card_cls   = "result-spam"  if is_spam else "result-ham"
    label_cls  = "result-label-spam" if is_spam else "result-label-ham"
    icon       = "🚫"           if is_spam else "✅"
    label_text = "SPAM"         if is_spam else "HAM"
    msg        = (
        "⚠️ Pesan ini kemungkinan besar adalah spam. Waspada terhadap link dan permintaan data pribadi."
        if is_spam else
        "✅ Pesan ini tampak aman (ham). Tidak terdeteksi sebagai spam."
    )

    st.markdown(f"""
    <div class="{card_cls}">
      <div style="display:flex;align-items:flex-start;justify-content:space-between;flex-wrap:wrap;gap:.8rem">
        <div>
          <span class="badge {'badge-red' if is_spam else 'badge-green'}" style="margin-bottom:.6rem">
            {icon} {label_text}
          </span>
          <div class="{label_cls}">{icon} Ini adalah {label_text}</div>
          <div class="result-conf">Keyakinan model: <strong>{conf:.1f}%</strong></div>
        </div>
      </div>
      <div class="result-msg">"{user_text[:120]}{'...' if len(user_text)>120 else ''}"</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Charts
    col_gauge, col_bar = st.columns(2)
    with col_gauge:
        st.markdown("<p style='text-align:center;font-size:.8rem;color:#7a80a0;margin-bottom:-.5rem'>Probabilitas Spam</p>", unsafe_allow_html=True)
        st.plotly_chart(gauge_chart(spam_p), use_container_width=True, config={"displayModeBar": False})

    with col_bar:
        st.markdown("<p style='text-align:center;font-size:.8rem;color:#7a80a0;margin-bottom:-.5rem'>Distribusi Probabilitas</p>", unsafe_allow_html=True)
        st.plotly_chart(prob_bar(proba), use_container_width=True, config={"displayModeBar": False})

    # Processed text
    with st.expander("🔬 Detail Preprocessing"):
        st.markdown(f"""
        <div class="card">
          <p style="font-size:.78rem;color:#7a80a0;margin-bottom:.4rem">Teks setelah preprocessing:</p>
          <p style="font-size:.88rem;color:#c5c9dd;font-family:monospace;word-break:break-all">{result['processed'] or '(kosong setelah preprocessing)'}</p>
        </div>
        """, unsafe_allow_html=True)

elif check_clicked and not user_text.strip():
    st.markdown("""
    <div class="card" style="border-color:rgba(247,192,84,.3)">
      <p style="margin:0;color:#f7c054">⚠️ Pesan tidak boleh kosong. Masukkan teks terlebih dahulu.</p>
    </div>
    """, unsafe_allow_html=True)


# ── Batch checker ─────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("<h3 style='font-family:Syne,sans-serif;font-size:1.15rem;margin-bottom:.3rem'>📋 Cek Banyak Pesan Sekaligus</h3>", unsafe_allow_html=True)
st.markdown("<p style='font-size:.85rem;color:#7a80a0;margin-bottom:.8rem'>Masukkan beberapa pesan, satu baris per pesan.</p>", unsafe_allow_html=True)

batch_text = st.text_area(
    label       = "batch",
    placeholder = "Pesan pertama...\nPesan kedua...\nPesan ketiga...",
    height      = 120,
    label_visibility = "collapsed",
)

if st.button("📊  Analisis Semua Pesan", use_container_width=True):
    lines = [l.strip() for l in batch_text.splitlines() if l.strip()]
    if not lines:
        st.markdown("<div class='card' style='border-color:rgba(247,192,84,.3)'><p style='margin:0;color:#f7c054'>⚠️ Masukkan minimal satu pesan.</p></div>", unsafe_allow_html=True)
    else:
        rows = []
        for msg in lines:
            r = predict(model, msg)
            rows.append({
                "Pesan"     : msg[:60] + ("..." if len(msg) > 60 else ""),
                "Prediksi"  : ("🚫 SPAM" if r["prediksi"] == "spam" else "✅ HAM"),
                "Keyakinan" : f"{r['keyakinan']:.1f}%",
                "P(Spam)"   : f"{r['probabilitas'].get('spam', 0):.1f}%",
                "P(Ham)"    : f"{r['probabilitas'].get('ham', 0):.1f}%",
            })
        df = pd.DataFrame(rows)

        spam_count = sum(1 for r in rows if "SPAM" in r["Prediksi"])
        ham_count  = len(rows) - spam_count

        mc1, mc2, mc3 = st.columns(3)
        mc1.metric("Total Pesan",    len(rows))
        mc2.metric("Spam Terdeteksi", spam_count, delta=f"{spam_count/len(rows)*100:.0f}%", delta_color="inverse")
        mc3.metric("Ham (Aman)",      ham_count,  delta=f"{ham_count/len(rows)*100:.0f}%")

        st.markdown("<br>", unsafe_allow_html=True)
        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
        )


# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center;margin-top:3rem;padding-top:1.5rem;border-top:1px solid #252a3a">
  <p style="font-size:.78rem;color:#4a5070;margin:0">
    SpamShield · Dibangun dengan Streamlit & Scikit-learn · Model: Linear SVM + TF-IDF
  </p>
</div>
""", unsafe_allow_html=True)
