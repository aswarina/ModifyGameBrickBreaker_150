Pada program ini terdapat dua library yang di-import, yaitu:

Tkinter: Digunakan untuk membuat tampilan game, seperti jendela permainan, canvas, tombol, dan objek lainnya.

Random: Di-import dalam program, tetapi belum digunakan dalam proses permainan.

Penjelasan Class

Program ini terdiri dari empat class utama yang memiliki fungsi berbeda.

1. Class Ball

Class Ball digunakan untuk membuat dan mengatur objek bola dalam permainan.

**init**() digunakan untuk menentukan atribut awal bola, seperti warna, ukuran, kecepatan, dan posisi bola.

draw() digunakan untuk menggerakkan bola serta mengatur pantulannya ketika mengenai dinding atau paddle.

speed_x dan speed_y digunakan untuk menentukan kecepatan dan arah gerak bola.

hit_bottom digunakan untuk mengetahui apakah bola sudah melewati batas bawah permainan.

2. Class Paddle

Class Paddle digunakan untuk membuat papan pemantul bola yang dapat digerakkan menggunakan keyboard.

**init**() digunakan untuk membuat paddle dan mengatur ukuran serta posisi awalnya.

draw() digunakan untuk menggerakkan paddle sesuai arah yang diberikan.

turn_left() digunakan untuk menggerakkan paddle ke kiri.

turn_right() digunakan untuk menggerakkan paddle ke kanan.

stop() digunakan untuk menghentikan pergerakan paddle ketika tombol dilepas.

3. Class Brick

Class Brick digunakan untuk membuat balok yang akan dihancurkan oleh bola.

Pada class ini, balok dibuat menggunakan fungsi create_polygon() agar menghasilkan bentuk hati. Setiap balok memiliki warna, simbol, dan nilai skor yang berbeda.

Method **init**() digunakan untuk mengatur posisi, bentuk, warna, dan skor dari setiap balok.

4. Class BrickBreakerGame

Class BrickBreakerGame merupakan class utama yang digunakan untuk mengatur seluruh jalannya permainan.

Beberapa method yang terdapat pada class ini yaitu:

**init**() digunakan untuk membuat jendela game, canvas, tombol Start, serta tampilan skor dan nyawa.

setup_level() digunakan untuk membuat paddle, bola, dan menyusun 24 balok dalam 4 baris.

start_game() digunakan untuk memulai permainan serta mengatur ulang skor dan nyawa.

game_loop() digunakan untuk menjalankan pergerakan objek, mengecek tabrakan bola dengan balok, memperbarui skor, serta menentukan kondisi menang atau kalah.

Pada method game_loop(), digunakan fungsi after() dari Tkinter agar proses permainan dapat berjalan secara berulang.
