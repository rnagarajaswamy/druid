## importing library
from pydruid import *
from pydruid.client import *
from pydruid.query import QueryBuilder
from pydruid.utils.postaggregator import *
from pydruid.utils.aggregators import *
from pydruid.utils.filters import *
from pydruid.client import *

try:
    
    # connecting to DRUID    
    client = PyDruid('http://192.168.8.105:8082', 'druid/v2')
    meta = client.segment_metadata(datasource='wikiticker')
    print(meta[0].keys())
    
    #print(meta[0]['columns'])
    bound = client.time_boundary(datasource='wikiticker')
    
    # print the result
    for n in bound:
        print(n)
# print the exception if any
except Exception as e:
    print("Error {0}".format(e))