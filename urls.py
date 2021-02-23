# ---------------------------------- [edit] ---------------------------------- #
from django.urls import path

from . import views

# ---------------------------------- [edit] ---------------------------------- #
app_name = 'pybo'
# ---------------------------------------------------------------------------- #

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    # ---------------------------------- [edit] ---------------------------------- #
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    # ---------------------------------------------------------------------------- #

]
