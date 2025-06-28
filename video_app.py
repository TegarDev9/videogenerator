import streamlit as st
import pandas as pd
import json
import time

# Helper functions to simulate API calls and workflow logic
# In a real application, these would be actual API calls.

def generate_video_concept(api_key, topic):
    """
    Simulates calling an AI agent to generate a video concept.
    In the real workflow, this uses an OpenAI GPT-4.1 model.
    """
    if not api_key:
        st.error("Kunci API OpenAI diperlukan.")
        return None
    st.info("Menghasilkan konsep video dengan AI...")
    time.sleep(2) # Simulate API call delay
    # Mocked response based on the workflow's example
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
    """Simulates saving the generated script idea to Google Sheets."""
    if not doc_id or not sheet_id:
        st.error("ID Dokumen dan ID Sheet Google Sheets diperlukan.")
        return False
    st.info("Menyimpan ide skrip ke Google Sheets...")
    time.sleep(1)
    # This would be a gspread or similar API call
    st.session_state.google_sheet_data.append(idea_data)
    st.success("Ide berhasil disimpan ke Google Sheets.")
    return True

def create_veo3_prompt(api_key, idea, environment):
    """
    Simulates creating a Veo3-compatible prompt using an AI agent.
    """
    if not api_key:
        st.error("Kunci API OpenAI diperlukan.")
        return None
    st.info("Membuat prompt yang kompatibel dengan Veo3...")
    time.sleep(2)
    # Mocked response for Veo3 prompt
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
    Simulates calling the Veo3 API (via fal.run) to generate a video.
    """
    if not api_key:
        st.error("Kunci API Fal AI diperlukan.")
        return None
    st.info("Mengirimkan permintaan pembuatan video ke Veo3...")
    time.sleep(2)
    st.warning("Memproses video... Ini mungkin memakan waktu beberapa menit.")
    for i in range(5):
        time.sleep(1) # Simulates 5 minute wait
    
    # Mocked response with a video URL
    video_url = "https://storage.googleapis.com/gtv-videos-bucket/sample/ForBiggerFun.mp4"
    st.success("Video berhasil dibuat!")
    return {"video": {"url": video_url}}

def log_video_output_to_sheets(doc_id, sheet_id, idea, video_url):
    """Simulates logging the final video output URL to Google Sheets."""
    if not doc_id or not sheet_id:
        st.error("ID Dokumen dan ID Sheet Google Sheets diperlukan.")
        return False
    st.info("Mencatat output video final ke Google Sheets...")
    time.sleep(1)
    
    # Find the corresponding idea and update it
    for row in st.session_state.google_sheet_data:
        if row.get('Idea') == idea:
            row['final_output'] = video_url
            row['production'] = 'selesai'
            break
            
    st.success("Output video berhasil dicatat.")
    return True

def upload_to_blotato(api_key, video_url):
    """Simulates uploading the video to Blotato."""
    if not api_key:
        st.error("Kunci API Blotato diperlukan.")
        return None
    st.info("Mengunggah video ke Blotato...")
    time.sleep(2)
    # Mocked response
    blotato_url = f"https://blotato.com/media/{hash(video_url)}"
    st.success(f"Video berhasil diunggah ke Blotato.")
    return {"url": blotato_url}

def post_to_social_media(api_key, platform, account_id, text, media_url):
    """Simulates posting to a social media platform via Blotato."""
    if not api_key:
        st.error("Kunci API Blotato diperlukan.")
        return None
    st.info(f"Memposting ke {platform}...")
    time.sleep(1.5)
    # In a real app, you would check the response
    st.success(f"Berhasil memposting ke {platform} (ID Akun: {account_id}).")
    return {"status": "sukses", "platform": platform}

# Initialize session state for data persistence
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
if 'blotato_media_url' not in st.session_state:
    st.session_state.blotato_media_url = None

# --- UI APLIKASI STREAMLIT ---
st.set_page_config(layout="wide")

st.title("🎬 Otomatisasi Pembuatan & Publikasi Video")
st.markdown("Aplikasi ini mengotomatiskan seluruh alur kerja pembuatan video berdasarkan alur kerja n8n Anda: menghasilkan ide, membuat video dengan AI, dan mempublikasikannya ke semua saluran sosial Anda.")

# --- Kolom Konfigurasi ---
st.sidebar.header("🔑 Konfigurasi API & Sheets")
openai_api_key = st.sidebar.text_input("Kunci API OpenAI (untuk Ide)", type="password")
fal_api_key = st.sidebar.text_input("Kunci API Fal AI (untuk Video)", type="password")
blotato_api_key = st.sidebar.text_input("Kunci API Blotato", type="password")
google_doc_id = st.sidebar.text_input("ID Dokumen Google Sheets", "")
google_sheet_id = st.sidebar.text_input("ID Sheet Google Sheets", "")

st.sidebar.header("📱 ID Media Sosial")
instagram_id = st.sidebar.text_input("ID Instagram", "1111")
youtube_id = st.sidebar.text_input("ID YouTube", "1111")
tiktok_id = st.sidebar.text_input("ID TikTok", "1111")
facebook_id = st.sidebar.text_input("ID Facebook", "1111")
twitter_id = st.sidebar.text_input("ID Twitter", "1111")
linkedin_id = st.sidebar.text_input("ID LinkedIn", "1111")
# --- Akhir Kolom Konfigurasi ---

st.header("🚀 Mulai Alur Kerja Anda")
video_topic = st.text_input("Masukkan topik untuk video Anda:", "Yeti melakukan Vlog dengan tongsisnya")

if st.button("Jalankan Alur Kerja Otomatisasi Lengkap"):
    if not all([openai_api_key, fal_api_key, blotato_api_key, google_doc_id, google_sheet_id]):
        st.error("Silakan isi semua kunci API dan detail Google Sheets di sidebar.")
    else:
        st.session_state.workflow_started = True
        st.session_state.video_concept = None
        st.session_state.veo3_prompt = None
        st.session_state.video_result = None
        st.session_state.blotato_media_url = None
        
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

        # --- LANGKAH 3: Publikasikan Video ke Media Sosial ---
        if st.session_state.video_result:
            with st.expander("✅ LANGKAH 3: Mempublikasikan Video ke Media Sosial", expanded=True):
                st.session_state.blotato_media_url = upload_to_blotato(blotato_api_key, st.session_state.video_result['video']['url'])
                if st.session_state.blotato_media_url:
                    caption = st.session_state.video_concept['Caption']
                    media_url = st.session_state.blotato_media_url['url']
                    
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        post_to_social_media(blotato_api_key, "Instagram", instagram_id, caption, media_url)
                        post_to_social_media(blotato_api_key, "Facebook", facebook_id, caption, media_url)
                    with col2:
                        post_to_social_media(blotato_api_key, "YouTube", youtube_id, caption, media_url)
                        post_to_social_media(blotato_api_key, "Twitter", twitter_id, caption, media_url)
                    with col3:
                        post_to_social_media(blotato_api_key, "TikTok", tiktok_id, caption, media_url)
                        post_to_social_media(blotato_api_key, "LinkedIn", linkedin_id, caption, media_url)

st.header("📊 Data Google Sheets (Simulasi)")
if st.session_state.google_sheet_data:
    df = pd.DataFrame(st.session_state.google_sheet_data)
    st.dataframe(df)
else:
    st.info("Tidak ada data yang dihasilkan.")

