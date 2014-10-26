from flask import Blueprint, request
from flask.ext import restful
from flask.ext.restful import fields, reqparse

from server.api.common import fields as custom_fields
from server.db import api as db_api

blueprint = Blueprint('v1', __name__)
api = restful.Api(blueprint, catch_all_404s=True)

job_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'position': fields.String,
    'addr': fields.String,
    'min_wage': fields.Integer,
    'max_wage': fields.Integer,
    'description': fields.String,
    'posted': custom_fields.DateTimeISO,
    'uri': fields.Url('.job', absolute=True)
}


class JobListView(restful.Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=unicode, required=True)
    parser.add_argument('position', type=unicode, required=True)
    parser.add_argument('addr', type=unicode)
    parser.add_argument('min_wage', type=int)
    parser.add_argument('max_wage', type=int)
    parser.add_argument('description', type=unicode, required=True)

    def get(self):
        jobs = db_api.job_get_all()
        return {'jobs': [restful.marshal(job, job_fields) for job in jobs]}

    def post(self):
        args = self.parser.parse_args()
        job = db_api.job_create(args)
        return {'job': {'id': job.id}}, 201


class JobView(restful.Resource):

    def get(self, id):
        job = db_api.job_get(id)
        return {'job': restful.marshal(job, job_fields)}

    def delete(self, id):
        db_api.job_delete(id)
        return {'result': True}


api.add_resource(JobListView, '/jobs', endpoint='jobs')
api.add_resource(JobView, '/jobs/<int:id>', endpoint='job')
