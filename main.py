import os
import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"❌ Gagal menjalankan: {command}")
        exit(1)

def main():
    print("🚀 Program Auto Git Update by Shohib\n")

    if not os.path.exists(".git"):
        print("❌ Folder ini bukan repository Git!")
        return

    print("📋 Mengecek perubahan...")
    run_command("git status")

    print("\n➕ Menambahkan semua perubahan...")
    run_command("git add .")

    pesan = input("\n📝 Masukkan pesan commit (kosongkan untuk 'update otomatis'): ")
    if not pesan.strip():
        pesan = "update otomatis"

    print("\n📦 Commit perubahan...")
    run_command(f'git commit -m "{pesan}"')

    print("\n⬆️ Mengirim perubahan ke GitHub...")
    run_command("git push origin main")

    print("\n✅ Semua perubahan berhasil diunggah ke GitHub!\n")

if __name__ == "__main__":
    main()
