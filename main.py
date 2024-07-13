meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
}

word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

for i in range(len(meme_dict)):
    meme=(input("Masukan key"))
    print(meme_dict[meme])
