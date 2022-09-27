from django.urls import  path
from .views import lime, my_list, foods, first_foods, second_foods, third_foods, fourth_foods, fifth_foods, End

urlpatterns = [
    path('', lime),
    path('list/', my_list),
    path('brain/', foods),     #1
    path('first/', first_foods),     #2
    path('second/', second_foods),  #3
    path('third/', third_foods),        #4
    path('fourth/', fourth_foods),    #5
    path('fifth/', fifth_foods),  #6
    path('End/', End)   #7
]