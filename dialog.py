from PySide6.QtWidgets import QDialog, QSlider, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QDialogButtonBox, QComboBox, QFileDialog, QFontDialog, QStatusBar, QInputDialog
from PySide6.QtGui import QFont

class Dialog_Slider(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Slider (QDialog)")
        label = QLabel("Slider:")

        slider = QSlider()
        slider.setMinimum(0)
        slider.setMaximum(100)
        slider.setValue(50)

        self.value = 0
        slider.valueChanged.connect(self.slider_vaule)

        ok_button = QPushButton("Ok")
        ok_button.clicked.connect(self.accept)
        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.reject)

        h_button_layout = QHBoxLayout()
        h_button_layout.addWidget(ok_button)
        h_button_layout.addWidget(cancel_button)

        v_layout = QVBoxLayout()
        v_layout.addWidget(label)
        v_layout.addWidget(slider)
        v_layout.addLayout(h_button_layout)

        self.setLayout(v_layout)

    def slider_vaule(self, value):
        self.value = value



class Dialog_Combo(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ComboBox (QDialog w/ QDialogButtonBox)")

        items = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        self.combo_box = QComboBox()
        for i in items:
            self.combo_box.addItem(i)

        self.selected_item = 'January'
        self.combo_box.currentTextChanged.connect(self.current_text)


        self.dialog_button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.dialog_button_box.clicked.connect(self.dialog_button)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.combo_box)
        v_layout.addWidget(self.dialog_button_box)
        self.setLayout(v_layout)

    def current_text(self, curr_text):
        self.selected_item = curr_text

    def dialog_button(self, button):
        std_button = self.dialog_button_box.standardButton(button)
        if std_button == QDialogButtonBox.Ok:
            self.accept()
        elif std_button == QDialogButtonBox.Cancel:
            self.reject()

class Dialog_File(QFileDialog):
    def get_existing_directory(self):
        dir = QFileDialog.getExistingDirectory(self, "Select Directory", "/home")
        if dir == '':
            print("No directory selected")
        else:
            print(f"Directory: {dir}")
    
    def get_open_file_name(self):
        file_name,_ = QFileDialog.getOpenFileName(self, "Select File", "/home", "Images (*.png *.jpg);;All Files (*.*)")
        if file_name == '':
            print("No file selected")
        else:
            print(f"File: {file_name}")

    def get_open_file_names(self):
        file_names,_ = QFileDialog.getOpenFileNames(self, "Select files", "/home", "Images (*.png *.jpg);;All files (*.*)")
        if not file_names == '':
            for f in file_names:
                print(f"File: {f}")


    def get_save_file_name(self):
        file_name,_ = QFileDialog.getSaveFileName(self, "Save File", "/home", "Images (*png *.jpg);;All Files (*.*)")
        if file_name == '':
            print("No location selected")
        else:
            print(f"Saved as: {file_name}")
    
class Font_Dialog(QFontDialog):
    def __init__(self):
        super().__init__()
        self.status_bar = QStatusBar()
    def get_font(self):
        ok, font = QFontDialog.getFont(QFont("Arial", 12), self)
        if ok:
            txt = self.status_bar.showMessage("Test your font", 10000)
            self.status_bar.setFont(font)
        else:
            print("No font selected")

class Input_Dialog(QInputDialog):
    def get_int(self):
        val,ok = QInputDialog.getInt(self, "getInt", "Enter value:", 25, -100, 100)
        if ok:
            print(f"Value: {val}")
        else:
            print("No value entered")
    
    def get_double(self):
        val,ok = QInputDialog.getDouble(self, "getDouble", "Enter vaule:", 50, 0, 100)
        if ok:
            print(f"Value: {val}")
        else:
            print("No value entered")
    
    def get_text(self):
        txt,ok = QInputDialog.getText(self, "getText", "Your text:")
        if ok and not txt =='':
            print(f"Your input: {txt}")
        else:
            print("No valid input")
    
    def get_item(self):
        items = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        item,ok = QInputDialog.getItem(self, "getItem", "Select item: ", items)
        if ok:
            print(f"Your item: {item}")
        else:
            print("No valid input")