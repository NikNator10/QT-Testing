from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QSizePolicy, QDialog
from dialog import Dialog_Slider, Dialog_Combo, Dialog_File, Font_Dialog, Input_Dialog

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dialog - Summary")
        self.resize(375, 75)

        self.s_dialog = Dialog_Slider()
        slider_button = QPushButton("Slider (QDialog)")
        slider_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        slider_button.clicked.connect(self.slider_dialog)

        self.c_dialog = Dialog_Combo()
        dialog_bb_button = QPushButton("ComboBox (QDialog w/ QDialogButtonBox)")
        dialog_bb_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        dialog_bb_button.clicked.connect(self.combo_dialog)

        self.file_dialog = Dialog_File()
        get_existing_directory_button = QPushButton("getExistingDirectory (QFileDialog)")
        get_existing_directory_button.clicked.connect(self.file_dialog.get_existing_directory)
        get_open_file_name_button = QPushButton("getOpenFileName (QFileDialog)")
        get_open_file_name_button.clicked.connect(self.file_dialog.get_open_file_name)
        get_open_file_names_button = QPushButton("getOpenFileNames (QFileDialog)")
        get_open_file_names_button.clicked.connect(self.file_dialog.get_open_file_names)
        get_save_file_name_button = QPushButton("getSaveFileName (QFileDialog)")
        get_save_file_name_button.clicked.connect(self.file_dialog.get_save_file_name)
        

        self.font_dialog = Font_Dialog()
        get_font_button = QPushButton("getFont (QFontDialog)")
        get_font_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        get_font_button.clicked.connect(self.font_dialog.get_font)

        self.input_dialog = Input_Dialog()
        get_int_button = QPushButton("getInt (QInputDialog)")
        get_int_button.clicked.connect(self.input_dialog.get_int)
        get_double_button = QPushButton("getDouble (QInputDialog)")
        get_double_button.clicked.connect(self.input_dialog.get_double)
        get_text_button = QPushButton("getText (QInputDialog)")
        get_text_button.clicked.connect(self.input_dialog.get_text)
        get_item_button = QPushButton("getItem (QInputDiaolg)")
        get_item_button.clicked.connect(self.input_dialog.get_item)

        v_file_layout = QVBoxLayout()
        v_file_layout.addWidget(get_existing_directory_button)
        v_file_layout.addWidget(get_open_file_name_button)
        v_file_layout.addWidget(get_open_file_names_button)
        v_file_layout.addWidget(get_save_file_name_button)

        v_input_layout = QVBoxLayout()
        v_input_layout.addWidget(get_int_button)
        v_input_layout.addWidget(get_double_button)
        v_input_layout.addWidget(get_text_button)
        v_input_layout.addWidget(get_item_button)

        h_button_layout = QHBoxLayout()
        h_button_layout.addWidget(slider_button)
        h_button_layout.addWidget(dialog_bb_button)
        h_button_layout.addLayout(v_file_layout)
        h_button_layout.addWidget(get_font_button)
        h_button_layout.addLayout(v_input_layout)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_button_layout)
        v_layout.addWidget(self.font_dialog.status_bar)
        self.setLayout(v_layout)

    def slider_dialog(self):
        ret = self.s_dialog.exec()
        if ret == QDialog.Accepted:
            print(f"Slider value: {self.s_dialog.value}")
        else:
            print("No valid input")

    def combo_dialog(self):
        ret = self.c_dialog.exec()
        if ret == QDialog.Accepted:
            print(f"Selected: {self.c_dialog.selected_item}")
        else:
            print("Nothing selected")