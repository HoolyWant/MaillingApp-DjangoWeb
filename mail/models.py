from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    contact_email = models.CharField(max_length=100, verbose_name='контактная почта')
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)

    def __str__(self):
        return f'{self.contact_email}'

    class Meta:
        verbose_name = 'клиент сервис'
        verbose_name_plural = 'клиент сервисы'


class MailDistributionSettings(models.Model):
    PERIOD_DAILY = 'daily'
    PERIOD_WEEKLY = 'weekly'
    PERIOD_MONTHLY = 'monthly'

    PERIODS = ((PERIOD_DAILY, 'Ежедневно'),
               (PERIOD_WEEKLY, 'Еженедельно'),
               (PERIOD_MONTHLY, 'Ещемесячно'))

    STATUS_CREATED = 'created'
    STATUS_STARTED = 'started'
    STATUS_DONE = 'done'

    STATUSES = ((STATUS_CREATED, 'Создана'),
                (STATUS_STARTED, 'Запущена'),
                (STATUS_DONE, 'Завершена'))
    date_start = models.TimeField(verbose_name='время начала рассылки')
    period = models.CharField(max_length=20, choices=PERIODS, default=PERIOD_DAILY, verbose_name='период')
    distribution_status = models.CharField(max_length=20,
                                           choices=STATUSES,
                                           default=STATUS_CREATED,
                                           verbose_name='статус')
    message = models.ForeignKey('MessagesForDistribution',
                                on_delete=models.CASCADE,
                                verbose_name='сообщение',
                                **NULLABLE)
    clients = models.ManyToManyField(Client, verbose_name='клиент')
    user = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name='пользователь')

    def __str__(self):
        return f'{self.message}({self.period})'

    class Meta:
        verbose_name = 'настройка рассылки'
        verbose_name_plural = 'настройки рассылки'


class MessagesForDistribution(models.Model):
    message_theme = models.CharField(max_length=100, verbose_name='тема письма')
    message_body = models.TextField(verbose_name='текст письма')
    user = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name='пользователь')

    def __str__(self):
        return self.message_theme

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Logs(models.Model):
    STATUS_OK = 'Ok'
    STATUS_FAILED = 'Failed'
    STATUSES = (
        (STATUS_OK, 'Успешно'),
        (STATUS_FAILED, 'Ошибка')
    )
    last_attempt = models.DateTimeField(auto_now_add='True', verbose_name='время последней попытки')
    attempt_status = models.CharField(max_length=8, choices=STATUSES, default=STATUS_OK, verbose_name='статус попытки')
    client = models.ForeignKey('Client', on_delete=models.CASCADE,
                               verbose_name='Клиент',
                               **NULLABLE)
    setting = models.ForeignKey('MailDistributionSettings', on_delete=models.CASCADE,
                                verbose_name='Настройки',
                                **NULLABLE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name='пользователь')

    def __str__(self):
        return f'{self.attempt_status}\n{self.last_attempt}'

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
#
#
#
#
