# Mendefinisikan fungsi untuk mengambil uang
def ambil_uang(saldo, jumlah):
  # Memeriksa apakah jumlah yang diminta tersedia di rekening
  if jumlah > saldo:
    print("Maaf, Anda tidak dapat mengambil jumlah tersebut")
  else:
    # Menghitung saldo setelah mengambil uang
    saldo = saldo - jumlah
    print("Anda telah mengambil uang sebesar", jumlah)
    print("Saldo Anda saat ini adalah", saldo)

# Mendefinisikan fungsi untuk menyetor uang
def setor_uang(saldo, jumlah):
  # Menghitung saldo setelah menyetor uang
  saldo = saldo + jumlah
  print("Anda telah menyetor uang sebesar", jumlah)
  print("Saldo Anda saat ini adalah", saldo)

# Mendefinisikan fungsi utama
def main():
  # Saldo awal
  saldo = 1000

  # Menampilkan menu
  print("Selamat datang di ATM kami!")
  print("Pilih transaksi yang ingin Anda lakukan:")
  print("1. Ambil uang")
  print("2. Setor uang")
  print("3. Keluar")

  # Meminta input pilihan
  pilihan = input("Masukkan nomor pilihan Anda: ")

  # Melakukan transaksi sesuai dengan pilihan
  if pilihan == "1":
    jumlah = int(input("Masukkan jumlah uang yang ingin Anda ambil: "))
    ambil_uang(saldo, jumlah)
  elif pilihan == "2":
    jumlah = int(input("Masukkan jumlah uang yang ingin Anda setor: "))
    setor_uang(saldo, jumlah)
  elif pilihan == "3":
    print("Terima kasih telah menggunakan ATM kami.")
  else:
    print("Maaf, pilihan Anda tidak valid.")

# Memanggil fungsi utama
main()
