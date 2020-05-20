from .. import app
# from flaskps.app.administration import Workshop, Lesson, Attend
from sqlalchemy import and_

@app.template_filter()
def get_attends_of(student, workshop):
    # Attend.query.filter(
    #     and_(
    #         student_id=student.id, lesson__in=workshop.lessons
    #     )
    # )
    return kasdfasdf'
