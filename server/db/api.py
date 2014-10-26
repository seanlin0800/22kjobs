from werkzeug import utils

from server.config import DB_BACKEND

_BACKEND_MAPPING = {
    'sqlalchemy': 'server.db.sqlalchemy.api'
}
IMPL = utils.import_string(_BACKEND_MAPPING.get(DB_BACKEND))
db = IMPL.db


def job_get(job_id):
    return IMPL.job_get(job_id)


def job_get_all():
    return IMPL.job_get_all()


def job_create(values):
    return IMPL.job_create(values)


def job_delete(job_id):
    return IMPL.job_delete(job_id)


def create_all():
    return IMPL.create_all()
