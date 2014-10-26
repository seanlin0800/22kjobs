from . import models
from .models import db


def job_get(job_id):
    return models.Job.query.get_or_404(job_id)


def job_get_all():
    return models.Job.query.all()


def job_create(values):
    job = models.Job(**values)
    db.session.add(job)
    db.session.commit()
    return job


def job_delete(job_id):
    job = models.Job.query.get_or_404(job_id)
    db.session.delete(job)
    db.session.commit()


def create_all():
    db.create_all()
