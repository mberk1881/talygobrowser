# Talygo Browser

**Talygo Browser**, PyQt5 ve QtWebEngine kullanarak geliştirilmiş basit, hafif bir web tarayıcısıdır. Bu tarayıcı, sekmeli gezinti, proxy desteği, konum paylaşımını engelleme ve tema değişikliği gibi özelliklerle birlikte gelir.

## Özellikler

- **Sekmeli Tarayıcı**: Birden fazla sekme açma ve yönetme.
- **Proxy Desteği**: HTTP proxy kullanarak internet bağlantısını yönlendirme.
- **Tema Değiştirme**: Aydınlık ve karanlık tema seçenekleri.
- **Konum Paylaşımını Engelleme**: Konum bilgisi paylaşımını devre dışı bırakma seçeneği.
- **Hızlı Başlangıç**: Web sayfalarını hızlıca açabilir ve sekmeleri yönetebilirsiniz.

## Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki yazılımların bilgisayarınızda yüklü olması gerekmektedir:

- Python 3.6+ (Python 3.x'in herhangi bir sürümü)
- PyQt5
- PyQtWebEngine

## Kurulum

### 1. Python'u Yükleyin

Eğer Python bilgisayarınızda yüklü değilse, [Python'un resmi sitesinden](https://www.python.org/downloads/) Python'u indirip yükleyebilirsiniz.

### 2. Gereksinimleri Yükleyin

Bu projede kullanılan tüm bağımlılıkları yüklemek için, terminal veya komut satırında şu komutları çalıştırın:

```bash
pip install PyQt5 PyQtWebEngine
```

### 3. Projeyi İndirin

GitHub üzerinden projeyi indirin ya da Git kullanarak klonlayın:

```bash
git clone https://github.com/mberk1881/talygobrowser.git
```

Proje klasörüne gidin:

```bash
cd talygobrowser
```

### 4. Çalıştırma

Projeyi çalıştırmak için şu komutu kullanın:

```bash
python main.py
```

Uygulama açılacaktır ve tarayıcı arayüzü üzerinden sekmeli gezinmeye başlayabilirsiniz.

## Kullanım

1. **URL Açma**: URL giriş alanına bir web adresi girip "Git" butonuna basarak yeni bir sekme açabilirsiniz.
2. **Yeni Sekme**: Tarayıcı penceresinin üst kısmında yer alan "Yeni Sekme" butonuna tıklayarak yeni sekmeler açabilirsiniz.
3. **Proxy Ayarı**: Eğer proxy kullanıyorsanız, proxy adresinizi **Ayarlar** menüsünden girebilirsiniz.
4. **Tema Değiştirme**: Tema ayarlarını **Ayarlar** menüsünden değiştirebilirsiniz. Aydınlık veya karanlık temalar arasından seçim yapabilirsiniz.
5. **Konum Paylaşımı**: **Ayarlar** menüsünden konum paylaşımını engellemek için seçenekleri değiştirebilirsiniz.

## Ayarlar

Proje çalıştırıldığında, ayarları şu dosya içerisinde saklar: `settings.txt`.

Bu dosya, tema (aydınlık/karanlık), proxy ayarı ve konum paylaşım izinlerini içerir. Eğer ayarları değiştirmek isterseniz, **Ayarlar** menüsünü kullanarak bu değişiklikleri kaydedebilirsiniz.

## Katkıda Bulunma

Bu projeye katkı sağlamak isterseniz:

1. Fork yapın (GitHub'da sağ üstte **Fork** butonuna tıklayın).
2. Yeni bir branch oluşturun:
   ```bash
   git checkout -b feature/yenilik
   ```
3. Değişikliklerinizi yapın ve commit edin:
   ```bash
   git commit -m "Yeni özellik eklendi"
   ```
4. Değişikliklerinizi kendi fork'unuza push edin:
   ```bash
   git push origin feature/yenilik
   ```
5. GitHub üzerinde pull request açın.

## Lisans

Bu proje **MIT Lisansı** ile lisanslanmıştır. Daha fazla bilgi için [LICENSE dosyasını](LICENSE) inceleyebilirsiniz.

## Sorular ve İletişim

Herhangi bir sorunuz olursa, lütfen [issue](https://github.com/mberk1881/talygobrowser/issues) açın ya da **mberk1881** ile iletişime geçin.
