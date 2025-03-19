from celery import Celery
from flask import Flask
import time
from test import get_query 



# Initialize Flask app
app = Flask(__name__)


app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379/0',  # Redis broker URL
    CELERY_RESULT_BACKEND='redis://localhost:6379/0',  # Redis backend URL
)


def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)
    return celery

celery = make_celery(app)


@celery.task
def compute_similarity(user_email):
    """A simple background task for computing similarity."""
    get_query(user_email.degree,user_email.specialisation)

    #time.sleep(10)  # example for testing
    print(f"Computed similarity for {user_email}")
    return f"Similarity computation for {user_email} completed."


if __name__ == '__main__':
    app.run(debug=True, port=8000)
