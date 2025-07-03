<<<<<<< HEAD
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import hashlib
import base64
import qrcode
from io import BytesIO
from kivy.core.image import Image as CoreImage

PRIVATE_SALT = "Gs1905*UzayKolonisi🚀"

def generate_password(master_key, service, length=16):
    combo = f"{master_key}|{service}|{PRIVATE_SALT}".encode()
    hash_digest = hashlib.sha256(combo).digest()
    return base64.b64encode(hash_digest).decode("utf-8")[:length]

class ZeusLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10, **kwargs)

        self.master_input = TextInput(hint_text="Anahtar (Master Key)", multiline=False, password=True)
        self.add_widget(self.master_input)

        self.service_input = TextInput(hint_text="Servis Adı (örnek: gmail)", multiline=False)
        self.add_widget(self.service_input)

        self.result_label = Label(text="", halign='center')
        self.add_widget(self.result_label)

        self.generate_btn = Button(text="🔐 Şifre Üret")
        self.generate_btn.bind(on_press=self.generate_password)
        self.add_widget(self.generate_btn)

        self.qr_btn = Button(text="📷 QR Kod Göster")
        self.qr_btn.bind(on_press=self.show_qr_code)
        self.add_widget(self.qr_btn)

    def generate_password(self, instance):
        master = self.master_input.text
        service = self.service_input.text
        if not master or not service:
            self.result_label.text = "⚠️ Alanlar boş olamaz"
            return
        password = generate_password(master, service)
        self.result_label.text = f"Şifre: {password}"

    def show_qr_code(self, instance):
        password_text = self.result_label.text.replace("Şifre: ", "")
        if not password_text:
            popup = Popup(title="Uyarı", content=Label(text="Önce şifre üret."), size_hint=(.6, .4))
            popup.open()
            return
        qr = qrcode.make(password_text)
        buffer = BytesIO()
        qr.save(buffer, format="PNG")
        buffer.seek(0)
        img = CoreImage(buffer, ext="png")

        popup = Popup(title="📷 QR Kod", size_hint=(.8, .8))
        img_label = Label()
        img_label.texture = img.texture
        popup.content = img_label
        popup.open()

class ZeusPassApp(App):
    def build(self):
        return ZeusLayout()

if __name__ == "__main__":
    ZeusPassApp().run()
=======
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import hashlib
import base64
import qrcode
from io import BytesIO
from kivy.core.image import Image as CoreImage

PRIVATE_SALT = "Gs1905*UzayKolonisi🚀"

def generate_password(master_key, service, length=16):
    combo = f"{master_key}|{service}|{PRIVATE_SALT}".encode()
    hash_digest = hashlib.sha256(combo).digest()
    return base64.b64encode(hash_digest).decode("utf-8")[:length]

class ZeusLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10, **kwargs)

        self.master_input = TextInput(hint_text="Anahtar (Master Key)", multiline=False, password=True)
        self.add_widget(self.master_input)

        self.service_input = TextInput(hint_text="Servis Adı (örnek: gmail)", multiline=False)
        self.add_widget(self.service_input)

        self.result_label = Label(text="", halign='center')
        self.add_widget(self.result_label)

        self.generate_btn = Button(text="🔐 Şifre Üret")
        self.generate_btn.bind(on_press=self.generate_password)
        self.add_widget(self.generate_btn)

        self.qr_btn = Button(text="📷 QR Kod Göster")
        self.qr_btn.bind(on_press=self.show_qr_code)
        self.add_widget(self.qr_btn)

    def generate_password(self, instance):
        master = self.master_input.text
        service = self.service_input.text
        if not master or not service:
            self.result_label.text = "⚠️ Alanlar boş olamaz"
            return
        password = generate_password(master, service)
        self.result_label.text = f"Şifre: {password}"

    def show_qr_code(self, instance):
        password_text = self.result_label.text.replace("Şifre: ", "")
        if not password_text:
            popup = Popup(title="Uyarı", content=Label(text="Önce şifre üret."), size_hint=(.6, .4))
            popup.open()
            return
        qr = qrcode.make(password_text)
        buffer = BytesIO()
        qr.save(buffer, format="PNG")
        buffer.seek(0)
        img = CoreImage(buffer, ext="png")

        popup = Popup(title="📷 QR Kod", size_hint=(.8, .8))
        img_label = Label()
        img_label.texture = img.texture
        popup.content = img_label
        popup.open()

class ZeusPassApp(App):
    def build(self):
        return ZeusLayout()

if __name__ == "__main__":
    ZeusPassApp().run()
>>>>>>> bf05dac3c54ae129a55397be3a5946cb7c80e222
