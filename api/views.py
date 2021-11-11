from django.http import HttpResponseBadRequest
from rest_framework.response import Response
from .models import Links
from .serializers import LinkSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
import random
import string


class AllLinkView(APIView):
    def get(self, req, *args, **kwargs):
        links = Links.objects.all()

        serializer = LinkSerializer(links, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class GetShortLinkView(APIView):
    def post(self, req, *args, **kwargs):
        try: 
            content = json.loads(req.body)
        except:
            return HttpResponseBadRequest('Please provide proper data')

        if not content.get('full_link'):
            return HttpResponseBadRequest('Please provide full link')

        s_link = self.get_short_link()

        Links.objects.create(
            short_link=s_link,
            full_link=content.get('full_link')
        )

        return Response({
            'short_link': s_link
        }, status=status.HTTP_200_OK)
    

    def get_short_link(self):
        links = Links.objects.all()

        while True:
            if not links:
                return self.get_random_link()
            for link in links:
                s_link = self.get_random_link()
                if s_link != link.short_link:
                   return s_link


    def get_random_link(self, N=6):
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
        return ''.join(random.choice(chars) for _ in range(N))


class GetFullLinkView(APIView):
    def post(self, req, *args, **kwargs):
        try: 
            content = json.loads(req.body)
        except:
            return HttpResponseBadRequest('Please provide proper data')

        if not content.get('short_link'):
            return HttpResponseBadRequest('Please provide short link')
        

        try:
            data = Links.objects.get(short_link=content.get('short_link'))
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = LinkSerializer(data)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
