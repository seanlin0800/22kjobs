from werkzeug import utils

from server.config import DB_BACKEND

try:
    IMPL = utils.import_string(
        'server.db.{}.api'.format(DB_BACKEND)
    )
except ImportError:
    IMPL = utils.import_string('server.db.sqlalchemy.api')

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
