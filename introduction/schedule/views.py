from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound


songs = {
    'Крошка Моя': 'Руки Вверх',
    'Настя': 'Я тебя люблю',
    'Группа Иванушки International': 'Про любовь',
    'Вера Брежнева': 'Люблю ли я тебя',
    'Филипп Киркоров': 'Опять метель',
    'Ани Лорак': 'Цветочек',
    'ГлюкoZa': 'Не выдумывай',
    'Дима Билан': 'Настоящая любовь',
    'Сергей Лазарев': 'Выше облаков',
    'Тату': 'Нас не догонят',
    'Макс Барских': 'Ты не вернешься',
    'Валерия': 'Я всё прощаю',
    'Ирина Аллегрова': 'Я тебя никому не отдам',
    'Алсу': 'Счастье',
    'Король и Шут': 'Гоп-стоп',
    'Би-2': 'Неизвестная песня',
    'Мумий Тролль': 'Я хочу быть с тобой',
    'Ногу Свело!': 'Про любовь',
    'Потап и Настя': 'Это мой стиль',
    'Сплин': 'Апрель',
    'Чайф': 'Время не ждет',
    'Бумер': 'Жизнь прекрасна',
    'Земфира': 'Прости меня моя любовь',
    'Кино': 'Группа крови',
    'Ленинград': 'Пусть говорят',
    'Машина Времени': 'Наутилус',
    'Наутилус Помпилиус': 'Прогулка с Огнем',
    'Пикник': 'Шансон о любви',
    'Ранетки': 'Не ври мне',
    'Сектор Газа': 'Когда наступит вечер',
    'Тараканы!': 'Жизнь прекрасна',
    'Ундервуд': 'Ленивая страна',
    'Чичерина': 'Я тебя люблю',
    'Яд': 'Жизнь прекрасна'
}


def schedule_list(request):
    # Передаем словарь songs в контекст
    context = {'songs': songs}
    return render(request, 'pages/schedule.html', context)