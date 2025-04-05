import sys
import re
from PyQt5 import QtWidgets, uic, QtGui, QtCore

class FormValidationApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("week5.ui", self)

        self.genderDropdown.addItems(["      ", "Laki-laki", "Perempuan", "tidak ingin memberi tahu"])
        self.educationDropdown.addItems(["      ", "SMA", "DIPLOMA", "S1", "S2", "S3"])

        self.saveButton.clicked.connect(self.validate_form)
        self.clearButton.clicked.connect(self.clear_form)

        self.shortcut = QtWidgets.QShortcut("Q", self)
        self.shortcut.activated.connect(self.close)

        # Label untuk Identitas
        self.identityLabel = QtWidgets.QLabel("Hendra Ahmad Yani - F1D022122", self)
        self.identityLabel.setAlignment(QtCore.Qt.AlignRight)
        self.identityLabel.setStyleSheet("color: white; font-size: 10pt;")
        self.identityLabel.setGeometry(200, 320, 190, 20)

        #pemanis
        self.gradient_position = 0
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_gradient)
        self.timer.start(50) 

    def validate_form(self):
        name = self.nameInput.text().strip()
        email = self.emailInput.text().strip()
        age = self.ageInput.text().strip()
        address = self.addressInput.toPlainText().strip()
        gender = self.genderDropdown.currentText()
        education = self.educationDropdown.currentText()

        if not name or not address:
            QtWidgets.QMessageBox.warning(self, "Error Mas", "Nama & Alamat Harus diisi")
            return
        
        if not email:
            QtWidgets.QMessageBox.warning(self, "Error Mas", "isi email")
            return

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            QtWidgets.QMessageBox.warning(self, "Error Mas", "format email salah!")
            return

        if not age:
            QtWidgets.QMessageBox.warning(self, "Error Mas", "umur harus diisi!")
            return

        if not age.isdigit():
            QtWidgets.QMessageBox.warning(self, "Error Mas", "umur harus nomor!")
            return
        
        Hp = self.phoneInput.text().replace("+62", "").replace(" ", "").strip()

        if not Hp:
            QtWidgets.QMessageBox.warning(self, "Error Mas", "Nomor Hp Harus diisi!")
            return

        if len(Hp) != 10: 
            QtWidgets.QMessageBox.warning(self, "Error Mas", "Nomor Hp harus 13 digit termasuk +62!")
            return

        if not Hp.startswith("8"):
            QtWidgets.QMessageBox.warning(self, "Error Mas", "Nomor Hp harus diikuti angka '8' setelah +62!")
            return

        if gender == "      " or education == "      ":
            QtWidgets.QMessageBox.warning(self, "Error Mas", "Pilih Jenis kelamin dan Pendidikan")
            return
        
        if gender == "tidak ingin memberi tahu":
            QtWidgets.QMessageBox.warning(self, "Error Mas", "Jenis Kelamin Harus di beritahu!")
            return

        QtWidgets.QMessageBox.information(self, "Berhasil", "Data Berhasil Disimpan!")
        self.clear_form()

    def clear_form(self):
        self.nameInput.clear()
        self.emailInput.clear()
        self.ageInput.clear()
        self.phoneInput.clear()
        self.addressInput.clear()
        self.genderDropdown.setCurrentIndex(0)
        self.educationDropdown.setCurrentIndex(0)

    def update_gradient(self):
        self.gradient_position += 0.01
        if self.gradient_position > 1:
            self.gradient_position = 0
        self.update()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        rect = self.rect()
        gradient = QtGui.QLinearGradient(0, 0, rect.width(), rect.height())

        gradient.setColorAt(0.0, QtGui.QColor(255, int(100 + 100 * self.gradient_position), 200))
        gradient.setColorAt(1.0, QtGui.QColor(int(100 + 100 * self.gradient_position), 200, 255))

        painter.fillRect(rect, gradient)

app = QtWidgets.QApplication(sys.argv)
window = FormValidationApp()
window.show()
sys.exit(app.exec_())
