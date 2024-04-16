class PaginationMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adding pagination-related context
        context['page_range'] = range(1, context['paginator'].num_pages + 1)
        context['current_page'] = context['page_obj'].number
        return context