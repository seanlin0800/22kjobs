from flask import Blueprint, request
from flask.ext import restful
from flask.ext.restful import fields, reqparse

from .. import models
from ..common.fields import DateTimeISO

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
    'posted': DateTimeISO,
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
        jobs = models.Job.query.all()
        return {'jobs': [restful.marshal(job, job_fields) for job in jobs]}

    def post(self):
        args = self.parser.parse_args()
        job = models.Job(
            name=args['name'],
            position=args['position'],
            addr=args['addr'],
            min_wage=args['min_wage'],
            max_wage=args['max_wage'],
            description=args['description'],
        )
        models.db.session.add(job)
        models.db.session.commit()
        return {'job': {'id': job.id}}


class JobView(restful.Resource):

    def get(self, id):
        job = models.Job.query.get_or_404(id)
        return {'job': restful.marshal(job, job_fields)}

    def delete(self, id):
        job = models.Job.query.get_or_404(id)
        models.db.session.delete(job)
        models.db.session.commit()
        return {'result': True}


api.add_resource(JobListView, '/jobs', endpoint='jobs')
api.add_resource(JobView, '/jobs/<int:id>', endpoint='job')
