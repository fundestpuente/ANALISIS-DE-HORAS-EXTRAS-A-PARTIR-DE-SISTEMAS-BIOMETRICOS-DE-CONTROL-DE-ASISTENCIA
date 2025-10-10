# ANALISIS DE HORAS EXTRAS A PARTIR DE SISTEMAS BIOMETRICOS DE CONTROL DE ASISTENCIA

**Curso:** Samsung Innovation Campus – Módulo de Python (Ecuador 2025)  
**Seccion:** EC-04

## 👥 Colaboradores
- Esteban Quiña
- Ulices Chingo 
- Alan Palma
- Brayan Maisincho
- Sofia Feijóo

---

## Descripción del Proyecto
Este proyecto automatiza el cálculo de horas extras a partir de datos obtenidos de relojes biométricos, resolviendo el problema del procesamiento manual y los errores en la nómina.
Su objetivo principal es generar reportes precisos y rápidos que garanticen pagos justos y cumplimiento laboral. Siendo los principales beneficiarios el departamento de recursos humanos y los empleados de la empresa.

---

## ⚙️ Instrucciones de Instalación y Ejecución

### Requisitos
- Python 3.9+ (recomendado)
- Git

### Pasos
1. Clonar el repositorio:
   ```bash
   git clone <https://github.com/fundestpuente/ANALISIS-DE-HORAS-EXTRAS-A-PARTIR-DE-SISTEMAS-BIOMETRICOS-DE-CONTROL-DE-ASISTENCIA.git>
   cd <ruta/al/proyecto>   # ej: cd ecuador04/proyecto
   ```
2. Abrir ```análisis.ipynb```, aquí se ejemplifica el uso del código. 
---

## 📂 Estructura del Código
```
ANALISIS-DE-HORAS-EXTRAS-A-PARTIR-DE-SISTEMAS-BIOMETRICOS-DE-CONTROL-DE-ASISTENCIA/
│
├── README.md 
├── analisis.ipybn            
├── src/                
│   ├── horas_extras.py
│   ├── procesamiento.py
│   ├── reporte.py
│   └── README.md
├── data/                  
│   ├── feriados_2024.csv
│   ├── miscelaneosmarzo2024.csv
│   ├── miscelaneosabril2024.csv
│   ├── miscelaneosmayo2024.csv
│   └── miscelaneosjunio2024.csv
├── output_data/                  
│   ├── reporte_horas_extras_marzo2024.csv
│   ├── reporte_horas_extras_abril2024.csv
│   ├── reporte_horas_extras_mayo2024.csv
│   └── reporte_horas_extras_junio2024.csv
└── .gitignore
```

---

## ✅ Herramientas Implementadas
- **Lenguaje:** Python 3.9
- **Librerías principales:** `pandas, datetime, numpy, matplotlib `
- **Otras herramientas:** ` GitHub Actions (CI)` 

