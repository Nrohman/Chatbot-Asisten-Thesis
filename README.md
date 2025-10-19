🎓 Asisten Thesis - Chatbot Pendamping Skripsi
Sebuah chatbot cerdas berbasis AI yang dirancang untuk membantu mahasiswa tingkat akhir dalam proses pengerjaan skripsi, mulai dari brainstorming ide hingga menyusun kerangka penelitian.

(Ganti gambar di atas dengan screenshot aplikasi Anda yang sudah berjalan)

🧠 Tentang Proyek
Proses pengerjaan skripsi seringkali menjadi tantangan besar bagi mahasiswa, dipenuhi dengan kebingungan, kebuntuan ide (writer's block), dan kebutuhan akan bimbingan yang konstan. Asisten Thesis lahir sebagai solusi untuk masalah ini.

Proyek ini adalah sebuah aplikasi web interaktif yang berfungsi sebagai mentor atau dosen pembimbing virtual. Chatbot ini tidak memberikan jawaban jadi, melainkan dirancang untuk memandu mahasiswa dengan pertanyaan-pertanyaan kritis, membantu mereka menyusun kerangka berpikir, dan memberikan saran yang terstruktur. Tujuannya adalah untuk menjadi partner diskusi yang mendorong mahasiswa berpikir kritis dan menemukan solusinya sendiri, kapan pun mereka butuhkan.

✨ Fitur Utama
Konsultasi Interaktif: Antarmuka chat yang responsif untuk sesi konsultasi yang alami dan berkelanjutan.

Fokus Bidang Studi Kustom: Pengguna dapat memasukkan bidang studi spesifik (contoh: Keamanan Siber, IoT, Data Science), dan chatbot akan menyesuaikan semua saran dan idenya agar relevan dengan bidang tersebut.

Pilihan Model AI Fleksibel: Pengguna dapat memilih antara model gemini-1.5-pro untuk penalaran yang mendalam atau gemini-1.5-flash untuk respons yang lebih cepat dan efisien.

Antarmuka Web Modern: Dibangun menggunakan Streamlit untuk tampilan yang bersih, modern, dan mudah digunakan.

Aman & Privat: API Key pengguna diinput langsung di antarmuka, tidak disimpan di server, dan digunakan hanya selama sesi berlangsung.

🚀 Dibangun Menggunakan
Aplikasi ini dibangun menggunakan teknologi modern di bidang AI dan pengembangan web Python.

Frontend: Streamlit

Backend & AI: Python, LangChain, Google Gemini API

⚙️ Menjalankan Secara Lokal
Untuk menjalankan proyek ini di komputer Anda, ikuti langkah-langkah berikut:

Clone repositori ini:

Bash

git clone https://github.com/nama-anda/nama-repositori-anda.git
Masuk ke direktori proyek:

Bash

cd nama-repositori-anda
Instal semua library yang dibutuhkan: (Pastikan Anda memiliki file requirements.txt di repositori Anda)

Bash

pip install -r requirements.txt
Jalankan aplikasi Streamlit:

Bash

streamlit run app.py
Aplikasi akan terbuka secara otomatis di browser Anda.

Konfigurasi
Aplikasi ini tidak memerlukan file .env. Semua konfigurasi dilakukan langsung melalui antarmuka di sidebar:

Masukkan Gemini API Key Anda.

Tuliskan Fokus Bidang Skripsi Anda.

Pilih Model Gemini yang ingin digunakan.

Klik tombol "Simpan Konfigurasi" untuk memulai.

try now : https://colab.research.google.com/drive/14_zF9enZqbZCeUm4AKm2np5XDWzkDp0A#scrollTo=pkiH7e7fDkXr
