from urllib import parse


NEO_USER = 'neo4j'
NEO_PASS = 'collatz'
NEO_URI = 'neo4j://localhost:7687'
NEO_HOST = parse.urlparse(NEO_URI).netloc

NEO_DATABASE_URL = f"neo4j://{NEO_USER}:{NEO_PASS}@{NEO_HOST}"
