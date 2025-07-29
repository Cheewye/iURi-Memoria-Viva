# 🐟 iURi Pescadores - Sistema Integrado de Alertas Marinas

## 📍 Visión General

Este módulo integra **todas las funcionalidades de alertas** para comunidades pesqueras de la Costa RJ (Maricá, Saquarema, Búzios, etc.) en una **aplicación unificada** que aprovecha lo mejor de cada componente desarrollado.

### 🎯 Objetivo
Crear un **painel visual interativo** accesible via web (PWA), capaz de integrar múltiples fuentes de datos oficiales para la seguridad y eficiencia de las comunidades pesqueras.

---

## 🏗️ Arquitectura Integrada

### 🔧 Backend (Flask + APIs)
```
app/routes/pescadores_routes.py
├── /pescadores/                    # Dashboard principal
├── /pescadores/api/alertas         # Alertas CPTEC/INPE
├── /pescadores/api/mare            # Tablas de marea Marinha
├── /pescadores/api/viento          # Datos OpenWeather
├── /pescadores/api/embarcacoes     # AISStream en tiempo real
├── /pescadores/api/layers          # Configuración de capas
└── /pescadores/api/status          # Status del sistema
```

### 🎨 Frontend (HTML + JS + Leaflet)
```
app/templates/pescadores_dashboard.html
├── Mapa interactivo con Leaflet
├── Sidebar con alertas en tiempo real
├── Control de capas (vento, temperatura, mareas)
├── Visualización de embarcaciones AIS
└── Diseño responsive para móviles
```

---

## 🌐 APIs Integradas

| API | Descripción | Estado | Clave Requerida |
|-----|-------------|--------|-----------------|
| **CPTEC/INPE** | Alertas meteorológicas | ✅ Activa | ❌ Pública |
| **Marinha do Brasil** | Tablas de marea | ✅ Activa | ❌ Pública |
| **OpenWeather** | Viento y clima | ✅ Activa | ✅ `OPENWEATHER_API_KEY` |
| **AISStream** | Embarcaciones en tiempo real | ✅ Activa | ✅ `AISSTREAM_API_KEY` |

### 🔑 Claves de API Configuradas
```bash
OPENWEATHER_API_KEY=12afd64ee5a3f56640049ebaff512154
AISSTREAM_API_KEY=67d035aad2aaf5b5180bf90220308e47293b14e0
```

---

## 🗺️ Cobertura Geográfica

### 📍 Región de Interés
- **Centro**: Maricá (-22.9187, -42.8168)
- **Norte**: Búzios (-22.7500, -41.8833)
- **Sur**: Cabo Frio (-22.8833, -42.0167)
- **Este**: Arraial do Cabo (-22.9667, -42.0167)
- **Oeste**: Saquarema (-22.9200, -42.5100)

### 🎯 Zonas Pesqueras Principales
1. **Maricá** - Comunidad pesquera tradicional
2. **Saquarema** - Pesca artesanal
3. **Arraial do Cabo** - Reserva marina
4. **Búzios** - Turismo y pesca
5. **Cabo Frio** - Pesca comercial

---

## 🚀 Instalación y Configuración

### 1. Instalación Automática
```bash
python setup_pescadores.py
```

### 2. Instalación Manual
```bash
# Instalar dependencias
pip install -r requirements_pescadores.txt

# Configurar variables de entorno
cp config/env.example .env
# Editar .env con tus claves de API

# Ejecutar servidor
python main.py
```

### 3. Acceso al Sistema
```
🌐 Dashboard Principal: http://localhost:8080/pescadores/
📊 API Status: http://localhost:8080/pescadores/api/status
🌩️ Alertas: http://localhost:8080/pescadores/api/alertas
🌊 Mareas: http://localhost:8080/pescadores/api/mare
💨 Viento: http://localhost:8080/pescadores/api/viento
🚢 Embarcaciones: http://localhost:8080/pescadores/api/embarcacoes
```

---

## 🎨 Características del Dashboard

### 📱 Diseño Responsive
- **Mobile-first** para comunidades pesqueras
- **PWA** para instalación en dispositivos
- **Offline-ready** para áreas sin internet

### 🗺️ Visualización Avanzada
- **Mapa Leaflet** con capas interactivas
- **Marcadores** de zonas pesqueras
- **Íconos animados** para embarcaciones
- **Heatmaps** para condiciones meteorológicas

### ⚡ Tiempo Real
- **Actualización automática** cada 5 minutos
- **Alertas push** para condiciones críticas
- **Streaming AIS** para embarcaciones
- **Cache inteligente** para optimizar datos

---

## 🔧 Configuración Avanzada

### 📊 Intervals de Actualización
```json
{
  "alertas": 300,      // 5 minutos
  "clima": 600,        // 10 minutos  
  "embarcacoes": 60,   // 1 minuto
  "mare": 3600         // 1 hora
}
```

### 🌍 Región Personalizable
```json
{
  "center": {"lat": -22.9187, "lng": -42.8168},
  "bounds": {
    "north": -22.5, "south": -23.5,
    "east": -42.0, "west": -44.0
  }
}
```

---

## 🧪 Testing y Desarrollo

### Pruebas Automáticas
```bash
# Ejecutar tests
python -m pytest tests/test_pescadores.py

# Verificar APIs
curl http://localhost:8080/pescadores/api/status
curl http://localhost:8080/pescadores/api/alertas
```

### Desarrollo Local
```bash
# Modo desarrollo
export DEBUG=True
export FLASK_ENV=development

# Ejecutar con recarga automática
python main.py
```

---

## 📈 Próximas Extensiones

### 🔮 Roadmap
- [ ] **Radar meteorológico** en tiempo real
- [ ] **Sensores IoT** costeros
- [ ] **Panel comunitario** para reportes
- [ ] **Modo offline** completo
- [ ] **Notificaciones push** móviles
- [ ] **Integración Defesa Civil**
- [ ] **Machine Learning** para predicciones

### 🎯 Integración iURi
- [ ] **Dispositivos iURi** físicos
- [ ] **Asistente de voz** local
- [ ] **Red LoRa** para datos
- [ ] **Blockchain** para trazabilidad

---

## 🤝 Contribución

### 📝 Código de Conducta
- **Respeto** a las comunidades pesqueras
- **Tecnologías abiertas** para soberanía popular
- **Documentación** clara y accesible
- **Testing** exhaustivo

### 🐛 Reportar Issues
1. Verificar que no sea un problema de configuración
2. Incluir logs y contexto completo
3. Describir pasos para reproducir
4. Sugerir solución si es posible

---

## 📄 Licencia

**Powered by iURi e tecnologias abertas para soberania popular**

- **Autor**: Cristian Barnes (Maricá, 2025)
- **Licencia**: MIT
- **Propósito**: Soberanía tecnológica para comunidades pesqueras

---

## 🆘 Soporte

### 📞 Contacto
- **Email**: cristian@iuriapp.com
- **Telegram**: @iURi_Support
- **WhatsApp**: +55 21 99999-9999

### 📚 Documentación
- **API Docs**: `/docs` (cuando esté disponible)
- **Guías**: `/guides`
- **Ejemplos**: `/examples`

---

## 🎉 Agradecimientos

- **Comunidades pesqueras** de Maricá y región
- **CPTEC/INPE** por datos meteorológicos
- **Marinha do Brasil** por tablas de marea
- **OpenWeather** por API de clima
- **AISStream** por datos de embarcaciones
- **Comunidad open source** por tecnologías base

---

**🐟 ¡El sistema está listo para servir a las comunidades pesqueras de la Costa RJ! 🐟** 