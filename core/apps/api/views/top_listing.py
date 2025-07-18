from django.db.models import Case, When
from core.apps.api.models import ListingModel
from core.apps.api.enums.listing import ListingStatus
import random


# is True
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from core.apps.api.serializers.listing import BaseListingSerializer
from rest_framework.permissions import AllowAny

from itertools import chain
from django.db.models import Case, When
from django.db.models import Case, When, Value, IntegerField
from datetime import date, timedelta



class ListingIsTopView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, type, pk):
        listing = get_object_or_404(ListingModel, pk=pk)
        
        today = date.today()

        if type == "check":
            listing.is_active = True
            listing.is_top = True
            listing.top_start_date = today
            listing.status = ListingStatus.APPROVED
        else:
            listing.is_active = False
            listing.is_top = False
            listing.status = ListingStatus.REJECTED

        if listing.toplisting is None:
            listing.is_top = False
        
        listing.save()
        
        serializer = BaseListingSerializer(listing)
        return Response(serializer.data, status=status.HTTP_200_OK)




def get_sorted_listings(queryset, is_top_count=3):
    top_ids = list(queryset.filter(is_top=True).values_list("id", flat=True))
    random.shuffle(top_ids)
    top_ids = top_ids[:is_top_count]

    preserved = Case(
        *[When(id=pk, then=Value(pos)) for pos, pk in enumerate(top_ids)],
        default=Value(9999),
        output_field=IntegerField()
    )

    return queryset.annotate(top_order=preserved).order_by("top_order", "-created_at")
