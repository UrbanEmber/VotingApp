from PyQt6.QtWidgets import QApplication, QMessageBox
from gui import VoteGUI
from model import VoteModel

class VoteController:
    """
    Connects UI interactions with vote logic.
    """
    def __init__(self) -> None:
        self.app: QApplication = QApplication([])
        self.gui: VoteGUI = VoteGUI()
        self.model: VoteModel = VoteModel()

        # Connecting the Submit Button
        self.gui.btn_submit.clicked.connect(self.cast_vote)

    def cast_vote(self) -> None:
        """
        Validates inputs and submits the vote.
        """
        voter_id: str = self.gui.input_voter_id.text().strip()
        first_name: str = self.gui.input_first_name.text().strip()
        last_name: str = self.gui.input_last_name.text().strip()
        candidate: str | None = self.get_selected_candidate()

        if not voter_id.isdigit():
            self.show_error("Invalid Voter ID! Please enter only numbers.")
            return
        if not first_name or not last_name:
            self.show_error("Name fields cannot be empty!")
            return
        if not candidate:
            self.show_error("You must select a candidate before submitting!")
            return

        try:
            self.model.vote(voter_id, first_name, last_name, candidate)
            self.gui.label_select_candidate.setText(self.model.get_results())

            QMessageBox.information(self.gui, "Vote Recorded", f"Voted for {candidate} successfully!")

            self.clear_inputs()

        except Exception as e:
            print(f"Error submitting vote: {e}")

    def get_selected_candidate(self) -> str | None:
        """
        Returns the selected candidate name.
        """
        if self.gui.radio_john.isChecked():
            return "John"
        elif self.gui.radio_jane.isChecked():
            return "Jane"
        return None

    def show_error(self, message: str) -> None:
        """
        Displays an error message dialog.
        """
        QMessageBox.critical(self.gui, "Error", message)

    def clear_inputs(self) -> None:
        """
        Clears input fields after voting.
        """
        self.gui.input_voter_id.clear()
        self.gui.input_first_name.clear()
        self.gui.input_last_name.clear()
        self.gui.radio_john.setAutoExclusive(False)
        self.gui.radio_jane.setAutoExclusive(False)
        self.gui.radio_john.setChecked(False)
        self.gui.radio_jane.setChecked(False)
        self.gui.radio_john.setAutoExclusive(True)
        self.gui.radio_jane.setAutoExclusive(True)

    def run(self) -> None:
        """
        Starts the application.
        """
        self.gui.show()
        self.app.exec()
