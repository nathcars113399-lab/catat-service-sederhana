import csv
import random
import time
from pathlib import Path


CSV_FILE = Path(__file__).with_name("data_service.csv")
CSV_HEADER = ["ID", "Date", "Nama", "Layanan", "Harga"]


def input_data_service():
    id_service = random.randint(1000, 9999)
    date_service = time.strftime("%d-%m-%Y")
    nama_service = input("Masukkan Nama Pelanggan: ")
    layanan_service = input("Masukkan Layanan: ")
    harga_service = input("Masukkan Harga: ")

    with CSV_FILE.open(mode="a+", newline="", encoding="utf-8") as file:
        file.seek(0, 2)
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(CSV_HEADER)

        writer.writerow(
            [id_service, date_service, nama_service, layanan_service, harga_service]
        )

    print(f"Data layanan untuk {nama_service} berhasil disimpan ke {CSV_FILE.name}.")


def main():
    while True:
        input_data_service()
        lanjut = input("Catat layanan pelanggan berikutnya? (y/n): ").strip().lower()
        if lanjut != "y":
            break


if __name__ == "__main__":
    main()
