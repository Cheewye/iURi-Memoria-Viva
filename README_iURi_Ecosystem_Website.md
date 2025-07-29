# 🌞 iURi Ecosystem - Website

## 📋 Descripción
Sitio web completo del ecosistema iURi - La revolución solar brasileira. Página responsiva y moderna con todas las secciones del portafolio de productos.

## 📁 Estructura del Proyecto
```
iuri-ecosystem-website/
├── index.html          # Página principal del sitio
├── README.md           # Este archivo con instrucciones
└── .htaccess           # Configuración del servidor (opcional)
```

## 🚀 Instalación Rápida

### 1. Preparar Archivos
```bash
# Crear carpeta del proyecto
mkdir iuri-ecosystem-website
cd iuri-ecosystem-website

# Guardar archivos
# - index.html (el archivo HTML principal)
# - README.md (este archivo)
# - .htaccess (opcional, para optimización)
```

### 2. Subir al Servidor
```bash
# Opción A: FTP/SFTP
# Subir todos los archivos a tu servidor web

# Opción B: Git (recomendado)
git init
git add .
git commit -m "Initial iURi Ecosystem website"
git remote add origin https://github.com/tu-usuario/iuri-ecosystem
git push -u origin main
```

### 3. Configurar Subdominio
- Crear subdominio: `ecosistema.iuriapp.com`
- Apuntar DNS al directorio del sitio
- Verificar que `index.html` esté en la raíz

## 🔧 Configuración del Servidor

### Archivo .htaccess (Opcional)
Crear archivo `.htaccess` en la raíz del sitio:

```apache
# Compression
<IfModule mod_deflate.c>
    AddOutputFilterByType DEFLATE text/plain
    AddOutputFilterByType DEFLATE text/html
    AddOutputFilterByType DEFLATE text/css
    AddOutputFilterByType DEFLATE application/javascript
</IfModule>

# Caching
<IfModule mod_expires.c>
    ExpiresActive on
    ExpiresByType text/css "access plus 1 month"
    ExpiresByType application/javascript "access plus 1 month"
    ExpiresByType text/html "access plus 1 hour"
</IfModule>

# Security
<Files ~ "^\.ht">
    Order allow,deny
    Deny from all
</Files>

# Redirects (opcional)
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
```

## 🌐 URLs de Acceso

Una vez instalado, podrás acceder a:

- **Página Principal**: `https://ecosistema.iuriapp.com`
- **Sección Productos**: `https://ecosistema.iuriapp.com#products`
- **Sección Ecosistema**: `https://ecosistema.iuriapp.com#ecosystem`
- **Sección Roadmap**: `https://ecosistema.iuriapp.com#roadmap`
- **Sección Impacto**: `https://ecosistema.iuriapp.com#impact`
- **Sección Contacto**: `https://ecosistema.iuriapp.com#contact`

## 📱 Características del Sitio

### ✅ Funcionalidades
- **Navegación Responsiva**: Mobile + Desktop
- **Scroll Suave**: Animaciones entre secciones
- **Animaciones Profesionales**: Loading effects y transiciones
- **Indicador de Progreso**: Barra de scroll
- **Contadores Animados**: Estadísticas dinámicas
- **Efectos Parallax**: En el hero section
- **Menu Móvil**: Hamburguesa para dispositivos móviles

### 🎨 Diseño
- **Glassmorphism Moderno**: Efectos de cristal
- **Gradientes Solares**: Colores coherentes con la marca
- **Tipografía Optimizada**: Legible en todos los dispositivos
- **SEO Básico**: Meta tags y estructura semántica
- **Performance Optimizado**: Carga rápida

### 📧 Contactos Configurados
- **Email**: contato@iuriapp.com
- **Web Principal**: https://iuriapp.com
- **Formulario de Contacto**: Integrado en la página

## 🔍 SEO y Optimización

### Meta Tags Incluidos
- Título optimizado para búsquedas
- Descripción atractiva
- Keywords relevantes
- Open Graph para redes sociales
- Twitter Cards

### Performance
- CSS y JS optimizados
- Imágenes comprimidas
- Lazy loading implementado
- Caché configurado

## 🛠️ Personalización

### Cambiar Colores
Editar variables CSS en `:root`:
```css
:root {
    --primary-blue: #667eea;
    --primary-purple: #764ba2;
    --accent-gold: #ffd700;
    --accent-orange: #ff8c00;
}
```

### Cambiar Contenido
- Editar texto directamente en `index.html`
- Actualizar imágenes y logos
- Modificar enlaces de contacto

### Agregar Nuevas Secciones
1. Crear nueva sección en HTML
2. Agregar enlace en navegación
3. Actualizar JavaScript si es necesario

## 📊 Analytics (Opcional)

### Google Analytics
Agregar antes de `</head>`:
```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

### Facebook Pixel
Agregar antes de `</head>`:
```html
<!-- Facebook Pixel -->
<script>
  !function(f,b,e,v,n,t,s)
  {if(f.fbq)return;n=f.fbq=function(){n.callMethod?
  n.callMethod.apply(n,arguments):n.queue.push(arguments)};
  if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
  n.queue=[];t=b.createElement(e);t.async=!0;
  t.src=v;s=b.getElementsByTagName(e)[0];
  s.parentNode.insertBefore(t,s)}(window, document,'script',
  'https://connect.facebook.net/en_US/fbevents.js');
  fbq('init', 'PIXEL_ID');
  fbq('track', 'PageView');
</script>
```

## 🚨 Solución de Problemas

### Enlaces No Funcionan
- Verificar que JavaScript esté habilitado
- Revisar consola del navegador para errores
- Asegurar que todos los IDs de sección existan

### Página No Carga
- Verificar que `index.html` esté en la raíz
- Comprobar permisos de archivos (644)
- Revisar logs del servidor

### Diseño Roto en Móvil
- Verificar viewport meta tag
- Comprobar CSS responsivo
- Testear en diferentes dispositivos

## 📞 Soporte

Para soporte técnico:
- **Email**: contato@iuriapp.com
- **Web**: https://iuriapp.com
- **Documentación**: Este README

## 🎯 Próximos Pasos

1. **Subir archivos** al servidor
2. **Configurar DNS** del subdominio
3. **Probar navegación** en diferentes dispositivos
4. **Configurar analytics** (opcional)
5. **Optimizar SEO** según necesidades
6. **Monitorear performance** con herramientas web

---

**¡Listo! Tu sitio web del ecosistema iURi estará funcionando perfectamente.** 🌞⚡🇧🇷 