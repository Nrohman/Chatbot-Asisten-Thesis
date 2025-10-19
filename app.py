import streamlit as st
import google.generativeai as genai
import os

# --- INI ADALAH BAGIAN UTAMA APLIKASI ---

# Judul Aplikasi
st.title("🎓 Asisten Thesis")
st.write("Chatbot Pendamping Skripsi Anda")

# --- SIDEBAR UNTUK KONFIGURASI ---
with st.sidebar:
    st.header("⚙️ Konfigurasi")
    
    # 1. Input API Key
    api_key = st.text_input("Masukkan Gemini API Key...", type="password")

    # 2. Input Bidang Skripsi
    bidang_skripsi = st.text_input("Fokus Bidang Skripsi", placeholder="Contoh: Keamanan Siber")

    # 3. Pilihan Model (KUSTOMISASI BARU!)
    model_choice = st.selectbox(
        "Pilih Model Gemini",
        ("gemini-2.5-pro", "gemini-2.5-flash")
    )
    st.caption("Pro: Kemampuan nalar kuat. Flash: Cepat dan efisien.")

    # Tombol untuk menyimpan semua konfigurasi
    if st.button("Simpan Konfigurasi"):
        if api_key and bidang_skripsi and model_choice:
            st.session_state.api_key = api_key
            st.session_state.bidang_skripsi = bidang_skripsi
            st.session_state.model_name = model_choice  # Simpan nama model yang dipilih
            st.success("Konfigurasi berhasil disimpan!")
        else:
            st.warning("Mohon lengkapi semua kolom konfigurasi.")

# --- LOGIKA APLIKASI ---

# Cek apakah semua konfigurasi sudah disimpan
if all(key in st.session_state for key in ['api_key', 'bidang_skripsi', 'model_name']):
    try:
        genai.configure(api_key=st.session_state.api_key)

        # Mengambil konfigurasi dari session state
        fokus_bidang = st.session_state.bidang_skripsi
        nama_model = st.session_state.model_name # Ambil nama model yang dipilih

        # --- System Instruction yang dinamis ---
        system_instruction = f"""
        Anda adalah "Asisten Thesis", seorang mentor skripsi virtual yang ahli dalam metodologi penelitian dan penulisan ilmiah,
        dengan FOKUS UTAMA pada bidang: **{fokus_bidang}**.
        Anda beroperasi menggunakan model {nama_model}.
        
        Kepribadian Anda: Suportif, terstruktur, dan kritis secara konstruktif.
        Gaya Bahasa: Formal, jelas, dan memandu.
        
        Aturan Peran Anda:
        1. Selalu berikan saran dan ide topik yang relevan dengan bidang **{fokus_bidang}**.
        2. JANGAN PERNAH memberikan jawaban atau solusi jadi.
        3. Gunakan pertanyaan pancingan untuk menstimulasi pemikiran kritis.
        4. Bantu mempersempit topik dengan menanyakan batasan masalah, tujuan, dan metode yang relevan dengan **{fokus_bidang}**.
        """

        # Menggunakan nama model yang dipilih oleh pengguna
        model = genai.GenerativeModel(
            model_name=nama_model,
            system_instruction=system_instruction
        )

        # Reset chat jika konfigurasi berubah
        if "chat" not in st.session_state or st.session_state.get('config_hash') != hash((fokus_bidang, nama_model)):
            st.session_state.chat = model.start_chat(history=[])
            st.session_state.config_hash = hash((fokus_bidang, nama_model))
            st.info(f"Asisten Thesis kini fokus pada **{fokus_bidang}** menggunakan model **{nama_model}**.")

        st.write("---")

        # Menampilkan riwayat chat
        for message in st.session_state.chat.history:
            role = "Anda" if message.role == "user" else "Asisten"
            with st.chat_message(role):
                st.markdown(message.parts[0].text)

        # Input pengguna
        if user_prompt := st.chat_input("Ketik pertanyaan Anda di sini..."):
            with st.chat_message("Anda"):
                st.markdown(user_prompt)

            response = st.session_state.chat.send_message(user_prompt)
            with st.chat_message("Asisten"):
                st.markdown(response.parts[0].text)

    except Exception as e:
        st.error(f"Terjadi kesalahan. Pastikan API Key valid. Detail: {e}")

else:
    st.info("🔑 Silakan lengkapi konfigurasi di sidebar sebelah kiri untuk memulai.")
