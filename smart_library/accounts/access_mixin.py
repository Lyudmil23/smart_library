from django.contrib.auth.mixins import UserPassesTestMixin


class CustomAccessMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return obj.pk == self.request.user.pk
