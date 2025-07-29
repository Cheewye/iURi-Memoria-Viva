# 🌊 iURi WebGL Fallback System
## Sistema de Compatibilidad para Dispositivos Antiguos

### 📋 Descripción General

El sistema de fallback WebGL de iURi garantiza que el ecosistema marino funcione en cualquier dispositivo, desde navegadores modernos con WebGL2 hasta dispositivos antiguos con capacidades limitadas.

### 🎯 Características Principales

#### ✅ **Detección Automática**
- Detecta automáticamente el soporte de WebGL2/WebGL1
- Activa fallback apropiado según las capacidades del dispositivo
- Informa al usuario sobre el modo de renderizado activo

#### 🔄 **Sistema de Fallback**
- **WebGL2**: Rendimiento óptimo para dispositivos modernos
- **WebGL1**: Compatibilidad garantizada para dispositivos antiguos
- **Canvas 2D**: Compatibilidad máxima para navegadores muy antiguos

#### 🎮 **Visores Disponibles**

1. **WebGL2 Marino Unificado**
   - Motor WebGL2 avanzado
   - Shaders GLSL 300 es
   - Todas las capas marinas
   - Rendimiento óptimo

2. **Visor WebGL1 Minimal**
   - WebGL1 optimizado
   - Shaders GLSL 100
   - Capas básicas (SST, Oxígeno, Salinidad)
   - Compatibilidad máxima

### 📁 Estructura de Archivos

```
app/static/js/
├── fallbackHandler.js          # Detección y fallback automático
├── webgl1_loader.js           # Loader WebGL1 minimal
├── webgl2_marine_advanced_engine.js    # Motor WebGL2 avanzado
└── webgl2_unified_marine_engine.js     # Motor WebGL2 unificado

app/templates/
├── webgl1_viewer.html         # Visor WebGL1 minimal
├── marine_webgl2_unified_dashboard.html # Dashboard WebGL2
└── pescadores_selector.html   # Selector de dashboards
```

### 🚀 Instalación y Uso

#### 1. **Carga Automática**
Los scripts se cargan automáticamente cuando se accede a los dashboards:

```html
<!-- En webgl1_viewer.html -->
<script src="/static/js/fallbackHandler.js"></script>
<script src="/static/js/webgl1_loader.js"></script>
```

#### 2. **Inicialización**
```javascript
// El fallback handler se inicializa automáticamente
const fallbackHandler = new WebGLFallbackHandler();

// Obtener información de compatibilidad
const compatibility = fallbackHandler.getCompatibilityInfo();
console.log(compatibility);
```

#### 3. **Uso del Visor WebGL1**
```javascript
// Inicializar loader WebGL1
const loader = new WebGL1MinimalLoader('glCanvas');

// Cambiar capa
loader.switchLayer('sst');     // Temperatura
loader.switchLayer('oxygen');  // Oxígeno
loader.switchLayer('salinity'); // Salinidad

// Actualizar datos
loader.updateData(mockData);
```

### 🔧 Configuración

#### **URLs Disponibles**
- **Selector Principal**: `/pescadores/selector`
- **WebGL2 Unificado**: `/pescadores/marine-webgl2-unified`
- **WebGL1 Minimal**: `/pescadores/webgl1-viewer`

#### **Compatibilidad por Navegador**

| Navegador | WebGL2 | WebGL1 | Canvas 2D |
|-----------|--------|--------|-----------|
| Chrome 51+ | ✅ | ✅ | ✅ |
| Firefox 51+ | ✅ | ✅ | ✅ |
| Safari 10+ | ✅ | ✅ | ✅ |
| IE 11 | ❌ | ✅ | ✅ |
| Edge 12+ | ✅ | ✅ | ✅ |
| Opera 38+ | ✅ | ✅ | ✅ |

### 🎨 Características de Renderizado

#### **WebGL2 (Avanzado)**
- Shaders GLSL 300 es
- Uniform buffers
- Vertex array objects (VAOs)
- Múltiples capas simultáneas
- Efectos avanzados

#### **WebGL1 (Minimal)**
- Shaders GLSL 100
- Texturas RGB básicas
- Una capa a la vez
- Renderizado optimizado

#### **Canvas 2D (Fallback)**
- Gradientes y patrones
- Texto informativo
- Simulación de datos
- Compatibilidad máxima

### 📊 Datos Simulados

El sistema incluye datos marinos simulados para demostración:

- **SST (Temperatura Superficial)**: 15-30°C
- **Oxígeno Disuelto**: 4-12 mg/L
- **Salinidad**: 30-40 PSU
- **Datos Mixtos**: Combinación de parámetros

### 🔍 Detección de Compatibilidad

```javascript
// Ejemplo de información de compatibilidad
{
    webgl2: true,           // WebGL2 soportado
    webgl1: true,           // WebGL1 soportado
    fallbackMode: false,    // No en modo fallback
    canvas2d: false,        // Canvas 2D disponible
    recommended: 'WebGL2'   // Modo recomendado
}
```

### 🛠️ Desarrollo

#### **Agregar Nueva Capa**
1. Actualizar `webgl1_loader.js` con nueva textura
2. Agregar método `update[Layer]Texture()`
3. Actualizar selector en `webgl1_viewer.html`

#### **Personalizar Fallback**
1. Modificar `fallbackHandler.js`
2. Agregar nuevos métodos de renderizado 2D
3. Actualizar detección de compatibilidad

### 📈 Métricas de Rendimiento

- **WebGL2**: 60 FPS, renderizado completo
- **WebGL1**: 30-60 FPS, renderizado básico
- **Canvas 2D**: 10-30 FPS, simulación

### 🚨 Solución de Problemas

#### **Problema**: WebGL no se inicializa
**Solución**: Verificar compatibilidad del navegador
```javascript
const compatibility = fallbackHandler.getCompatibilityInfo();
if (!compatibility.webgl2 && !compatibility.webgl1) {
    console.log("Usando Canvas 2D fallback");
}
```

#### **Problema**: Rendimiento lento
**Solución**: Reducir resolución de texturas
```javascript
// En webgl1_loader.js
const textureSize = 128; // Reducir de 256 a 128
```

#### **Problema**: Errores de shader
**Solución**: Verificar conversión GLSL
```javascript
// Usar convertGLSL300to100() para WebGL1
const convertedShaders = fallbackHandler.adaptShaders(vertexSource, fragmentSource);
```

### 🎯 Casos de Uso

1. **Dispositivos Modernos**: WebGL2 para máxima calidad
2. **Dispositivos Antiguos**: WebGL1 para compatibilidad
3. **Navegadores Muy Antiguos**: Canvas 2D para funcionamiento básico
4. **Dispositivos Móviles**: WebGL1 optimizado para batería

### 📝 Notas de Desarrollo

- **Autor**: Cristian Barnes (Maricá, 2025)
- **Versión**: 1.0.0
- **Compatibilidad**: IE 11+, Chrome 51+, Firefox 51+, Safari 10+
- **Licencia**: Tecnologías abiertas para soberanía popular

### 🌐 URLs de Acceso

- **Selector**: http://localhost:8080/pescadores/selector
- **WebGL1 Viewer**: http://localhost:8080/pescadores/webgl1-viewer
- **WebGL2 Unificado**: http://localhost:8080/pescadores/marine-webgl2-unified

---

**🚀 iURi Marine Ecosystem - Garantizando compatibilidad universal** 