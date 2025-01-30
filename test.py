import os
import json
import hashlib

# Foydalanuvchi ma'lumotlari saqlanadigan fayl
USER_DATA_FILE = "/data/data/com.termux/files/home/users.json"

# Agar fayl mavjud bo‘lmasa, uni yaratamiz
if not os.path.exists(USER_DATA_FILE):
    with open(USER_DATA_FILE, "w") as f:
        json.dump({}, f)

# Parolni hash qilish funksiyasi
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Foydalanuvchini ro‘yxatdan o‘tkazish
def register():
    username = input("Yangi login kiriting: ")

    # Fayldan mavjud foydalanuvchilarni o‘qish
    with open(USER_DATA_FILE, "r") as f:
        users = json.load(f)

    if username in users:
        print("❌ Bu foydalanuvchi allaqachon mavjud!")
        return

    password = input("Parol kiriting: ")
    users[username] = hash_password(password)

    # Yangi foydalanuvchini saqlash
    with open(USER_DATA_FILE, "w") as f:
        json.dump(users, f)

    print("✅ Foydalanuvchi muvaffaqiyatli ro‘yxatdan o‘tdi!")

# Foydalanuvchini tizimga kiritish
def login():
    username = input("Loginni kiriting: ")
    password = input("Parolni kiriting: ")

    # Fayldan foydalanuvchilarni o‘qish
    with open(USER_DATA_FILE, "r") as f:
        users = json.load(f)

    if username in users and users[username] == hash_password(password):
        print("✅ Tizimga muvaffaqiyatli kirdingiz!")
    else:
        print("❌ Xato: Login yoki parol noto‘g‘ri!")

# Termux-dan chiqish
def termux_exit():
    print("🚪 Termux dasturidan chiqilmoqda...")
    os.system("exit")

# Bosh menyu
def main():
    while True:
        print("\n📌 Termux Auth System")
        print("1️⃣ Register (Ro‘yxatdan o‘tish)")
        print("2️⃣ Login (Tizimga kirish)")
        print("3️⃣ Exit (Chiqish)")

        choice = input("Buyruqni tanlang (1/2/3): ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            termux_exit()
            break
        else:
            print("❌ Noto‘g‘ri buyruq! Qaytadan urinib ko‘ring.")

# Dastur ishga tushishi
if __name__ == "__main__":
    main()
