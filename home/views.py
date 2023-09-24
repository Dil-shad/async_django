from django.http import HttpResponse
import time,asyncio
from movies.models import Movie
from stories.models import Story

from asgiref.sync import sync_to_async


# helper functions
def get_movies():
    print('prepare to get movies')
    time.sleep(2)
    qs = Movie.objects.all()
    print(qs)
    print('got all movies')


def get_stories():
    print('prepare to get stories')
    time.sleep(5)
    qs = Story.objects.all()
    print(qs)
    print('got all stories')


###############################################################


@sync_to_async
def get_movies_async():
    print('prepare to get movies')
    asyncio.sleep(2)
    qs = Movie.objects.all()
    print(qs)
    print('got all movies')


@sync_to_async
def get_stories_async():
    print('prepare to get stories')
    asyncio.sleep(5)
    qs = Story.objects.all()
    print(qs)
    print('got all stories')

################################################################


def home_view(request):
    return HttpResponse("hello World!")


def main_view(request):
    start_time = time.time()
    get_movies()
    get_stories()
    total = (time.time() - start_time)
    print("Total time", total)
    return HttpResponse('sync')
    #Total time 7.0239105224609375

# Note
""" 
When creating async await functions(without the sync_to_async decorator) 
instead of 'time.sleep(x)'we should use await 'asyncio.sleep(x)' instead.
"""

async def main_view_async(request):
    start_time = time.time()
    # task1=asyncio.ensure_future(get_movies_async())
    # task2=asyncio.ensure_future(get_stories_async())
    # await asyncio.wait([task1,task2])
    #easy way 
    await asyncio.gather(get_stories_async(),get_movies_async())
    total = (time.time() - start_time)
    print("Total time", total)
    return HttpResponse('async')
    #7.002111911773682
    
    
