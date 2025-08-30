from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Colaborador
from .forms import ColaboradorForm

class ColaboradorListView(ListView):
    model = Colaborador
    template_name = "colaboradores/colaborador_list.html"
    context_object_name = "colaboradores"
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(Q(nome__icontains=q) | Q(cpf__icontains=q) | Q(matricula__icontains=q))
        return qs

class ColaboradorCreateView(CreateView):
    model = Colaborador
    form_class = ColaboradorForm
    template_name = "colaboradores/colaborador_form.html"
    success_url = reverse_lazy("colaboradores:list")

class ColaboradorUpdateView(UpdateView):
    model = Colaborador
    form_class = ColaboradorForm
    template_name = "colaboradores/colaborador_form.html"
    success_url = reverse_lazy("colaboradores:list")

class ColaboradorDeleteView(DeleteView):
    model = Colaborador
    template_name = "colaboradores/colaborador_confirm_delete.html"
    success_url = reverse_lazy("colaboradores:list")
