class Payslip:
    def __init__(self):
        self.name=None
        self.number=None
        self.hours=None
        self.payRate=None

record= Payslip()

print("Pay Slip Generator")

record.name=input("Please enter the employees name:")
record.number=int(input("Please enter the employees number:"))
record.hours=int(input("Please enter the amount of hours worked:"))
record.payRate=float(input("Please enter the pay rate:"))
total = record.hours * record.payRate
print("Name:", record.name)
print("Employee number:", record.number)

print("Hours worked:",record.hours)
print("Pay rate:", record.payRate)
print("Total pay:", total)
     


