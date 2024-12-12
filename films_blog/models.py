from django.db import models

class FilmModel(models.Model):
    GENRE = (
        ('Ужасы', 'Ужасы'),
        ('Комедия', 'Комедия'),
        ('Приключения', 'Приключения')
    )
    image = models.ImageField(upload_to='films/', verbose_name='Загрузите фото фильма')
    title = models.CharField(max_length=100, verbose_name='Укажите название фильма')
    description = models.TextField(verbose_name='Укажите описание', blank=True)
    price = models.FloatField(verbose_name='Укажите цену на фильм', default=10)
    created_at = models.DateField(auto_now_add=True)
    genre = models.CharField(max_length=100, choices=GENRE, default='Комедия')
    time_watch = models.TimeField(verbose_name='Укажите длительность фильма', blank=True)
    director = models.CharField(max_length=100, verbose_name='Укажите режжисера', default='Иван Иванов')
    trailer = models.URLField(verbose_name='Укажите ссылку трейлера фильма', null=True)


    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return self.title

class Review(models.Model):
    STARS = (
        ('⭐', '⭐'),
        ('⭐⭐', '⭐⭐'),
        ('⭐⭐⭐', '⭐⭐⭐'),
        ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
        ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),

    )
    film = models.ForeignKey(FilmModel, on_delete=models.CASCADE, related_name='reviews')
    created_at = models.DateField(auto_now_add=True)
    text_review = models.TextField(verbose_name='Напишите отзыв о фильме')
    stars = models.CharField(max_length=100, verbose_name="Поставьте оценку", choices=STARS, default='⭐')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return F'{self.film}-{self.stars}'
