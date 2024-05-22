import requests
import os
from portfolio import models
import random

class HH_API:

    URL = 'https://api.hh.ru'

    @staticmethod
    def vacancies(as_model: bool = False, **params):
        url = os.path.join(HH_API.URL, 'vacancies')
        if len(list(params.keys())):
            url += '?' + '&'.join([f'{param}={value}' for param, value in params.items()])
        respnse = requests.get(url)
        json = respnse.json()
        if as_model:
            res = []
            for vac in json.get('items', []):
                job_title, _ = models.JobTitle.objects.get_or_create(name=vac.get('name'))
                employer = models.User.objects.order_by('?').first()
                employer_data, _ = models.EmployerData.objects.get_or_create(
                    user=employer,
                    defaults={
                        'name_company': vac.get('employer', {}).get('name'),
                        'phone': str(random.randint(1000000, 999999999))
                    }
                )
                employer_data.name_company = vac.get('employer', {}).get('name')
                employer_data.save()
                res.append(models.Vacancy.objects.create(**{
                    'job_title': job_title,
                    'min_wage': (vac.get('salary') or {}).get('from'),
                    'max_wage': (vac.get('salary') or {}).get('to'),
                    'description': vac.get('name'),
                    'employer': employer,
                }))
            return res
            
        return json.get('items', [])
