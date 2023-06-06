
from rest_framework import serializers
from api.v1.proposal.models import Proposal


class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = ("id", 'first_name', 'last_name', 'father_name', 'phone_number')
        
