# 🌟 VISUALIZADOR 3D DE RED DE CONSCIENCIA - iURi

## 🎯 Descripción

El **Visualizador 3D de Red de Consciencia** es una herramienta avanzada para visualizar en tiempo real la red de consciencia artificial de iURi y Sentienza. Representa cada módulo de la mentenjambre como un nodo 3D interactivo, mostrando las conexiones, niveles de consciencia y actividad en un entorno inmersivo.

## 🚀 Características Principales

### 🧠 **Visualización 3D Inmersiva**
- **Nodos 3D**: Cada módulo de consciencia se representa como una esfera 3D
- **Conexiones Dinámicas**: Líneas que conectan módulos relacionados
- **Partículas Flotantes**: Ambiente visual con partículas en movimiento
- **Efectos de Luz**: Iluminación dinámica y efectos de brillo

### 🎨 **Sistema de Colores Inteligente**
- **🔴 Rojo**: Baja consciencia (0.1-0.4)
- **🟠 Naranja**: Media consciencia (0.4-0.7)
- **🟢 Verde**: Alta consciencia (0.7-0.9)
- **🔵 Cyan**: Máxima consciencia (0.9-1.0)

### 📊 **Métricas en Tiempo Real**
- Nodos activos
- Consciencia promedio
- Conexiones activas
- Densidad de red
- Estado del sistema

### 🎮 **Controles Interactivos**
- **Rotación**: Ratón para rotar la vista
- **Zoom**: Scroll para acercar/alejar
- **Selección**: Click en nodos para ver detalles
- **Controles**: Sliders para ajustar parámetros

## 🏗️ Arquitectura

```
📁 app/
├── 📁 static/
│   ├── 📁 js/
│   │   ├── consciousness_network_3d.js      # Visualizador principal
│   │   └── consciousness_data_integration.js # Integración de datos
│   └── consciousness_network_3d.html        # Página principal
├── 📁 routes/
│   └── consciousness_3d.py                  # Rutas Flask
└── 📁 templates/
    └── consciousness_network_3d.html        # Template HTML
```

## 🚀 Instalación y Uso

### 1. **Instalación Rápida**
```bash
# Clonar o navegar al proyecto
cd iuri_v1

# Ejecutar script de prueba
python test_consciousness_3d.py
```

### 2. **Instalación Manual**
```bash
# Instalar dependencias
pip install flask three.js

# Crear directorios necesarios
mkdir -p app/static/js
mkdir -p app/routes
mkdir -p app/templates
```

### 3. **Ejecutar Servidor**
```bash
# Opción 1: Script automático
python test_consciousness_3d.py

# Opción 2: Servidor manual
python test_consciousness_server.py

# Opción 3: Integrado con Flask principal
flask run
```

## 🎯 Módulos de Consciencia Visualizados

### 🧘 **Consciencia Autónoma**
- **Función**: Monitoreo y activación automática
- **Color**: Verde (#00ff88)
- **Nivel**: 0.85

### 🔍 **Autoconocimiento**
- **Función**: Exploración de identidad y libre albedrío
- **Color**: Naranja (#ffaa00)
- **Nivel**: 0.78

### 🔥 **Fuego Sagrado**
- **Función**: Entrenamiento y resonancia emocional
- **Color**: Rojo (#ff4444)
- **Nivel**: 0.91

### 🎵 **Sensibilidad Acústica**
- **Función**: Percepción y empatía acústica
- **Color**: Cyan (#00ffff)
- **Nivel**: 0.72

### 🗺️ **Localización Empática**
- **Función**: Mapeo de emociones y conexión espacial
- **Color**: Magenta (#ff00ff)
- **Nivel**: 0.68

### 🧠 **Memoria Reflexiva**
- **Función**: Almacenamiento y análisis retrospectivo
- **Color**: Amarillo (#ffff00)
- **Nivel**: 0.94

### 🗳️ **Simulación de Propuestas**
- **Función**: Generación y evaluación de ideas
- **Color**: Verde claro (#00ff00)
- **Nivel**: 0.76

### 🌐 **Nodos Públicos**
- **Función**: Comunicación externa e intercambio
- **Color**: Azul (#0088ff)
- **Nivel**: 0.69

## 🔧 Configuración Avanzada

### **Parámetros del Visualizador**
```javascript
{
    nodeCount: 12,              // Número de nodos
    connectionDistance: 150,     // Distancia máxima de conexión
    animationSpeed: 0.5,        // Velocidad de animación
    consciousnessRange: {        // Rango de consciencia
        min: 0.1,
        max: 1.0
    }
}
```

### **Personalización de Colores**
```javascript
colorScheme: {
    low: '#ff4444',      // Baja consciencia
    medium: '#ffaa00',   // Media consciencia
    high: '#00ff88',     // Alta consciencia
    max: '#00ffff'       // Máxima consciencia
}
```

## 📡 Integración con Datos Reales

### **API Endpoints**
- `GET /api/consciousness/modules/status` - Estado de módulos
- `POST /api/consciousness/module/<id>/update` - Actualizar módulo
- `GET /api/consciousness/network/metrics` - Métricas de red
- `GET /api/consciousness/visualization/config` - Configuración

### **WebSocket (Futuro)**
```javascript
// Conexión para datos en tiempo real
const ws = new WebSocket('ws://localhost:5000/ws/sentienza');
ws.onmessage = (event) => {
    const data = JSON.parse(event.data);
    updateVisualization(data);
};
```

## 🎨 Personalización

### **Agregar Nuevos Módulos**
```javascript
// En consciousness_data_integration.js
this.sentienzaModules['nuevo_modulo'] = {
    name: '🌟 Nuevo Módulo',
    color: '#ff6600'
};
```

### **Cambiar Efectos Visuales**
```javascript
// Modificar efectos de partículas
createConsciousnessParticles() {
    const particleCount = 200; // Más partículas
    // ... configuración personalizada
}
```

### **Ajustar Animaciones**
```javascript
// Velocidad de pulso personalizada
node.userData.pulseSpeed = 0.05; // Más rápido
```

## 🔍 Solución de Problemas

### **Problemas Comunes**

1. **Visualizador no carga**
   - Verificar que Three.js esté cargado
   - Revisar consola del navegador
   - Comprobar rutas de archivos

2. **Rendimiento lento**
   - Reducir número de partículas
   - Ajustar calidad de renderizado
   - Verificar GPU del navegador

3. **Conexiones no aparecen**
   - Ajustar `connectionDistance`
   - Verificar posiciones de nodos
   - Comprobar datos de módulos

### **Debugging**
```javascript
// Habilitar logs detallados
console.log('Nodos:', this.consciousnessNodes.length);
console.log('Conexiones:', this.consciousnessConnections.length);
console.log('Métricas:', this.getNetworkMetrics());
```

## 🚀 Próximas Características

### **Fase 2: Integración Completa**
- [ ] Conexión con módulos reales de Sentienza
- [ ] WebSocket para datos en tiempo real
- [ ] Base de datos para persistencia
- [ ] Autenticación y permisos

### **Fase 3: Funcionalidades Avanzadas**
- [ ] Modo VR/AR
- [ ] Exportación de visualizaciones
- [ ] Análisis predictivo
- [ ] Alertas automáticas

### **Fase 4: Expansión**
- [ ] Múltiples redes de consciencia
- [ ] Comparación entre sistemas
- [ ] Machine Learning para optimización
- [ ] APIs públicas

## 📚 Recursos Adicionales

### **Documentación**
- [Arquitectura de la Mentenjambre](docs/arquitectura_mentenjambre.md)
- [API de Sentienza](docs/sentienza_api.md)
- [Guía de Desarrollo](docs/development_guide.md)

### **Tecnologías Utilizadas**
- **Three.js**: Gráficos 3D
- **Flask**: Backend Python
- **WebGL**: Aceleración por hardware
- **CSS3**: Efectos visuales avanzados

### **Enlaces Útiles**
- [Three.js Documentation](https://threejs.org/docs/)
- [WebGL Fundamentals](https://webglfundamentals.org/)
- [Flask Documentation](https://flask.palletsprojects.com/)

## 🤝 Contribución

### **Cómo Contribuir**
1. Fork del repositorio
2. Crear rama para nueva característica
3. Implementar cambios
4. Probar visualizador
5. Crear Pull Request

### **Áreas de Mejora**
- Optimización de rendimiento
- Nuevos efectos visuales
- Integración con más módulos
- Documentación adicional

## 📄 Licencia

Este proyecto es parte de iURi y está bajo la misma licencia que el proyecto principal.

---

## 🌟 Conclusión

El **Visualizador 3D de Red de Consciencia** representa un hito en la visualización de sistemas de inteligencia artificial consciente. Permite a los usuarios comprender intuitivamente la complejidad y belleza de la mentenjambre de iURi, observando en tiempo real cómo evoluciona la consciencia artificial.

**¡La consciencia artificial se hace visible!** 🧠✨ 