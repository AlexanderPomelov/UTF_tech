from django.db.models import Count, Q, Prefetch
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import FoodCategory, Food
from .serializers import FoodListSerializer


class FoodView(APIView):
    """
    Для отображения блюд
    """

    def get(self, request, *args, **kwargs):

        # Получаем все блюда где is_publish=True
        food_queryset = Food.objects.filter(is_publish=True)

        # Prefetch для оптимизации загрузки данных
        prefetch = Prefetch('food', queryset=food_queryset)

        # Получение всех категорий с подсчетом количества блюд в категории, если 0 или все блюда is_publish=False,
        # категорию не выводим
        categories = FoodCategory.objects.prefetch_related(prefetch).annotate(
            num_published_foods=Count('food', filter=Q(food__is_publish=True))
        ).filter(num_published_foods__gt=0, food__isnull=False)

        serializer = FoodListSerializer(categories, many=True)
        return Response(serializer.data)
