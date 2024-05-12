from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserDataStatuses(models.IntegerChoices):
    ACITVE = 1, 'принимает предложения'
    SEARCHING = 2, 'в активном поиске'
    BUSY = 3, 'не рассматривает предложения'

class SexChoises(models.IntegerChoices):
    MALE = 1, "мужской"
    FEMALE = 2, "женский"
    NOT_STATED = 3, "не указан"

class MarkShoises(models.IntegerChoices):
    ONE = 1, "ужасно"
    TWO = 2, "плохо"
    THREE = 3, "средне"
    FOUR = 4, "хорошо"
    FIVE = 5, "отлично"

class EducationTypeChoises(models.IntegerChoices):
    SECONDARY = 1, "Среднее"
    SECONDARY_SPECIAL = 2, "Среднее специальное"
    UNFINISHED_HIDH = 3, "Неоконченное высшее"
    HIGH = 4, "Высшее"
    BACHELOR = 5, "Бакалавр"
    MASTER = 6, "Магистр"
    CANDIDATE = 7, "Кандидат наук"
    DOCTOR = 8, "Доктор наук"

class Region(models.Model):
    name = models.TextField(verbose_name="регион")

    class Meta:
        verbose_name = 'регион'
        verbose_name_plural = 'регионы'

class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, verbose_name="телефон")
    status = models.IntegerField(verbose_name="статус", choices=UserDataStatuses.choices)
    region = models.ForeignKey(Region, verbose_name="регион", null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'данные пользователя'
        verbose_name_plural = 'данные пользователей'


class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="пользователь")
    last_name = models.TextField(verbose_name="фамилия")
    first_name = models.TextField(verbose_name="имя")
    sex = models.IntegerField(verbose_name="пол", choices=SexChoises.choices)
    date_birth = models.DateField(verbose_name="дата рождения", null=True, blank=True)
    phone = models.CharField(max_length=15, verbose_name="телефон", null=True, blank=True)
    citizenship1= models.CharField(max_length=255, verbose_name="гражданство", null=True, blank=True) # поправить
    citizenship2 = models.CharField(max_length=255, null=True, blank=True, verbose_name="гражданство")
    citizenship3 = models.CharField(max_length=255, null=True, blank=True, verbose_name="гражданство")

    class Meta:
        verbose_name = 'резюме'
        verbose_name_plural = 'резюме'


class Skill(models.Model):
    name = models.TextField(verbose_name="навык")

    class Meta:
        verbose_name = 'навык'
        verbose_name_plural = 'навыки'

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="пользователь")
    time = models.DateTimeField(verbose_name="время создания")
    mark = models.IntegerField(verbose_name="оценка", choices=MarkShoises.choices)
    text = models.TextField(verbose_name="текст")

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'

class Country(models.Model):
    name = models.TextField(verbose_name="страна")

    class Meta:
        verbose_name = 'страна'
        verbose_name_plural = 'страны'

class Specialization(models.Model):
    name = models.TextField(verbose_name="специализация")

    class Meta:
        verbose_name = 'специализация'
        verbose_name_plural = 'специализации'

class JobTitle(models.Model):
    name = models.TextField(verbose_name="должность")

    class Meta:
        verbose_name = 'должность'
        verbose_name_plural = 'должности'

class Education(models.Model):
    type = models.IntegerField(verbose_name="вид образования", choices=EducationTypeChoises.choices)
    name_institution = models.TextField(verbose_name="название учебного заведения")
    faculty = models.TextField(verbose_name="факультет")
    end_year = models.DateField(verbose_name="дата выпуска")
    specialization = models.ForeignKey(Specialization, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="пользователь")
    
    class Meta:
        verbose_name = 'образование'
        verbose_name_plural = 'образования'


class Experience(models.Model):
    name_company = models.TextField(verbose_name="название компании")
    text = models.TextField(verbose_name="обязанности и достижения")
    date_begin = models.DateField(verbose_name="дата начала")
    date_end = models.DateField(verbose_name="дата окончания")
    job_title = models.ForeignKey(JobTitle, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="должность")

    class Meta:
        verbose_name = 'опыт работы'
        verbose_name_plural = 'опыт работы'

class SocialNetworks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="пользователь")
    vk = models.TextField(verbose_name="VK", null=True, blank=True)
    mailru = models.TextField(verbose_name="mail.ru", null=True, blank=True)
    gmail =models.TextField(verbose_name="Gmail", null=True, blank=True)

    class Meta:
        verbose_name = 'социальные сети'
        verbose_name_plural = 'социальные сети'

class EmployerData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, verbose_name="телефон")
    verification  = models.BooleanField(verbose_name="верификация")
    region = models.ForeignKey(Region, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="регион")
    social_networks = models.ForeignKey(SocialNetworks, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="социальные сети")

    class Meta:
        verbose_name = 'работодатель'
        verbose_name_plural = 'работодатели'

class Vacancy(models.Model):
    job_title = models.ForeignKey(JobTitle, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="должность")
    min_wage = models.IntegerField(verbose_name="минимальная з/п")
    max_wage = models.IntegerField(verbose_name="максимальная з/п")
    description = models.TextField(verbose_name="описание")
    emloyer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="работодатель")

    class Meta:
        verbose_name = 'вакансия'
        verbose_name_plural = 'вакаснии'

class Chat(models.Model):
    emloyer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="работодатель", related_name="employer_chat")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="кандидат", related_name="candidate_chat")
    created_at = models.DateTimeField(verbose_name="время создания")

    class Meta:
        verbose_name = 'чат'
        verbose_name_plural = 'чат'

class Message(models.Model):
    created_at = models.DateTimeField(verbose_name="время создания")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="отправитель")
    text = models.TextField(verbose_name="текст")

    
    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'

