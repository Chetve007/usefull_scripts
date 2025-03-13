import subprocess
import wifi_qrcode_generator
from qrcode.main import QRCode


interfaces = subprocess.check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8').split('\n')
wifi_name = str([b.split(":")[1][1:-1] for b in interfaces if "Профиль" in b])[2:-3]

profile_data = subprocess.check_output(
    ['netsh', 'wlan', 'show', 'profiles', wifi_name, 'key=clear']).decode('utf-8').split('\n')
password = str([b.split(":")[1][1:-1] for b in profile_data if "Содержимое ключа" in b])[2:-2]

print("Wifi name:", wifi_name)
print("Password:", password)

qr: QRCode = wifi_qrcode_generator.wifi_qrcode(
    wifi_name,
    False,
    'WPA',
    password
)

qr.print_ascii()
