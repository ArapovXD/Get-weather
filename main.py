from PyQt5 import QtCore, QtGui, QtWidgets
from interface import  Ui_Dialog
import sys
import pyowm


app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()


def get_weather(city):
        owm = pyowm.OWM('27ad7157889e4147ce58328bfb1fa56f')
        place = ui.lineEdit.text()
        mgr = owm.weather_manager()

        try:
                observation = mgr.weather_at_place(place)
                w = observation.weather
                temp = w.temperature('celsius')['temp']
                ui.label.setText(f'Температура: {temp} C')
        except:
                ui.label.setText('Территория не найдена.')

ui.pushButton.clicked.connect(get_weather)

sys.exit(app.exec_())