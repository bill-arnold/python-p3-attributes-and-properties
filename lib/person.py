#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    approved_jobs = ["Engineer", "Doctor", "Teacher", "Artist"]

    def __init__(self, name, job):
        self._name = None  # Initialize name to None initially
        self._job = None  # Initialize job to None initially
        self.name = name  # Use the property setter for validation and title casing
        self.job = job  # Use the property setter for validation

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not 0 < len(value) < 25:
            print("Name must be a string under 25 characters.")
        else:
            self._name = value.title()  # Convert to title case before saving

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value not in self.approved_jobs:
            print("Job must be in list of approved jobs.")
        else:
            self._job = value

    pass
