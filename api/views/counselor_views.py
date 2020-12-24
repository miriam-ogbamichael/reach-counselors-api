from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.counselor import Counselor
from ..serializers import CounselorSerializer, UserSerializer

# Create your views here.
class Counselors(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = CounselorSerializer
    def get(self, request):
        """Index request"""
        # Get all the counselors:
        counselors = Counselor.objects.all()
        # Filter the counselors by owner, so you can only see your owned counselors
        # counselors = Counselor.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = CounselorSerializer(counselors, many=True).data
        return Response({ 'counselors': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['counselor']['owner'] = request.user.id
        # Serialize/create counselor
        counselor = CounselorSerializer(data=request.data['counselor'])
        # If the counselor data is valid according to our serializer...
        if counselor.is_valid():
            # Save the created counselor & send a response
            counselor.save()
            return Response({ 'counselor': counselor.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(counselor.errors, status=status.HTTP_400_BAD_REQUEST)

class CounselorDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the counselor to show
        counselor = get_object_or_404(Counselor, pk=pk)
        # Only want to show owned counselors?
        if not request.user.id == counselor.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this counselor')

        # Run the data through the serializer so it's formatted
        data = CounselorSerializer(counselor).data
        return Response({ 'counselor': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate counselor to delete
        counselor = get_object_or_404(Counselor, pk=pk)
        # Check the counselor's owner agains the user making this request
        if not request.user.id == counselor.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this counselor')
        # Only delete if the user owns the  counselor
        counselor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Remove owner from request object
        # This "gets" the owner key on the data['counselor'] dictionary
        # and returns False if it doesn't find it. So, if it's found we
        # remove it.
        if request.data['counselor'].get('owner', False):
            del request.data['counselor']['owner']

        # Locate Counselor
        # get_object_or_404 returns a object representation of our Counselor
        counselor = get_object_or_404(Counselor, pk=pk)
        # Check if user is the same as the request.user.id
        if not request.user.id == counselor.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this counselor')

        # Add owner to data object now that we know this user owns the resource
        request.data['counselor']['owner'] = request.user.id
        # Validate updates with serializer
        data = CounselorSerializer(counselor, data=request.data['counselor'])
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
