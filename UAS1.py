while True:
    try:
        def fungsi():
            print("Daftar MataKuliah Pemrograman :")
            x = ["Pemrograman Basis data", "Pemrograman Berbasis Event",
                 "Pemrograman Web", "Pemrograman Berorientasi Object",
                 "Pemrograman Visual", "Pemrograman .Net"]
            for i in x:
                print(i)
            a = int(
                input("Masukkan index elemen nama Mata Kuliah yang ingin dihapus :"))
            b = int(
                input("isi dengan bilangan negatif untuk berhenti menghapus nama Mata Kuliah :"))

            def hapus():
                x.pop(a)
                print("HASIL PEMILIHAN")
                for h in x:
                    if a >= 0 and b < 0:
                        print(h)

            hapus()

        fungsi()
        break
    except:
        print("\r\nYang anda masukkan bukan angka, silahkan pilih kembali!")
        print("="*30)
