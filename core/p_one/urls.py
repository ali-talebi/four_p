from django.urls import path 
from .views import total_p1_methods,p1_method_select,p1_method_amel_scores


urlpatterns = [
    path('api/v1/p1_grading/',total_p1_methods.as_view(),name="total_p1_grading"),
    path('api/v1/p1_select_method/<int:method_id>/',p1_method_select.as_view(),name="p1_select_method"),
    path('api/v1/p1_method_avamel_amel_scores/<int:method_id>/<int:amel_id>/',p1_method_amel_scores.as_view()),

]