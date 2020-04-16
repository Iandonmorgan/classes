from companies import Company
from employees_departments import Employee

amazon = Company("Amazon", "123 Fake St.", "Global Domination")
walmart = Company("Wal-Mart", "456 Nota Real St.", "Global Domination")

mike = Employee("Mike")
michael = Employee("Michael")
bruce = Employee("Bruce")
billy = Employee("Billy")
bob = Employee("Bob")

amazon.hire(mike, "President")
walmart.hire(michael, "President")
walmart.hire(bruce, "Vice President")
amazon.hire(billy, "Vice President")
walmart.hire(bob, "Secretary")

companies = [amazon, walmart]

for company in companies:
    print(f'{company.business_name} is in the {company.industry_type} industry and has the following employees:')
    for employee in company.employees:
        print(f'* {employee.name}')
    print(f'')