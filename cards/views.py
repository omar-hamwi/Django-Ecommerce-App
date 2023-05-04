
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render 

def home(request):
        return render(request,"cards/home.html")

def home(request):
    return render(request,"cards/base.html")






# class CardCreateView(CreateView):
#     model = Card
#     fields = ["question", "answer", "box"]
#     success_url = reverse_lazy("card-create")


# class CardUpdateView(CardCreateView, UpdateView):
#     success_url = reverse_lazy("card-list")


# class BoxView(CardListView):
#     template_name = "cards/box.html"
#     form_class = CardCheckForm

#     def get_queryset(self):
#         return Card.objects.filter(box=self.kwargs["box_num"])

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["box_number"] = self.kwargs["box_num"]
#         if self.object_list:
#             context["check_card"] = random.choice(self.object_list)
#         return context

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             card = get_object_or_404(Card, id=form.cleaned_data["card_id"])
#             card.move(form.cleaned_data["solved"])

#         return redirect(request.META.get("HTTP_REFERER"))
