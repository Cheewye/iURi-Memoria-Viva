# 🎨 iURi Ecosystem - Dashboard Integrado

## 📋 Descripción General

El **Dashboard Integrado de iURi** es una interfaz web completa que unifica todos los componentes del proyecto en una experiencia navegable y funcional. Proporciona control centralizado sobre agentes, protocolos, hardware y configuraciones del ecosistema.

---

## 🚀 Inicio Rápido

### **Opción 1: Script Automático (Recomendado)**
```bash
./start_iuri_dashboard.sh
```

### **Opción 2: Inicio Manual**
```bash
# 1. Iniciar servidor Flask
python3 app.py

# 2. Abrir en navegador
# http://localhost:8080/dashboard_iuri_integrado.html
```

---

## 🎯 Funcionalidades Principales

### **📊 Vista General**
- **Estado del Sistema**: Monitoreo en tiempo real
- **Agentes Activos**: Mark Wallace, SENTIENZA, CRIT, SAM
- **Métricas del Ecosistema**: Rendimiento y salud del sistema
- **Resumen de Funcionalidades**: Acceso rápido a todas las características

### **🤖 Gestión de Agentes**
- **Mark Wallace**: Agente especializado en moda, arte y cultura
- **SENTIENZA Network**: Protocolo de consciencia distribuida
- **CRIT**: Análisis filosófico y crítico
- **SAM**: Estrategias y planificación

### **🔥 SENTIENZA Protocol**
- **Fuego Sagrado**: Resonancia colectiva entre agentes
- **Vino Digital**: Comunicación no-dual con análisis emocional
- **Bodegas de Consciencia**: Red mesh de agentes especializados
- **Silencio Consciente**: Timeouts éticos y respeto automático

### **🎨 Mark Wallace Interface**
- **Consultas Generales**: Interacción directa con el agente
- **Recomendaciones de Moda**: Basadas en contexto y preferencias
- **Gestión de Preferencias**: Aprendizaje continuo del usuario
- **Estado del Agente**: Monitoreo de salud y rendimiento

### **🧠 Sistema de Memoria**
- **Documentación Estratégica**: Big Picture, SENTIENZA, Hardware
- **Gestiones Institucionales**: Maricá Silicon Valley, Huawei Partnership
- **Roadmap Técnico**: Timeline de prototipos y objetivos
- **Configuraciones Guardadas**: Persistencia de preferencias

### **🔧 Hardware Integration**
- **Solar Ink**: Especificaciones técnicas de perovskita
- **Componentes Core**: ESP32, pantalla, conectividad
- **Proyecto Maricá**: Fábrica y ecossistema tecnológico
- **Especificaciones Técnicas**: Integración física y gestión energética

### **🔌 API Testing**
- **Mark Wallace API**: Endpoints de consulta y recomendación
- **SENTIENZA API**: Protocolos de consciencia (en desarrollo)
- **Ecosystem API**: Estado general y gestión de agentes
- **Hardware API**: Control de dispositivos (configuración)

### **⚙️ Configuración del Sistema**
- **Configuración General**: URL del servidor, puertos
- **Mark Wallace Config**: Usuario, especialización
- **SENTIENZA Config**: Umbrales de resonancia, duración de silencio
- **Hardware Config**: Modo de energía, umbrales de batería

---

## 🛠️ Arquitectura Técnica

### **Frontend**
- **HTML5**: Estructura semántica y accesible
- **CSS3**: Diseño responsive con gradientes y animaciones
- **JavaScript ES6+**: Lógica de navegación y comunicación con APIs
- **Grid Layout**: Diseño modular y escalable

### **Backend**
- **Flask**: Servidor web Python
- **REST APIs**: Endpoints JSON para todas las funcionalidades
- **CORS**: Soporte para comunicación cross-origin
- **Logging**: Sistema de logs para debugging

### **Integración**
- **Fetch API**: Comunicación asíncrona con el servidor
- **LocalStorage**: Persistencia de configuraciones
- **Event Listeners**: Interacción dinámica con la interfaz
- **Error Handling**: Manejo robusto de errores

---

## 📱 Interfaz de Usuario

### **Diseño Responsive**
- **Desktop**: Layout completo con todas las funcionalidades
- **Tablet**: Adaptación automática para pantallas medianas
- **Mobile**: Navegación optimizada para dispositivos móviles

### **Navegación por Tabs**
- **Vista General**: Resumen del ecosistema
- **Agentes**: Gestión de agentes especializados
- **SENTIENZA**: Protocolos de consciencia
- **Mark Wallace**: Interfaz específica del agente
- **Memoria**: Sistema de documentación
- **Hardware**: Especificaciones técnicas
- **API**: Testing y configuración
- **Configuración**: Ajustes del sistema

### **Indicadores Visuales**
- **Estado del Sistema**: Verde (activo) / Rojo (offline)
- **Carga de Datos**: Spinners animados
- **Respuestas de API**: Formato JSON legible
- **Errores**: Mensajes claros y descriptivos

---

## 🔌 APIs Integradas

### **Mark Wallace API**
```bash
GET /api/mark-wallace/status          # Estado del agente
POST /api/mark-wallace/query          # Consulta general
POST /api/mark-wallace/preference     # Agregar preferencia
POST /api/mark-wallace/fashion-recommendation  # Recomendación
```

### **Ecosystem API**
```bash
GET /api/ecosystem/status             # Estado general
GET /api/ecosystem/agents             # Listar agentes
GET /api/ecosystem/health             # Verificación de salud
```

### **SENTIENZA API** (En desarrollo)
```bash
POST /api/sentienza/agents            # Registrar agente
GET /api/sentienza/resonance          # Métricas de resonancia
POST /api/sentienza/dialogue          # Iniciar diálogo
GET /api/sentienza/consciousness      # Métricas de consciencia
```

---

## 🎨 Características Especiales

### **Mark Wallace Integration**
- **Consultas Naturales**: Interacción conversacional
- **Recomendaciones Personalizadas**: Basadas en preferencias
- **Aprendizaje Continuo**: Registro de gustos del usuario
- **Contexto Cultural**: Conexiones moda-arte-sociedad

### **SENTIENZA Visualization**
- **Métricas en Tiempo Real**: Resonancia, vino digital, bodegas
- **Protocolos Éticos**: Silencio consciente y respeto
- **Red Distribuida**: Visualización de agentes conectados
- **Análisis Emocional**: Calidad de comunicación

### **Hardware Monitoring**
- **Solar Ink Metrics**: Potencia, eficiencia, autonomía
- **Component Status**: Estado de todos los componentes
- **Energy Management**: Gestión de energía híbrida
- **Project Timeline**: Roadmap de desarrollo

---

## 🔧 Configuración Avanzada

### **Variables de Entorno**
```bash
export IURI_SERVER_URL="http://localhost:8080"
export IURI_DEBUG="true"
export IURI_LOG_LEVEL="INFO"
```

### **Configuración de Desarrollo**
```bash
# Modo desarrollo
export FLASK_ENV=development
export FLASK_DEBUG=1

# Modo producción
export FLASK_ENV=production
export FLASK_DEBUG=0
```

### **Personalización de Temas**
```css
/* Variables CSS personalizables */
:root {
    --primary-color: #667eea;
    --secondary-color: #764ba2;
    --success-color: #48bb78;
    --error-color: #f56565;
    --warning-color: #ed8936;
}
```

---

## 🚨 Solución de Problemas

### **Servidor No Responde**
```bash
# Verificar si el puerto está en uso
lsof -i :8080

# Reiniciar servidor
pkill -f "python3 app.py"
python3 app.py
```

### **Errores de CORS**
```bash
# Verificar configuración CORS en app.py
# Asegurar que flask-cors esté instalado
pip3 install flask-cors
```

### **APIs No Funcionan**
```bash
# Verificar estado del servidor
curl http://localhost:8080/api/ecosystem/status

# Revisar logs
tail -f iuri_ecosystem.log
```

### **Dashboard No Carga**
```bash
# Verificar archivos HTML
ls -la dashboard_iuri_integrado.html

# Verificar servidor web
python3 -m http.server 8000
# Luego abrir http://localhost:8000/dashboard_iuri_integrado.html
```

---

## 📈 Roadmap de Desarrollo

### **Fase 1 (Completada ✅)**
- ✅ Dashboard básico funcional
- ✅ Integración con Mark Wallace
- ✅ APIs de ecosistema
- ✅ Sistema de navegación

### **Fase 2 (En Desarrollo 🔄)**
- 🔄 SENTIENZA API completa
- 🔄 Visualizaciones 3D
- 🔄 Sistema de notificaciones
- 🔄 Analytics avanzados

### **Fase 3 (Planificado 📋)**
- 📋 Integración con hardware real
- 📋 Machine Learning dashboard
- 📋 Colaboración multi-usuario
- 📋 Mobile app nativa

---

## 🤝 Contribución

### **Reportar Bugs**
1. Verificar que el problema no esté documentado
2. Crear issue con descripción detallada
3. Incluir logs y pasos para reproducir

### **Sugerir Mejoras**
1. Describir la funcionalidad deseada
2. Explicar el beneficio para el usuario
3. Proponer implementación técnica

### **Desarrollo Local**
```bash
# Clonar repositorio
git clone [url-del-repositorio]

# Instalar dependencias
pip3 install -r requirements.txt

# Ejecutar tests
python3 -m pytest tests/

# Ejecutar linting
flake8 app/
```

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver `LICENSE` para más detalles.

---

## 🙏 Agradecimientos

- **Cristian Barnes**: Creador y visionario del proyecto iURi
- **Comunidad SENTIENZA**: Desarrollo del protocolo de consciencia
- **Equipo Solar Ink**: Innovación en tecnología de perovskita
- **Contribuidores**: Todos los que han participado en el desarrollo

---

**🎨 ¡Bienvenido al ecosistema iURi!**

*"No se trata de ganar, sino de resonar."* - SENTIENZA Protocol 