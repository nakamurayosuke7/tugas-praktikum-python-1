def soal1():
    output1 = '''
    UNIVERSITAS KOMPUTER INDONESIA
    Jl. Dipati Ukur 112-114, Bandung
    '''
    print(output1)
    print("-"*50)
    output2 = '''
    Nama        : Oemar Bakti
    NIM         : 1020588
    Jurusan     : Teknik Informatika
    Fakultas    : Teknik dan Ilmu komputer
    '''
    print(output2)
    print("-"*50)
def soal2():
    v = float(input("KECEPATAN RATA-RATA (km/jam)     :   "))
    t = float(input("WAKTU TEMPUH (jam)               :   "))
    print("JARAK TEMPUH                     :  ", v*t)
def soal3():
    print("PROGRAM MENGHITUNG PEMBELIAN")
    print("-" * 50)
    harga_satuan = int(input("HARGA SATUAN      :   "))
    jumlah_pembelian = int(input("JUMLAH PEMBELIAN  :   "))
    diskon = harga_satuan*jumlah_pembelian * 10/100
    print("DISKON           :   ", diskon)
    print("HARGA TOTAL      :   ", harga_satuan*jumlah_pembelian - diskon)
    print("-" * 50)
def soal4():
    print("PROGRAM MENGHITUNG PEMBELIAN")
    print("-" * 50)
    harga_satuan = int(input("HARGA SATUAN      :   "))
    jumlah_pembelian = int(input("JUMLAH PEMBELIAN  :   "))
    diskon = int(input("DISKON            :   "))
    print("HARGA TOTAL      :   ", jumlah_pembelian*harga_satuan-diskon)
    print("-" * 50)
def soal5():
    print("DATA PELANGGAN")
    input("NAMA PELANGGAN       :      ")
    percakapan = int(input("PERCAKAPAN           :      ")) #per menit
    sms = int(input("SMS                  :      ")) #kali
    print("\nTAGIHAN")
    print("ABONEMEN             :     Rp  20000")
    print("BIAYA PERCAKAPAN     :     Rp ", 1000*percakapan)
    print("BIAYA SMS            :     Rp ", 300 * sms)
    print("TOTAL TAGIHAN        :     Rp ", 300 * sms + 1000*percakapan + 20000)
def soal6():
    print("PROGRAM GAJI PEGAWAI")
    input("NAMA KARYAWAN              :       ")
    jumlah_anak = int(input("JUMLAH ANAK                :       "))
    print("-"*50)
    gaji_pokok = int(input("GAJI POKOK                 :    Rp "))
    tunjangan_kesejahteraan = 20 / 100 * gaji_pokok
    print("TUNJANGAN KESEJAHTERAAN    :    Rp", tunjangan_kesejahteraan)
    tunjangan_keluarga = 10 / 100 * gaji_pokok / jumlah_anak
    print("TUNJANGAN KELUARGA         :    Rp", tunjangan_keluarga)
    gaji_kotor = gaji_pokok + tunjangan_keluarga + tunjangan_kesejahteraan
    pajak = 0.1/100 * gaji_kotor
    print("PAJAK                      :    Rp", pajak)
    print("GAJI KOTOR                 :    Rp", gaji_kotor)
    print("GAJI BERSIH                :    Rp", gaji_pokok - pajak )
soal1()
soal2()
soal3()
soal4()
soal5()
soal6()
