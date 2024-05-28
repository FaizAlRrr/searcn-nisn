import os
os.system("cls")
while True:
     data1 = {
          'nama' : "Faiz Al Rasyid",
          'nisn' : 1202,
          'alamat' : "Lahat"
     }
     data2 = {
          'nama' : "adit",
          'nisn' : 1201,
          'alamat' : "Lahat"
     }
     data3 = {
          'nama' : "Rasyid",
          'nisn' : 1222,
          'alamat' : "Palmbang"
     }
     data4 = {
          'nama' : "AlElDoel",
          'nisn' : 1120,
          'alamat' : "Lahat"
     }
     data5 = {
          'nama' : "Kaguma",
          'nisn' : 1521,
          'alamat' : "Jakarta"
     }
     data6 = {
          'nama' : "Spiderman",
          'nisn' : 1234,
          'alamat' : "Kalimantan"
     }
     data7 = {
          'nama' : "Kayang",
          'nisn' : 5324,
          'alamat' : "Kalimantan"
     }
     data8 = {
          'nama' : "Kopi satu",
          'nisn' : 8462,
          'alamat' : "Kalimantan"
     }

     data_pelajar = {
          1202 : data1,
          1201 : data2,
          1222 : data3,
          1120 : data4,
          1521 : data5,
          1234 : data6,
          5324 : data7,
          8462 : data8
     }


     try:
          nisnSiswa = int(input("Masukkan NISN siswa : "))
          if nisnSiswa in data_pelajar:
               print(f"Nama siswa\t: {data_pelajar[nisnSiswa] ['nama']}\nAlamat siswa\t: {data_pelajar[nisnSiswa]["alamat"]}\nNISN\t\t: {data_pelajar[nisnSiswa] ['nisn']}")
          else:
               print("NISN tidak ditemukan silahkan coba lagi")
     except ValueError:
               print("Masukkan angka!")