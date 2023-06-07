import uuid
from django.db import models
from django.contrib.auth.models import User


class Description(models.Model):
    DescriptionId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    Name = models.CharField(verbose_name='name', max_length=150, blank=True, null=False)
    Alignment = models.CharField(verbose_name='alignment', max_length=3000, blank=True, null=False)
    God = models.CharField(verbose_name='god', max_length=100, blank=True, null=False)
    Country = models.CharField(verbose_name='country', max_length=50, blank=True, null=False)
    Race = models.CharField(verbose_name='race', max_length=30, blank=True, null=False)
    Size = models.CharField(verbose_name='size', max_length=30, blank=True, null=False)
    Age = models.CharField(verbose_name='age', max_length=10, blank=True, null=False)

    def __str__(self):
        return f'{self.DescriptionId} {self.Name}'


class Stat(models.Model):
    StatId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    Strength = models.IntegerField(verbose_name='strength', blank=True, null=False)
    Dexterity = models.IntegerField(verbose_name='dexterity', blank=True, null=False)
    Constitution = models.IntegerField(verbose_name='constitution', blank=True, null=False)
    Intelligence = models.IntegerField(verbose_name='intelligence', blank=True, null=False)
    Wisdom = models.IntegerField(verbose_name='wisdom', blank=True, null=False)
    Charisma = models.IntegerField(verbose_name='charisma', blank=True, null=False)
    Speed = models.IntegerField(verbose_name='speed', blank=True, null=False)
    HP = models.IntegerField(verbose_name='hp', blank=True, null=False)
    Time_hp = models.IntegerField(verbose_name='time_hp', blank=True, null=False)

    def __str__(self):
        return f'{self.StatId}'


class Cell(models.Model):
    CellId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    Round = models.IntegerField(verbose_name='round', blank=True, null=False)
    NameMagic = models.CharField(verbose_name='nameMagic', blank=True, max_length=100, null=False)
    CubeMagic = models.IntegerField(verbose_name='cubeMagic', blank=True, null=False)
    TypeCubeMagic = models.IntegerField(verbose_name='typeCubeMagic', blank=True, null=False)
    DamageMagic = models.IntegerField(verbose_name='damageMagic', blank=True, null=False)
    Complexity = models.IntegerField(verbose_name='сomplexity', blank=True, null=False)

    def __str__(self):
        return f'{self.CellId} {self.NameMagic}'


class Weapon(models.Model):
    WeaponId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    NameWeapon = models.CharField(verbose_name='nameWeapon', blank=True, max_length=100, null=False)
    CubeWeapon = models.IntegerField(verbose_name='cubeWeapon', blank=True, null=False)
    TypeCubeWeapon = models.IntegerField(verbose_name='typeCubeWeapon', null=False)
    DamageWeapon = models.IntegerField(verbose_name='damageWeapon', blank=True, null=False)
    CritWeapon = models.IntegerField(verbose_name='critWeapon', blank=True, null=False)
    TypeWeapon = models.BooleanField(verbose_name='typeWeapon', blank=True, null=False)
    Ammo = models.IntegerField(verbose_name='ammo', blank=True, null=False)
    Bonus = models.IntegerField(verbose_name='Bonus', blank=True, null=False)

    def __str__(self):
        return f'{self.WeaponId} {self.NameWeapon}'


class Money(models.Model):
    MoneyId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    CM = models.IntegerField(verbose_name='Copper', blank=True, null=False)
    SM = models.IntegerField(verbose_name='Silver', blank=True, null=False)
    GM = models.IntegerField(verbose_name='Gold', blank=True, null=False)
    PM = models.IntegerField(verbose_name='Platinum', blank=True, null=False)

    def __str__(self):
        return f'{self.MoneyId}'


class Character(models.Model):
    CharacterId = models.UUIDField(primary_key=True,verbose_name='charId', default=uuid.uuid4, editable=True)
    Description = models.ForeignKey(Description, verbose_name='description', blank=True, on_delete=models.CASCADE)
    Stat = models.ForeignKey(Stat, verbose_name='stat', blank=True, on_delete=models.CASCADE)
    Cell = models.ForeignKey(Cell, verbose_name='cell', blank=True, on_delete=models.CASCADE)
    Weapon = models.ForeignKey(Weapon, verbose_name='weapon', blank=True, on_delete=models.CASCADE)
    Money = models.ForeignKey(Money, verbose_name='money', blank=True, on_delete=models.CASCADE)
    Inventory = models.CharField(verbose_name='inventory', blank=True, max_length=10000, null=False)

    def __str__(self):
        return f'{self.CharacterId} {self.Description.Name}'


class User(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    UserID = models.UUIDField(primary_key=True, verbose_name='userId', default=uuid.uuid4, editable=False)

    def __str__(self):
        return f'{self.UserID}'


class Session(models.Model):
    SessionId = models.UUIDField(primary_key=True, verbose_name='sessionId', default=uuid.uuid4, editable=True)
    NameSession = models.CharField(verbose_name='nameSession', max_length=60)
    User_id = models.ForeignKey(User, verbose_name='user', on_delete=models.CASCADE)
    UserStatus = models.CharField(verbose_name='userStatus', blank=True, max_length=100, null=False)
    CharacterID = models.ForeignKey(Character, verbose_name='character', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f'{self.NameSession}'
