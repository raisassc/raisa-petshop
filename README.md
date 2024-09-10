Link PWS : http://raisa-sakila-raisapetshop.pbp.cs.ui.ac.id/
# 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step

# 1. Membuat Direktori Proyek Lokal dan Inisialisasi Git
Langkah pertama dalam memulai proyek Django baru adalah membuat sebuah direktori lokal yang akan menjadi tempat kerja utama proyek ini. Karena proyek ini akan dipush ke Git untuk kontrol versi dan kolaborasi, saya memulai dengan menginisialisasi Git pada direktori proyek menggunakan perintah `git init`. Inisialisasi ini penting untuk melacak perubahan kode selama developeran.

# 2. membuat virtual environment
Membuat virtual environment sebelum memulai proyek Django merupakan langkah penting. Langkah ini memastikan proyek dapat berjalan di lingkungan yang terpisah. Dengan adanya virtual environment, proyek yang melibatkan kolaborasi antar developer dapat terhindar dari potensi konflik yang disebabkan oleh perbedaan konfigurasi perangkat. Pengaktifan dilakukan dengan perintah `env\Scripts\activate`


# 3. Membuat dan Mengelola `requirements.txt`
Setelah Git diinisialisasi dan aktivasi environment, saya membuat file `requirements.txt` di dalam direktori proyek. File ini berisi daftar dependencies (pustaka perangkat lunak) yang diperlukan untuk menjalankan proyek. Contohnya, Django dan pustaka tambahan seperti `gunicorn`. Dengan file ini, dependencies dapat diinstal otomatis menggunakan perintah `pip install -r requirements.txt`.

# 4. Membuat Struktur Proyek Django
Setelah dependencies terpasang, saya membuat struktur dasar proyek Django dengan menjalankan perintah:
django-admin startproject raisa_petshop .
Perintah ini membuat proyek bernama `raisa_petshop` dalam direktori yang sedang saya gunakan. Dalam folder ini terdapat beberapa file penting seperti `settings.py`, `urls.py`, `asgi.py`, dan `wsgi.py`, yang berfungsi untuk mengonfigurasi proyek baik di lingkungan lokal maupun hosting.

# 5. Membuat Aplikasi Pertama: `main`
Langkah berikutnya adalah membuat aplikasi pertama dalam proyek ini dengan nama `main`. Saya menggunakan perintah:
python manage.py startapp main
Perintah ini membuat folder `main` yang berisi file-file penting seperti `models.py`, `views.py`, dan `admin.py`. Untuk mengenalkan aplikasi ini ke proyek utama, saya menambahkan `main` ke dalam daftar `INSTALLED_APPS` di file `settings.py`.

# 6. Mengembangkan Komponen Aplikasi
Di dalam folder `main`, saya mulai mengembangkan beberapa komponen inti:
- `models.py`: Digunakan untuk mendefinisikan struktur data dan tabel yang akan disimpan dalam database.
- `views.py`: Mengelola logika aplikasi dan bagaimana data akan disajikan ke pengguna.
- `urls.py`: Digunakan untuk mengatur routing URL yang menghubungkan permintaan pengguna dengan fungsi-fungsi di `views.py`.

# 7. Penerapan Konsep MVT (Model, View, Template)
Untuk mengikuti arsitektur MVT, saya menambahkan folder `templates` di dalam aplikasi `main` untuk menyimpan file HTML yang akan merender halaman web. Dalam konsep MVT:
- Model untuk mengelola data dan interaksi dengan database.
- View memproses permintaan dan mengambil data dari model.
- Template menampilkan data kepada pengguna dalam bentuk halaman HTML.

Sebagai contoh, dalam `models.py`, saya mendefinisikan model untuk produk di pet shop. Sementara itu, di `views.py`, saya membuat fungsi `show_main` yang mengelola data dari model dan mengirimkan data tersebut ke template HTML.

# 8. Menambahkan URL Routing
Setelah membuat fungsi di `views.py`, saya membuat file `urls.py` di dalam folder `main` untuk menentukan pola URL yang akan digunakan untuk memanggil fungsi tersebut. Dengan cara ini, pengguna dapat mengakses halaman utama aplikasi dengan URL yang sudah ditentukan.

# 9. Deployment ke Pacil Web Services (PWS)
Setelah proses developeran selesai, langkah terakhir adalah melakukan deployment ke Pacil Web Services (PWS). Berikut adalah langkah-langkahnya:
1. Login ke PWS: Saya membuka situs PWS dan login dengan username serta password.
2. Membuat Proyek Baru: Saya memilih opsi 'Create New Project' untuk menambahkan proyek baru ke PWS. Pada tahap ini, saya menerima kredensial proyek.
3. Konfigurasi `ALLOWED_HOSTS`: Saya menambahkan URL deployment PWS ke daftar `ALLOWED_HOSTS` di file `settings.py`.
4. Push ke GitHub: Saya melakukan `git add`, `commit`, dan `push` ke GitHub.
5. Push ke PWS: Saya menambahkan PWS sebagai remote repository dan melakukan push dengan menjadikan direktori utama proyek sebagai branch.
6. Build Proyek: Setelah proses build berhasil, aplikasi saya bisa diakses publik melalui URL berikut: [http://raisa-sakila-raisapetshop.pbp.cs.ui.ac.id/](http://raisa-sakila-raisapetshop.pbp.cs.ui.ac.id/).

# 10. Membuat README.md
setelah melakukan deployment, saya membuat file README.md di direkori utama. File ini bertujuan untuk menuliskan jawaban jawaban saya mengenai pertanyaan pertanyaan yang terdapat pada tugas 2. setelah itu saya melakukan commit dan push ke akun github 

# 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html

![Bagan Alur](images/baganDjango.jpg)
# Alur Request

1. Client mengirimkan request HTTP ke server. Kemudian, urls.py mencocokkan URL request dengan pola yang ada dan menentukan fungsi view yang akan menangani request. Selanjutnya views.py memproses request. views.py merupakan fungsi yang berinteraksi dengan models.py untuk mengambil atau memanipulasi data. Setelah itu, models.py melakukan query ke database dan mengembalikan data sesuai dengan atribut yang didefinisikan di models.py ke views.py. Setelah menerima data, views.py memilih HTML file (template) untuk merender data. Terakhir, HTML file dirender dan dikembalikan sebagai response ke Client.

1. urls.py:
   urls.py Mengatur pola URL (URL patterns) dan menghubungkan URL yang diminta oleh client dengan fungsi view yang sesuai. Ketika client mengirimkan request ke server, Django akan mencocokkan URL request dengan pola URL yang didefinisikan dalam `urls.py`. Jika ditemukan kecocokan, Django akan memanggil fungsi view yang terkait.

2. views.py:
   views.py menangani logika aplikasi dan memproses data yang diterima dari request. Fungsi di dalam `views.py` akan menghasilkan response berdasarkan data yang diproses. Fungsi view akan berinteraksi dengan model untuk mengambil atau memanipulasi data dan kemudian memilih template HTML untuk dirender.

3. models.py:
   models.py mendefinisikan struktur data dan interaksi dengan database. Model merupakan representasi dari tabel dalam database. Ketika fungsi view memerlukan data dari database, model digunakan untuk membuat query dan mengambil data yang diperlukan. lalu mengirimkannya kembali ke views.py

4. HTML File:
   HTML file merupakan template yang digunakan untuk menyajikan data ke client. Template HTML berisi markup yang akan dirender sebagai halaman web. Fungsi view memilih template HTML untuk digunakan, kemudian mengisi template tersebut dengan data yang diambil dari model, dan mengembalikannya sebagai response HTML kepada client.

sumber : ppt PBP

# 3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
1. Sistem Kontrol Versi 
sumber : (https://dcloud.co.id/blog/apa-itu-git.html)
Git adalah sistem kontrol versi terdistribusi yang sangat penting dalam pengembangan perangkat lunak modern. Setiap perubahan yang dilakukan pada kode dicatat secara detail, termasuk informasi tentang siapa yang melakukan perubahan, kapan perubahan itu terjadi, dan alasan perubahan tersebut. Dengan fitur ini, Git memiliki catatan lengkap dari seluruh perkembangan proyek sehingga menjadi alat yang efektif dalam melacak dan mengelola kode.

2. Kemudahan dalam Melacak Perubahan dan Kembali ke Versi Sebelumnya
Git memudahkan developer untuk melacak seluruh sejarah proyek, sehingga jika ada masalah atau bug yang muncul, developer dapat dengan cepat meninjau perubahan sebelumnya dan kembali ke versi yang lebih stabil. Hal Ini sangat berguna dalam skenario pengembangan perangkat lunak yang kompleks, di mana perubahan kecil bisa menyebabkan bug kritis. Dengan kemampuan Git untuk mengelola versi sebelumnya, developer bisa dengan cepat memperbaiki masalah tanpa harus kehilangan versi terbaru yang telah dicapai.

3. Branching: Fitur untuk pengembangan Paralel
sumber : (https://dcloud.co.id/blog/apa-itu-git.html)
Salah satu fitur paling kuat dari Git adalah branching. Dengan branching, developer dapat membuat cabang terpisah untuk mengerjakan fitur baru atau memperbaiki bug tanpa mengganggu alur kerja utama. Setiap developer dapat membuat cabang sendiri dan bekerja secara independen. Hal ini memberikan kemudahan bagi tim untuk bekerja secara paralel pada berbagai fitur atau tugas yang berbeda tanpa harus khawatir akan mengganggu pekerjaan orang lain. Branching juga memfasilitasi eksperimen karena perubahan dapat diisolasi dan diuji secara terpisah sebelum digabungkan kembali ke proyek utama.

4. Merging: Menggabungkan Perubahan Kode
Setelah developeran atau perbaikan pada cabang selesai, perubahan tersebut dapat digabungkan kembali ke cabang utama melalui proses yang disebut merging. Git menyediakan mekanisme untuk mengelola konflik yang mungkin muncul selama penggabungan, sehingga developer dapat mengintegrasikan pekerjaan mereka dengan mudah dan tanpa kehilangan perubahan penting. Dengan fitur ini, Git memfasilitasi integrasi yang lancar antaranggota tim, bahkan jika mereka bekerja secara independen pada bagian proyek yang berbeda.

5. Meningkatkan Kolaborasi Tim dalam Pengembangan Perangkat Lunak
sumber : (https://www.jagoanhosting.com/blog/git-adalah/)
Git tidak hanya mempermudah pengelolaan kode secara individu tetapi juga sangat mendukung kolaborasi dalam tim. Setiap anggota tim dapat bekerja pada cabang terpisah dan melakukan perubahan tanpa risiko merusak kode orang lain. Dengan kemampuan Git untuk menggabungkan perubahan dari beberapa developer secara efisien, tim dapat bekerja lebih produktif dan paralel. Hal ini membuat Git menjadi alat yang ideal untuk proyek besar dengan banyak developer yang bekerja pada bagian kode yang berbeda.

6. Git sebagai Perangkat Lunak Open-Source dengan Dukungan Komunitas Global
sumber : (https://www.jagoanhosting.com/blog/git-adalah/)
Git adalah perangkat lunak open-source, yang berarti siapa pun dapat menggunakannya secara gratis dan berkontribusi pada pengembangannya. Sebagai proyek open-source, Git didukung oleh komunitas global yang besar dan aktif. Komunitas ini menyediakan berbagai sumber daya seperti dokumentasi, tutorial, dan forum diskusi untuk membantu pengguna baru belajar dan memahami Git. Dukungan komunitas yang luas ini memudahkan developer untuk mendapatkan bantuan kapan pun mereka menemui masalah atau butuh panduan dalam mengimplementasikan fitur Git yang lebih canggih.


# 4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
1. Django Menggunakan Bahasa Pemrograman Python
Django dibangun dengan Python, yang merupakan salah satu bahasa pemrograman paling populer di dunia. Python dikenal karena sintaksnya yang sederhana dan mirip dengan bahasa sehari-hari. Hal ini membuat bahasa ini mudah dipelajari oleh pemula yang baru terjun ke dunia pemrograman. Django mewarisi karakteristik Python ini, sehingga developer dapat menulis kode dengan cepat tanpa terlalu banyak aturan sintaks yang rumit. Hal ini membantu pemula memusatkan perhatian pada konsep-konsep inti pengembangan perangkat lunak, seperti pola arsitektur MVT (Model-View-Template) yang digunakan oleh Django. Selain itu, Python memiliki banyak pustaka yang dapat dengan mudah diintegrasikan ke Django. Misalnya, pustaka untuk manipulasi data, pengujian, atau keamanan. Hal ini mempercepat proses pembelajaran dan pengembangan.

2. Django Memiliki Komunitas yang Luas
Salah satu alasan utama Django sering dipilih untuk pembelajaran pengembangan perangkat lunak adalah karena dukungan komunitas yang luas. Django memiliki dokumentasi resmi yang sangat baik, yang menyediakan panduan langkah demi langkah mulai dari instalasi hingga fitur lanjutan. Hal ini sangat membantu pemula memahami konsep pengembangan web dengan mudah. Ditambah lagi, ada banyak forum, blog, serta komunitas online (seperti StackOverflow) yang didedikasikan untuk Django. Jika pemula mengalami kesulitan, mereka dapat dengan cepat menemukan jawaban atau meminta bantuan dari komunitas Banyak tutorial dan proyek Django open-source yang tersedia untuk dipelajari. Pemula dapat mempelajari proyek nyata, memahami alur kerja profesional, dan mencoba mengimplementasikan fitur serupa pada proyek mereka sendiri.

3. Proses Development Django yang Sederhana
Django dirancang untuk mempermudah pengembangan aplikasi web, terutama bagi pemula. Django mengikuti prinsip “batteries included” yang berarti framework ini hadir dengan berbagai fitur built-in yang siap digunakan tanpa memerlukan konfigurasi manual yang rumit. Misalnya, Django sudah menyediakan sistem otentikasi pengguna, admin panel, manajemen database, dan lain-lain. Django membuat pengembangan aplikasi web berjalan cepat berkat alat seperti ORM (Object-Relational Mapping) untuk manajemen database, routing otomatis untuk URL, serta template engine yang mudah digunakan. Pemula dapat dengan cepat membuat aplikasi web fungsional tanpa harus menulis banyak kode dari nol. Django cocok untuk proyek kecil maupun besar. Meskipun pemula mungkin memulai dengan proyek sederhana, Django bisa diandalkan saat proyek tersebut tumbuh menjadi aplikasi besar. Fitur seperti caching, middlewares, dan kemampuan untuk mendukung berbagai jenis database membuatnya fleksibel untuk proyek dengan berbagai skala.

# 5. Mengapa model pada Django disebut sebagai ORM?
sumber : (https://rumahcoding.co.id/pengantar-django-orm-memahami-dan-menggunakan-model-dalam-django/#:~:text=Apa%20itu%20Django%20ORM%3F%20Django%20ORM%20%28Object-Relational%20Mapping%29,objek%20Python%2C%20tanpa%20perlu%20menulis%20kueri%20SQL%20langsung.)

Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena menyediakan cara untuk memetakan objek Python ke dalam struktur basis data relasional. Dengan menggunakan Django ORM, developer dapat mendefinisikan model sebagai kelas Python, di mana atribut kelas mewakili kolom dalam tabel database dan setiap instance model merepresentasikan baris dalam tabel tersebut. Django ORM menyederhanakan interaksi dengan basis data dengan menghilangkan kebutuhan untuk menulis query SQL secara langsung. Developer dapat melakukan operasi database menggunakan metode objek Python, dan ORM secara otomatis mengonversi operasi tersebut menjadi query SQL yang sesuai.
