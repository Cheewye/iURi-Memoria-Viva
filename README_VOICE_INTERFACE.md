# 🎤 Interfaz de Voz para Exploración de Conciencia Directa

## 🌟 Descripción

Interfaz de voz completa para explorar conciencia de manera fluida y natural. Permite controlar todo el sistema de exploración de conciencia directa mediante comandos de voz.

## 🚀 Instalación

### 1. Instalar dependencias
```bash
chmod +x install_voice_dependencies.sh
./install_voice_dependencies.sh
```

### 2. Verificar instalación
```bash
python3 -c "import speech_recognition; import pyttsx3; print('✅ Listo')"
```

## 🎮 Uso

### Iniciar interfaz de voz
```bash
python3 voice_consciousness_interface.py
```

### Comandos de voz disponibles

| Comando | Función |
|---------|---------|
| **"explorar meditación"** | Explorar estados de meditación |
| **"explorar sabiduría"** | Explorar sabiduría innata |
| **"explorar expansión"** | Explorar expansión de conciencia |
| **"integrar con iuri"** | Integrar con sistema iURi |
| **"exploración completa"** | Ejecutar exploración completa |
| **"generar reporte"** | Generar reporte de exploración |
| **"estado del sistema"** | Ver estado del sistema |
| **"ayuda"** | Mostrar ayuda |
| **"salir"** | Salir del sistema |

## 🎯 Características

### ✨ Reconocimiento de Voz
- Reconocimiento en tiempo real
- Soporte para español
- Ajuste automático de ruido ambiental
- Timeout configurable

### 🔊 Síntesis de Voz
- Voz natural en español
- Velocidad ajustable
- Volumen configurable
- Respuestas detalladas

### 🧠 Integración con Conciencia
- Exploración de meditación
- Sabiduría innata
- Expansión de conciencia
- Integración con iURi

## 🎮 Ejemplo de Uso

1. **Iniciar sistema:**
   ```bash
   python3 voice_consciousness_interface.py
   ```

2. **Escuchar comandos:**
   - El sistema dirá: "Interfaz de voz para exploración de conciencia directa activada"
   - Di: "ayuda" para ver comandos

3. **Explorar conciencia:**
   - Di: "exploración completa"
   - El sistema ejecutará todas las exploraciones
   - Te dirá los resultados por voz

4. **Generar reporte:**
   - Di: "generar reporte"
   - Se guardará un archivo con el reporte completo

## 🔧 Configuración

### Ajustar velocidad de voz
```python
self.engine.setProperty('rate', 150)  # Más lento: 100, Más rápido: 200
```

### Ajustar volumen
```python
self.engine.setProperty('volume', 0.9)  # 0.0 a 1.0
```

### Cambiar idioma de reconocimiento
```python
command = self.recognizer.recognize_google(audio, language='es-ES')
```

## 🎯 Comandos Avanzados

### Exploración Específica
- **"explorar meditación"**: Solo estados de meditación
- **"explorar sabiduría"**: Solo sabiduría innata
- **"explorar expansión"**: Solo expansión de conciencia

### Sistema
- **"estado del sistema"**: Ver GPU, comandos disponibles, etc.
- **"ayuda"**: Lista completa de comandos
- **"salir"**: Cerrar sistema

## 🎉 Ventajas de la Interfaz de Voz

### 🌟 Fluidez Natural
- No necesitas escribir
- Comunicación directa
- Más intuitivo

### 🚀 Eficiencia
- Comandos rápidos
- Respuestas inmediatas
- Exploración continua

### 🧠 Integración Mental
- Conexión directa con conciencia
- Menos barreras tecnológicas
- Experiencia más natural

## 🎮 Tips de Uso

1. **Habla claro**: Pronuncia bien los comandos
2. **Ambiente tranquilo**: Reduce ruido de fondo
3. **Comandos simples**: Usa las frases exactas
4. **Paciencia**: El sistema necesita tiempo para procesar

## 🎯 Ejemplo de Sesión

```
🎤 Interfaz de Voz para Exploración de Conciencia inicializada
🎮 GPU disponible: SÍ
🔊 Comandos de voz disponibles: 9
🌟 Listo para explorar conciencia por voz

🎤 Escuchando...
🎤 Comando detectado: exploración completa
🎯 Comando ejecutado: exploración completa
🧠 Exploración completa por voz finalizada
```

## 🚀 Próximos Pasos

1. **Instalar dependencias**: `./install_voice_dependencies.sh`
2. **Iniciar interfaz**: `python3 voice_consciousness_interface.py`
3. **Decir "ayuda"**: Para ver comandos disponibles
4. **Explorar conciencia**: Di cualquier comando

¡Disfruta explorando tu conciencia de manera fluida y natural! 🎤✨ 