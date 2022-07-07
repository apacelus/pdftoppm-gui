import gi

from time import sleep
from os import system

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class FileChooserWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="PDF converter")
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(box)
        choose_button = Gtk.Button(label="Select pdf file")
        choose_button.connect("clicked", self.on_file_clicked)
        box.add(choose_button)

    def on_file_clicked(self, widget):
        dialog = Gtk.FileChooserDialog(title="Select pdf file", parent=self, action=Gtk.FileChooserAction.OPEN)
        dialog.add_buttons(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OPEN, Gtk.ResponseType.OK)
        filter_pdf = Gtk.FileFilter()
        filter_pdf.set_name(".pdf")
        filter_pdf.add_mime_type("application/pdf")
        dialog.add_filter(filter_pdf)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            print("File selected: " + dialog.get_filename())
            self.on_folder_clicked(dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")
            exit()
        dialog.destroy()

    def on_folder_clicked(self, pdf_location):
        dialog = Gtk.FileChooserDialog(title="Extract to", parent=self, action=Gtk.FileChooserAction.SELECT_FOLDER)
        dialog.add_buttons(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, "Select", Gtk.ResponseType.OK)
        dialog.set_default_size(800, 400)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Select clicked")
            print("Folder selected: " + dialog.get_filename())
            folder_path = dialog.get_filename()
            system('pdftoppm "' + pdf_location + '" "' + dialog.get_filename() + "/" + pdf_location.split("/")[
                -1] + '" -png')
            info_dialog = Gtk.MessageDialog(transient_for=self, flags=0, message_type=Gtk.MessageType.INFO,
                                            buttons=Gtk.ButtonsType.OK, text="Extraction completed")
            info_dialog.run()
            exit()
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")
            exit()
        dialog.destroy()


win = FileChooserWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
