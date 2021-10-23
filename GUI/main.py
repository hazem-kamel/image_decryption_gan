import sys
# from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QFileDialog
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
from Face_Recognition.FaceRecognizer import FaceRecognizer
from Face_Recognition.FaceRecognizer import BrowserDataBase
import time
from PyQt5.QtTest import QTest
import os

class FaceRecognition(QDialog):
    def __init__(self):
        super(FaceRecognition, self).__init__()
        loadUi('main-ui.ui', self)
        self.person_not_recognized_label.hide()
        self.x_label.hide()
        self.person_recognized_label.hide()
        self.person_name_label.hide()
        self.button_data.hide()
        self.button_validation.clicked.connect(self.uploadValidationImage)
        # self.button_data.clicked.connect(self.uploadDataImage)

    def uploadValidationImage(self):
        image_valid_name = QFileDialog.getOpenFileName(self, 'Open File', 'c\\', 'Image files (*.jpg *.jp2)')
        self.image_valid_path = image_valid_name[0]
        pixmap_valid = QPixmap(self.image_valid_path)
        self.image_validation.setPixmap(QPixmap(pixmap_valid))
        self.image_validation.setScaledContents(True);
        found=self.uploadDataImage()
    def doAction(self,num):
        self.progressBar.setValue(num)
    def uploadDataImage(self):
        # print('upload data')
        # image_data_name = QFileDialog.getOpenFileName(self, 'Open File', 'c\\', 'Image files (*.jpg *.jp2)')
        # image_data_path = image_data_name[0]
        # pixmap_data = QPixmap(image_data_path)
        # self.image_data.setPixmap(QPixmap(pixmap_data))
        # FaceRecognizer(self.image_valid_path,image_data_path)
        # self.image_data.clear()
        # pixmap_data = QPixmap('C:/Users/ROG/Desktop/Masters/Semester3/Biometric Systems/Project/Datasets/CASIA-WebFace/images/490624/490624_1.jpg')
        # self.image_data.setPixmap(QPixmap(pixmap_data))
        os.chdir(sys.path[1] + '\Datasets\CASIA-WebFace\images')
        rootdir = os.getcwd()
        found = False
        num = 0
        while not found:
            for subdir, dirs, files in os.walk(rootdir):
                os.chdir(subdir)
                for file in files:
                    state = BrowserDataBase(self.image_valid_path, file, subdir)
                    img_string = file.replace("\\", "/")
                    QTest.qWait(50)
                    self.image_data.clear()
                    pixmap_data = QPixmap(img_string)
                    self.image_data.setPixmap(QPixmap(pixmap_data))
                    # num = num+1
                    # self.doAction(num)
                    found = state
                    if(state == True):
                        self.person_recognized_label.show()
                        return found



# Main
app = QApplication(sys.argv)
FaceApp = FaceRecognition()
widget = QWidget(FaceApp)
FaceApp.setFixedWidth(1126)
FaceApp.setFixedHeight(873)
# widget.show()
FaceApp.show()
sys.exit(app.exec_())
try:
    sys.exit(app.exec())

except:
    print('Exiting')
