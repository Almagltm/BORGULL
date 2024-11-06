import random
import string

# Daftar pertanyaan dan respons
responses = {
    "halo": ["Hai!", "Halo! Apa kabar?", "Selamat datang!"],
    "selamat pagi": ["selamat pagi juga"],
    "apa kabar": ["Saya baik-baik saja, terima kasih!", "Baik, dan kamu?"],
    "siapa kamu": ["Saya adalah chatbot sederhana Alma", "Saya chatbot, siap membantu!"],
    "terima kasih": ["Sama-sama!", "Senang bisa membantu!"],
    "bagaimana aturan di USU":["Aturan berpakaian di USU yaitu,anda harus menggunakan kemeja atau minimal baju berkerah"],
    "apakah boleh memakai sendal":["tidak boleh!! karena itu tidak sopan"],
    "bagaimana dengan rambut":["untuk rambut tidak ada ketentuan asalkan rambut tidak mengganggu kamu ketika belajar yahh"],
    "i love you":["i love you too, i love u more"],
    "selamat tinggal": ["Sampai jumpa!", "Selamat tinggal! Semoga harimu menyenangkan!"]
    
}

def chatbot_response(user_input):
    """Menghasilkan respons berdasarkan input pengguna."""
    user_input = user_input.lower()
    user_input = user_input.translate(str.maketrans("", "", string.punctuation))

    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    
    return "Maaf, saya tidak mengerti."

def main():
    """Fungsi utama untuk menjalankan chatbot."""
    print("Chatbot: Halo! Saya di sini untuk membantu. Ketik 'selamat tinggal' untuk keluar.")
    
    while True:
        user_input = input("Anda: ")
        
        if user_input.lower() == "selamat tinggal":
            print("Chatbot: Selamat tinggal! Semoga harimu menyenangkan!")
            break
        
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
