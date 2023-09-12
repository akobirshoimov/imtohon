from django.urls import path
from .views import AllKitob,DetailKitob,UpdateKitob,CreateKitob,DeleteKitob,AllAvtor,DetailAvtorlar,CreateAvtorlar,UpdateAvtorlar,DeleteAvtorlar,get_book

urlpatterns = [
    #kitoblar
    path('all/',AllKitob.as_view()),
    path('get_book/<int:avtor_id>/',get_book.as_view()),
    path('detail_kitob/<int:kitob_id>/',DetailKitob.as_view()),
    path('update_kitob/<int:kitob_id>/',UpdateKitob.as_view()),
    path('create_kitob/',CreateKitob.as_view()),
    path('delete_kitob/<int:kitob_id>/',DeleteKitob.as_view()),
    #avtorlar
    path('all_avtor/',AllAvtor.as_view()),
    path('detail_avtor/<int:avtor_id>/',DeleteAvtorlar.as_view()),
    path('update_avtor/<int:avtor_id>/',UpdateAvtorlar.as_view()),
    path('create_avtor/',CreateAvtorlar.as_view()),
    path('delete_avtor/<int:avtor_id>/',DeleteAvtorlar.as_view())
]