from .forms import PostSearchForm


def add_variable_to_context(request):
    return {
        'search_form': PostSearchForm()
    }