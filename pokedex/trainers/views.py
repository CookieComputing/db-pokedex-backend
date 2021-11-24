"""
Views for trainer related modules. These can be thought of as DAOs for the models.
"""

from django.http import HttpRequest, HttpResponse, Http404
from django.core import serializers
from django.shortcuts import get_object_or_404
from datetime import datetime
from trainers.models import Trainers
import json
from django.views.decorators.csrf import csrf_exempt

JSONSerializer = serializers.get_serializer("json")
DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%SZ'

"""
Serializes a set of model objects into a JSON array
"""
def to_json(model_objects):
    json_serializer = JSONSerializer()
    return json_serializer.serialize(model_objects)

"""
Serializes a single model object and strips the array wrapper
"""
def to_json_one(model_object):
    json_data = to_json([model_object])
    data = json.loads(json_data)[0]
    return json.dumps(data)

"""
Converts a date of birth string into a datetime object.

:raises: Error if the string provided does not correspond to the date time format
"""
def to_dob(date_t: str) -> datetime:
    return datetime.strptime(date_t, DATETIME_FORMAT)

def assert_post(request: HttpRequest) -> None:
    if request.method != 'POST':
        raise Http404("Expected POST request")

@csrf_exempt
def create_trainer(request: HttpRequest) -> HttpResponse:
    assert_post(request)
    json_obj = request.body.decode('utf-8')
    post_req = json.loads(json_obj)
    new_trainer = Trainers.objects.create(
        first_name=post_req['first_name'],
        last_name=post_req['last_name'],
        username=post_req['username'],
        password=post_req['password'],
        email=post_req['email'],
        date_of_birth=to_dob(post_req['date_of_birth'])
    )
    return HttpResponse(to_json_one(new_trainer))

def find_all_trainers(_: HttpRequest) -> HttpResponse:
    trainers = Trainers.objects.all()
    return HttpResponse(to_json(trainers))

def find_trainer_by_id(_: HttpRequest, trainer_id: int) -> HttpResponse:
    trainer = get_object_or_404(Trainers, pk=trainer_id)
    return HttpResponse(to_json_one(trainer))

@csrf_exempt
def update_trainer(request: HttpRequest, trainer_id: int) -> HttpResponse:
    assert_post(request)
    trainer = get_object_or_404(Trainers, pk=trainer_id)
    json_obj = request.body.decode('utf-8')
    post_req = json.loads(json_obj)

    trainer.first_name = post_req.get('first_name', trainer.first_name)
    trainer.last_name = post_req.get('last_name', trainer.last_name)
    trainer.username = post_req.get('username', trainer.username)
    trainer.password = post_req.get('password', trainer.password)
    trainer.email = post_req.get('email', trainer.email)
    
    if 'date_of_birth' in post_req:
        trainer.date_of_birth = to_dob(post_req['date_of_birth'])

    trainer.save()
    return HttpResponse(to_json_one(trainer))

@csrf_exempt
def delete_trainer(request: HttpRequest, trainer_id: int) -> HttpResponse:
    # Even if there is no data, request should still be a POST
    assert_post(request)

    trainer = get_object_or_404(Trainers, pk=trainer_id)
    trainer.delete()
    return HttpResponse(json.dumps({}))
    