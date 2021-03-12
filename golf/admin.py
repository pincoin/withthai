from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _


class AreaAdmin(admin.ModelAdmin):
    list_display = ('title_english', 'title_thai', 'title_korean', 'slug', 'position')
    prepopulated_fields = {'slug': ('title_english',)}
    ordering = ('position',)


class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('title_english', 'title_thai', 'title_korean', 'slug', 'area', 'position')
    list_filter = ('area__title_english',)
    prepopulated_fields = {'slug': ('title_english',)}
    ordering = ('area', 'position',)


class DistrictAdmin(admin.ModelAdmin):
    list_display = ('title_english', 'title_thai', 'title_korean', 'slug', 'province', 'position')
    list_filter = ('province__title_english',)
    prepopulated_fields = {'slug': ('title_english',)}
    ordering = ('province', 'position',)


class ClubAdmin(admin.ModelAdmin):
    list_display = ('title_english', 'title_thai', 'title_korean', 'district',
                    'slug', 'hole', 'green_fee_selling_price', 'position')
    list_filter = ('district__province__title_english', 'hole')
    prepopulated_fields = {'slug': ('title_english',)}
    readonly_fields = ('club_link',)
    ordering = ('district', 'position',)

    def club_link(self, obj=None):
        return mark_safe('<a href="{url}">{text}</a>'.format(
            url=reverse('booking:golf-club-booking', args=(obj.slug,)),
            text='{}'.format(obj.title_english),
        ))

    club_link.short_description = _('Golf club')
