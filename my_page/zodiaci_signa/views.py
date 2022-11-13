from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

zodiacs = {
    'aries': 'Знак зодиака Овен',
    'taurus': 'Знак зодиака Телец',
    'gemini': 'Знак зодиака Близнецы',
    'cancer': 'Знак зодиака Рак',
    'leo': 'Знак зодиака Лев',
    'virgo': 'Знак зодиака Дева',
    'libra': 'Знак зодиака Весы',
    'scorpio': 'Знак зодиака Скорпион',
    'saggitarius': 'Знак зодиака Стрелец',
    'capricorn': 'Знак зодиака Козерог',
    'aquarius': 'Знак зодиака Водолей',
    'pisces': 'Знак зодиака Рыбы',
}
types_of_zadiac = {
    'earth': ('capricorn', 'taurus', 'virgo'),
    'fire': ('aries', 'leo', 'saggitarius'),
    'air': ('libra', 'aquarius', 'gemini'),
    'water': ('cancer', 'scorpio', 'pisces')

}


def path_creator(request, list, path_name):
    result = ''
    zodiacs_list = list
    for sign in zodiacs_list:
        result += f'<li><a href="{sign}">{sign.title()}</a></li>'
    response = f'<ol>{result}</ol>'
    return response


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    try:
        return HttpResponse(zodiacs[sign_zodiac])
    except KeyError:
        return HttpResponse(f'Введено неверное значение - {sign_zodiac}')


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs_list = list(zodiacs)
    if sign_zodiac > len(zodiacs_list):
        return HttpResponseNotFound('Нифига')
    else:
        zodiac_name = zodiacs_list[sign_zodiac - 1]
        redirected_urls = reverse('horoscope_name', args=(zodiac_name,))
        return HttpResponseRedirect(redirected_urls)

def index(request):
    response = path_creator(request, zodiacs, path_name=reverse('home'))
    return HttpResponse(response)


def typing(request):
    result = ''
    for sign in types_of_zadiac:
        path = reverse('types', args=(sign,))
        result += f'<li><a href="{path}">{sign.title()}</a></li>'
        response = f'<ol>{result}</ol>'
    return HttpResponse(response)

def chosen_one(request, typess):
    result=''
    for sign_type in types_of_zadiac[typess]:
        print(types_of_zadiac[typess])
        path = reverse('horoscope_name', args=(sign_type, ))
        result += f'<li><a href={path}>{sign_type.title()}</a></li>'
        response = f'<ol>{result}</ol>'
        print(response)
    return HttpResponse(response)

def get_date(request, date):
    pass


