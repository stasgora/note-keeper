from gi.repository import Gtk

from common.about import get_about_text


class GtkAboutPopup(Gtk.Dialog):
	def __init__(self, parent):
		Gtk.Dialog.__init__(self, 'O programie', parent, 0)
		self.set_default_size(400, 300)

		layout = self.get_content_area()
		label = Gtk.Label()
		label.set_line_wrap(True)
		label.set_xalign(0)
		label.get_style_context().add_class('about-field')
		label.set_text(get_about_text())
		layout.add(label)
		self.show_all()
