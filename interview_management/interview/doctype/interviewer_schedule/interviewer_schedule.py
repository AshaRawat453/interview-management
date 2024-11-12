# Copyright (c) 2024, asha rawat and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from frappe.utils import today  
import frappe


class interviewerschedule(Document):
    def validate(self):
        current_date = today()  
        if self.interview_date < current_date:
            frappe.throw("Select the current date")
    
    def after_delete(self):
        frappe.msgprint(f"Deleted the record {self.name} from {self.doctype} successfully.")

    def onload(self):
        frappe.msgprint(f"you are viewing {self.name} doctument from {self.doctype}.")

        
	
            
# from frappe.model.document import Document
# import frappe
# from frappe.utils import today

# class InterviewSchedule(Document):
#     def validate(self):
#         current_date = today()

#         if self.interview_date < current_date:
#             frappe.throw("Please select a valid interview date. The date cannot be in the past.")
    
#     def before_delete(self):
#         frappe.throw("Are you sure you want to delete this record?")
    
#     def after_delete(self):
#         frappe.msgprint(f"Deleted the record {self.name} from {self.doctype} successfully.")