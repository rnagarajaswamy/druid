## importing library
from pydruid import *
from pydruid.client import *
from pydruid.query import QueryBuilder
from pydruid.utils.postaggregator import *
from pydruid.utils.aggregators import *
from pydruid.utils.filters import *
from pydruid.client import *

# code block starts here 
try:
    # connecting to DRUID
    client = PyDruid('http://192.168.8.105:8082', 'druid/v2')
    #client = PyDruid('http://10.107.1.124:8082', 'druid/v2')
    
    # defining the query object and rules
    bound = client.time_boundary(datasource='wikiticker')
    for d in bound:
        print(d)    
    
except Exception as e:
    print("Error {0}".format(e))
