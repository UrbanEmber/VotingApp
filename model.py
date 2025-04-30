class VoteModel:
    """
    Handles vote tallying logic.
    """
    def __init__(self):
        self.votes = {"John": 0, "Jane": 0}

    def vote(self, candidate):
        """
        Adds a vote to the selected candidate.
        :param candidate: str ("John" or "Jane")
        """
        if candidate in self.votes:
            self.votes[candidate] += 1
        else:
            raise ValueError("Invalid candidate.")

    def get_results(self):
        """
        Returns formatted vote results.
        """
        total_votes = sum(self.votes.values())
        return f"John - {self.votes['John']}, Jane - {self.votes['Jane']}, Total - {total_votes}"
