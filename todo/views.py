from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/list',
        'Detail': '/detail/int:pk>',
        'Create': '/create',
        'Update': '/update/<int:pk>',
        'Delete': '/delete/<int:pk>'
    }

    return Response(api_urls)


@api_view(['GET'])
def taskList(request):
    print(request.method)
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def detailView(request, pk):
    task = Task.objects.get(pk=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createTask(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['PUT', 'POST'])
def updateTask(request, pk):
    task = Task.objects.get(pk=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteTask(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()

    return Response('Item successfully delete!')
