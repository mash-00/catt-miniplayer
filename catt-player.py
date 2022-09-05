#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, gi

try:
    gi.require_version("Gtk", "3.0")
    from gi.repository import Gtk, Gdk
except:
    print('Gtk not available')
    sys.exit(1)
#try:
    #gi.require_version('Notify', '0.7')
    #from gi.repository import Notify
#except:
#    pass

class CattEntry(Gtk.Entry):
    def __init__(self):
        Gtk.Entry.__init__(self)

class CattPlayer(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Cast All the Things! - Player")
        Gtk.Window.set_default_size(self, 640, 50)
        self.set_position(Gtk.WindowPosition.CENTER)
        #Notify.init("Simple GTK3 Application")

        self.box = Gtk.Grid()
        self.add(self.box)

        self.button9 = Gtk.Button(label="Cast\n(Clipboard)")
        self.button9.set_halign(Gtk.Align.BASELINE)
        self.button9.set_valign(Gtk.Align.BASELINE)
        self.button9.connect("clicked", self.on_button9_clicked)
        self.box.add(self.button9)

        self.button10 = Gtk.Button(label="Add to queue\n(Clipboard)")
        self.button10.set_halign(Gtk.Align.BASELINE)
        self.button10.set_valign(Gtk.Align.BASELINE)
        self.button10.connect("clicked", self.on_button10_clicked)
        self.box.attach(self.button10, 1, 0, 2, 1)

        castEntry = CattEntry()
        self.box.attach_next_to(castEntry, self.button10, Gtk.PositionType.RIGHT, 1, 1)

        self.button8 = Gtk.Button(label="Cast")
        self.button8.set_halign(Gtk.Align.BASELINE)
        self.button8.set_valign(Gtk.Align.BASELINE)
        self.button8.connect("clicked", self.on_button8_clicked, castEntry)
        self.box.attach_next_to(self.button8, castEntry, Gtk.PositionType.RIGHT, 1, 1)

        self.button4 = Gtk.Button(label="Add to queue")
        self.button4.set_halign(Gtk.Align.BASELINE)
        self.button4.set_valign(Gtk.Align.BASELINE)
        self.button4.connect("clicked", self.on_button4_clicked, castEntry)
        self.box.attach_next_to(self.button4, self.button8, Gtk.PositionType.RIGHT, 2, 1)
       
        self.button = Gtk.Button(label="Play")
        self.button.set_halign(Gtk.Align.BASELINE)
        self.button.set_valign(Gtk.Align.BASELINE)
        self.button.connect("clicked", self.on_button_clicked)
        self.box.attach_next_to(self.button, self.button9, Gtk.PositionType.BOTTOM, 1, 2)

        self.button2 = Gtk.Button(label="Pause")
        self.button2.set_halign(Gtk.Align.BASELINE)
        self.button2.set_valign(Gtk.Align.BASELINE)
        self.button2.connect("clicked", self.on_button2_clicked)
        self.box.attach_next_to(self.button2, self.button, Gtk.PositionType.RIGHT, 1, 2)

        self.button3 = Gtk.Button(label="Stop")
        self.button3.set_halign(Gtk.Align.BASELINE)
        self.button3.set_valign(Gtk.Align.BASELINE)
        self.button3.connect("clicked", self.on_button3_clicked)
        self.box.attach_next_to(self.button3, self.button2, Gtk.PositionType.RIGHT, 1, 1)

        self.button5 = Gtk.Button(label="Skip/Next")
        self.button5.set_halign(Gtk.Align.BASELINE)
        self.button5.set_valign(Gtk.Align.BASELINE)
        self.button5.connect("clicked", self.on_button5_clicked)
        self.box.attach_next_to(self.button5, self.button3, Gtk.PositionType.BOTTOM, 1, 1)

        self.button6 = Gtk.Button(label="Clear queue\n(YouTube only)")
        self.button6.set_halign(Gtk.Align.BASELINE)
        self.button6.set_valign(Gtk.Align.BASELINE)
        self.button6.connect("clicked", self.on_button6_clicked)
        self.box.add(self.button6)

        self.button11 = Gtk.Button(label="Rewind\n(15s)")
        self.button11.set_halign(Gtk.Align.BASELINE)
        self.button11.set_valign(Gtk.Align.BASELINE)
        self.button11.connect("clicked", self.on_button11_clicked)
        self.box.attach_next_to(self.button11, self.button, Gtk.PositionType.BOTTOM, 1, 2)

        self.button12 = Gtk.Button(label="Forward\n(15s)")
        self.button12.set_halign(Gtk.Align.BASELINE)
        self.button12.set_valign(Gtk.Align.BASELINE)
        self.button12.connect("clicked", self.on_button12_clicked)
        self.box.attach_next_to(self.button12, self.button11, Gtk.PositionType.RIGHT, 1, 2)

        self.button13 = Gtk.Button(label="Seek\n(0)")
        self.button13.set_halign(Gtk.Align.BASELINE)
        self.button13.set_valign(Gtk.Align.BASELINE)
        self.button13.connect("clicked", self.on_button13_clicked)
        self.box.attach_next_to(self.button13, self.button12, Gtk.PositionType.RIGHT, 1, 2)

        self.button7 = Gtk.Button(label="Custom button\n(HELP)")
        self.button7.set_halign(Gtk.Align.BASELINE)
        self.button7.set_valign(Gtk.Align.BASELINE)
        self.button7.connect("clicked", self.on_button7_clicked)
        self.box.attach_next_to(self.button7, self.button5, Gtk.PositionType.RIGHT, 1, 1)

    def on_button_clicked(self, widget):
        os.system('CLI_CATT="catt "%s; /bin/bash -c "$CLI_CATT"' % ('play'))
    def on_button2_clicked(self, widget):
        os.system('CLI_CATT="catt "%s; /bin/bash -c "$CLI_CATT"' % ('pause'))
    def on_button3_clicked(self, widget):
        os.system('CLI_CATT="catt "%s; /bin/bash -c "$CLI_CATT"' % ('stop'))
    def on_button8_clicked(self, widget, data):
        url = data.get_text()
        os.system('CLI_CATT_CAST="catt cast "%s; /bin/bash -c "$CLI_CATT_CAST"' % (url))
    def on_button4_clicked(self, widget, data):
        url = data.get_text()
        os.system('CLI_CATT_ADD="catt add "%s; /bin/bash -c "$CLI_CATT_ADD"' % (url))
    def on_button5_clicked(self, widget):
        os.system('CLI_CATT="catt "%s; /bin/bash -c "$CLI_CATT"' % ('skip'))
    def on_button6_clicked(self, widget):
        os.system('CLI_CATT="catt "%s; /bin/bash -c "$CLI_CATT"' % ('clear'))
    def on_button9_clicked(self, widget):
        self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
        url = self.clipboard.wait_for_text()
        os.system('CLI_CATT_CAST="catt cast "%s; /bin/bash -c "$CLI_CATT_CAST"' % (url))
    def on_button10_clicked(self, widget):
        self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
        url = self.clipboard.wait_for_text()
        os.system('CLI_CATT_ADD="catt add "%s; /bin/bash -c "$CLI_CATT_ADD"' % (url))
    def on_button11_clicked(self, widget):
        os.system('CLI_CATT_RWND="catt rewind "%s; /bin/bash -c "$CLI_CATT_RWND"' % ('15'))
    def on_button12_clicked(self, widget):
        os.system('CLI_CATT_FFWD="catt ffwd "%s; /bin/bash -c "$CLI_CATT_FFWD"' % ('15'))
    def on_button13_clicked(self, widget):
        os.system('CLI_CATT_SEEK="catt seek "%s; /bin/bash -c "$CLI_CATT_SEEK"' % ('0'))
    def on_button7_clicked(self, widget):
        #n = Notify.Notification.new("Custom button (HELP)")
        #n.show()
        #print "Custom button (HELP)"
        os.system('CLI_CATT="catt "%s; /bin/bash -c "$CLI_CATT"' % ('--help'))

win = CattPlayer()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
