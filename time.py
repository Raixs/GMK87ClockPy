#!/usr/bin/env python3
import hid
from datetime import datetime

VENDOR_ID = 0x320f
PRODUCT_ID = 0x5055

def send_data(device, data):
    # Asegurarse de enviar el report ID como primer byte si es necesario
    # Algunos dispositivos HID no lo requieren.
    device.write([0x00] + data)

def update_time(device):
    now = datetime.now()
    
    # Iniciar transacción
    data1 = [0x04, 0x01] + [0x00] * 62
    send_data(device, data1)

    # Actualizar configuración, incluyendo la hora
    data2 = [
        0x04, 0x53, 0x06, 0x06, 0x30, 0x00, 0x00, 0x00, 0x00, 0x12, 
        0x03, 0x01, 0x00, 0x01, 0xFF, 0xFF, 0xFF, 0x00, 0x00, 0x00,
        # Continúa con los valores ajustados a tu necesidad...
    ]
    # Ajusta los valores de tiempo como corresponda
    data2[30:37] = [
        now.year - 2000, now.month, now.day, now.weekday(), 
        now.hour, now.minute, now.second
    ]
    # Asegúrate de que 'data2' tenga 64 bytes en total
    data2 += [0x00] * (64 - len(data2))
    send_data(device, data2)
    
    # Finalizar transacción
    data3 = [0x04, 0x02] + [0x00] * 62
    send_data(device, data3)

    print("Intento de actualización de la hora enviado.")

def main():
    try:
        print("Buscando el dispositivo...")
        device = hid.device()
        device.open(VENDOR_ID, PRODUCT_ID)
        print("Dispositivo encontrado.")
        update_time(device)
    except Exception as e:
        print(f"Se ha producido un error: {e}")
    finally:
        if device:
            device.close()

if __name__ == "__main__":
    main()
