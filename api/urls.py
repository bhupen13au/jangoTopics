from rest_framework import routers
from .views import *


router = routers.SimpleRouter()
router.register(r'employee', EmployeeViewSet)
# router.register(r'artadd', ArticleView.add)
# router.register(r'artget', ArticleView.get)
urlpatterns = router.urls
