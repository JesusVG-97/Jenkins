
# 📦 RA5.1 - Jenkins + CI/CD + Docker

Este repositorio contiene el desarrollo completo de la práctica **RA5.1** de la asignatura *Ciberseguridad en entornos de las tecnologías de la información*, centrada en la **implantación segura de pipelines CI/CD usando Jenkins y Docker**.

---

## 🧾 Descripción de la práctica

La actividad consiste en:

1. Crear una pipeline Jenkins (`Jenkinsfile`) que:
   - Clona el repositorio desde GitHub.
   - Instala dependencias.
   - Ejecuta tests automatizados escritos en Python.

2. Crear una segunda pipeline (`Jenkinsfile.docker`) que:
   - Construye una imagen Docker.
   - Ejecuta un contenedor basado en esa imagen.
   - Lanza las pruebas dentro del contenedor.
   - Automatiza todo esto con `docker-compose`.

---

## 🗂️ Estructura del repositorio

```
Jenkins/
├── python/
│   ├── calculadora.py            # Código fuente de la aplicación (calculadora)
│   └── test_calculadora.py       # Tests automatizados con pytest
├── Jenkinsfile                   # Pipeline Jenkins sin Docker
├── Jenkinsfile.docker            # Pipeline Jenkins usando Docker y Docker Compose
├── Dockerfile                    # Imagen Docker para ejecutar la app
├── docker-compose.yml            # Entorno Docker para ejecutar la app y pruebas
└── README.md                     # Explicación del proyecto
```

---

## ⚙️ Requisitos previos

- Jenkins instalado localmente o en un contenedor Docker.
- Docker y Docker Compose instalados.
- Python 3.10+ (si ejecutas localmente).
- GitHub (repositorio privado o público con esta estructura).

---

## 🚀 Pipeline 1: Jenkinsfile

Este pipeline realiza la ejecución **sin Docker**, directamente en el agente Jenkins.

### 🔧 Etapas

1. Clona el repositorio desde GitHub.
2. Instala `pytest`.
3. Ejecuta las pruebas en el directorio `python`.

### 📍Configuración

En Jenkins:

- Crear un nuevo proyecto tipo **Pipeline**.
- En “Pipeline script from SCM”:
  - SCM: Git
  - URL del repositorio: `https://github.com/TU_USUARIO/ACT_RA5_1-Jenkins.git`
  - Script Path: `Jenkinsfile`

---

## 🐳 Pipeline 2: Jenkinsfile.docker

Esta pipeline utiliza Docker y Docker Compose para automatizar todo el entorno.

### 🔧 Etapas

1. Construye una imagen Docker usando el `Dockerfile`.
2. Ejecuta un contenedor que lanza las pruebas con `pytest`.
3. Ejecuta `docker-compose` para levantar el entorno completo.

### 📍Configuración

Igual que la anterior, pero usando `Jenkinsfile.docker` en el campo `Script Path`.

---

## 🔬 Pruebas automatizadas

Las pruebas están definidas en `python/test_calculadora.py` e incluyen:

- Suma
- Resta
- Multiplicación
- División
- División por cero (con manejo de excepciones)

Framework utilizado: **pytest**

---

---

## 🧑‍💻 Autor

**Jesús Valverde Galí**  
Usuario GitHub: `@JesusVG-97`

---

## 📚 Referencias

- [Jenkins Oficial](https://www.jenkins.io)
- [CI/CD con Docker en Jenkins](https://www.jenkins.io/doc/book/pipeline/docker/)
- [Guía de práctica - Ciberseguridad PePS](https://psegarrac.github.io/Ciberseguridad-PePS/tema5/cd/ci/2022/01/13/jenkins.html#tareas)

---
