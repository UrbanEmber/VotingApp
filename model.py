import csv
import os


class VoteModel:
    """
    Handles vote tallying and records votes to a CSV file.
    """

    def __init__(self):
        self.votes = {"John": 0, "Jane": 0}
        self.filename = "votes.csv"

        # Initialize CSV file if it doesn’t exist
        if not os.path.exists(self.filename):
            self.create_csv()

    def create_csv(self):
        """
        Creates the CSV file with headers.
        """
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Voter ID", "First Name", "Last Name", "Candidate"])

    def vote(self, voter_id, first_name, last_name, candidate):
        """
        Adds a vote, records it to CSV, and updates tally.
        """
        if candidate in self.votes:
            self.votes[candidate] += 1
        else:
            raise ValueError("Invalid candidate.")

        self.record_vote(voter_id, first_name, last_name, candidate)

    def record_vote(self, voter_id, first_name, last_name, candidate):
        """
        Saves vote information into the CSV file.
        """
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([voter_id, first_name, last_name, candidate])

    def get_results(self):
        """
        Returns formatted vote results.
        """
        total_votes = sum(self.votes.values())
        return f"John - {self.votes['John']}, Jane - {self.votes['Jane']}, Total - {total_votes}"
