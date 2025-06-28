import streamlit as st
import pandas as pd
import json
import time

# Fungsi pembantu untuk mensimulasikan panggilan API dan logika alur kerja
# Dalam aplikasi nyata, ini akan menjadi panggilan API yang sebenarnya.

def generate_video_concept(api_key, topic):
    """
    Mensimulasikan pemanggilan agen AI untuk menghasilkan konsep video.
    Dalam alur kerja nyata, ini menggunakan model OpenAI GPT-4.1.
    """
    if not api_key:
        st.error("Kunci API OpenAI diperlukan.")
        return None
    st.info("Menghasilkan konsep video dengan AI...")
    time.sleep(2) # Mensimulasikan penundaan panggilan API
    # Respons tiruan berdasarkan contoh alur kerja
    mock_response = {
        "output": [{
            "Caption": f"Lihatlah Yeti ini nge-vlog! 🏔️ #yeti #vlog #himalaya #cryptozoology #viral #petualangan #menjelajah #trending #fyp #komedi #makhlukmitos",
            "Idea": "Yeti berbicara ke kamera, membuat vlog dengan tongsisnya.",
            "Environment": "Puncak gunung yang tertutup salju, matahari terbenam di latar belakang, gaya dokumenter genggam.",
            "Status": "untuk produksi"
        }]
    }
    st.success("Konsep video berhasil dibuat.")
    return mock_response['output'][0]

def save_idea_to_sheets(doc_id, sheet_id, idea_data):
    """Mensimulasikan penyimpanan ide skrip yang dihasilkan ke Google Sheets."""
    if not doc_id or not sheet_id:
        st.error("ID Dokumen dan ID Sheet Google Sheets diperlukan.")
        return False
    st.info("Menyimpan ide skrip ke Google Sheets...")
    time.sleep(1)
    # Ini akan menjadi panggilan API gspread atau yang serupa
    st.session_state.google_sheet_data.append(idea_data)
    st.success("Ide berhasil disimpan ke Google Sheets.")
    return True

def create_veo3_prompt(api_key, idea, environment):
    """
    Mensimulasikan pembuatan prompt yang kompatibel dengan Veo3 menggunakan agen AI.
    """
    if not api_key:
        st.error("Kunci API OpenAI diperlukan.")
        return None
    st.info("Membuat prompt yang kompatibel dengan Veo3...")
    time.sleep(2)
    # Respons tiruan untuk prompt Veo3
    mock_prompt = (
        f"Seorang yeti yang ramah sedang vlogging selfie-style dari puncak gunung yang tertutup salju saat matahari terbenam. "
        f"Karakter utama: Yeti besar berbulu putih dengan senyum ramah. "
        f"Mereka berkata: 'Wow, pemandangannya luar biasa dari sini! Kalian tidak akan percaya ini!'. "
        f"Mereka mengarahkan kamera untuk menunjukkan pemandangan lembah di bawah. "
        f"Waktu: Senja. "
        f"Lensa: Lensa sudut lebar, gaya dokumenter genggam. "
        f"Audio: Angin sepoi-sepoi, suara langkah kaki di salju. "
        f"Latar Belakang: {environment}"
    )
    st.success("Prompt Veo3 berhasil dibuat.")
    return mock_prompt

def generate_video_with_veo3(api_key, prompt):
    """
    Mensimulasikan pemanggilan API Veo3 (melalui fal.run) untuk menghasilkan video.
    """
    if not api_key:
        st.error("Kunci API Fal AI diperlukan.")
        return None
    st.info("Mengirimkan permintaan pembuatan video ke Veo3...")
    time.sleep(2)
    st.warning("Memproses video... Ini mungkin memakan waktu beberapa menit.")
    for i in range(5):
        time.sleep(1) # Mensimulasikan tunggu 5 menit
    
    # Respons tiruan dengan URL video
    video_url = "https://storage.googleapis.com/gtv-videos-bucket/sample/ForBiggerFun.mp4"
    st.success("Video berhasil dibuat!")
    return {"video": {"url": video_url}}

def log_video_output_to_sheets(doc_id, sheet_id, idea, video_url):
    """Mensimulasikan pencatatan URL output video final ke Google Sheets."""
    if not doc_id or not sheet_id:
        st.error("ID Dokumen dan ID Sheet Google Sheets diperlukan.")
        return False
    st.info("Mencatat output video final ke Google Sheets...")
    time.sleep(1)
    
    # Temukan ide yang sesuai dan perbarui
    for row in st.session_state.google_sheet_data:
        if row.get('Idea') == idea:
            row['final_output'] = video_url
            row['production'] = 'selesai'
            break
            
    st.success("Output video berhasil dicatat.")
    return True

# Inisialisasi status sesi untuk persistensi data
if 'google_sheet_data' not in st.session_state:
    st.session_state.google_sheet_data = []
if 'workflow_started' not in st.session_state:
    st.session_state.workflow_started = False
if 'video_concept' not in st.session_state:
    st.session_state.video_concept = None
if 'veo3_prompt' not in st.session_state:
    st.session_state.veo3_prompt = None
if 'video_result' not in st.session_state:
    st.session_state.video_result = None

# --- UI APLIKASI STREAMLIT ---
st.set_page_config(layout="wide")

st.title("🎬 Otomatisasi Pembuatan Video")
st.markdown("Aplikasi ini mengotomatiskan alur kerja pembuatan video berdasarkan alur kerja n8n Anda: menghasilkan ide dan membuat video dengan AI.")

# --- Kolom Konfigurasi ---
st.sidebar.header("🔑 Konfigurasi API & Sheets")
openai_api_key = st.sidebar.text_input("Kunci API OpenAI (untuk Ide)", type="password")
fal_api_key = st.sidebar.text_input("Kunci API Fal AI (untuk Video)", type="password")
google_doc_id = st.sidebar.text_input("ID Dokumen Google Sheets", "")
google_sheet_id = st.sidebar.text_input("ID Sheet Google Sheets", "")
# --- Akhir Kolom Konfigurasi ---

st.header("🚀 Mulai Alur Kerja Anda")
video_topic = st.text_input("Masukkan topik untuk video Anda:", "Yeti melakukan Vlog dengan tongsisnya")

if st.button("Jalankan Alur Kerja Otomatisasi"):
    if not all([openai_api_key, fal_api_key, google_doc_id, google_sheet_id]):
        st.error("Silakan isi semua kunci API dan detail Google Sheets di sidebar.")
    else:
        st.session_state.workflow_started = True
        st.session_state.video_concept = None
        st.session_state.veo3_prompt = None
        st.session_state.video_result = None
        
        # --- LANGKAH 1: Hasilkan Skrip & Prompt ---
        with st.expander("✅ LANGKAH 1: Menghasilkan Skrip & Prompt dengan AI", expanded=True):
            st.session_state.video_concept = generate_video_concept(openai_api_key, video_topic)
            if st.session_state.video_concept:
                st.json(st.session_state.video_concept)
                save_idea_to_sheets(google_doc_id, google_sheet_id, st.session_state.video_concept)

        # --- LANGKAH 2: Buat Video Menggunakan Veo3 ---
        if st.session_state.video_concept:
            with st.expander("✅ LANGKAH 2: Membuat Video Menggunakan Veo3", expanded=True):
                st.session_state.veo3_prompt = create_veo3_prompt(
                    openai_api_key,
                    st.session_state.video_concept['Idea'],
                    st.session_state.video_concept['Environment']
                )
                if st.session_state.veo3_prompt:
                    st.text_area("Prompt Veo3 yang Dihasilkan", st.session_state.veo3_prompt, height=200)
                    st.session_state.video_result = generate_video_with_veo3(fal_api_key, st.session_state.veo3_prompt)
                    if st.session_state.video_result:
                        st.video(st.session_state.video_result['video']['url'])
                        log_video_output_to_sheets(
                            google_doc_id,
                            google_sheet_id,
                            st.session_state.video_concept['Idea'],
                            st.session_state.video_result['video']['url']
                        )

st.header("📊 Data Google Sheets (Simulasi)")
if st.session_state.google_sheet_data:
    df = pd.DataFrame(st.session_state.google_sheet_data)
    st.dataframe(df)
else:
    st.info("Tidak ada data yang dihasilkan.")


