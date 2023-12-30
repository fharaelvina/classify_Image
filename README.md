# Aplikasi Pengenalan Batu, Kertas, Gunting dengan Transfer Learning
## Deskripsi Proyek
Proyek ini menggunakan transfer learning untuk membuat model pengenalan gambar batu, kertas, dan gunting. Dataset awalnya diunduh dalam format zip (rps.zip), dan kemudian dipecah menjadi set pelatihan, validasi, dan uji. Selanjutnya, dilakukan augmentasi data menggunakan ImageDataGenerator untuk meningkatkan kinerja model.

## Struktur Direktori
rps/: Direktori utama yang berisi dataset awal.
train/: Direktori set pelatihan.
val/: Direktori set validasi.
test/: Direktori set uji.
## Visualisasi Data
Satu gambar acak dari setiap kelas pada set pelatihan ditampilkan untuk memberikan gambaran tentang isi dataset.




## Augmentasi Data
Gambar-gambar pada set pelatihan diperkaya melalui augmentasi data menggunakan ImageDataGenerator. Contoh augmentasi termasuk rotasi, pergeseran, dan pembalikan horizontal.

![](https://github.com/fharaelvina/classify_Image/blob/main/augmented.png)

## Transfer Learning dengan MobileNetV2
Model menggunakan arsitektur MobileNetV2 sebagai base model untuk transfer learning. Lapisan-lapisan MobileNetV2 yang telah dilatih tidak di-train ulang, dan dilanjutkan dengan lapisan GlobalAveragePooling2D dan lapisan Dense dengan fungsi aktivasi softmax.

## Statistik Pelatihan
Model dilatih dengan optimizer Adam dan fungsi kerugian categorical crossentropy selama 5 epoch.

### Accuracy
![](https://github.com/fharaelvina/classify_Image/blob/main/accuracy.png)

### Loss
![](https://github.com/fharaelvina/classify_Image/blob/main/loss.png)

Akurasi Pelatihan: ~98%
Akurasi Validasi: ~95%
## Simpan Model
Model yang telah dilatih disimpan sebagai model.h5 untuk penggunaan selanjutnya.

## Instruksi Penggunaan
Unduh dataset awal dalam format zip (rps.zip) dan ekstrak ke direktori proyek.
Jalankan skrip Python (train_model.py) untuk melatih model dan simpan sebagai model.h5.
Gunakan model untuk melakukan prediksi pada gambar batu, kertas, dan gunting.

## Tampilan Awal
![](https://github.com/fharaelvina/classify_Image/blob/main/tampilan%20awal.png)

## Hasil
![](https://github.com/fharaelvina/classify_Image/blob/main/hasil.png)
