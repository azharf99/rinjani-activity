from django.db import models
import datetime

# Create your models here.
class Choice(models.TextChoices):
    YES = 'Yes', "Ya"
    NO = 'No', "Tidak"

class General(models.Model):
    tipe = models.CharField(max_length=20, default="Umum")
    tanggal = models.DateField(auto_now_add=True)
    usia = models.IntegerField()
    berat_badan = models.FloatField()
    tinggi_badan = models.FloatField()
    suhu_tubuh = models.FloatField(blank=True)
    perkembangan = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return "%s %s" % ("Data", self.id)

class Food(models.Model):
    tipe = models.CharField(max_length=20, default="Makan")
    tanggal = models.DateField()
    waktu = models.TimeField()
    makanan = models.CharField(max_length=200)
    porsi_suapan = models.FloatField()
    durasi_makan = models.FloatField(blank=True)
    catatan_makan = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return "%s %s %s" % (self.tanggal, self.makanan, self.porsi_suapan)

class Breast(models.Model):
    tipe = models.CharField(max_length=20, default="Menyusui")
    tanggal = models.DateField()
    waktu = models.TimeField()
    durasi_nyusu = models.FloatField()
    catatan_nyusu = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return "%s %s" % (self.tanggal, self.durasi_nyusu)

class Sleep(models.Model):
    tipe = models.CharField(max_length=20, default="Tidur")
    tanggal = models.DateField()
    waktu = models.TimeField()
    durasi_tidur = models.FloatField()
    catatan_tidur = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return "%s %s" % (self.tanggal, self.durasi_tidur)

class Hygiene(models.Model):
    class Water(models.TextChoices):
        NORMAL = 'Normal', "Dingin"
        WARM = 'Warm', "Hangat"

    class Bath(models.TextChoices):
        MORNING = 'Morning', "Pagi"
        EVENING = 'Evening', "Sore"
        EMERGENCY = 'Emergency', "Darurat"

    tipe = models.CharField(max_length=20, default="Mandi")
    tanggal = models.DateField()
    waktu = models.TimeField()
    mandi = models.CharField(max_length=10, choices=Bath.choices)
    durasi_mandi = models.FloatField(blank=True)
    merk_sabun = models.CharField(max_length=50)
    jenis_air = models.CharField(max_length=6, choices=Water.choices, default=Water.WARM)
    gosok_kepala = models.CharField(max_length=3, choices=Choice.choices, default=Choice.YES)
    gosok_gigi = models.CharField(max_length=3, choices=Choice.choices, default=Choice.YES)
    gosok_lidah = models.CharField(max_length=3, choices=Choice.choices, default=Choice.YES)
    catatan_mandi = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return "%s %s %s" % (self.tanggal, self.mandi, self.jenis_air)

class Diaper(models.Model):
    tipe = models.CharField(max_length=20, default="Popok")
    tanggal = models.DateField()
    waktu = models.TimeField()
    bab = models.CharField(max_length=3, choices=Choice.choices, default=Choice.NO)
    tekstur_bab = models.CharField(max_length=100, blank=True)
    warna_bab = models.CharField(max_length=100, blank=True)
    catatan_diaper = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return "%s %s" % (self.tanggal, self.bab)

class Medicine(models.Model):
    tipe = models.CharField(max_length=20, default="Obat")
    tanggal = models.DateField()
    waktu = models.TimeField()
    nama_obat = models.CharField(max_length=100)
    dosis = models.CharField(max_length=100)
    manfaat = models.CharField(max_length=200)
    vaksin = models.CharField(max_length=3, choices=Choice.choices, default=Choice.YES)

    def __str__(self):
        return "%s %s %s" % (self.tanggal, self.nama_obat, self.dosis)