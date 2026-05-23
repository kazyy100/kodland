import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def gen_anime_quote(anime):

    quote_pool = {
        "NARUTO": [
            {"quote": "Aku tidak akan menyerah! Aku tidak akan mengalah! Aku tidak AKAN MENINGGALKAN TEMAN-TEMANKU!", "character": "Naruto Uzumaki"},
            {"quote": "Aku tidak peduli seberapa kuat musuhku, aku akan terus berjuang sampai akhir!", "character": "Sasuke Uchiha"},
            {"quote": "Kekuatan sejati datang dari dalam dirimu sendiri, bukan dari kekuatan yang diberikan oleh orang lain.", "character": "Kakashi Hatake"},
            {"quote": "Aku tidak akan pernah melupakan teman-temanku, bahkan jika aku harus berjuang sendirian!", "character": "Sakura Haruno"},    
        ],

    }

    quote = random.choice(quote_pool[anime])

    return f"{quote['quote']} - {quote['character']}"


def get_waste_type(waste):
    waste_types = {
        "plastik": "Sampah Plastik",
        "kertas": "Sampah Kertas",
        "logam": "Sampah Logam",
        "organik": "Sampah Organik",
        "elektronik": "Sampah Elektronik"
    }

    return waste_types.get(waste.lower(), "Jenis sampah tidak dikenali")
def get_reduce_waste_tips(how_many):
    tips = {
        "plastik": "Kurangi penggunaan plastik sekali pakai, gunakan tas belanja kain dan botol minum yang dapat digunakan kembali.",
        "kertas": "Gunakan kertas daur ulang, cetak dua sisi, dan hindari mencetak jika tidak perlu.",
        "logam": "Daur ulang logam seperti kaleng dan aluminium, dan hindari penggunaan produk logam sekali pakai.",
        "organik": "Komposkan sisa makanan dan limbah organik untuk mengurangi sampah yang masuk ke tempat pembuangan akhir.",
        "elektronik": "Daur ulang perangkat elektronik yang sudah tidak terpakai, dan hindari membeli perangkat baru jika masih bisa diperbaiki."
    }

    return random.choices(list(tips.values()), k=how_many)
