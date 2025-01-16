# Instrucciones de uso:

1. Navega a la carpeta deseada.
2. Selecciona los archivos PDF que deseas manipular.
3. Haz clic en "Importar".
4. Se generará una carpeta `output` con los nuevos archivos no editables.


# Proyecto PDFs

Este proyecto permite la gestión y manipulación de archivos PDF.

## Requisitos

- Python 3.x
- Librerías necesarias (pueden ser instaladas con `pip`):
  - PyPDF2
  - reportlab

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/proyecto-pdfs.git
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd proyecto-pdfs
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

### Combinar PDFs

Para combinar varios archivos PDF en uno solo, usa el siguiente comando:
```bash
python combinar_pdfs.py archivo1.pdf archivo2.pdf archivo_salida.pdf
```

### Dividir PDF

Para dividir un archivo PDF en páginas individuales, usa el siguiente comando:
```bash
python dividir_pdf.py archivo.pdf
```

### Agregar Marca de Agua

Para agregar una marca de agua a un archivo PDF, usa el siguiente comando:
```bash
python agregar_marca_agua.py archivo.pdf marca_agua.pdf archivo_salida.pdf
```

## Contribuir

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Agrega nueva funcionalidad'`).
4. Sube tus cambios a tu fork (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
