from lib2to3.pgen2.token import LESS
from shutil import SameFileError
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
# from gql.transport.requests import RequestsHTTPTransport

LESSWRONG_ENDPOINT = "https://www.lesswrong.com/graphql"
EAFORUM_ENDPOINT = "https://forum.effectivealtruism.org/graphql"
SAMPLE_HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}

# Select your transport with a defined url endpoint
transport = AIOHTTPTransport(url=LESSWRONG_ENDPOINT, headers=SAMPLE_HEADERS)
# transport = RequestsHTTPTransport(url=LESSWRONG_ENDPOINT, =SAMPLE_HEADERS)

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)

# Provide a GraphQL query
query = gql(
    """
    {
      posts(input: {
        terms: {
          view: "top"
          limit: 100
          meta: null  # this seems to get both meta and non-meta posts
        }
      }) {
        results {
          _id
          title
          slug
          pageUrl
          postedAt
          baseScore
          voteCount
          meta
          question
          url
          user {
            username
            slug
          }
      }
    }
"""
)

# Execute the query on the transport
result = client.execute(query)
print(result)