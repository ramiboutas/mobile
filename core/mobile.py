from functools import cache

from django.urls import reverse_lazy
from django.utils.functional import cached_property


class MobileApp(object):
    def __init__(
        self,
        title,
        slug,
        description=None,
        keywords=None,
        icon_url=None,
        download_url=None,
        free=True,
        promote_in_modal=True,
        extra_attrs={},
    ) -> None:
        self.slug = slug
        self.free = free
        self.title = title
        self.description = description
        self.icon_url = icon_url
        self.keywords = keywords
        self.promote_in_modal = promote_in_modal
        self.download_url = download_url
        self.extra_attrs = extra_attrs

    @cached_property
    def index_url(self):
        return f"/{self.slug}/"

    def get_absolute_url(self):
        return self.index_url

    @cached_property
    def info_url(self):
        return reverse_lazy("appinfo", kwargs={"slug": self.slug})

    @cached_property
    def privacy_url(self):
        return reverse_lazy("privacy", kwargs={"slug": self.slug})


APPS = (
    MobileApp(
        title="DGT Test anteriores",
        slug="dgt",
        download_url="https://ramiboutas.com/mobile/dgt-tests-anteriores/",
        icon_url="https://ramiboutas.s3.amazonaws.com/stuff/media/mobile/dgt-tests-anteriores/icon/icon.png",
        extra_attrs={
            "credits_text": "Los tests de esta aplicación están extraidos de la página oficial de la DGT....",
            "credits_url": "https://revista.dgt.es/",
        },
    ),
)


@cache
def get_app(slug):
    for app in APPS:
        if app.slug == slug:
            return app
