
from oscar.apps.promotions.views import HomeView as CoreHomeView

from oscar.core.loading import get_class, get_model
from oscar.apps.catalogue.signals import product_viewed
Category = get_model('catalogue', 'category')
get_product_search_handler_class = get_class(
    'catalogue.search_handlers', 'get_product_search_handler_class')

class HomeView(CoreHomeView):
    context_object_name = "products"
    template_name = 'promotions/home.html'

    def get(self, request, *args, **kwargs):
        try:
            self.search_handler = self.get_search_handler(
                self.request.GET, request.get_full_path(), [])
        except InvalidPage:
            # Redirect to page one.
            messages.error(request, ('The given page number was invalid.'))
            return redirect('promotions:home')
        return super(HomeView, self).get(request, *args, **kwargs)

    def get_search_handler(self, *args, **kwargs):
        return get_product_search_handler_class()(*args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = {}
        ctx['summary'] = ("All products")
        search_context = self.search_handler.get_search_context_data(
            self.context_object_name)
        ctx.update(search_context)
        return ctx
