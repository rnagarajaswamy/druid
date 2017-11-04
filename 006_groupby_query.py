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
  
    # defining the query object and rules
    group = client.groupby(
                datasource='wikiticker',
                granularity='day',
                intervals='2015-09-01/2015-09-13',
                dimensions=["regionName", "page"],
                #filter=~(Dimension("reply_to_name") == "Not A Reply"),
                aggregations={"count": longsum("count")},
                context={"timeout": 10000},
                limit_spec={
                                "type": "default",
                                "limit": 50,
                                "columns" : ["count"]
                            }                
    )
    # printing the result
    for k in range(2):
        print(group[k])
        
# print the exception if any
except Exception as e:
    print("Erro : {0}".format(e))
             