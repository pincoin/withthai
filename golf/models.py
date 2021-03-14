from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils import Choices
from model_utils import models as model_utils_models


class Area(model_utils_models.TimeStampedModel):
    title_english = models.CharField(
        verbose_name=_('Area english name'),
        max_length=255,
    )

    title_thai = models.CharField(
        verbose_name=_('Area Thai name'),
        max_length=255,
    )

    title_korean = models.CharField(
        verbose_name=_('Area Korean name'),
        max_length=255,
    )

    slug = models.SlugField(
        verbose_name=_('Slug'),
        help_text=_('A short label containing only letters, numbers, underscores or hyphens for URL'),
        max_length=255,
        db_index=True,
        unique=True,
        allow_unicode=True,
    )

    position = models.IntegerField(
        verbose_name=_('Position'),
        default=0,
        db_index=True,
    )

    class Meta:
        verbose_name = _('Area')
        verbose_name_plural = _('Areas')

    def __str__(self):
        return f'{self.title_english}'


class Province(model_utils_models.TimeStampedModel):
    title_english = models.CharField(
        verbose_name=_('Province English name'),
        max_length=255,
    )

    title_thai = models.CharField(
        verbose_name=_('Province Thai name'),
        max_length=255,
    )

    title_korean = models.CharField(
        verbose_name=_('Province Korean name'),
        max_length=255,
    )

    slug = models.SlugField(
        verbose_name=_('Slug'),
        help_text=_('A short label containing only letters, numbers, underscores or hyphens for URL'),
        max_length=255,
        db_index=True,
        unique=True,
        allow_unicode=True,
    )

    area = models.ForeignKey(
        'golf.Area',
        verbose_name=_('Location area'),
        db_index=True,
        on_delete=models.CASCADE,
    )

    position = models.IntegerField(
        verbose_name=_('Position'),
        default=0,
        db_index=True,
    )

    class Meta:
        verbose_name = _('Province')
        verbose_name_plural = _('Provinces')

    def __str__(self):
        return '{}'.format(self.title_english)


class District(model_utils_models.TimeStampedModel):
    title_english = models.CharField(
        verbose_name=_('District English name'),
        max_length=255,
    )

    title_thai = models.CharField(
        verbose_name=_('District Thai name'),
        max_length=255,
    )

    title_korean = models.CharField(
        verbose_name=_('District Korean name'),
        max_length=255,
    )

    slug = models.SlugField(
        verbose_name=_('Slug'),
        help_text=_('A short label containing only letters, numbers, underscores or hyphens for URL'),
        max_length=255,
        db_index=True,
        unique=True,
        allow_unicode=True,
    )

    province = models.ForeignKey(
        'golf.Province',
        verbose_name=_('Province'),
        db_index=True,
        on_delete=models.CASCADE,
    )

    position = models.IntegerField(
        verbose_name=_('Position'),
        default=0,
        db_index=True,
    )

    class Meta:
        verbose_name = _('District')
        verbose_name_plural = _('Districts')

    def __str__(self):
        return f'{self.title_english}'


class Club(model_utils_models.TimeStampedModel):
    HOLE_CHOICES = Choices(
        (0, 'eighteen', _('18 Holes')),
        (1, 'nine', _('9 Holes')),
        (2, 'twentyseven', _('27 Holes')),
        (3, 'thirtysix', _('36 Holes')),
    )

    STATUS_CHOICES = Choices(
        (0, 'open', _('Club open')),
        (1, 'closed', _('Club closed')),
    )

    title_english = models.CharField(
        verbose_name=_('Golf club English name'),
        max_length=255,
        db_index=True,
    )

    title_thai = models.CharField(
        verbose_name=_('Golf club Thai name'),
        max_length=255,
        db_index=True,
    )

    title_korean = models.CharField(
        verbose_name=_('Golf club Korean name'),
        max_length=255,
        db_index=True,
    )

    slug = models.SlugField(
        verbose_name=_('Slug'),
        help_text=_('A short label containing only letters, numbers, underscores or hyphens for URL'),
        max_length=255,
        db_index=True,
        unique=True,
        allow_unicode=True,
    )

    district = models.ForeignKey(
        'golf.District',
        verbose_name=_('District'),
        db_index=True,
        on_delete=models.CASCADE,
    )

    phone = models.CharField(
        verbose_name=_('Phone number'),
        max_length=32,
        blank=True,
        null=True,
    )

    email = models.EmailField(
        verbose_name=_('Email address'),
        max_length=255,
        blank=True,
        null=True,
    )

    fax = models.CharField(
        verbose_name=_('Fax number'),
        max_length=16,
        blank=True,
        null=True,
    )

    website = models.URLField(
        verbose_name=_('Website'),
        max_length=255,
        blank=True,
        null=True,
    )

    address = models.CharField(
        verbose_name=_('Golf club address'),
        max_length=255,
        blank=True,
        null=True,
    )

    distance_from_downtown = models.IntegerField(
        verbose_name=_('Distance from downtown'),
        blank=True,
        null=True,
    )

    estimated_time_from_downtown = models.IntegerField(
        verbose_name=_('Estimated time from downtown'),
        blank=True,
        null=True,
    )

    distance_from_airport = models.IntegerField(
        verbose_name=_('Distance from airport'),
        blank=True,
        null=True,
    )

    estimated_time_from_airport = models.IntegerField(
        verbose_name=_('Estimated time from airport'),
        blank=True,
        null=True,
    )

    hole = models.IntegerField(
        verbose_name=_('No. of holes'),
        choices=HOLE_CHOICES,
        default=HOLE_CHOICES.eighteen,
        db_index=True,
    )

    green_fee_selling_price = models.DecimalField(
        verbose_name=_('Start from'),
        max_digits=11,
        decimal_places=2,
        help_text=_('THB'),
        db_index=True,
    )

    caddie_fee_selling_price = models.DecimalField(
        verbose_name=_('Caddie fee'),
        max_digits=11,
        decimal_places=2,
        help_text=_('THB'),
        db_index=True,
    )

    cart_fee_selling_price = models.DecimalField(
        verbose_name=_('Cart fee'),
        max_digits=11,
        decimal_places=2,
        help_text=_('THB'),
        db_index=True,
    )

    weekday_min_pax = models.IntegerField(
        verbose_name=_('Weekday minimum PAX'),
        default=1,
    )

    weekday_max_pax = models.IntegerField(
        verbose_name=_('Weekday maximum PAX'),
        default=4,
    )

    holiday_min_pax = models.IntegerField(
        verbose_name=_('holiday minimum PAX'),
        default=1,
    )

    holiday_max_pax = models.IntegerField(
        verbose_name=_('holiday maximum PAX'),
        default=4,
    )

    cart_compulsory_pax = models.IntegerField(
        verbose_name=_('Require golf cart pax+'),
        default=0,
        db_index=True,
    )

    cart_compulsory_holiday = models.BooleanField(
        verbose_name=_('Require golf cart on holidays'),
        default=False,
        db_index=True,
    )

    cart_on_fairway = models.BooleanField(
        verbose_name=_('Cart on fairway'),
        default=False,
        db_index=True,
    )

    weekdays_min_in_advance = models.IntegerField(
        verbose_name=_('Weekdays minimum in advance'),
        default=1,
        db_index=True,
    )

    weekdays_max_in_advance = models.IntegerField(
        verbose_name=_('Weekdays maximum in advance'),
        default=30,
        db_index=True,
    )

    weekend_min_in_advance = models.IntegerField(
        verbose_name=_('Weekend minimum in advance'),
        default=1,
        db_index=True,
    )

    weekend_max_in_advance = models.IntegerField(
        verbose_name=_('Weekend maximum in advance'),
        default=7,
        db_index=True,
    )

    latitude = models.DecimalField(
        verbose_name=_('Latitude'),
        max_digits=9,
        decimal_places=6,
        default=0,
    )

    longitude = models.DecimalField(
        verbose_name=_('Longitude'),
        max_digits=9,
        decimal_places=6,
        default=0,
    )

    position = models.IntegerField(
        verbose_name=_('Position'),
        default=0,
        db_index=True,
    )

    status = models.IntegerField(
        verbose_name=_('Club status'),
        choices=STATUS_CHOICES,
        default=STATUS_CHOICES.open,
        db_index=True,
    )

    class Meta:
        verbose_name = _('Golf club')
        verbose_name_plural = _('Golf clubs')

    def __str__(self):
        return f'{self.title_english} {self.email} {self.phone}'
