# Proyecto de Análisis de Métricas de Commits Con Arquitectura Hexagonal

Este proyecto es una API que permite analizar métricas de commits en repositorios de Git.

## Instalación de Dependencias

> [!IMPORTANT]
> Para instalar las dependencias necesarias, asegúrate de tener `pip` instalado y ejecuta el siguiente comando:

```bash
pip install -r requirements.txt
```

> [!NOTE]
> La URL para probar la api es: http://192.168.50.191:3000/analyze usando el metodo POST

Un ejemplo del cuerpo (body) de la solicitud es:
{
"repoUrl": "https://github.com/Chuch3x/Calidad_Analisis_Estatico/"
}
