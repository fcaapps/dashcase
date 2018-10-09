from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import requests

class EmbedToken:
    def __init__(self, report_id, group_id, settings=None):
        self.username = 'powerbi@fernandocastro.onmicrosoft.com'
        self.password = 'Qvpmdace2'
        self.client_id = '2635aae5-0d73-4123-a154-f6ccbeed28e0'
        self.report_id = report_id
        self.group_id = group_id
        if settings is None:
            self.settings = {'accessLevel': 'View', 'allowSaveAs': 'false'}
        else:
            self.settings = settings
        self.access_token = self.get_access_token()
        self.config = self.get_embed_token()

    def get_access_token(self):
        data = {
            'grant_type': 'password',
            'scope': 'openid',
            'resource': r'https://analysis.windows.net/powerbi/api',
            'client_id': self.client_id,
            'username': self.username,
            'password': self.password
        }
        response = requests.post('https://login.microsoftonline.com/common/oauth2/token', data=data)
        return response.json().get('access_token')

    def get_embed_token(self):
        dest = 'https://api.powerbi.com/v1.0/myorg/groups/' + self.group_id \
               + '/reports/' + self.report_id + '/GenerateToken'
        # dest = 'https://api.powerbi.com/v1.0/myorg/groups/' + self.group_id \
        #        + '/dashboards/' + self.report_id + '/GenerateToken'
        embed_url = 'https://app.powerbi.com/reportEmbed?reportId=' \
                    + self.report_id + '&groupId=' + self.group_id
        # embed_url = 'https://app.powerbi.com/dashboardEmbed?dashboardId=' \
        #             + self.report_id + '&groupId=' + self.group_id
        headers = {'Authorization': 'Bearer ' + self.access_token}
        response = requests.post(dest, data=self.settings, headers=headers)
        self.token = response.json().get('token')
        return {'token_orig': self.access_token, 'token': self.token, 'destino': dest, 'setting': self.settings, 'embed_url': embed_url, 'report_id': self.report_id, 'resposta': response.url, 'header': headers}

    def get_report(self):
        headers = {'Authorization': 'Bearer ' + self.token}
        dest = 'https://app.powerbi.com/reportEmbed?reportId=' + self.report_id + \
               '&amp;groupId=' + self.group_id
        # dest = 'https://app.powerbi.com/dashboardEmbed?dashboardId=' + self.report_id + \
        #        '&amp;groupId=' + self.group_id
        response = requests.get(dest, data=self.settings, headers=headers)
        return response


# Create your views here.
@login_required
def vendas(request):
    return render(request, 'vendas.html', {'status_ativo': 'modelos'})

def analise_vendas(request):
    conf = EmbedToken('2835d1ca-48f9-4446-82c5-6dbe0c282881', '41029e6a-f22b-4e0b-a215-8efde20bdc5d')
    token = conf.get_embed_token()
    return render(request, 'analise_vendas.html', {'selectedReport': token.get('report_id'), 'embedToken': token.get('token'), 'embed_url': token.get('embed_url'), 'headers': token.get('header')})
