# Tugas Lab 1 dan Lab 2

* Simpan project Praktikum ini ke repository server
* Buat penjelasan setiap lab pada file Readme.md


## Bagaimana Caranya?
* Download terlebih dahulu **"Python"** dihalaman **https://www.python.org**,

![1](https://user-images.githubusercontent.com/56512562/72215169-213d4a80-3542-11ea-83d0-430f3609808a.png)
![3](https://user-images.githubusercontent.com/56512562/72215170-28645880-3542-11ea-8545-754cb643fa3c.png)
![5](https://user-images.githubusercontent.com/56512562/72215195-927cfd80-3542-11ea-9b51-80f05c2bd6ab.png)

* Setelah selesai, download juga **"Pycharm"** dihalaman **https://www.jetbrains.com/pycharm/**

![6](https://user-images.githubusercontent.com/56512562/72215388-2223ab80-3545-11ea-935a-48afe72ca608.png)
![7](https://user-images.githubusercontent.com/56512562/72215506-e50be900-3545-11ea-9a86-a8461eddb553.png)
  
  * **"Next"** saja hingga selesai
  
 ![8](https://user-images.githubusercontent.com/56512562/72215743-b3951c80-3549-11ea-9126-fb7d77017672.png)

  * Seperti inilah tampilannya.


## Nah setelah selesai mendownload semuanya maka kerjakan tugasnya

# Lab 1
Perlu diketahui perintah keluaran/output merupakan **"print()"**.

## Penggunaan "End"
**"End"** merupakan parameter yang berguna sebagai masukan **nilai karakter untuk mengakhiri statment/keputusan**. Ketika keluaran yang diperintahkan tanpa menggunakan fungsi **"End"** maka keluaran tersebut berada dalam baris baru. Tetapi ketika memakai fungsi **"End"** maka keluaran tidak akan langsung berada pada garis baru.
* Sebagai contoh :
```
# Penggunaan End
print("PENGGUNAAN END")
print('A', end='')
print('B', end='')
print('C', end='')
print()
print('X')
print('y')
print('Z')
```
* Maka output yang didapatkan :

![9](https://user-images.githubusercontent.com/56512562/72215961-218f1300-354d-11ea-91b7-379ba307a1ea.png)

* Keterangan :

Ketika **A**, **B**, dan **C** dalam baris yang sama tanpa mengunakan fungsi **"End"**, maka berbeda dengan **X**, **Y**, dan **Z** yang berada dalam baris yang berbeda dalam menggunakan fungsi **"End"**.

  * Ketika ingin menambahkan garis baru dengan manual bisa saja dengan menambahkan **"\n"** didepan maupun diakhir kalimat.
  * Sebagai contoh :
  
  ```print('A', end="\n")```
  
## Penggunaan "Separator"

**"Separator"** merupakan fungsi yang digunakan untuk memperjelas batas yang diberikan.

* Sebagai contoh :
```
# Penggunaan Separator
print("PENGGUNAAN SEPARATOR")
w, x, y, z = 10, 15, 20, 25
print(w, x, y, z)
print(w, x, y, z, sep=',')
print(w, x, y, z, sep='')
print(w, x, y, z, sep=':')
print(w, x, y, z, sep='-----')
```

* Maka output yang didapatkan :

![image](https://user-images.githubusercontent.com/56512562/72216117-62882700-354f-11ea-9370-ee39abf84515.png)

* Keterangan :

Kita dapat memasukan apa saja batasan yang diberikan untuk setiap indeks yang ada menggunakan fungsi **"Separator"** dengan memasukan perintah **"sep='batasan menurut anda'"** sebagai tambahan.

## Pemformatan String

**"Pemformatan String"** digunakan agar pengguna dapat mengatur dan mengubah posisi sedemikian ruoa yang diinginkan pengguna.

* Sebagai contoh pemformatan :
```
# String Format
print("STRING SEBELUM DI FORMAT")
print(0,10**0)
print(1,10**1)
print(2,10**2)
print(3,10**3)
print(4,10**4)
print(5,10**5)
print(6,10**6)
print(7,10**7)
print(8,10**8)
print(9,10**9)
print(10,10**10)
```

* Maka output yang didapatkan :

![00](https://user-images.githubusercontent.com/56512562/72216382-ceb85a00-3552-11ea-83cc-88ad3a8366fa.png)
Lalu kita akan merubahnya menjadi 
![000](https://user-images.githubusercontent.com/56512562/72216384-d841c200-3552-11ea-9fb6-d6437354b169.png)

dengan menggunakan kode tersebut :
```
# String Format
print("STRING SETELAH DI FORMAT")
print('{0:>3} {1:>16}'.format(0,10**0))
print('{0:>3} {1:>16}'.format(1,10**1))
print('{0:>3} {1:>16}'.format(2,10**2))
print('{0:>3} {1:>16}'.format(3,10**3))
print('{0:>3} {1:>16}'.format(4,10**4))
print('{0:>3} {1:>16}'.format(5,10**5))
print('{0:>3} {1:>16}'.format(6,10**6))
print('{0:>3} {1:>16}'.format(7,10**7))
print('{0:>3} {1:>16}'.format(8,10**8))
print('{0:>3} {1:>16}'.format(9,10**9))
print('{0:>3} {1:>16}'.format(10,10**10))
```
Contoh diatas terdapat simbol **{ }** yang merupakan **_placeholder_** atau **penempatan arguments**.


# Lab 2

Dalam pembahasan kali ini adalah menggunakan **Operator pada Python**. Sebagai contoh program untuk me**masukan** dua nilai input, men**cetak** nilai, meng**gabung**kan nilai, men**jumlah**kan, serta mem**bagi**kan nilai.

* Kode :
```
a=input("Masukan nilai a : ")
b=input("Masukan nilai b : ")
print("Variable a = ", a)
print("Variable b = ", b)
print("Hasil penggabungan {0} & {1} = %a".format(a,b) %(a+b))

#Konversi Nilai Variable
a=int(a)
b=int(b)

print("Hasil penjumlahan {0} + {1} = %d".format(a,b) %(a+b))
print("Hasil pembagian {0} / {1} = %d".format(a,b) %(a/b))
```

* Maka output yang didapatkan :

![01](https://user-images.githubusercontent.com/56512562/72216588-4f785580-3555-11ea-95cc-ac488ded5d01.png)

* Keterangan :

Untuk memasukan nilai, pengguna harus terlebih dahulu menjalankan program diatas. Sebagai contoh saya memasukan nilai **100** sebagai variabel pertama, dan memasukan nilai **50** sebagai variabel kedua. Setelah menentukan nilai variabel maka program akan menjalankan perintah selanjutnya yaitu menggabungkan kedua nilai variabel,
* Kode :
```print("Hasil penggabungan {0} & {1} = %a".format(a,b) %(a+b))```

input yang telah ditentukan akan diubah dengan fungsi **"Format"**. Output yang dihasilkan dalam program ini merupakan tipe data **"String"** yang dapat diubah bentuk dengan menggunakan **"Arithmetic Operator"**. Ada sebuah perintah yang tidak dapat diajalankan di tipe data **"String"** yaitu **"/"**, maka dari itu nilai variabel harus terlebih dahulu di**"konversikan"** dengan tipe data **"Integer"** ataupun **"Float"**.
* Kode :
```
a = int(a)
b = int(b)
```
Setelah dikonversikan maka pengguna dapat melaksanakan perintah selanjutnya seperti berikut
* Kode : 
```
print("Hasil penjumlahan {0} + {1} = %d".format(a,b) %(a+b))
print("Hasil pembagian {0} / {1} = %d".format(a,b) %(a/b))
```
perintah diatas merupakan perintah untuk mencetak, menghitung, dan memformat kembali output yang didapatkan.




## Terima Kasih
