from django.views.generic.edit import CreateView
from cfp.models import Proposal

class ProposalCreate(CreateView):
    model = Proposal
    template_name = 'cfp.html'
    fields = ['first_name', 
              'last_name',
              'email',
              'profile_link',
              'phone',
              'monthly_talk', 
              'category',
              'speaker_bio',
             'talk_title',
             'audience_level',
             'description',
             'abstract',
             'outcomes',
             'talk_history',
             'file_submission',
             'prior_talks']
