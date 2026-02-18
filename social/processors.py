from .models import Link


def ctx_direct(request):
    icon_map = {
        'LINK_X': 'twitter',
        'LINK_FACEBOOK': 'facebook',
        'LINK_INSTAGRAM': 'instagram',
    }
    links = Link.objects.all()
    social_links = [(link.url, icon_map.get(link.key)) for link in links if link.key in icon_map]
    return {"social_links": social_links}