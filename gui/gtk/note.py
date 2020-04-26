from gi.repository import Gtk, Gdk


class Note(Gtk.Label):
	def __init__(self, text):
		super(Note, self).__init__(text)
		self.set_line_wrap(True)
		self.get_style_context().add_class('note')
		css = Gtk.CssProvider()
		css.load_from_data(b"""
			.note {
				background-color: white;
				border-radius: 5px;
				color: #222;
				padding: .8em 1em;
				margin: 1em;
				box-shadow: 0 3px 6px rgba(0,0,0,0.4);
			}
			""")
		Gtk.StyleContext().add_provider_for_screen(Gdk.Screen.get_default(), css, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

