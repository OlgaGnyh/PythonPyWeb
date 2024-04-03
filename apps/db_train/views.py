from django.shortcuts import render
from django.views import View
from .models import Author, AuthorProfile, Entry, Tag
from django.db.models import Q, Max, Min, Avg, Count


class TrainView(View):
    def get(self, request):
        # Создайте здесь запросы к БД
        # TODO Какие авторы имеют самую высокую уровень самооценки(self_esteem)?
        max_self_esteem = Author.objects.aggregate(max_self_esteem=Max('self_esteem'))
        self.answer1 = Author.objects.filter(self_esteem=max_self_esteem['max_self_esteem'])

        # TODO Какой автор имеет наибольшее количество опубликованных статей?
        count_entry = Entry.objects.annotate(count_entry=Count('author')).values('id', 'count_entry').order_by('count_entry').latest("id")
        self.answer2 = Author.objects.filter(id=count_entry.get('id'))

        # TODO Какие статьи содержат тег 'Кино' или 'Музыка' ?
        obj1 = Entry.objects.filter(tags__name__contains='Кино')
        obj2 = Entry.objects.filter(tags__name__contains='Музыка')
        self.answer3 = obj1.union(obj2)

        # TODO Сколько авторов женского пола зарегистрировано в системе?
        self.answer4 = None

        # TODO Какой процент авторов согласился с правилами при регистрации?
        self.answer5 = None

        # TODO Какие авторы имеют стаж от 1 до 5 лет?
        self.answer6 = None

        # TODO Какой автор имеет наибольший возраст?
        self.answer7 = None

        # TODO Сколько авторов указали свой номер телефона?
        self.answer8 = None

        # TODO Какие авторы имеют возраст младше 25 лет?
        self.answer9 = None

        # TODO Сколько статей написано каждым автором?
        self.answer10 = None

        context = {f'answer{index}': self.__dict__[f'answer{index}'] for index in range(1, 11)}
        return render(request, 'train_db/training_db.html', context=context)

