from typing import Any
from django.core.management import BaseCommand
from portfolio import models
from csv import DictReader
from faker import Faker
import random

class Command(BaseCommand):
    help = "Заполняет таблицу Region данными из region_200.csv"

    def handle(self, *args: Any, **options: Any):

        fake = Faker()

        # ready
        print('Filling region table')  
        for _ in range(500):
            country = fake.country()
            models.Region.objects.create(name=country)
        print("Данные успешно импортированы в таблицу Region.")
        
        print('Filling User table') 
        for _ in range(500):
            # Generate fake user data
            username = fake.user_name()
            email = fake.email()
            password = fake.password()
            first_name = fake.first_name()
            last_name = fake.last_name()
            # Create user object
            user = models.User.objects.get_or_create(username=username,first_name=first_name,last_name=last_name,email=email, password=password)
            # Save the user object
            # user.save()
            # self.stdout.write(self.style.SUCCESS(f'Successfully created user: {username}'))
        print("Данные успешно импортированы в таблицу User.")

        print('Filling SocialNetworks table')
        all_user_data = models.User.objects.all()
        users  = random.sample(list(all_user_data), len(all_user_data))
        for _ in range (50):
            url_vk = fake.url()
            url_mailru = fake.email()
            url_gmail = fake.email()
            user = random.choice(users)
            models.SocialNetworks.objects.create(user=user, vk=url_vk, mailru=url_mailru, gmail=url_gmail)
        print("Данные успешно импортированы в таблицу SocialNetworks.")


        print('Filling Skill table') 
        with open('/home/ubuntu/OAIT/portfolio/management/commands/skill_name_200.csv', 'r', encoding='utf-8') as file:    
            csv_reader = DictReader(file)
            for row in csv_reader:
                models.Skill.objects.create(name=row['name'])
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



        print('Filling UserData table')  
        # csv_reader = DictReader(file)
        all_region_data = models.Region.objects.all()
        all_users = models.User.objects.all()
        # all_users = [user_data.user for user_data in all_user_data]
        random_users = random.sample(list(all_users), len(all_users))
        print(len(all_users))
        list_indexes = random.sample(range(0, len(all_users)), len(all_users)-5)
        for i in range (len(all_users)-10):
            random_user = random_users[i]
            random_phone =  random.randint(10000000000, 99999999999)
            random_stat =  random.randint(1, 6)
            random_region = random.choice(all_region_data)
            user_data, _ = models.UserData.objects.get_or_create(user=random_user, phone=random_phone, status=random_stat, region=random_region)
        
        
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



        print('Filling EmployerData table')
        all_region_data = models.Region.objects.all()
        all_user_data = models.UserData.objects.all()
        all_Userss_data = models.User.objects.all()
        all_social_n_data = models.User.objects.all() 
        all_users = [user_data.user for user_data in all_user_data]
        all_users_not_ordinary = []
        for i in range (len(all_Userss_data)):
            if all_Userss_data[i] not in all_users:
                all_users_not_ordinary.append(all_Userss_data[i])
        random_users = random.sample(list(all_users_not_ordinary), len(all_users_not_ordinary)-1)
        print(len(all_users_not_ordinary))
        list_indexes = random.sample(range(0,len(all_users_not_ordinary)), len(all_users_not_ordinary))
        print(max(list_indexes))
        for i in range (max(list_indexes)):
            random_user = random_users[list_indexes[i]]
            random_phone =  random.randint(10000000000, 99999999999)
            random_stat =  random.randint(1, 6)
            company = fake.company()
            random_region = random.choice(all_region_data)
            sn = random.choice(all_social_n_data)
            ver = fake.boolean()
            # user_data, _ = models.UserData.objects.get_or_create(user=random_user, phone=random_phone, status=random_stat, region=random_region)

            emp, _ = models.EmployerData.objects.get_or_create(user=random_user, name_company=company, phone=random_phone, verification=ver, region=random_region)
        
        print('Filling Review table')
        # print('Данные успешно импортированы в таблицу Emp')

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

            review, _ = models.Review.objects.get_or_create(emloyer=random_emp, user=random_user, time=fake_date, mark=mark, text=text)
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
            education, _ = models.Education.objects.get_or_create(resume=random_res, type_ed=random_type, name_institution=random_spec1, faculty=random_spec, end_year=fake_date, specialization=random_spec)
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
            chat, _ = models.Chat.objects.get_or_create(emloyer=random_emp, user=random_user, created_at=fake_date_time)
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
                random_user = random_chat.emloyer
            
            message, _ = models.Message.objects.get_or_create(created_at=fake_date_time, user=random_user, text=text, chat=random_chat)
        print("Данные успешно импортированы в таблицу Message.")

        
        print('Filling Vacancy table')
        all_emp_data = models.EmployerData.objects.all()
        all_employers = [emp_data.user for emp_data in all_emp_data]

        all_Job_data = models.JobTitle.objects.all()

        for _ in range (200):
            min_wage =  random.randint(1000, 900000)
            max_wage =  min_wage + random.randint(0, 90000)
            random_employer = random.choice(all_employers)
            random_job = random.choice(all_Job_data)
            text = fake.text(max_nb_chars = 50)
            vacancy, _= models.Vacancy.objects.get_or_create(job_title=random_job,min_wage=min_wage, max_wage=max_wage,description=text, emloyer=random_employer)
            random_vac = [models.Skill.objects.order_by('?').first() for _ in range(random.randint(0, 6))]
            vacancy.skills.add(*random_vac)
        print("Данные успешно импортированы в таблицу Vacancy.")