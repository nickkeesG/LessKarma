from lib2to3.pgen2.token import LESS
from shutil import SameFileError
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
# from gql.transport.requests import RequestsHTTPTransport
from time import sleep

import json

from gql_schemas import POST_MINIMAL_SCHEMA, get_full_schema

LESSWRONG_ENDPOINT = "https://www.lesswrong.com/graphql"
EAFORUM_ENDPOINT = "https://forum.effectivealtruism.org/graphql"
SAMPLE_HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
LIMIT = 250

# Select your transport with a defined url endpoint
transport = AIOHTTPTransport(url=LESSWRONG_ENDPOINT, headers=SAMPLE_HEADERS)
# transport = RequestsHTTPTransport(url=LESSWRONG_ENDPOINT, =SAMPLE_HEADERS)

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)

offset = 27250
while True:
    filename = 'data/lesswrong_2022-06-03_T11H07M/post_scraping_sort-by-old_offset-{}_limit-{}.json'.format(offset, LIMIT)
    print('Saving posts {} to {} - {}'.format(offset, offset+LIMIT-1, filename))
    # Provide a GraphQL query
    query = gql(get_full_schema(limit=LIMIT, offset=offset))
    # Execute the query on the transport
    try:
        result = client.execute(query)
    except:
        print('Error in API query:', query)
        raise Exception
    try:
        with open(filename, 'w') as f:
            json.dump(result['posts'], f)
    except:
        print('Error in writing JSON to file', filename)
        raise Exception
    num_posts = len(result['posts']['results'])
    if num_posts != LIMIT:
        print('Returned less than {} posts, only saved {}!'.format(LIMIT, num_posts))
        offset = offset + num_posts
    elif num_posts == LIMIT:
        print('Correctly saved {} posts'.format(LIMIT))
        offset = offset + LIMIT
    sleep(12)

# posts = result['posts']['results']
# none_keys = [i for i in posts[0].keys() if posts[0][i] is None and posts[1][i] is None and posts[2][i] is None and posts[3][i] is None and posts[4][i] is None and posts[5][i] is None]
# print(none_keys)