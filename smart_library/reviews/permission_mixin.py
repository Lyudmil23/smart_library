from django.core.exceptions import PermissionDenied


class PermissionRequiredMixin:
    def get_object(self, queryset=None):
        review = super().get_object()
        if review.user != self.request.user:
            raise PermissionDenied
        return review