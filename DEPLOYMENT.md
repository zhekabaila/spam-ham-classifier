# Deployment Guide: Spam/Ham Classifier

Project ini telah di-dockerize agar mudah di-deploy ke VPS. Berikut adalah instruksi untuk menjalankan aplikasi menggunakan Docker dan mengonfigurasi Nginx sebagai reverse proxy.

## 1. Persiapan VPS
Pastikan VPS Anda sudah terinstall:
- Docker
- Docker Compose
- Nginx

## 2. Struktur File Docker
Saya telah membuat file berikut di direktori root project:
- `Dockerfile`: Definisi image aplikasi.
- `.dockerignore`: Daftar file yang tidak perlu dimasukkan ke dalam image (seperti `venv`).
- `docker-compose.yml`: Untuk menjalankan kontainer dengan konfigurasi port dan volume.

## 3. Cara Menjalankan dengan Docker
Jalankan perintah berikut di direktori project:

```bash
# Build dan jalankan kontainer di background
docker compose up -d --build
```

Aplikasi akan berjalan di port `8501`.

## 4. Konfigurasi Nginx (Reverse Proxy)
Buat file konfigurasi Nginx baru (misal: `/etc/nginx/sites-available/spam-classifier`):

```nginx
server {
    listen 80;
    server_name spam-ham-classifier.coreapps.web.id;

    location / {
        proxy_pass http://localhost:8501;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        # Streamlit memerlukan konfigurasi WebSocket
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_read_timeout 86400;
    }
}
```

Setelah itu, aktifkan konfigurasi dan restart Nginx:
```bash
sudo ln -s /etc/nginx/sites-available/spam-classifier /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

## 5. SSL (HTTPS) dengan Certbot
Karena Anda ingin menggunakan HTTPS, gunakan Certbot untuk mendapatkan sertifikat gratis:
```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d spam-ham-classifier.coreapps.web.id
```

## 6. Catatan Penting
- **Models & Data**: Saya telah menggunakan `volumes` di `docker-compose.yml` agar file model (`.pkl`) dan data tetap sinkron antara VPS dan kontainer.
- **Port**: Pastikan port `8501` tidak diblokir oleh firewall VPS (ufw/iptables) jika ingin diakses langsung, namun karena kita menggunakan Nginx, port tersebut cukup terbuka untuk `localhost` saja.
