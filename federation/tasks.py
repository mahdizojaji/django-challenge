from celery import shared_task

from federation.models import Stadium, StadiumSeatPlace


@shared_task(ignore_result=True)
def create_stadium_seat_place(stadium_id):
    stadium = Stadium.objects.get(id=stadium_id)
    StadiumSeatPlace.objects.bulk_create([
        StadiumSeatPlace(stadium_seat_id=seat_id, stadium=stadium) for seat_id in range(1, stadium.capacity + 1)
    ])
