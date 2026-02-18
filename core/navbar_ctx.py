# Context processor para incluir el menú en todas las vistas
def get_context_global(request):
    menu_items = [
        {'name': 'home', 'url': 'home', 'label': 'Inicio'},
        {'name': 'about', 'url': 'about', 'label': 'Historia'},
        {'name': 'services', 'url': 'services', 'label': 'Servicios'},
        {'name': 'store', 'url': 'store', 'label': 'Visítanos'},
        {'name': 'contact', 'url': 'contact', 'label': 'Contacto'},
        {'name': 'blog', 'url': 'blog', 'label': 'Blog'},
    ]
    return {'menu_items': menu_items}