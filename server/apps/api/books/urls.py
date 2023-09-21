from rest_framework.routers import SimpleRouter
from .views import BookViewSet

app_name = "books"

router = SimpleRouter()
router.register("book", BookViewSet, basename="book")

urlpatterns = router.urls
