# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 10:24:23 2021

@author: Johan.Dunevall
"""

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi
from qt_material import apply_stylesheet

from CoboltLaser import CoboltLaser

import sys
import json

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("commander-vachir.ui", self)
        
        with open('settings.json') as f:
                self.settings = json.load(f)
        
        self.cb_main()        
        self.laserCombo.activated.connect(self.cb_activated)
          
    def cb_main(self):
        
        self.laserCombo.addItems(self.settings['Device']['Laser'].keys())
        self.cb_activated()
    
    def cb_activated(self):
                
        self.laserSerialnumber.setText(self.settings['Device']['Laser'][self.laserCombo.currentText()]['Serialnumber'])
        self.laserMode.setText(self.settings['Device']['Laser'][self.laserCombo.currentText()]['Mode'])
        self.laserValue.setText(self.settings['Device']['Laser'][self.laserCombo.currentText()]['Value'])
        
        print(self.settings['Device']['Laser'][self.laserCombo.currentText()]['Serialnumber'])
        laser = CoboltLaser(serialnumber = self.settings['Device']['Laser'][self.laserCombo.currentText()]['Serialnumber'])
        self.laserPort.setText(laser.port)
        self.laserStatus.setText(laser.status)
        print(laser.port)
        laser.disconnect()
        
    def refresh(self):
                
        self.laserName.setText(self.settings['Device']['Laser']['06-638-MLD']['Port'])
        self.laserSerialnumber.setText(str(self.settings['Device']['Laser']['06-638-MLD']['Serialnumber']))
    
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(window)
    widget.setFixedWidth(400)
    widget.setFixedHeight(400)
    
    apply_stylesheet(app, theme='dark_teal.xml')
    
    # Run
    widget.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()