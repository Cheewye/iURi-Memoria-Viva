# 🤖 Firmware – iURi UR Receiver ESP32

Este módulo contiene el firmware y diagrama para que Claude integre el sistema simbólico UR con hardware físico.

---

## 📁 Archivos

- `ur_receiver_esp32.ino` – Código para ESP32: recibe símbolos UR vía serial (ej: {"ur": "aURa"}) y activa LED o motor.
- `esquema_ur_receiver.png` – Diagrama de conexiones electrónicas (pin 2 para LED, pin 4 para vibración).

---

## 🔌 Instrucciones para Claude

1. Subí el sketch `ur_receiver_esp32.ino` al ESP32 usando Arduino IDE o PlatformIO.
2. Conectá un LED al pin D2 con resistencia de 220Ω.
3. Conectá un motor vibrador al pin D4 con transistor + diodo + alimentación.
4. El ESP32 debe recibir datos por serial USB desde un host (PC, Raspberry o sistema iURi).
5. El host debe enviar JSON con símbolos UR, como: {"ur": "aURa"}.

---

## ⚡ Expansión

Claude puede agregar más símbolos UR en el `if` del sketch y controlar efectos adicionales como zumbadores, servos, o pantallas OLED.
