from django.shortcuts import render
from django.http import Http404

DATA_PRODUK = [
    {
        'id': 1, 
        'nama': 'ASUS ROG Zephyrus G14', 
        'harga': 'Rp 28.500.000', 
        'gambar': 'https://images.unsplash.com/photo-1593642702821-c8da6771f0c6?q=80&w=800',
        'deskripsi': 'Laptop gaming paling powerful dan stylish untuk mobilitas tinggi.'
    },
    {
        'id': 2, 
        'nama': 'Keychron K2 Wireless', 
        'harga': 'Rp 1.650.000', 
        'gambar': 'https://images.unsplash.com/photo-1595225476474-87563907a212?q=80&w=800',
        'deskripsi': 'Mechanical keyboard minimalis dengan switch tactile yang memuaskan.'
    },
    {
        'id': 3, 
        'nama': 'LG UltraFine 4K Display', 
        'harga': 'Rp 8.200.000', 
        'gambar': 'https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?q=80&w=800',
        'deskripsi': 'Monitor dengan akurasi warna luar biasa untuk profesional kreatif.'
    },
   {
        'id': 4, 
        'nama': 'Logitech MX Master 3S', 
        'harga': 'Rp 1.450.000', 
        'gambar': 'https://images.unsplash.com/photo-1635350736475-c8cef4b21906?q=80&w=800', # Link Baru
        'deskripsi': 'Mouse produktivitas paling ergonomis dengan fitur scroll super cepat dan klik senyap.'
    },
    {
        'id': 5, 
        'nama': 'Samsung 990 Pro 1TB', 
        'harga': 'Rp 2.400.000', 
        'gambar': 'https://images.unsplash.com/photo-1591488320449-011701bb6704?q=80&w=800', # Link Baru
        'deskripsi': 'SSD NVMe Gen4 tercepat untuk performa loading game dan rendering video instan.'
    },
    {
        'id': 6, 
        'nama': 'Sony WH-1000XM5', 
        'harga': 'Rp 4.800.000', 
        'gambar': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?q=80&w=800',
        'deskripsi': 'Headphone dengan noise cancelling terbaik di kelasnya.'
    },
]

def home(request):
    return render(request, 'home.html')

def daftar_produk(request):
    return render(request, 'daftar_produk.html', {'semua_produk': DATA_PRODUK})

def detail_produk(request, id):
    produk_pilihan = next((p for p in DATA_PRODUK if p['id'] == id), None)
    if produk_pilihan:
        return render(request, 'detail_produk.html', {'produk': produk_pilihan})
    raise Http404("Produk tidak ditemukan")

def kontak(request):
    return render(request, 'kontak.html')