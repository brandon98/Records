class TestResults:
    def __init__(self):
        self.name=None
        self.score=None

record= TestResults()

record.name=input("Please enter your name:")
record.score=input("Please enter your test score:")

print("Name:",record.name)
print("Score:",record.score)
