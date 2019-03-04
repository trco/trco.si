from django.views.generic.base import TemplateView


class Index(TemplateView):
    template_name = 'pages/index.html'


class OpenSourceView(TemplateView):
    template_name = 'pages/open_source.html'


class ProjectsView(TemplateView):
    template_name = 'pages/projects.html'
