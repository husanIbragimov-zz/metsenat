from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from apps.account.models import Account


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=128, write_only=True)
    password2 = serializers.CharField(min_length=6, max_length=128, write_only=True)
    phone = serializers.CharField(min_length=9, max_length=13, write_only=True)
    is_physical_person = serializers.BooleanField(default=False)
    is_legal_entity = serializers.BooleanField(default=False)
    is_student = serializers.BooleanField(default=False)

    class Meta:
        model = Account
        fields = ('id',
                  'full_name',
                  'phone',
                  'password',
                  'password2',
                  'is_physical_person',
                  'is_legal_entity',
                  'is_student',
                  )

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise serializers.ValidationError({'success': True,
                                               'message': 'Password did not match, please try again'})
        return attrs

    def create(self, validated_data):
        del validated_data['password2']
        return Account.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(min_length=9, max_length=13, required=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.SerializerMethodField(read_only=True)
    full_name = serializers.CharField(max_length=100, read_only=True)

    def get_token(self, obj):
        user = Account.objects.filter(phone=obj.get('phone')).first()
        return user.token

    def get_full_name(self, obj):
        user = Account.objects.filter(phone=obj.get('phone')).first()
        return user.full_name

    class Meta:
        model = Account
        fields = ('phone', 'password', 'token', 'full_name')

    def validate(self, attrs):
        phone = attrs.get('phone')
        password = attrs.get('password')
        user = authenticate(phone=phone, password=password)
        if not user:
            raise AuthenticationFailed({
                'message': 'Phone or password is not correct'
            })
        if not user.is_active:
            raise AuthenticationFailed({
                'message': 'Account disabled'
            })

        data = {
            'success': True,
            'phone': user.phone,
            'token': user.token,
            'full_name': user.full_name,
        }
        return data


class AccountSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(source='get_gender_display')

    class Meta:
        model = Account
        fields = (
            'id',
            'full_name',
            'phone',
            'gender',
            'date_login',
            'date_created',
            # 'get_physical_person_count',
            # 'get_legal_entity_count',
            # 'get_student_count'
        )
        extra_kwargs = {
            'is_active': {'read_only': True}
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'full_name', 'phone')
