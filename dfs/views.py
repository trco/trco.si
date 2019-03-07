from django.forms import CheckboxSelectMultiple, CheckboxInput, DateInput
from django.urls import reverse_lazy
from django.views import generic

from funky_sheets.formsets import HotView

from .models import Movie


class Dfs(generic.TemplateView):
    template_name = 'dfs/dfs.html'


class CreateMovieView(HotView):
    model = Movie
    template_name = 'dfs/create_update_movie.html'
    prefix = 'table'
    success_url = reverse_lazy('dfs:update_movie')
    fields = (
        'id',
        'title',
        'director',
        'release_date',
        'parents_guide',
        'imdb_rating',
        'genre',
        'imdb_link',
    )

    factory_kwargs = {
        'widgets': {
            'release_date': DateInput(attrs={'type': 'date'}),
            'genre': CheckboxSelectMultiple(),
            'parents_guide': CheckboxInput(),
        }
    }

    hot_settings = {
        # 'columnSorting': 'true',
        'contextMenu': 'true',
        'autoWrapRow': 'true',
        'rowHeaders': 'true',
        'search': 'true',
        'licenseKey': 'non-commercial-and-evaluation',
    }


class UpdateMovieView(CreateMovieView):
    action = 'update'
    button_text = 'Update'

    hot_settings = {
        # 'columnSorting': 'true',
        'contextMenu': 'true',
        'autoWrapRow': 'true',
        'rowHeaders': 'true',
        'search': 'true',
        'licenseKey': 'non-commercial-and-evaluation',
    }
