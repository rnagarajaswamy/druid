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
    query = PyDruid('http://192.168.8.105:8082', 'druid/v2')
    #client = PyDruid('http://10.107.1.124:8082', 'druid/v2')
    
    # defining the query object and rules
    top = query.topn(
                datasource="wikiticker"
                , granularity="all"
                , intervals=["2015-09-12/2015-09-13"]
                , dimension="regionName"
                , filter=~(Dimension("regionName") == None)
                , aggregations={"edits":longsum("count")}
                , metric="edits"
                , threshold=5
             )  

    #print(json.dumps(top.query_dict, indent=2))  
    print(top.result)
    df = top.export_pandas()
    print(df)
except Exception as e:
    print("Error {0}".format(e))

'''output
{
  "queryType": "topN",
  "dataSource": "wikiticker",
  "granularity": "hour",
  "intervals": [
    "2015-09-12/2015-09-13"
  ],
  "dimension": "regionName",
  "filter": {
    "type": "not",
    "field": {
      "type": "selector",
      "dimension": "regionName",
      "value": null
    }
  },
  "aggregations": [
    {
      "type": "longSum",
      "fieldName": "count",
      "name": "edits"
    }
  ],
  "metric": "edits",
  "threshold": 1
}  '''