from django.views.generic import TemplateView

class TestPage(TemplateView):
    template_name = 'test.html'

class ThankPage(TemplateView):
    template_name = 'thank.html'

class HomePage(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse("test"))
        return super().get(request, *args, **kwargs)
