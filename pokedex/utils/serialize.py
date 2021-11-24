"""
Helper module to provide utility functions for serializing or deserializing objects
"""
from django.core import serializers
from datetime import datetime
import json
from typing import Dict, Any

from django.http.request import HttpRequest

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
Converts a string with a datetime format into a datetime object.

:raises: Error if the string provided does not correspond to the date time format
"""
def to_datetime(date_t: str) -> datetime:
    return datetime.strptime(date_t, DATETIME_FORMAT)

"""
Converts a request's body (which should be a json object) into a Python dictionary

:raises: Error if the body cannot be correctly parsed
"""
def from_json(request: HttpRequest) -> Dict[str, Any]:
    json_obj = request.body.decode('utf-8')
    post_req = json.loads(json_obj)
    return post_req