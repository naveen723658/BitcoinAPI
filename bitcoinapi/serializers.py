from rest_framework import serializers

from . models import bitcoin

class bitcoinSerializer(serializers.ModelSerializer):
   class Meta:
       model = bitcoin
       fields = ('price', 'timestamp')

