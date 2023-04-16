from django.db import models
from django.contrib.auth.models import User


class Skins(models.Model):
    title = models.CharField(verbose_name='Skin name', max_length=255)
    # slug = models.SlugField(verbose_name='Skin URL', max_length=255, unique=True, db_index=True)
    photo = models.ImageField(verbose_name='Skin photo', upload_to='photos/%Y/%m/%d', blank=True, null=True)
    price = models.IntegerField(verbose_name='Skin price')
    float = models.FloatField(verbose_name='Skin float')
    availability = models.BooleanField(verbose_name='Skin availability', default=True)
    amount = models.IntegerField(verbose_name='Skin amount', default=0)
    amount_likes = models.IntegerField(verbose_name='Skin like', default=0)
    amount_dislikes = models.IntegerField(verbose_name='Skin dislike', default=0)
    amount_orders = models.IntegerField(verbose_name='Skin orders', default=0)
    pattern = models.IntegerField(verbose_name='Skin pattern')
    CHOICE_APPEARANCE_OPTIONS = [
        ('Factory-New', 'Factory-New'),
        ('Minimal-Wear', 'Minimal-Wear'),
        ('Field-Tested', 'Field-Tested'),
        ('Well-Worn', 'Well-Worn'),
        ('Battle-Scarred', 'Battle-Scarred')
    ]
    appearance = models.CharField(verbose_name='Skin type', max_length=255, choices=CHOICE_APPEARANCE_OPTIONS)
    is_stattrak = models.BooleanField(verbose_name='Skin is StatTrak', default=False)
    # category = models.ForeignKey('SkinCategories', on_delete=models.CASCADE, verbose_name='Skin category')
    CHOICE_CATEGORY_OPTIONS = [
        ('Knife', (
                ('Bayonet', 'Bayonet'),
                ('Bowie', 'Bowie'),
                ('Butterfly', 'Butterfly'),
                ('Falchion', 'Falchion'),
                ('Flip', 'Flip'),
                ('Gut', 'Gut'),
                ('Huntsman', 'Huntsman'),
                ('Karambit', 'Karambit'),
                ('M9-Bayonet', 'M9-Bayonet'),
                ('Navaja', 'Navaja'),
                ('Shadow-Daggers', 'Shadow-Daggers'),
                ('Stiletto', 'Stiletto'),
                ('Talon', 'Talon'),
                ('Ursus', 'Ursus'),
                ('Classic', 'Classic'),
                ('Skeleton', 'Skeleton'),
                ('Nomad', 'Nomad'),
                ('Survival', 'Survival'),
                ('Paracord', 'Paracord'),
            )
        ),
        ('Gloves', (
                ('Bloodhound', 'Bloodhound'),
                ('Driver', 'Driver'),
                ('Hand-Wraps', 'Hand-Wraps'),
                ('Hydra', 'Hydra'),
                ('Moto', 'Moto'),
                ('Specialist', 'Specialist'),
                ('Sport', 'Sport'),
            )
        ),
        ('Pistols', (
                ('CZ75-Auto', 'CZ75-Auto'),
                ('Desert-Eagle', 'Desert-Eagle'),
                ('Dual-Berettas', 'Dual-Berettas'),
                ('Five-SeveN', 'Five-SeveN'),
                ('Glock-18', 'Glock-18'),
                ('P2000', 'P2000'),
                ('P250', 'P250'),
                ('R8-Revolver', 'R8-Revolver'),
                ('Tec-9', 'Tec-9'),
                ('USP-S', 'USP-S'),
            )
        ),
        ('Sub-Machine Guns', (
                ('MAC-10', 'MAC-10'),
                ('MP5-SD', 'MP5-SD'),
                ('MP7', 'MP7'),
                ('MP9', 'MP9'),
                ('P90', 'P90'),
                ('PP-Bizon', 'PP-Bizon'),
                ('UMP-45', 'UMP-45'),
            )
        ),
        ('Assault Rifles', (
                ('AK-47', 'AK-47'),
                ('AUG', 'AUG'),
                ('FAMAS', 'FAMAS'),
                ('Galil-AR', 'Galil-AR'),
                ('M4A1-S', 'M4A1-S'),
                ('M4A4', 'M4A4'),
                ('SG-553', 'SG-553'),
            )
        ),
        ('Sniper Rifles', (
                ('AWP', 'AWP'),
                ('G3SG1', 'G3SG1'),
                ('SCAR-20', 'SCAR-20'),
                ('SSG-08', 'SSG-08'),
            )
        ),
        ('Shotguns', (
                ('MAG-7', 'MAG-7'),
                ('Nova', 'Nova'),
                ('Sawed-Off', 'Sawed-Off'),
                ('XM1014', 'XM1014'),
            )
        ),
        ('Machine Guns', (
                ('M249', 'M249'),
                ('Negev', 'Negev'),
            )
        ),
        ('Keys', 'Keys'),
        ('Other', (
                ('Sticker', 'Sticker'),
                ('Case', 'Case'),
                ('Graffiti', 'Graffiti'),
                ('Music', 'Music'),
                ('Badge', 'Badge'),
                ('Agents', 'Agents'),
                ('Patch', 'Patch'),
            )
        )
    ]
    category = models.CharField(verbose_name='Skin category', max_length=200, choices=CHOICE_CATEGORY_OPTIONS)
    CHOICE_QUALITY_OPTIONS = [
        ('Consumer-Grade', 'Consumer-Grade'),
        ('Industrial-Grade', 'Industrial-Grade'),
        ('Mil-Spec-Grade', 'Mil-Spec-Grade'),
        ('Restricted', 'Restricted'),
        ('Classified', 'Classified'),
        ('Covert', 'Covert'),
    ]
    quality = models.CharField(verbose_name='Skin quality', max_length=200, choices=CHOICE_QUALITY_OPTIONS)
    time_create = models.DateTimeField(verbose_name='Skin time create', auto_now_add=True, null=True)
    time_update = models.DateTimeField(verbose_name='Skin time update', auto_now=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Skin'
        verbose_name_plural = 'Skins'


class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    orders = models.TextField('User orders', blank=True)
    like = models.TextField('User liking skin', blank=True)
    dislike = models.TextField('User unliking skin', blank=True)
    favorite = models.TextField('User favorite skin', blank=True)
    basket = models.TextField('User basket', blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


# class SkinCategories(models.Model):
#     name = models.CharField(verbose_name='Category name', max_length=200)
#     slug = models.SlugField(verbose_name='Category URL', max_length=255, unique=True, db_index=True)
