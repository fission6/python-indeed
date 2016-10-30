import urllib.request
import json
from urllib.parse import urlencode
import types , sys


class IndeedApi(object):

    def __init__(self, publisher_id, **kwargs):

        self.publisher_id = publisher_id
        self.base_url = 'http://api.indeed.com/ads/'

    def search(self, query=None, location='US', country_code='us'):

        action = 'apisearch'
        query_params = {
            'q' : query,
            'l' : location,
            'co': country_code,
            'format' : 'json',
            'v' : '2',
            'publisher' : self.publisher_id
        }
#.encode('utf-8') if type(v) is types.UnicodeType else v) \#
#.encode('utf-8') if type(v) is types.UnicodeType else v
        query_params = dict([(k, v) \
                             for (k, v) in query_params.items()])
        query_string = urlencode(query_params)
        service_req = '{0}{1}?{2}'.format(self.base_url, action, query_string)
    #   request = urllib2.urlopen(service_req)
        request = urllib.request.urlopen(service_req)
        results = request.read()
        data = json.loads(results.decode('utf-8'))

        return data

    def job_details(self, job_keys):

        action = 'apigetjobs'
        query_params = {
            'jobkeys' : ','.join(job_keys),
            'format' : 'json',
            'v' : '2',
            'publisher' : self.publisher_id
        }

        query_string = urlencode(query_params)
        service_req = '{0}{1}?{2}'.format(self.base_url, action, query_string)

        request = urllib.request.urlopen(service_req)
        results = request.read()
        data = json.loads(results.decode('utf-8'))

        return data
