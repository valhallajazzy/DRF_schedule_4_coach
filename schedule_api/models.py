from django.db import models


class Gender:
    GENDER = (
            ('male', 'мужской'),
            ('female', 'женский')
        )


class Client(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=255, verbose_name='Отчество')
    date_of_birth = models.DateField(db_index=True, verbose_name='Дата рождения')
    gender = models.CharField(max_length=255, choices=Gender.GENDER, verbose_name='пол')


class SportClub(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название спортивного клуба')
    address = models.TextField(verbose_name='Адрес спортивного клуба',
                               help_text='ул. Березовая, д.5')


class Coach(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=255, verbose_name='Отчество')
    date_of_birth = models.DateField(db_index=True, verbose_name='Дата рождения')
    gender = models.CharField(max_length=255, choices=Gender.GENDER, verbose_name='пол')
    kind_of_training = models.CharField(max_length=255,
                                        verbose_name='Вид деятельности',
                                        help_text='Тренер по боксу')
    sport_clubs = models.ManyToManyField(SportClub,
                                         blank=True,
                                         verbose_name='Спортивные клубы',
                                         related_name='club_coaches')


class Training(models.Model):
    training_date = models.DateField(db_index=True)
    training_time = models.TimeField(db_index=True)
    client = models.ForeignKey(Client,
                               on_delete=models.CASCADE,
                               verbose_name='Клиент',
                               related_name='trainings')
    coach = models.ForeignKey(Coach,
                              on_delete=models.CASCADE,
                              verbose_name='Тренер',
                              related_name='works')
    club = models.ForeignKey(SportClub,
                             on_delete=models.CASCADE,
                             verbose_name='Спортивный клуб',
                             related_name='meetings')

