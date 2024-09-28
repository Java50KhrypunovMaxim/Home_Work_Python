class GroupLimitError(Exception):
    def __init__(self, message="You cannot add more than 10 students to a group."):
        self.message = message
        super().__init__(self.message)
