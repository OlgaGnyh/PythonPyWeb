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
        count_entry = Entry.objects.annotate(count_entry=Count('author', distinct=True)).values('id', 'count_entry').order_by('count_entry').latest("id")
        self.answer2 = Author.objects.filter(id=count_entry.get('id'))

        # TODO Какие статьи содержат тег 'Кино' или 'Музыка' ?
        obj1 = Entry.objects.filter(tags__name__contains='Кино')
        obj2 = Entry.objects.filter(tags__name__contains='Музыка')
        self.answer3 = obj1.union(obj2)

        # TODO Сколько авторов женского пола зарегистрировано в системе?
        self.answer4 = Author.objects.filter(gender='ж').count()

        # TODO Какой процент авторов согласился с правилами при регистрации?
        count_all_Author = Author.objects.count()
        count_reg_Author = Author.objects.filter(status_rule=True).count()
        self.answer5 = round((count_reg_Author / count_all_Author * 100), 1)

        # TODO Какие авторы имеют стаж от 1 до 5 лет?
        self.answer6 = Author.objects.filter(authorprofile__stage__gte=1).filter(authorprofile__stage__lte=5)

        # TODO Какой автор имеет наибольший возраст?
        max_age = Author.objects.aggregate(max_age=Max('age'))
        author_max_age = Author.objects.filter(age=max_age['max_age'])
        # self.answer7 = author_max_age
        # self.answer7 = max_age.get('max_age')
        self.answer7 = f'{author_max_age}, {max_age.get('max_age')}'

        # TODO Сколько авторов указали свой номер телефона?
        self.answer8 = Author.objects.filter(phone_number__isnull=False).count()

        # TODO Какие авторы имеют возраст младше 25 лет?
        self.answer9 = Author.objects.filter(age__lt=25)

        # TODO Сколько статей написано каждым автором?
        # asd = Entry.objects.annotate(count_entry=Count('author', distinct=True)).values('author','count_entry')
        # asd2 = []
        # for i in asd:
        #     asd2.append(f'Автор: {asd[i].get('author')}; Число статей: {asd[i].get('count_entry')}')
        # self.answer10 = asd
        self.answer10 = Entry.objects.annotate(count_entry=Count('author', distinct=True)).values('author', 'count_entry')

        context = {f'answer{index}': self.__dict__[f'answer{index}'] for index in range(1, 11)}
        return render(request, 'train_db/training_db.html', context=context)

