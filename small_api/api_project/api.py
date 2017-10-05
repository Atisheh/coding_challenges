from models import Offer
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.paginator import Paginator
from tastypie.utils import trailing_slash
from django.conf.urls import url
from collections import defaultdict
from django.db.models import Count

class OfferResource(ModelResource):

    def prepend_urls(self):
        self._meta.resource_name
        return [
            url(r"^(?P<resource_name>%s)/overview%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('overview'), name="api_overview"),
        ]

    def overview(self, request, **kwargs):
        offers = Offer.objects.all()
        offer_values = offers.values('location', 'category')
        result = defaultdict(list)
        values = offer_values.annotate(Count('category'))
        values = values.order_by('location', 'category__count')

        for item in values:
            result[item['location']].append(item['category'])

        return self.create_response(request, result)

    class Meta:
        queryset = Offer.objects.all()
        resource_name = 'offer'
        # just used for testing, not secure at all
        authorization = Authorization()
        # allow patch too to easily update entries
        allowed_methods = ['get', 'post', 'put', 'patch']
        paginator_class = Paginator
