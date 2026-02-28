import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Place, Rating
def get_places(request):
    places = Place.objects.all()

    # 🔹 Filters
    if request.GET.get("ramp") == "true":
        places = places.filter(has_ramp=True)

    if request.GET.get("elevator") == "true":
        places = places.filter(has_elevator=True)

    if request.GET.get("toilet") == "true":
        places = places.filter(has_accessible_toilet=True)

    data = []
    for place in places:
        data.append({
            "id": place.id,
            "name": place.name,
            "location": place.location,
            "has_ramp": place.has_ramp,
            "has_elevator": place.has_elevator,
            "has_accessible_toilet": place.has_accessible_toilet,
            "average_rating": place.average_rating
        })

    return JsonResponse(data, safe=False)

@csrf_exempt
def add_place(request):
    if request.method == "POST":
        body = json.loads(request.body)

        place = Place.objects.create(
            name=body.get("name"),
            location=body.get("location"),
            has_ramp=body.get("has_ramp", False),
            has_elevator=body.get("has_elevator", False),
            has_accessible_toilet=body.get("has_accessible_toilet", False),
        )

        return JsonResponse({"message": "Place added", "id": place.id})

    return JsonResponse({"error": "Invalid request"})


@csrf_exempt
def add_rating(request, place_id):
    if request.method == "POST":
        body = json.loads(request.body)

        place = Place.objects.get(id=place_id)

        Rating.objects.create(
            place=place,
            rating=body.get("rating"),
            comment=body.get("comment", "")
        )

        return JsonResponse({"message": "Rating added"})

    return JsonResponse({"error": "Invalid request"})