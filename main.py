meme_dict = {
    "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
    "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
    "WYD": "Menanyakan tentang apa yang sedang dilakukan sekarang"
}

word = input("Ketik kata yang tidak kamu mengerti (gunakan huruf kapital semua!): ")

if word in meme_dict.keys():
    print("Arti dari", word, "adalah:", meme_dict[word])
else:
    print("Maaf, kata tersebut tidak ditemukan dalam kamus.")
