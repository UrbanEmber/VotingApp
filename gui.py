from PyQt6.QtWidgets import (
    QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget,
    QPushButton, QRadioButton, QButtonGroup
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIntValidator  # Ensures numeric input for Voter ID


class VoteGUI(QMainWindow):
    """
    GUI for the voting system.
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Voting System")
        self.setGeometry(100, 100, 400, 300)

        # Central Widget and Layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Voter ID Input (Numbers Only)
        self.label_voter_id = QLabel("Enter Voter ID (Numbers Only):")
        self.layout.addWidget(self.label_voter_id)

        self.input_voter_id = QLineEdit()
        self.input_voter_id.setPlaceholderText("Voter ID")
        self.input_voter_id.setValidator(QIntValidator())  # Ensures only numbers
        self.layout.addWidget(self.input_voter_id)

        # First Name Input
        self.label_first_name = QLabel("Enter First Name:")
        self.layout.addWidget(self.label_first_name)

        self.input_first_name = QLineEdit()
        self.input_first_name.setPlaceholderText("First Name")
        self.layout.addWidget(self.input_first_name)

        # Last Name Input
        self.label_last_name = QLabel("Enter Last Name:")
        self.layout.addWidget(self.label_last_name)

        self.input_last_name = QLineEdit()
        self.input_last_name.setPlaceholderText("Last Name")
        self.layout.addWidget(self.input_last_name)

        # Candidate Selection - Radio Buttons
        self.label_select_candidate = QLabel("Select a Candidate:")
        self.layout.addWidget(self.label_select_candidate)

        self.radio_john = QRadioButton("Vote for John")
        self.radio_jane = QRadioButton("Vote for Jane")

        self.button_group = QButtonGroup()
        self.button_group.addButton(self.radio_john)
        self.button_group.addButton(self.radio_jane)

        self.layout.addWidget(self.radio_john)
        self.layout.addWidget(self.radio_jane)

        # Submit Button
        self.btn_submit = QPushButton("Submit Vote")
        self.layout.addWidget(self.btn_submit)
