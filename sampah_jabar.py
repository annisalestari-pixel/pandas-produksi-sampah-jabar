import pandas as pd

# =====================================
# MEMBACA FILE CSV
# =====================================
# file csv berada di folder yang sama
data = pd.read_csv(
    "disperkim-od_16984_jumlah_sampah_yang_ditangani_berdasarkan_kabupatenkota_data.csv"
)

print("Data awal:")
print(data.head())


# =====================================
# SOAL NO 1
# Membuat DataFrame dengan kolom:
# nama kabupaten/kota, jumlah sampah, dan tahun
# =====================================
data_pilih = data[["nama_kabupaten_kota", "jumlah_sampah", "tahun"]]

print("\nSOAL NO 1:")
print(data_pilih.head())


# =====================================
# SOAL NO 2
# Menghitung total sampah untuk tahun tertentu
# menggunakan iterrows
# =====================================
tahun_dicari = 2015
total_sampah = 0

for i, baris in data_pilih.iterrows():
    if baris["tahun"] == tahun_dicari:
        total_sampah = total_sampah + baris["jumlah_sampah"]

print("\nSOAL NO 2:")
print("Total sampah tahun", tahun_dicari, "=", total_sampah)


# =====================================
# SOAL NO 3
# Menjumlahkan total sampah per tahun
# =====================================
total_per_tahun = {}

for i, baris in data_pilih.iterrows():
    tahun = baris["tahun"]
    jumlah = baris["jumlah_sampah"]

    if tahun in total_per_tahun:
        total_per_tahun[tahun] = total_per_tahun[tahun] + jumlah
    else:
        total_per_tahun[tahun] = jumlah

print("\nSOAL NO 3:")
for t in total_per_tahun:
    print("Tahun", t, "=", total_per_tahun[t])


# =====================================
# SOAL NO 4
# Menjumlahkan sampah per kabupaten/kota per tahun
# =====================================
hasil = {}

for i, baris in data_pilih.iterrows():
    kota = baris["nama_kabupaten_kota"]
    tahun = baris["tahun"]
    jumlah = baris["jumlah_sampah"]

    kunci = kota + " - " + str(tahun)

    if kunci in hasil:
        hasil[kunci] = hasil[kunci] + jumlah
    else:
        hasil[kunci] = jumlah

print("\nSOAL NO 4:")
for k in hasil:
    print(k, "=", hasil[k])


# =====================================
# MENYIMPAN HASIL KE CSV DAN EXCEL
# =====================================
hasil_akhir = []

for k in hasil:
    nama, tahun = k.split(" - ")
    hasil_akhir.append([nama, tahun, hasil[k]])

df_hasil = pd.DataFrame(
    hasil_akhir,
    columns=["Kabupaten/Kota", "Tahun", "Total Sampah"]
)

df_hasil.to_csv("hasil_sampah.csv", index=False)
df_hasil.to_excel("hasil_sampah.xlsx", index=False)

print("\nFile hasil_sampah.csv dan hasil_sampah.xlsx berhasil dibuat")
