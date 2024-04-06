import django
import os
from django.db.models import Count


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

if __name__ == "__main__":
    from apps.db_train_alternative.models import Blog, Author, AuthorProfile, Entry, Tag
    import datetime
    # TODO Сделайте здесь запросы

    # obj = Entry.objects.filter(author__name__contains='thinker')
    # print(obj)
    #
    # obj = Entry.objects.filter(author__authorprofile__city=None)
    ## obj = Entry.objects.filter(author__authorprofile__city__iexact='Самара'
    # print(obj)
    #
    # print(Entry.objects.get(id__exact=4))
    # print(Entry.objects.get(id=4))  # Аналогично exact
    # print(Blog.objects.get(name__iexact="Путешествия по миру"))

    # print(Entry.objects.filter(headline__contains='мод'))

    # print(Entry.objects.filter(id__in=[1, 3, 4]))
    # print(Entry.objects.filter(number_of_comments__in='123'))
    # inner_qs = Blog.objects.filter(name__contains='Путешествия')
    # entries = Entry.objects.filter(blog__in=inner_qs)
    # print(entries)

    ## Вывести все записи, у которых число комментарием больше 10
    # print(Entry.objects.filter(number_of_comments__gt=10))

    ## Вывести все записи, которые опубликованы (поле pub_date) позже и равное 01.06.2023
    # print(Entry.objects.filter(pub_date__gte=datetime.date(2023, 6, 1)))

    # # Вывести все записи, у которых число комментарием больше 10 и рейтинг < 4
    # print(Entry.objects.filter(number_of_comments__gt=10).filter(rating__lt=4))

    # # Вывести все записи, у которых заголовок статьи лексиграфически <= "Зя"
    # print(Entry.objects.filter(headline__lte="Зя"))
    #
    # print(Entry.objects.filter(headline__startswith='Как'))
    #
    # print(Entry.objects.filter(headline__endswith='ния'))

    # # Вывести записи между 01.01.2023 и 31.12.2023
    # start_date = datetime.date(2023, 1, 1)
    # end_date = datetime.date(2023, 12, 31)
    # print(Entry.objects.filter(pub_date__range=(start_date, end_date)))
    # print(Entry.objects.filter(pub_date__year=2023))

    # # Вывести записи старше 2022 года
    # print(Entry.objects.filter(pub_date__year__lt=2022))

    # # Вывести все записи за февраль доступных годов, отобразить название, дату публикации, заголовок
    # print(Entry.objects.filter(pub_date__month=2).values('blog__name', 'pub_date', 'headline'))

    # Вывести username авторов у которых есть публикации с 1 по 15 апреля 2023 года, вывести без использования range. Пример для работы с __day
    # print(Entry.objects.filter(pub_date__year=2023).filter(pub_date__day__gte=1).filter(
    #     pub_date__day__lte=15).values_list("author__name").distinct())

    # # Вывести статьи опубликованные в понедельник (так как datetime работает по американской системе,
    # # то начало недели идёт с воскресенья, а заканчивается субботой, поэтому понедельник второй день в неделе)
    # print(Entry.objects.filter(pub_date__week_day=2).values('blog__name', 'pub_date', 'headline'))

    # # Вывод всех записей по конкретной дате
    # print(Entry.objects.filter(pub_date__date=datetime.date(2022, 6, 1)))

    # Вывод всех записей новее конкретной даты
    # print(Entry.objects.filter(pub_date__date__gt=datetime.date(2024, 1, 1)))
    #
    # # Вывод записей по конкретному времени
    # print(Entry.objects.filter(pub_date__time=datetime.time(12, 00)))

    # # Вывод записей по временному диапазону с 6 утра до 17 вечера
    # print(Entry.objects.filter(pub_date__time__range=(datetime.time(6), datetime.time(17))))
    # print(Entry.objects.filter(pub_date__date__range=(datetime.date(2023, 8, 1), datetime.date(2024, 1, 1))))

    # # Вывести всех авторов которые не указали город
    # print(AuthorProfile.objects.filter(city__isnull=True))

    # # Вывести записи где в тексте статьи встречается патерн \w*стран\w*
    # print(Entry.objects.filter(body_text__regex=r'\w*стран\w*'))

    # # Вывести записи авторов с почтовыми доменами @gmail.com и @mail.ru
    # print(Entry.objects.filter(author__email__iregex=r'\w+(@gmail.com|@mail.ru)'))

    # # Если необходимо вывести записи авторов с почтовыми доменами @gmail.com и @mail.ru, но чтобы значения не повторялись, то используем distinct()
    # print(Entry.objects.filter(author__email__iregex=r'\w+(@gmail.com|@mail.ru)').distinct())

    # all_obj = Blog.objects.all()
    # print("Вывод всех значений в таблице Blog\n", all_obj)
    #
    # all_obj = Blog.objects.first()
    # print("Вывод первого значения в таблице Blog\n", all_obj)

    # all_obj = Blog.objects.all()
    # obj_first = all_obj.first()
    # print("Разные запросы на вывод в Blog\n", f"Первое значение таблицы = {obj_first}\n",
    #       f"Все значения = {all_obj}")

    # all_obj = Blog.objects.all()
    # for idx, value in enumerate(all_obj):
    #     print(f"idx = {idx}, value = {value}")
    # print(all_obj[0])  # Получение 0-го элемента
    # print(all_obj[2:4])  # Получение 2 и 3 элемента
    # print(all_obj.latest("id"))  # Получение последнего элемента
    # print(Blog.objects.latest("id"))  # Одинаково работает

    # # Пример получения элемента по одному условию
    # print(Blog.objects.get(id=1))
    # # Пример получения элемента по двум условиям. Условия работают с оператором И, т.е. выведется строка, только с
    # # совпадением и первого и второго параметра.
    # print(Blog.objects.get(id=1, name="Путешествия по миру"))
    # # Если нет совпадений, то выйдет исключение "db.models.Blog.DoesNotExist: Blog matching query does not exist."
    # print(Blog.objects.get(id=2, name="Путешествия по миру"))

    # # Вывод всех строк таблицы Blog у которых значение id >= 2.
    # print(Blog.objects.filter(id__gte=2))
    #
    # # Вывод всех строк таблицы Blog кроме тех у которых значение id >= 2.
    # print(Blog.objects.exclude(id__gte=2))

    # try:
    #     Blog.objects.get(id=2, name="Путешествия по миру")
    # except Blog.DoesNotExist:
    #     print("Не существует")
    # # Пример для filter
    # print(Blog.objects.filter(id=2, name="Путешествия по миру").exists())

    # filtered_data = Blog.objects.filter(id__gte=2)
    # print(filtered_data.order_by("id"))  # упорядочивание по возрастанию по полю id
    # print(filtered_data.order_by("-id"))  # упорядочивание по уменьшению по полю id
    # print(filtered_data.order_by("-name", "id"))  # упорядочивание по двум параметрам, сначала по первому на уменьшение,
    # # затем второе на увеличение. Можно упорядочивание провести по сколь угодно параметрам.

    # Запрос, аннотирующий количество статей для каждого блога,
    # при этом добавляется новая колонка number_of_entries для вывода
    entry = Blog.objects.annotate(number_of_entries=Count('entries')).values('name', 'number_of_entries')
    print(entry)

    entry = Entry.objects.annotate(count_entry=Count('author')).values('author', 'count_entry')
    print(entry)

    count_entry = Entry.objects.aggregate(count_entry=Count('author', distinct=True))
    print(count_entry)
    # print(Author.objects.filter(id=count_entry.get('id')))



