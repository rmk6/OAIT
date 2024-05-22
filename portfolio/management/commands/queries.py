from typing import Any
from django.core.management import BaseCommand
from portfolio import models

class Command(BaseCommand):
    
    def handle(self, *args: Any, **options: Any):
        print('------- вывод 4* отзывов о компаниях -------')
        print(str(models.Review.objects.filter(mark=models.MarkChoises.FOUR).query).replace('"', ''))

        print('\n\n------- вывод всех резюме, где в присоединенной таблице опыте работы указана конкретная профессия (название профессии) -------')
        all_expierences_with_job_titles = models.Experience.objects.filter(job_title__name='Software Developer').values_list('resume_id')
        print(str(models.Resume.objects.filter(pk__in=all_expierences_with_job_titles).query).replace('"', ''))

        # print('\n\n------- вывод всех чатов между пользователями и работадателями, для которых существует отзыв от пользователя на работадателя -------')
        # all_reviews = models.Review.objects.all()
        # all_employers_and_users = all_reviews.values_list('employer', '')