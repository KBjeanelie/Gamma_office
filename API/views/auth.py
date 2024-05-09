from API.serializers.auth_serializer import LoginSerializer, PasswordChangeSerializer, PasswordResetSerializer, UtilisateurSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


class GetAllStatusView(APIView):
    """

    Args:
        APIView (_type_): CETTE CLASSE DE VUE PERMET DE LISTER TOUTES LES STATUS DES AGENTS DE L'APPLICATION
    """
    def get(self, request):
        return Response({
            'statut_agent_reception': 'Agent reception',
            'statut_agent_regisseur':'Agent regisseur',
            'statut_agent_charge_de_diplome':'Agent chargé de diplôme',
            'statut_agent_de_verification':'Agent de vérification',
            'statut_agent_de_production':'Agent de production',
            'statut_agent_de_distribution':'Agent de distribution'
        })
    

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        refresh_token = request.data.get('refresh')
        if refresh_token:
            try:
                RefreshToken(refresh_token).blacklist()
                return Response(status=status.HTTP_205_RESET_CONTENT)
            except Exception as e:
                return Response({'error': 'Invalid refresh token'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Refresh token is required'}, status=status.HTTP_400_BAD_REQUEST)

class PasswordResetView(APIView):
    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)

class PasswordChangeView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = PasswordChangeSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)

class AccountEditView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def put(self, request):
        instance = self.get_object()
        serializer = UtilisateurSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class ProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = UtilisateurSerializer(request.user)
        return Response(serializer.data)
