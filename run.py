import sys
import os
from PyQt5.QtCore import QUrl, Qt, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QLineEdit, QMenu, QAction, QDialog, QFormLayout, QLabel, QComboBox, QCheckBox, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage, QWebEngineSettings
from PyQt5.QtNetwork import QNetworkProxy, QNetworkAccessManager, QNetworkRequest, QNetworkReply

# Tema tercihini saklamak için bir dosya adı
SETTINGS_FILE = "settings.txt"


class WebView(QWebEngineView):
    def __init__(self, url, parent=None, enable_geolocation=True, proxy=None):
        super(WebView, self).__init__(parent)
        self.setUrl(QUrl(url))  # URL doğru şekilde yüklenmeli

        # Konum paylaşımını engelleme (Geolocation izni)
        self.page().settings().setAttribute(QWebEngineSettings.LocalStorageEnabled, False)  # Yerel depolama devre dışı
        if not enable_geolocation:
            self.page().setFeaturePermission(QUrl(url), QWebEnginePage.Geolocation, QWebEnginePage.PermissionPolicy.Allow)  # Geolocation'ı engelle

        # Proxy ayarları
        self.set_proxy(proxy)

    def set_proxy(self, proxy: str):
        """Proxy ayarlarını yap."""
        if proxy:
            network_proxy = QNetworkProxy(QNetworkProxy.HttpProxy, "127.0.0.1", 8080)  # Burada kendi proxy adresini kullanabilirsiniz
            QNetworkProxy.setApplicationProxy(network_proxy)
        else:
            QNetworkProxy.setApplicationProxy(QNetworkProxy())  # Varsayılan proxy ayarlarını sıfırla


class BrowserTab(QWidget):
    def __init__(self, url, parent=None, enable_geolocation=True, proxy=None):
        super(BrowserTab, self).__init__(parent)
        self.layout = QVBoxLayout()
        self.browser = WebView(url, proxy=proxy)
        self.layout.addWidget(self.browser)
        self.setLayout(self.layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TalyGo Browser")
        self.setGeometry(100, 100, 1000, 800)

        # Ayarları yükle
        self.light_theme, self.enable_geolocation, self.proxy = self.load_settings()

        # Ana Layout
        self.tabs = QTabWidget(self)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)

        # URL girişi için input kutusu ve butonlar
        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText("Bir URL girin (örn: https://www.talygobrowser.com)")
        self.url_button = QPushButton("  Git  ", self)
        self.url_button.clicked.connect(self.open_url)

        # Yeni sekme butonu
        self.new_tab_button = QPushButton("  Yeni Sekme  ", self)
        self.new_tab_button.clicked.connect(self.add_new_tab)

        # Üç nokta menü butonu
        self.menu_button = QPushButton("  ⋮  ", self)
        self.menu_button.setFixedSize(30, 30)
        self.menu_button.clicked.connect(self.show_menu)

        # Butonlar ve layout yerleşimi
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.url_input)
        button_layout.addWidget(self.url_button)
        button_layout.addWidget(self.new_tab_button)
        button_layout.addWidget(self.menu_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.tabs)

        central_widget = QWidget(self)
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # İlk sekmeyi ekle
        self.add_new_tab()

        # Tema başlangıçta uygulanır
        self.apply_theme()

        # Uygulama her zaman tam ekran penceresi modunda başlasın
        self.showMaximized()  # Tam ekran penceresi (başlık çubuğu ve menü ile)

        # Proxy'yi kontrol et
        self.check_proxy()

    def add_new_tab(self):
        # İlk sekme olarak bir boş sayfa veya istenen URL eklenebilir
        default_url = "https://www.duckduckgo.com"
        new_tab = BrowserTab(default_url, enable_geolocation=self.enable_geolocation, proxy=self.proxy)
        self.tabs.addTab(new_tab, "Yeni Sekme")

    def open_url(self):
        url = self.url_input.text()  # Kullanıcının girdiği URL
        if url:  # Eğer URL girilmişse
            if not url.startswith("http://") and not url.startswith("https://"):
                url = "https://" + url  # Eğer URL başında "http://" ya da "https://" yoksa, ekle
            new_tab = BrowserTab(url, enable_geolocation=self.enable_geolocation, proxy=self.proxy)
            self.tabs.addTab(new_tab, f"URL: {url}")
            self.tabs.setCurrentWidget(new_tab)  # Yeni sekmeyi aktif yap
        else:
            print("URL boş!")

    def close_tab(self, index):
        self.tabs.removeTab(index)

    def show_menu(self):
        menu = QMenu(self)

        # Hakkında menüsü
        about_action = QAction("Hakkında", self)
        about_action.triggered.connect(self.show_about)
        menu.addAction(about_action)

        # Ayarlar menüsü
        settings_action = QAction("Ayarlar", self)
        settings_action.triggered.connect(self.show_settings)
        menu.addAction(settings_action)

        menu.exec_(self.menu_button.mapToGlobal(self.menu_button.pos()))

    def show_about(self):
        about_dialog = QDialog(self)
        about_dialog.setWindowTitle("Hakkında")

        about_layout = QVBoxLayout()

        about_layout.addWidget(QLabel("Yapımcı: Mustafa Berk Aslan"))
        about_layout.addWidget(QLabel("GitHub: @mberk1881"))
        about_layout.addWidget(QLabel("Discord: @mberk1881"))
        about_layout.addWidget(QLabel("Instagram: @mustafaberkaslan"))
        about_layout.addWidget(QLabel("Twitter: @b4rkwhr"))

        about_dialog.setLayout(about_layout)
        about_dialog.exec_()

    def show_settings(self):
        settings_dialog = QDialog(self)
        settings_dialog.setWindowTitle("Ayarlar")

        settings_layout = QFormLayout()

        # Tema seçimi (Karanlık/Aydınlık)
        theme_combo = QComboBox(self)
        theme_combo.addItem("Aydınlık")
        theme_combo.addItem("Karanlık")
        theme_combo.setCurrentIndex(0 if self.light_theme else 1)
        theme_combo.currentIndexChanged.connect(self.change_theme)

        # Konum paylaşımı (Engelleme)
        geolocation_checkbox = QCheckBox("Konum Paylaşımını Engelle", self)
        geolocation_checkbox.setChecked(not self.enable_geolocation)
        geolocation_checkbox.stateChanged.connect(self.toggle_geolocation)

        # Proxy ayarı
        proxy_input = QLineEdit(self)
        proxy_input.setPlaceholderText("Proxy (örn: http://127.0.0.1:8080)")
        proxy_input.setText(self.proxy if self.proxy else "")
        settings_layout.addRow("Proxy Ayarı", proxy_input)

        settings_layout.addRow("Tema Seçimi", theme_combo)
        settings_layout.addRow(proxy_input)

        save_button = QPushButton("Kaydet", self)
        save_button.clicked.connect(lambda: self.save_settings(theme_combo.currentIndex(), geolocation_checkbox.isChecked(), proxy_input.text(), settings_dialog))
        settings_layout.addWidget(save_button)

        settings_dialog.setLayout(settings_layout)
        settings_dialog.exec_()

    def change_theme(self, index):
        if index == 0:  # Aydınlık
            self.light_theme = True
        else:  # Karanlık
            self.light_theme = False

        self.apply_theme()

    def toggle_geolocation(self, state):
        # Konum paylaşımını engelle
        self.enable_geolocation = state != Qt.Checked

    def apply_theme(self):
        if self.light_theme:
            self.setStyleSheet("""
                QWidget {
                    background-color: #f0f0f0;
                    color: black;
                }
                QLineEdit, QPushButton {
                    background-color: #fff;
                    border: 1px solid #ccc;
                    color: black;
                }
                QTabWidget::pane {
                    background: white;
                }
                QTabWidget::tab-bar {
                    alignment: center;
                }
                QTabBar::tab {
                    background-color: #f0f0f0;
                    padding: 10px;
                }
            """)
        else:  # Karanlık tema
            self.setStyleSheet("""
                QWidget {
                    background-color: #121212;
                    color: white;
                }
                QLineEdit, QPushButton {
                    background-color: #333;
                    border: 1px solid #555;
                    color: white;
                }
                QTabWidget::pane {
                    background: #121212;
                }
                QTabWidget::tab-bar {
                    alignment: center;
                }
                QTabBar::tab {
                    background-color: #333;
                    padding: 10px;
                }
            """)

    def load_settings(self):
        if os.path.exists(SETTINGS_FILE):
            with open(SETTINGS_FILE, 'r') as f:
                settings = f.readlines()
                if len(settings) >= 3:
                    theme = settings[0].strip() == "light"
                    enable_geolocation = settings[1].strip() == "True"
                    proxy = settings[2].strip()
                    return theme, enable_geolocation, proxy
        # Varsayılan ayarlar
        return True, True, ""  # Varsayılan olarak aydınlık tema, konum paylaşımı açık ve proxy boş

    def save_settings(self, theme_index, enable_geolocation, proxy, settings_dialog):
        theme = "light" if theme_index == 0 else "dark"
        with open(SETTINGS_FILE, 'w') as f:
            f.write(f"{theme}\n")
            f.write(f"{'True' if enable_geolocation else 'False'}\n")
            f.write(f"{proxy}\n")

        # Değişiklikleri kaydettik, kullanıcıya bildirelim
        QMessageBox.information(self, "Başarılı", "Değişiklikler kaydedildi! İyi kullanımlar :) - b4rkwhr")
        settings_dialog.accept()  # Ayarlar penceresini kapat

    def check_proxy(self):
        if self.proxy:  # Eğer proxy ayarı varsa
            # Basit bir HTTP istek kontrolü yapalım
            manager = QNetworkAccessManager()
            url = QUrl("https://www.google.com")
            request = QNetworkRequest(url)

            reply = manager.get(request)
            reply.finished.connect(lambda: self.proxy_check_reply(reply))
        
    def proxy_check_reply(self, reply):
        if reply.error() != QNetworkReply.NoError:
            # Proxy hatalı, kullanıcıya bilgi ver ve proxy ayarlarını temizle
            QMessageBox.warning(self, "Proxy Hatası", "Proxy geçersiz veya çalışmıyor. Proxy ayarı sıfırlanacak.")
            self.proxy = ""  # Proxy'yi sıfırla
            self.save_settings(0, self.enable_geolocation, "", None)  # Ayarları kaydet ve proxy'yi sil
            QTimer.singleShot(0, lambda: self.restart_application())  # Uygulamayı yeniden başlat

    def restart_application(self):
        # Uygulamayı yeniden başlat
        QApplication.quit()
        os.execv(sys.executable, ['python'] + sys.argv)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
