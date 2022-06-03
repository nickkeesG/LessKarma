from lib2to3.pgen2.token import LESS
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

# Select the preferred transport
transport = AIOHTTPTransport(url=LESSWRONG_ENDPOINT, headers=SAMPLE_HEADERS)
# transport = RequestsHTTPTransport(url=LESSWRONG_ENDPOINT, headers=SAMPLE_HEADERS)

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)

offset = 0
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
    num_posts = len(result['posts']['results'])
    if num_posts == 0: # Likely due to no remaining posts, safe to exit loop
        print('Likely no posts remaining, returned {}'.format(num_posts))
        break
    elif num_posts != LIMIT: # May be due to API inconsistency returning less than LIMIT posts despite sufficient posts
        print('Returned less than {} posts, only saved {}!'.format(LIMIT, num_posts))
    elif num_posts == LIMIT: # Expected response
        print('Correctly saved {} posts'.format(LIMIT))
    offset = offset + num_posts
    try:
        with open(filename, 'w') as f:
            json.dump(result['posts'], f)
    except:
        print('Error in writing JSON to file', filename)
        raise Exception
    sleep(12) # To comply with rate limiting
