from django.shortcuts import redirect, render
from django.http import HttpResponse

from . import models
from .forms import LaboratorioForm

# Create your views here.}+
#GET
def list_laboratorio(request):
    if 'numvisitas' in request.session:
        num = request.session["numvisitas"]
    else:
        num = 0
    
    request.session["numvisitas"] = num + 1
    labs = models.Laboratorio.objects.all().order_by('id')

    context =   {   'numvisitas' : request.session["numvisitas"],
                    'labs' : labs,  
                }

    return render(request, 'index.html', context)
#POST
def new_laboratorio(request):
    data = {
        'form': LaboratorioForm()
    }

    if request.method == 'POST':
        formulario = LaboratorioForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('list_laboratorio')
        else:
            data["form"] = formulario
    return render(request, 'laboratorio/add.html', data)
#PUT
def update_laboratorio(request, id):
    lab_id = models.Laboratorio.objects.get(id = id)

    if request.method == 'POST':
        data = request.POST.copy()
        formulario = LaboratorioForm(data, instance = lab_id)
        if formulario.is_valid():
            formulario.save()
        return redirect('list_laboratorio')
    else:
        context = { 'form': LaboratorioForm(instance = lab_id) }
    return render(request, 'laboratorio/update.html', context)
#DELETE
def delete_laboratorio(request, id):
    if request.method == 'POST':
        from .models import Producto, DirectorGeneral
        Producto.objects.filter(laboratorio = id).delete()
        DirectorGeneral.objects.filter(laboratorio = id).delete()

        models.Laboratorio.objects.get(id = id).delete()
        return redirect('list_laboratorio')
    
    lab = models.Laboratorio.objects.get(id=id)
    context = {'lab' : lab}
    return render(request, 'laboratorio/delete.html', context)