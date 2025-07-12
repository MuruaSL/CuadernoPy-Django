from datetime import datetime


#contexto usado para traer el año actual para el footer por ejemplo
def year_processor(request):
    return {'year': datetime.now().year}
