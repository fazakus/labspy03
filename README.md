# labspy03

**Nama    : Faza Ardan Kusuma<br>
NIM     : 312010001<br>
Kelas   : TI.20.B1**

## Pertemuan 7 - Tugas Praktikum 3

Pada tugas 3 di pertemuan 7 ini, diberikan 3 program, yaitu :

| No | Description | Link |
|----|----|----|
| 1 | Latihan 1 | [Clik Here](#pertemuan-7---tugas-praktikum-3) |
| 2 | Latihan 2 | [Clik Here]() |
| 3 | Program 1 | [Clik Here]() |

## Latihan 1
Berikut adalah soal latihan 1

![latihan1](Pic/Latihan%201.png)<br>

Pada latihan 1 ini, saya disuruh membuat bilangan acak dengan nilai kurang dari 0.5, dengan menggunakan kombinasi while dan for dan menggunakan fungsi random.

**For dan While**<br>
* For disebut <i>counted loop</i> (perulangan yang terhitung)
* While disebut <i>uncounted loop</i> (perulangan yang tak terhitung)<br>

Perbedaannya adalah perulangan for biasanya digunakan untuk mengulangi kode yang sudah diketahui banyak perulangannya. Sementara while untuk perulangan yang memiliki syarat dan tidak tentu berapa banyak perulangannya.

**Random**<br>
Random berfungsi untuk mengacak sebuah bilangan


Untuk latihan 1 saya menggunakan syntax sebagai berikut :
![syntaxlat1](Pic/syntaxlatihan1%20.png)<br>

Penjelasan :<br>

* Variabel i berfungsi untuk menampung indeks<br>
* Fungsi dari ***range(n)***, berfungsi untuk membuat list dengan range sesuai dengan yang angka yang di inputkan ***(n)***<br>
* ***while 1:*** berfungsi untuk, menyatakan  kondisi 1 <br> 
* Kondisi 1 dengan syntax :
```python
 n = random.random()
        if n < 0.5 :
            break
```
* Maka dengan kondisi tersebut bahwa 1 = bernilai random dibawah 0.5 dengan fungsi ***random()*** dan ***if n < 0.5***
* ***Break*** untuk mencegah terjadinya looping tak terhingga

Hasil dari output source code latihan 1 :<br>
> Jika n = 5, maka outputnya akan menjadi 5:<br>
>![outputlat1-1](Pic/outputlatihan1-1.png)<br>
> Jika n = 7 , maka outputnya akan menjadi 7 baris :<br>
>![outputlat1-2](Pic/outputlatihan1-2.png)<br>