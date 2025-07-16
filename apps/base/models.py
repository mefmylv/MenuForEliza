from django.db import models

# Create your models here.
MEAL_CHOICES = (
    ("ALL", 'Все'),
    ('Breakfast', 'Завтрак'),
    ('Lunch', 'Обед'),
    ('Dinner','Ужин')
)
class Category_food(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Категория'
    )

    class Meta:
        verbose_name = 'Категория еды'
        verbose_name_plural= 'Категории'

class Foods(models.Model):
    category = models.ForeignKey(
        Category_food,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        related_name="foods"
    )
    meal = models.CharField(
        max_length=155,
        choices = MEAL_CHOICES,
        verbose_name='Прием Пищи'

    )
    title = models.CharField(max_length=155, verbose_name="Название еды")
    image = models.ImageField(verbose_name='Картинка еды')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'


class About_us(models.Model):
    chefs_name = models.CharField(max_length=155, verbose_name='Имена поваров')
    chefs_photos = models.ImageField(verbose_name='Фото шефа')

    class Meta:
        verbose_name= 'О нас'
        verbose_name_plural = 'О нас'