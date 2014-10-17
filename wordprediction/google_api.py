import httplib2
import pprint
import sys

#  from apiclient.discovery import build
from googleapiclient.discovery import build
#  from apiclient.errors import HttpError
from googleapiclient.errors import HttpError

from oauth2client.client import AccessTokenRefreshError
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client import tools


# Enter your Google Developer Project number
PROJECT_NUMBER = '374337386391'

FLOW = flow_from_clientsecrets(
    '../client_secret.json',
    scope='https://www.googleapis.com/auth/bigquery'
)


def main():
    storage = Storage('bigquery_credentials.dat')
    credentials = storage.get()

    if credentials is None or credentials.invalid:
        # Run oauth2 flow with default arguments.
        credentials = tools.run_flow(FLOW, storage,
                                     tools.argparser.parse_args([]))

    http = httplib2.Http()
    http = credentials.authorize(http)

    bigquery_service = build('bigquery', 'v2', http=http)

    try:
        query_request = bigquery_service.jobs()
        query = "SELECT * FROM [publicdata:samples.trigrams] WHERE first = 'have' AND second = 'a' AND thid = 'smoking' IGNORE CASE;"
        query_data = {
            'query': query
        }
        query_response = query_request.query(projectId=PROJECT_NUMBER,
                                             body=query_data).execute()
        print 'Query Results:'
        for row in query_response['rows']:
            result_row = []
            for field in row['f']:
                result_row.append(field['v'])
            print ('\t').join(result_row)

    except HttpError as err:
        print 'Error:', pprint.pprint(err.content)

    except AccessTokenRefreshError:
        print ("Credentials have been revoked or expired, please re-run"
               "the application to re-authorize")


if __name__ == '__main__':
    main()
