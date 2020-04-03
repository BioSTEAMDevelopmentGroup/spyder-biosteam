# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 01:30:45 2020

@author: yoelr
"""
from biosteam import main_flowsheet as flowsheet
from spyder.api.plugins import SpyderPluginWidget
from .widgets import FlowsheetWidget
from PyQt5.QtWidgets import QVBoxLayout
from spyder.config.base import _

__all__ = ('FlowsheetViewer',)

class FlowsheetViewer(SpyderPluginWidget):
    """A dynamic and interactive flowsheet for BioSTEAM."""
    
    CONF_SECTION = 'BioSTEAM flowsheet'
    CONF_DEFAULTS = [(CONF_SECTION, {})]
    
    def __init__(self, parent):
        SpyderPluginWidget.__init__(self, parent)
        self.main = parent
        self.flowsheet_gui = FlowsheetWidget(flowsheet)
        
        # Graphical view
        layout = QVBoxLayout(self)
        layout.addWidget(self.flowsheet_gui)
        self.setLayout(layout)
        
    # SpyderPlugin API
    def get_plugin_title(self):
        """Return widget title."""
        return _("BioSTEAM flowsheet")

    def get_plugin_icon(self):
        """Return widget icon."""
        pass

    def refresh_plugin(self):
        """Refresh flowsheet widget."""
        pass

    def register_plugin(self):
        """Register plugin in Spyder's main window."""
        self.add_dockwidget()

    def on_first_registration(self):
        """Action to be performed on first plugin registration."""
        try:
            self.main.tabify_plugins(self.main.help, self)
        except:
            self.tabify(self.main.help)

    def get_focus_widget(self):
        """Return flowsheet gui and give it focus."""
        return self.flowsheet_gui

    def get_plugin_actions(self):
        """Return plugin actions."""
        return []
        
        