from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import fake_accounts
from .serializers import AccountSerializer

class AccountView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,*args,**kwargs):

        accounts = fake_accounts.objects#.filter(user = request.user.id)
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)


    def post(self, request, *args,**kwargs):

        data = {
            'firstName': request.data.get('Name'),
            'lastName': request.data.get('LastName'),
            #'creationDate': request.data.get(''),
            'accountEmail': request.data.get('Email'),
            #'accountID': request.data.get(''),
            'fake_ccNumber': request.data.get('ccNumber'),
            'fake_ccIssuer': request.data.get('ccIssuer'),
            'fake_ethereumAddress': request.data.get('ethereumAddress'),
            'fake_currencyName': request.data.get('currencyName'),
            'fake_currencyCode': request.data.get('currencyCode'),
        }
        serializer = AccountSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class AccountsDetailedView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self,account_ID):
        try:
            return fake_accounts.objects.get(id = account_ID)
        except fake_accounts.DoesNotExist:
            return None

    def get(self,request,account_ID,*args,**kwargs):
        fake_accounts_instance = self.get_object(account_ID)
        if not fake_accounts_instance:
            return Response(
                {"res": "Object does not exist"}, status = status.HTTP_404_NOT_FOUND
            )
        serializer = AccountSerializer(fake_accounts_instance)
        return Response(serializer.data,status=status.HTTP_200_OK)



    def put(self, request, account_ID,*args,**kwargs):
        fake_accounts_instance = self.get_object(account_ID)
        if not fake_accounts_instance:
            return Response(
                {"res":"Object does not exist"}, status = status.HTTP_400_BAD_REQUEST
            )
        data = {
            'firstName': request.data.get('Name'),
            'lastName': request.data.get('LastName'),
            #'creationDate': request.data.get(''),
            'accountEmail': request.data.get('Email'),
            #'accountID': request.data.get(''),
            'fake_ccNumber': request.data.get('ccNumber'),
            'fake_ccIssuer': request.data.get('ccIssuer'),
            'fake_ethereumAddress': request.data.get('ethereumAddress'),
            'fake_currencyName': request.data.get('currencyName'),
            'fake_currencyCode': request.data.get('currencyCode'),
        }

        serializer = AccountSerializer(instance=fake_accounts_instance,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,account_ID,*args,**kwargs):
        fake_accounts_instance = self.get_object(account_ID)
        if not fake_accounts_instance:
            return Response(
                {"res": "Object does not exist"},status=status.HTTP_204_NO_CONTENT
            )
        fake_accounts_instance.delete()
        return Response(
                {"res": "Object has been deleted"}, status=status.HTTP_200_OK
            )
