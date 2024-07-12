import gi
from simulador import Simulador
from enfermedad import Enfermedad

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gio

class SimulacionVirus(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.ApplicationWindow.__init__(self, application=app, title="Simulación de propagación de un virus")
        # Inicializar el simulador
        self.tasa_transmision = 0.3
        self.tasa_recuperacion = 5
        self.covid = Enfermedad(self.tasa_transmision, self.tasa_recuperacion)
        self.simulador = Simulador(num_dias=50, enfermedad =self.covid)
        self.dia_actual = 0

#____________________________________________________________________________________________________________________
        # Caja principal
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.set_child(main_box)

        # Barra de encabezado
        header_bar = Gtk.HeaderBar()
        self.set_titlebar(header_bar)
        self.set_title("Simulación de propagación de un virus")

        # Menú popover
        menu = Gio.Menu.new()
        popover = Gtk.PopoverMenu()
        popover.set_menu_model(menu)

        menu_button = Gtk.MenuButton()
        menu_button.set_popover(popover)
        menu_button.set_icon_name("open-menu-symbolic")
        header_bar.pack_end(menu_button)

        # Acción para mostrar "Acerca de"
        about_action = Gio.SimpleAction.new("about", None)
        about_action.connect("activate", self.show_about_dialog)
        self.add_action(about_action)
        menu.append("Acerca de", "win.about")

        # Acción para salir
        quit_action = Gio.SimpleAction.new("quit", None)
        quit_action.connect("activate", self.on_quit_action)
        self.add_action(quit_action)
        menu.append("Salir", "win.quit")

        # Caja horizontal para los dos apartados
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        main_box.append(hbox)

#---------------------------------------------------------------------------------------------------------------
        # Apartado izquierdo: Proceso de contagio
        left_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        hbox.append(left_box)

        left_title = Gtk.Label(label="Proceso de contagio")
        left_box.append(left_title)

        self.dia_label = Gtk.Label(label="Día: 1")
        left_box.append(self.dia_label)

        self.suceptibles_label = Gtk.Label(label="Suceptibles: 0")
        left_box.append(self.suceptibles_label)

        self.infectados_label = Gtk.Label(label="Infectados: 0")
        left_box.append(self.infectados_label)

        self.recuperados_label = Gtk.Label(label="Recuperados: 0")
        left_box.append(self.recuperados_label)
#-------------------------------------------------------------------------------------
        # Separador entre los apartados
        separator = Gtk.Separator(orientation=Gtk.Orientation.VERTICAL)
        hbox.append(separator)
#--------------------------------------------------------------------------------------
        # Apartado derecho: Cálculos finales
        right_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        hbox.append(right_box)

        right_title = Gtk.Label(label="Cálculos finales de toda la comunidad")
        right_box.append(right_title)

        self.tasa_recuperacion_label = Gtk.Label(label="Tasa de recuperación: 5 días")
        right_box.append(self.tasa_recuperacion_label)

        self.tasa_transmision_label = Gtk.Label(label="Tasa de transmisión: 30%")
        right_box.append(self.tasa_transmision_label)

        self.porcentaje_no_infectados_label = Gtk.Label(label="Porcentaje de no infectados: %") # funcion calcular_suceptibles_totales
        right_box.append(self.porcentaje_no_infectados_label)

        self.porcentaje_no_recuperados_label = Gtk.Label(label="Porcentaje de no recuperados: %") #funcion calcular_infectados_totales
        right_box.append(self.porcentaje_no_recuperados_label)

        self.porcentaje_recuperados_label = Gtk.Label(label="Porcentaje de recuperados: %")#funcion calcular_recuperados_totales
        right_box.append(self.porcentaje_recuperados_label)
#_____________________________________________________________________________________________________________________
        # Botón "Día siguiente"
        self.boton_siguiente = Gtk.Button(label="Día Siguiente")
        self.boton_siguiente.connect("clicked", self.on_boton_siguiente_clicked)
        main_box.append(self.boton_siguiente)

    def on_boton_siguiente_clicked(self, widget):
        if self.dia_actual < self.simulador.num_dias:
            self.simulador.ejecutar_simulacion()
            self.actualizar_datos()
            self.dia_actual += 1
            self.dia_label.set_label(f"Día: {self.dia_actual}")
#_____________________________________________________________________________________________________________________

    def actualizar_datos(self):
        suceptibles, infectados, recuperados = self.simulador.guardar_comunidad(self.dia_actual, self.simulador.comunidad.personas)

        self.suceptibles_label.set_label(f"Suceptibles: {suceptibles}")
        self.infectados_label.set_label(f"Infectados: {infectados}")
        self.recuperados_label.set_label(f"Recuperados: {recuperados}")

        porcentaje_suceptible = self.simulador.calcular_suceptibles_totales()
        porcentaje_infectados = self.simulador.calcular_infectados_totales()
        porcentaje_recuperados = self.simulador.calcular_recuperados_totales()

        self.porcentaje_no_infectados_label.set_label(f"Porcentaje de no infectados: {porcentaje_suceptible:.2f}%")
        self.porcentaje_no_recuperados_label.set_label(f"Porcentaje de no recuperados: {porcentaje_infectados:.2f}%")
        self.porcentaje_recuperados_label.set_label(f"Porcentaje de recuperados: {porcentaje_recuperados:.2f}%")


    def show_about_dialog(self, action, param):
        about_dialog = Gtk.AboutDialog()
        about_dialog.set_transient_for(self)
        about_dialog.set_modal(True)
        about_dialog.set_program_name("Simulador")
        about_dialog.set_version("1.0")
        about_dialog.set_authors(["Antonia Rojas"])
        about_dialog.set_comments("Esta es una aplicación para simular la propagación de un virus.")
        about_dialog.run()
        about_dialog.hide()


    def on_quit_action(self, action, param):
        self.close()


class SimulacionVirusApp(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self, application_id="com.ejemplo.simulacionvirus")

    def do_activate(self):
        window = SimulacionVirus(self)
        window.present()

def main():
    app = SimulacionVirusApp()
    app.run()

if __name__ == "__main__":
    main()


