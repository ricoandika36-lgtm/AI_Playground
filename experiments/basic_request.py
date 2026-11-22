from core.config import MODEL_NAME
def run_basic_request(client):
    print("\n=== EXPERIMENT 01: BASIC REQUEST ===")

    response = client.responses.create(
        model=MODEL_NAME,
        input="Saya sedang membangun aplikasi manajemen inventaris bernama Resima. Tech stack: "
        "- Frontend: React + Vite"
        "- Backend: Python + FastAPI"
        "- Database: PostgreSQL"
        "- ORM: SQLAlchemy" 
        "Saya ingin mengembangkan fitur AI Inventory Assistant yang dapat:" \
        "1. Memahami pertanyaan pengguna tentang stok barang." \
        "2. Mengambil data inventaris dari database." \
        "3. Mendeteksi barang yang stoknya menipis." \
        "4. Memberikan rekomendasi restock berdasarkan data." \
        "5. Menjelaskan alasan di balik setiap rekomendasi." \
        "Tugas kamu:" \
        "A. Analisis arsitektur sistem yang paling tepat." \
        "B. Jelaskan bagaimana LLM berkomunikasi dengan backend." \
        "C. Rancang mekanisme tool calling agar AI dapat mengambil data stok." \
        "D. Buat contoh implementasi Python menggunakan FastAPI dan OpenAI Responses API." \
        "E. Jelaskan bagaimana mencegah AI mengarang data inventaris." \
        "F. Identifikasi risiko keamanan dan cara mengatasinya." \
        "Persyaratan:"
        "- Jangan langsung membuat sistem yang terlalu kompleks."
        "- Gunakan prinsip clean architecture."
        "- Pisahkan tanggung jawab LLM, backend, dan database."
        "- Berikan contoh kode yang realistis."
        "- Jelaskan keputusan teknis dan trade-off-nya." \
        "Susun jawaban secara sistematis dari arsitektur hingga implementasi."
    )

    print("\n[AI RESPONSE]")
    print(response.output_text)

    print("\n[TOKEN USAGE]")
    print(f"input tokens : {response.usage.input_tokens}")
    print(f"output tokens : {response.usage.output_tokens}")
    print(f"total tokens : {response.usage.total_tokens}")
    print(f"Model used: {response.model}")
