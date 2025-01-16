import fitz  # PyMuPDF
from PIL import Image
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.scrollview import ScrollView
from kivy.uix.progressbar import ProgressBar
from kivy.properties import ObjectProperty
import os


def convert_pdf_to_non_editable(input_pdf, output_pdf):
    pdf_document = fitz.open(input_pdf)
    image_pages = []
    for page_number in range(len(pdf_document)):
        page = pdf_document[page_number]
        pix = page.get_pixmap(dpi=400)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        image_pages.append(img)
    pdf_document.close()
    if image_pages:
        image_pages[0].save(output_pdf, save_all=True, append_images=image_pages[1:])
    else:
        pass


class FileApp(BoxLayout):
    file_chooser = ObjectProperty(None)  # Referencia al FileChooser
    file_list = []  # Lista de archivos seleccionados

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        # Botón para seleccionar archivos
        self.add_widget(Label(text="Selecciona archivos:", size_hint=(1, 0.1)))
        self.file_chooser = FileChooserListView(
            size_hint=(1, 0.5),
            filters=["*.*"],
            multiselect=True,
            path=os.path.dirname(__file__),
        )
        self.add_widget(self.file_chooser)

        # Botón para añadir archivos seleccionados
        btn_add = Button(text="Añadir Archivos", size_hint=(1, 0.1))
        btn_add.bind(on_press=self.add_files)
        self.add_widget(btn_add)

        # Botón para seleccionar todos los archivos PDF en el directorio
        btn_select_all_pdfs = Button(
            text="Seleccionar Todos los PDFs", size_hint=(1, 0.1)
        )
        btn_select_all_pdfs.bind(on_press=self.select_all_pdfs)
        self.add_widget(btn_select_all_pdfs)

        # Área para mostrar la lista de archivos seleccionados
        self.file_display = ScrollView(size_hint=(1, 0.2))
        self.file_display_label = Label(
            size_hint_y=None, height=200, text="Archivos añadidos:\n"
        )
        self.file_display.add_widget(self.file_display_label)
        self.add_widget(self.file_display)

        # Barra de progreso
        self.progress_bar = ProgressBar(max=100, size_hint=(1, 0.1))
        self.add_widget(self.progress_bar)

        # Botón para exportar
        btn_export = Button(text="Exportar Archivos", size_hint=(1, 0.1))
        btn_export.bind(on_press=self.export_files)
        self.add_widget(btn_export)

    def add_files(self, instance):
        """Añadir archivos seleccionados a la lista."""
        selected = self.file_chooser.selection
        if selected:
            self.file_list.extend(selected)
            self.file_display_label.text += "\n".join(selected) + "\n"

    def select_all_pdfs(self, instance):
        """Seleccionar todos los archivos PDF en el directorio."""
        directory = self.file_chooser.path
        pdf_files = [
            os.path.join(directory, f)
            for f in os.listdir(directory)
            if f.lower().endswith(".pdf")
        ]
        if pdf_files:
            self.file_list.extend(pdf_files)
            self.file_display_label.text += "\n".join(pdf_files) + "\n"

    def export_files(self, instance):
        """Exportar los archivos seleccionados."""
        if self.file_list:
            output_dir = os.path.join(os.path.dirname(__file__), "output")
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            total_files = len(self.file_list)
            for index, file in enumerate(self.file_list):
                convert_pdf_to_non_editable(
                    file, os.path.join(output_dir, os.path.basename(file))
                )
                self.progress_bar.value = (index + 1) / total_files * 100
            # Aquí puedes agregar lógica para procesar o exportar los archivos.
        else:
            pass


class FileManagerApp(App):
    def build(self):
        return FileApp()


if __name__ == "__main__":
    FileManagerApp().run()
