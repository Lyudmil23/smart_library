class OrderedQuerysetMixin:
    def get_queryset(self):
        return super().get_queryset().order_by('id')