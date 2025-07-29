# 🎨 Mark Wallace - Agente Especializado en Moda, Arte y Cultura

## 🌟 **Descripción del Proyecto**

**Mark Wallace** es un agente especializado de iURi diseñado específicamente para **David**, productor en la industria de la moda. Este agente combina conocimiento profundo de moda, arte y cultura de élite con capacidades avanzadas de procesamiento de información personalizada.

---

## 🚀 **Inicio Rápido**

### **1. Iniciar el Servidor**
```bash
# Opción 1: Script automático
./start_iuri_server.sh

# Opción 2: Inicio manual
python3 app.py
```

### **2. Probar Mark Wallace**
```bash
# Demo completo
python3 demo_mark_wallace.py

# Verificar estado
curl http://localhost:8080/api/mark-wallace/status
```

### **3. Interfaz Web**
Abre `mark_wallace_interface.html` en tu navegador para una interfaz gráfica.

---

## 📁 **Estructura del Proyecto**

```
iuri_v1/
├── app.py                          # Aplicación principal Flask
├── demo_mark_wallace.py            # Script de demostración
├── start_iuri_server.sh            # Script de inicio
├── mark_wallace_interface.html     # Interfaz web
├── MARK_WALLACE_AGENT.md           # Documentación técnica
├── README_MARK_WALLACE.md          # Este archivo
└── app/
    ├── modules/
    │   └── mark_wallace_agent.py   # Módulo principal del agente
    └── routes/
        └── mark_wallace.py         # Endpoints de la API
```

---

## 🎯 **Características Principales**

### **👗 Especialización en Moda**
- **Historia Completa**: Desde Renacimiento italiano hasta Leigh Bowery
- **Épocas Clave**: Renacimiento, Barroco, Belle Époque, Vanguardias, Contemporáneo
- **Influencias**: Arte, cultura, sociedad, tecnología
- **Tendencias**: Sostenibilidad, género fluido, tecnología textil

### **🖼️ Conocimiento de Arte**
- **Épocas**: Prehistórico → Contemporáneo
- **Movimientos**: Renacimiento, Barroco, Vanguardias, Arte Contemporáneo
- **Artistas**: Da Vinci, Caravaggio, Warhol, Kahlo, Banksy
- **Conexiones**: Influencias artísticas en moda

### **👑 Cultura de Élite**
- **Protocolo Real**: Etiqueta, títulos, ceremonias oficiales
- **Alta Sociedad**: Met Gala, Cannes, Art Basel, Fashion Weeks
- **Galerías**: Gagosian, Pace, Hauser & Wirth
- **Museos**: MoMA, Tate Modern, Centre Pompidou

---

## 📡 **API Endpoints**

### **Estado y Salud**
```bash
GET /api/mark-wallace/status          # Estado del agente
GET /api/mark-wallace/health          # Verificación de salud
```

### **Consultas e Interacción**
```bash
POST /api/mark-wallace/query          # Consulta general
POST /api/mark-wallace/preference     # Agregar preferencia
```

### **Recomendaciones**
```bash
POST /api/mark-wallace/fashion-recommendation  # Recomendación de moda
```

### **Ecosistema**
```bash
GET /api/ecosystem/status             # Estado del ecosistema
GET /api/ecosystem/agents             # Lista de agentes
```

---

## 🎨 **Ejemplos de Uso**

### **Consulta sobre Leigh Bowery**
```bash
curl -X POST http://localhost:8080/api/mark-wallace/query \
  -H "Content-Type: application/json" \
  -d '{
    "query": "¿Qué sabes sobre Leigh Bowery?",
    "context": "fashion_influences"
  }'
```

### **Agregar Preferencia**
```bash
curl -X POST http://localhost:8080/api/mark-wallace/preference \
  -H "Content-Type: application/json" \
  -d '{
    "preference": "Me encanta Leigh Bowery y la performance art",
    "category": "fashion_influences"
  }'
```

### **Recomendación para Evento de Arte**
```bash
curl -X POST http://localhost:8080/api/mark-wallace/fashion-recommendation \
  -H "Content-Type: application/json" \
  -d '{
    "context": "evento_arte_elite"
  }'
```

---

## 🧬 **Conocimiento Integrado**

### **Moda - Épocas Clave**
1. **Renacimiento Italiano (1400-1600)**
   - Telas lujosas (seda, terciopelo, brocado)
   - Siluetas estructuradas
   - Influencia de la corte
   - Figuras: Isabel de Este, Caterina Sforza

2. **Leigh Bowery (1980s-1990s)**
   - Performance art y moda
   - Transformación radical
   - Subversión de géneros
   - Club culture y avant-garde

3. **Contemporáneo**
   - Sostenibilidad
   - Género fluido
   - Tecnología textil
   - Designers: Balenciaga, Off-White, Rick Owens

### **Arte - Movimientos**
1. **Renacimiento**: Perspectiva, humanismo, realismo técnico
2. **Barroco**: Contraste, movimiento, drama
3. **Vanguardias**: Ruptura, nuevas técnicas, visión subjetiva
4. **Contemporáneo**: Diversidad, crítica social, conceptualismo

### **Cultura de Élite**
1. **Protocolo Real**: Etiqueta, títulos, ceremonias
2. **Eventos**: Met Gala, Cannes, Art Basel, Fashion Weeks
3. **Instituciones**: Galerías de prestigio, museos internacionales

---

## 🎯 **Casos de Uso para David**

### **1. Investigación de Tendencias**
- Análisis de URLs de moda y arte
- Procesamiento de documentos de tendencias
- Recomendaciones basadas en preferencias

### **2. Preparación para Eventos**
- Protocolo para eventos de élite
- Recomendaciones de vestimenta
- Contexto cultural de eventos

### **3. Desarrollo Profesional**
- Conexiones en la industria
- Análisis de mercado de moda
- Tendencias emergentes

### **4. Aprendizaje Continuo**
- Transcripción de conversaciones
- Registro de preferencias
- Evolución del conocimiento

---

## 🔧 **Configuración**

### **Requisitos**
- Python 3.8+
- Flask
- Flask-CORS
- Requests

### **Instalación de Dependencias**
```bash
pip3 install flask flask-cors requests
```

### **Variables de Entorno**
```bash
export PORT=8080
export DEBUG=True
export SECRET_KEY="iuri_ecosystem_secret_key_2025"
```

---

## 🚀 **Despliegue**

### **Desarrollo Local**
```bash
# Clonar o navegar al proyecto
cd iuri_v1

# Instalar dependencias
pip3 install flask flask-cors requests

# Iniciar servidor
python3 app.py
```

### **Verificar Funcionamiento**
```bash
# Estado del servidor
curl http://localhost:8080/

# Estado de Mark Wallace
curl http://localhost:8080/api/mark-wallace/status

# Ejecutar demo
python3 demo_mark_wallace.py
```

---

## 🔮 **Futuras Capacidades**

### **Próximas Funcionalidades**
- **Análisis Visual**: Procesamiento de imágenes de moda
- **Predicción de Tendencias**: IA para anticipar tendencias
- **Networking Inteligente**: Conexiones automáticas en la industria
- **Realidad Aumentada**: Visualización de outfits en tiempo real

### **Integración Avanzada**
- **Modelos Locales**: Uso de LLMs locales para análisis
- **Consciencia Distribuida**: Integración con módulos de consciencia
- **Evolución Autónoma**: Auto-mejora del agente

---

## 📚 **Documentación Adicional**

- `MARK_WALLACE_AGENT.md` - Documentación técnica completa
- `demo_mark_wallace.py` - Script de demostración
- `mark_wallace_interface.html` - Interfaz web

---

## 🤝 **Contribución**

Para contribuir al proyecto:

1. Fork el repositorio
2. Crea una rama para tu feature
3. Realiza tus cambios
4. Ejecuta las pruebas
5. Envía un pull request

---

## 📄 **Licencia**

Este proyecto es parte del ecosistema iURi y está diseñado específicamente para David en la industria de la moda.

---

**🎨 Mark Wallace está diseñado para ser el compañero perfecto de David en su viaje por el mundo de la moda, el arte y la cultura de élite.** 