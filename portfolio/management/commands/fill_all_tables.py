from typing import Any
from django.core.management import BaseCommand
from portfolio import models
from csv import DictReader
from faker import Faker
import random
from faker_education import SchoolProvider

class Command(BaseCommand):
    help = "Заполняет таблицу Region данными из region_200.csv"

    def clear_all_tables(self):
        all_models = [
            models.Region,
            models.UserData,
            models.Vacancy,
            models.Skill,
            models.Country,
            models.Resume,
            models.Review,
            models.Specialization,
            models.JobTitle,
            models.Education,
            models.Experience,
            models.SocialNetworks,
            models.EmployerData,
            models.Chat,
            models.Message,
        ]

        for model_class in all_models:
            model_class.objects.all().delete()
        models.User.objects.filter(is_superuser=False).delete()


    def handle(self, *args: Any, **options: Any):

        fake = Faker()
        fake.add_provider(SchoolProvider)
        
        # ready
        self.clear_all_tables()
        print('--------- ALL DATA CLEARED ----------')
        print('Filling region table')  
        for _ in range(500):
            city = fake.city()
            models.Region.objects.get_or_create(name=city)
        print("Данные успешно импортированы в таблицу Region.")
        
        print('Filling User table') 
        for _ in range(1500):
            # Generate fake user data
            username = fake.user_name()
            email = fake.email()
            first_name = fake.first_name()
            last_name = fake.last_name()
            # Create user object
            models.User.objects.get_or_create(
                username=username, 
                defaults=dict(first_name=first_name,last_name=last_name,email=email)
            )
            
        print("Данные успешно импортированы в таблицу User.")

        print('Filling SocialNetworks table')
        all_user_data = models.User.objects.all()
        users  = random.sample(list(all_user_data), len(all_user_data))
        for _ in range (50):
            url_vk = fake.url()
            url_mailru = fake.email()
            url_gmail = fake.email()
            user = random.choice(users)
            models.SocialNetworks.objects.get_or_create(
                user=user,
                defaults=dict(vk=url_vk, mailru=url_mailru, gmail=url_gmail)
            )
        print("Данные успешно импортированы в таблицу SocialNetworks.")


        print('Filling Skill table') 
        with open('/home/ubuntu/OAIT/portfolio/management/commands/skill_name_200.csv', 'r', encoding='utf-8') as file:    
            csv_reader = DictReader(file)
            for row in csv_reader:
                models.Skill.objects.get_or_create(name=row['name'])
        print("Данные успешно импортированы в таблицу Skill.")   

        print('Filling Country table') #ready
        for _ in range(200):
            country = fake.country()
            c, _= models.Country.objects.get_or_create(name=country)
        print("Данные успешно импортированы в таблицу Country.")

        print('Filling Specialization table')#ready
        with open('/home/ubuntu/OAIT/portfolio/management/commands/job_titles_name_200.csv', 'r', encoding='utf-8') as file:    
            csv_reader = DictReader(file)
            for row in csv_reader:
                specialization, _ =  models.Specialization.objects.get_or_create(name=row['name'])
        print("Данные успешно импортированы в таблицу Specialization.")
        
        print('Filling JobTitle table')#ready
        with open('/home/ubuntu/OAIT/portfolio/management/commands/job_titles_name_200.csv', 'r', encoding='utf-8') as file:   
            csv_reader = DictReader(file)
            for row in csv_reader:   
                JobTitle, _ = models.JobTitle.objects.get_or_create(name=row['name'])
        print("Данные успешно импортированы в таблицу JobTitle.")

        print('Filling EmployerData table')
        all_users = models.User.objects.all()
        
        simple_users = all_users[:int(all_users.count() / 2)]
        employers_users = all_users[int(all_users.count() / 2):]
        all_region_data = models.Region.objects.all()
        for employer_user in employers_users:
            
            random_phone = random.randint(10000000000, 99999999999)
            random_stat = random.randint(1, 6)
            company = fake.company()
            random_region = random.choice(all_region_data)
            ver = fake.boolean()
            emp, _ = models.EmployerData.objects.get_or_create(user=employer_user, name_company=company, phone=random_phone, verification=ver, region=random_region)
        
        print('Filling Review table')
        all_emp_data = models.EmployerData.objects.all()
        all_employers = [emp_data.user for emp_data in all_emp_data]

        for emp_user in random.sample(all_employers, k=random.randint(200, len(all_employers) - 1)):
            models.Review.objects.get_or_create(
                employer=emp_user,
                user=random.choice(list(simple_users)),
                defaults=dict(
                    mark=random.randint(0, 5),
                    text=fake.text()
                )
            )

        print('Данные успешно импортированы в таблицу Review')


        print('Filling Vacancy table')
        all_Job_data = models.JobTitle.objects.all()

        for _ in range (200):
            min_wage =  random.randint(1000, 900000)
      
      
            max_wage =  min_wage + random.randint(0, 90000)
            random_employer = random.choice(all_employers)
            random_job = random.choice(all_Job_data)
            text = fake.text(max_nb_chars = 50)
            vacancy, _= models.Vacancy.objects.get_or_create(
                job_title=random_job,
                employer=random_employer,
                defaults=dict(min_wage=min_wage, max_wage=max_wage,description=text)
            )
            random_vac = [models.Skill.objects.order_by('?').first() for _ in range(random.randint(0, 6))]
            vacancy.skills.add(*random_vac)
        print("Данные успешно импортированы в таблицу Vacancy.")

        print('Filling UserData table')  
        # csv_reader = DictReader(file)
        all_region_data = models.Region.objects.all()
        
        print(len(all_users))

        for simple_user in simple_users:
            random_phone =  random.randint(10000000000, 99999999999)
            random_stat =  random.randint(1, 6)
            random_region = random.choice(all_region_data)
            user_data, _ = models.UserData.objects.get_or_create(user=simple_user, phone=random_phone, status=random_stat, region=random_region)

            random_vac = [models.Vacancy.objects.order_by('?').first() for _ in range(random.randint(0, 6))]
            user_data.vacancies.add(*random_vac)
        print("Данные успешно импортированы в таблицу UserData.")
                    
        
        print('Filling Resume table')
        all_user_data = models.UserData.objects.all()
        all_users = [user_data.user for user_data in all_user_data]
        all_countries_data=models.Country.objects.all()
        for _ in range(200):
            random_user = random.choice(all_users)
            first_name = fake.first_name()
            last_name = fake.last_name()
            random_phone =  random.randint(10000000000, 99999999999)
            citizenship = random.choice(all_countries_data)
            sex = random.randint(1, 4)

            resume_data, _ = models.Resume.objects.get_or_create(user=random_user, first_name=first_name, last_name=last_name, sex = sex,phone=random_phone,citizenship1=citizenship)

            random_vac = [models.Skill.objects.order_by('?').first() for _ in range(random.randint(0, 6))]
            resume_data.skills.add(*random_vac)

            i = random.randint(0,2)
            if i ==1:
                citizenship2 = random.choice(all_countries_data) 
                resume_data.citizenship2 = citizenship2
                resume_data.save()

                j = random.randint(0,2)
                if j ==1:
                    citizenship3 = random.choice(all_countries_data)
                    resume_data.citizenship3 = citizenship3
                    resume_data.save()
        print("Данные успешно импортированы в таблицу Resume.")


        print('Filling Review table')
        all_user_data = models.UserData.objects.all()
        all_users = [user_data.user for user_data in all_user_data]
            
        all_emp_data = models.EmployerData.objects.all()
        all_employers = [emp_data.user for emp_data in all_emp_data]

        for _ in range (50):
            random_user = random.choice(all_users)
            random_emp = random.choice(all_employers)
            fake_date = fake.date_time_between(start_date="-20y", end_date="now")
            mark =  random.randint(1, 6)
            text = fake.text(max_nb_chars=50)

            review, _ = models.Review.objects.get_or_create(employer=random_emp, user=random_user, time=fake_date, mark=mark, text=text)
        print("Данные успешно импортированы в таблицу Review.")


        print('Filling Education table')
        all_spec_data = models.Specialization.objects.all()
        all_res_data = models.Resume.objects.all()
        for _ in range(50):
            random_type = random.randint(1, 9)
            fake_date = fake.date_time_between(start_date="-20y", end_date="now")
            random_spec = random.choice(all_spec_data)
            random_spec1 = random.choice(all_spec_data)
            random_res = random.choice(all_res_data)
            fake.state()
            education, _ = models.Education.objects.get_or_create(
                resume=random_res, 
                type_ed=random_type, 
                name_institution=fake.school_name(), 
                faculty=random_spec, 
                end_year=fake_date, 
                specialization=random_spec
            )
        print("Данные успешно импортированы в таблицу Education.")

        print('Filling Experience table')
        all_res_data = models.Resume.objects.all()
        all_job_data = models.JobTitle.objects.all()
        all_emp_data = models.EmployerData.objects.all()
        all_comp = [emp_data.name_company for emp_data in all_emp_data]

        for _ in range(50):
            random_res = random.choice(all_res_data)
            random_job = random.choice(all_job_data)
            random_name_comp = random.choice(all_comp)

            fake_date = fake.date_time_between(start_date="-20y", end_date="now")
            fake_date1 = fake.date_time_between(start_date="-20y", end_date="now")

            text = fake.text(max_nb_chars=50)
            random_res = random.choice(all_res_data)
            exp, _ = models.Experience.objects.get_or_create(resume=random_res, name_company=random_name_comp, text=text, date_begin=fake_date, date_end=fake_date1, job_title=random_job)
        print("Данные успешно импортированы в таблицу Experience.")
        
        print('Filling Chat table')
        all_emp_data = models.EmployerData.objects.all()
        all_emp = [emp_data.user for emp_data in all_emp_data]
        all_user_data = models.UserData.objects.all()
        all_users = [user_data.user for user_data in all_user_data]
        for _ in range (100):
            random_user = random.choice(all_users)
            random_emp = random.choice(all_emp)
            fake_date_time = fake.date_time_between(start_date="-20y",end_date="now")
            chat, _ = models.Chat.objects.get_or_create(employer=random_emp, user=random_user, created_at=fake_date_time)
        print("Данные успешно импортированы в таблицу Chat.")

        print('Filling Message table')
        all_chats_data = models.Chat.objects.all()
        for _ in range (100):
            random_chat = random.choice(all_chats_data)
            text = fake.text(max_nb_chars=50)

            i = random.randint(0,1)
            if i == 1:
                random_user = random_chat.user
            else:
                random_user = random_chat.employer
            
            message, _ = models.Message.objects.get_or_create(created_at=fake_date_time, user=random_user, text=text, chat=random_chat)
        print("Данные успешно импортированы в таблицу Message.")


        for i, user in enumerate(models.User.objects.filter(is_superuser=False)):
            password = fake.password()
            print(f'Setting password of {i + 1}/{models.User.objects.filter(is_superuser=False).count()}')
            user.set_password(password)
            user.save()