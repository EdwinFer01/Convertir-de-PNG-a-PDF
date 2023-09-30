from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.boxlayout import BoxLayout

class ConvertirApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        file_chooser = FileChooserListView()
        layout.add_widget(file_chooser)
        convertir_button = Button(text="Convertir PDF")
        convertir_button.bind(on_press=lambda x: self.convertir(file_chooser.path))
        layout.add_widget(convertir_button)
        return layout

    def convertir(self, carpeta_salida):
        archivo_pdf = self.root.children[0].path
        convertir_pdf_a_png(archivo_pdf, carpeta_salida)

if __name__ == '__main__':
    ConvertirApp().run()
