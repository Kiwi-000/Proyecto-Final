import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gio

class Window(Gtk.ApplicationWindow):
    def __init__(self, app):
        super().__init__(application=app, title="Simulador Propagación Enfermedad")
        
        self.set_default_size(600, 400)
        self.set_border_width(10)

        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        self.set_child(main_box)
        
        # Espacios para el avance de los días y los resultados finales
        content_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=20)
        main_box.append(content_box)

        # Espacio para el avance de los días
        self.dia_frame = Gtk.Frame(label="Día")
        dia_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        
        self.dia_label = Gtk.Label(label="DIA{dia}:")
        self.susceptibles_label = Gtk.Label(label="Suceptibles = {} ")
        self.infectados_label = Gtk.Label(label="Infectados = {}")
        self.recuperados_label = Gtk.Label(label="Recuperados = {}")
        
        dia_box.append(self.dia_label)
        dia_box.append(self.susceptibles_label)
        dia_box.append(self.infectados_label)
        dia_box.append(self.recuperados_label)
        self.dia_frame.set_child(dia_box)
        
        # Espacio para los resultados finales
        self.resultados_frame = Gtk.Frame(label="Resultados del análisis")
        resultados_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        
        self.contagios_label = Gtk.Label(label=" % CONTAGIOS = ")
        self.transmision_label = Gtk.Label(label="TASA DE TRANSMICION = ")
        self.recuperados_tasa_label = Gtk.Label(label="TASA DE RECUPERADOS = ")
        
        resultados_box.append(self.contagios_label)
        resultados_box.append(self.transmision_label)
        resultados_box.append(self.recuperados_tasa_label)
        self.resultados_frame.set_child(resultados_box)
        
        content_box.append(self.dia_frame)
        content_box.append(self.resultados_frame)
        
        # Botones
        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=20)
        
        siguiente_dia_button = Gtk.Button(label="Siguiente Día")
        siguiente_dia_button.set_size_request(150, 50)
        siguiente_dia_button.connect("clicked", self.on_siguiente_dia_clicked)
        
        resultados_button = Gtk.Button(label="Resultados")
        resultados_button.set_size_request(150, 50)
        resultados_button.connect("clicked", self.on_resultados_clicked)
        
        button_box.append(siguiente_dia_button)
        button_box.append(resultados_button)
        
        main_box.append(button_box)
    
    def on_siguiente_dia_clicked(self, widget):
        # Aquí irá la lógica para actualizar el estado del día siguiente
        pass
    
    def on_resultados_clicked(self, widget):
        # Aquí irá la lógica para mostrar los resultados del análisis
        pass

class GtkApp(Gtk.Application):
    def __init__(self):
        super().__init__(application_id='org.gtk.example')

    def do_activate(self):
        win = Window(self)
        win.present()

def main():
    app = GtkApp()
    app.run()

if __name__ == "__main__":
    main()

