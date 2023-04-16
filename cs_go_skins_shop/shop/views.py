from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User

menu = [
    {'title': 'home', 'url_name': 'home'},
    {'title': 'shop', 'url_name': 'shop'},
    {'title': 'about', 'url_name': 'about'},
    {'title': 'contact', 'url_name': 'contact'},
]

def shopHome(request):
    context = {
        'title': 'home',
        'menu': menu,
    }
    return render(request, 'shop/index.html', context)

def shopShop(request):
    knifes_list = ['Bayonet', 'Bowie', 'Butterfly', 'Falchion', 'Flip', 'Gut', 'Huntsman', 'Karambit', 'M9-Bayonet', 'Navaja', 'Shadow-Daggers', 'Stiletto', 'Talon', 'Ursus', 'Classic', 'Skeleton', 'Nomad', 'Survival', 'Paracord']
    gloves_list = ['Bloodhound', 'Driver', 'Hand-Wraps', 'Hydra', 'Moto', 'Specialist', 'Sport']
    pistols_list = ['CZ75-Auto', 'Desert-Eagle', 'Dual-Berettas', 'Five-SeveN', 'Glock-18', 'P2000', 'P250', 'R8-Revolver', 'Tec-9', 'USP-S']
    sub_machine_guns_list = ['MAC-10', 'MP5-SD', 'MP7', 'MP9', 'P90', 'PP-Bizon', 'UMP-45']
    assault_rifles_list = ['AK-47', 'AUG', 'FAMAS', 'Galil-AR', 'M4A1-S', 'M4A4', 'SG-553']
    sniper_rifles_list = ['AWP', 'G3SG1', 'SCAR-20', 'SSG-08']
    shotguns_list = ['MAG-7', 'Nova', 'Sawed-Off', 'XM1014']
    machine_guns_list = ['M249', 'Negev']
    others_list = ['Sticker', 'Case', 'Graffiti', 'Music', 'Badge', 'Agents', 'Patch']
    appearances_list = ['Factory-New', 'Minimal-Wear', 'Field-Tested', 'Well-Worn', 'Battle-Scarred']
    qualities_list = ['Consumer-Grade', 'Industrial-Grade', 'Mil-Spec-Grade', 'Restricted', 'Classified', 'Covert']
    def requst_get():
        def check_if_true(mapping, key, value):
            if value:
                mapping[key] = value

        def check_type():
            check_type_list = []
            if request.GET.get('knifes'):
                knife_list = []
                for item in knifes_list:
                    if request.GET.get(item):
                        knife_list.append(item)
                if not knife_list:
                    check_type_list += knifes_list
                else:
                    check_type_list += knife_list

            if request.GET.get('gloves'):
                glove_list = []
                for item in gloves_list:
                    if request.GET.get(item):
                        glove_list.append(item)
                if not glove_list:
                    check_type_list += gloves_list
                else:
                    check_type_list += glove_list

            if request.GET.get('pistols'):
                pistol_list = []
                for item in pistols_list:
                    if request.GET.get(item):
                        pistol_list.append(item)
                if not pistol_list:
                    check_type_list += pistols_list
                else:
                    check_type_list += pistol_list

            if request.GET.get('sub-machine-guns'):
                sub_machine_gun_list = []
                for item in sub_machine_guns_list:
                    if request.GET.get(item):
                        sub_machine_gun_list.append(item)
                if not sub_machine_gun_list:
                    check_type_list += sub_machine_guns_list
                else:
                    check_type_list += sub_machine_gun_list

            if request.GET.get('assault-rifles'):
                assault_rifle_list = []
                for item in assault_rifles_list:
                    if request.GET.get(item):
                        assault_rifle_list.append(item)
                if not assault_rifle_list:
                    check_type_list += assault_rifles_list
                else:
                    check_type_list += assault_rifle_list

            if request.GET.get('sniper-rifles'):
                sniper_rifle_list = []
                for item in sniper_rifles_list:
                    if request.GET.get(item):
                        sniper_rifle_list.append(item)
                if not sniper_rifle_list:
                    check_type_list += sniper_rifles_list
                else:
                    check_type_list += sniper_rifle_list

            if request.GET.get('shotguns'):
                shotgun_list = []
                for item in shotguns_list:
                    if request.GET.get(item):
                        shotgun_list.append(item)
                if not shotgun_list:
                    check_type_list += shotguns_list
                else:
                    check_type_list += shotgun_list

            if request.GET.get('machine-guns'):
                machine_gun_list = []
                for item in machine_guns_list:
                    if request.GET.get(item):
                        machine_gun_list.append(item)
                if not machine_gun_list:
                    check_type_list += machine_guns_list
                else:
                    check_type_list += machine_gun_list

            if request.GET.get('keys'):
                check_type_list += ['Keys']

            if request.GET.get('other'):
                other_list = []
                for item in others_list:
                    if request.GET.get(item):
                        other_list.append(item)
                if not other_list:
                    check_type_list += others_list
                else:
                    check_type_list += other_list
            return check_type_list

        def check_appearance():
            check_appearance_list = []
            for item in appearances_list:
                if request.GET.get(item):
                    check_appearance_list.append(item)
            return check_appearance_list

        def check_min_price():
            min_price = 0
            if request.GET.get('min-price'):
                min_price = int(request.GET.get('min-price'))

            return min_price

        def check_max_price():
            max_price = 0
            if request.GET.get('max-price'):
                max_price = int(request.GET.get('max-price'))

            return max_price

        def check_is_stattrak():
            stattrak = False
            if request.GET.get('stattrak'):
                stattrak = True

            return stattrak

        def check_min_float():
            min_float = 0
            if request.GET.get('min-float'):
                min_float = float(request.GET.get('min-float'))

            return min_float

        def check_max_float():
            max_float = 0
            if request.GET.get('max-float'):
                max_float = float(request.GET.get('max-float'))

            return max_float

        def check_quality():
            check_quality_list = []
            for item in qualities_list:
                if request.GET.get(item):
                    check_quality_list.append(item)

            return check_quality_list

        def check_pattern():
            pattern = 0
            if request.GET.get('pattern'):
                pattern = int(request.GET.get('pattern'))

            return pattern

        def sort_publishing():
            publishing = '-time_create'
            if request.GET.get('sort-publishing'):
                publishing = 'time_create'

            return publishing

        def sort_price():
            price = '-price'
            if request.GET.get('sort-price'):
                price = 'price'

            return price

        def sort_float():
            float = '-float'
            if request.GET.get('sort-float'):
                float = 'float'

            return float

        def search():
            search_word = ''
            if request.GET.get('search'):
                search_word = request.GET.get('search')

            return search_word

        if not check_type() and not check_appearance() and not check_min_price() and not check_max_price() and not check_is_stattrak() and not check_min_float() and not check_max_float() and not check_quality() and not check_pattern() and not search():
            skins = Skins.objects.all().order_by(sort_publishing(), sort_price(), sort_float())
        else:
            check_dict = {}
            check_if_true(check_dict, 'category__in', check_type())
            check_if_true(check_dict, 'appearance__in', check_appearance())
            check_if_true(check_dict, 'price__gte', check_min_price())
            check_if_true(check_dict, 'price__lte', check_max_price())
            check_if_true(check_dict, 'is_stattrak', check_is_stattrak())
            check_if_true(check_dict, 'float__gte', check_min_float())
            check_if_true(check_dict, 'float__lte', check_max_float())
            check_if_true(check_dict, 'quality__in', check_quality())
            check_if_true(check_dict, 'pattern', check_pattern())
            check_if_true(check_dict, 'title__startswith', search())

            skins = Skins.objects.filter(**check_dict).order_by(sort_publishing(), sort_price(), sort_float())
        return skins

    if request.user.is_authenticated:
        orders_list = []
        user, __ = User.objects.get_or_create(username=request.user.username)
        user_profile = Profiles.objects.get(user=user)
        if len(user_profile.orders) > 0:
            orders_list.append(user_profile.orders)
            print(orders_list)
        for item in requst_get():
            if request.POST.get(f'basket_{item.title}'):
                orders_list.append(item.pk)

    context = {
        'title': 'shop',
        'menu': menu,
        'skins': requst_get(),
        'knifes': knifes_list,
        'gloves': gloves_list,
        'pistols': pistols_list,
        'sub_machine_guns': sub_machine_guns_list,
        'assault_rifles': assault_rifles_list,
        'sniper_rifles': sniper_rifles_list,
        'shotguns': shotguns_list,
        'machine_guns': machine_guns_list,
        'other': others_list,
        'appearance': appearances_list,
        'quality': qualities_list,
    }
    return render(request, 'shop/shop.html', context)

def shopAbout(request):
    context = {
        'title': 'about',
        'menu': menu,
    }
    return render(request, 'shop/about.html', context)

def shopContact(request):
    context = {
        'title': 'contact',
        'menu': menu,
    }
    return render(request, 'shop/contact.html', context)
