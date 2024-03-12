from django.shortcuts import render

from django.http import JsonResponse
from .models import Collaborator
from .serializers import CollaboratorSerializer

from django.shortcuts import render

def index(request):
    # Lógica para renderizar la página de inicio
    return render(request, 'index.html')

def create_collaborator(request):
    if request.method == 'POST':
        # Obtener los datos del formulario enviado en la solicitud POST
        id_colaborador = request.POST.get('id_colaborador')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        dni = request.POST.get('dni')
        estado = request.POST.get('estado')

        # Crear un nuevo objeto Collaborator con los datos recibidos
        collaborator = Collaborator.objects.create(
            id_colaborador=id_colaborador,
            nombre=nombre,
            apellido=apellido,
            dni=dni,
            estado=estado
        )

        # Guardar el colaborador en la base de datos
        collaborator.save()

        # Devolver una respuesta JSON con un mensaje de éxito y los datos del colaborador creado
        serializer = CollaboratorSerializer(collaborator)
        return JsonResponse({'message': 'Collaborator created successfully', 'data': serializer.data}, status=201)
    else:
        # Si la solicitud no es POST, devolver un error indicando que se esperaba una solicitud POST
        return JsonResponse({'error': 'This endpoint expects a POST request to create a collaborator'}, status=400)

def get_collaborators(request):
    collaborators = Collaborator.objects.all()
    serializer = CollaboratorSerializer(collaborators, many=True)
    return JsonResponse(serializer.data, safe=False)

def get_collaborators(request):
    collaborators = Collaborator.objects.all()
    serializer = CollaboratorSerializer(collaborators, many=True)
    return JsonResponse(serializer.data, safe=False)

def get_collaborator(request, collaborator_id):
    collaborator = Collaborator.objects.get(id_colaborador=collaborator_id)
    serializer = CollaboratorSerializer(collaborator)
    return JsonResponse(serializer.data)

def get_collaborators(request):
    collaborators = Collaborator.objects.all()
    return render(request, 'collaborators_list.html', {'collaborators': collaborators})

def update_collaborator(request, collaborator_id):
    try:
        collaborator = Collaborator.objects.get(id_colaborador=collaborator_id)
    except Collaborator.DoesNotExist:
        return JsonResponse({'error': 'Collaborator does not exist'}, status=404)

    if request.method == 'PUT' or request.method == 'PATCH':
        data = request.POST if request.method == 'POST' else request.PUT
        serializer = CollaboratorSerializer(collaborator, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    else:
        return JsonResponse({'error': 'Only PUT or PATCH requests are allowed'}, status=405)

def delete_collaborator(request, collaborator_id):
    collaborator = Collaborator.objects.get(id=collaborator_id)
    collaborator.delete()
    return JsonResponse({'message': 'Collaborator deleted successfully'}, status=204)

