from django.db import models


class Cases(models.Model):

    class CaseType(models.TextChoices):
        B2B = 'B2', 'b2b'
        E_COMMERCE = 'EC', 'e_commerce'
        BOT = 'BT', 'bot'

    title = models.CharField(max_length=50, verbose_name='Заголовок')
    desc = models.TextField(max_length=5000, verbose_name='Описание')
    image = models.ImageField(verbose_name='Фотография кейса')
    case_type = models.CharField(
        max_length=2,
        choices=CaseType.choices,
        verbose_name='Тип кейса'
    )

    class Meta:
        db_table = 'cases'
        verbose_name = 'Кейс'
        verbose_name_plural = 'Кейсы'

    def __str__(self):
        return self.title


class CaseTaskText(models.Model):
    task_text = models.TextField(max_length=5000, verbose_name='Блок текста о задаче кейса')
    case = models.ForeignKey(
        Cases,
        on_delete=models.CASCADE,
        verbose_name='Блок о кейсе(задача)',
        related_name='case_task_text'
    )

    class Meta:
        db_table = 'cases_task_text'
        verbose_name = 'Блок текста о задаче'
        verbose_name_plural = 'Блок текста о задаче'

    def __str__(self):
        return self.task_text


class CaseResultText(models.Model):
    result_text = models.TextField(max_length=5000, verbose_name='Блок текста о результате кейса')
    case = models.ForeignKey(
        Cases,
        on_delete=models.CASCADE,
        verbose_name='Блок о кейсе(результат)',
        related_name='case_result_text'
    )

    class Meta:
        db_table = 'cases_result_text'
        verbose_name = 'Блок текста о результате'
        verbose_name_plural = 'Блок текста о результате'

    def __str__(self):
        return self.result_text
