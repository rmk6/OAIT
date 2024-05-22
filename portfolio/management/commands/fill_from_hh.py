from typing import Any
from django.core.management import BaseCommand
from portfolio.hh_api import HH_API
from portfolio import models

class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any):
        created_vacancies = HH_API.vacancies(as_model=True)
        for vacancy in created_vacancies:
            vacancy: models.Vacancy
            print('Vacancy name:', vacancy.job_title.name)
            print('Eployer:', vacancy.employer.employerdata.name_company)
            print('Salary:', vacancy.min_wage, '-', vacancy.max_wage)
            print('\n')
        