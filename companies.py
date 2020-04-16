from employees_departments import Employee

class Company:
    def __init__(self, business_name, address, industry_type):
        self.business_name = business_name
        self.address = address
        self.industry_type = industry_type
        self.employees = list()
    
    def hire(self, employee, jobtitle):
        Employee.hired(employee, jobtitle)
        self.employees.append(employee)