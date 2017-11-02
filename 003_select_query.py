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
    client = PyDruid('http://192.168.8.104:8082', 'druid/v2')
    
    # defining the query object and rules
    varSelect = client.select(
            datasource='wikiticker',
            dimensions=["regionName"],
            granularity='all',
            intervals=["2015-09-12/2015-09-13"], 
            paging_spec={'pagingIdentifies': {}, 'threshold': 5}            
    )
    
    # print the values in query object
    for d in varSelect:
        print(d)    
    
except Exception as e:
    print("Error {0}".format(e))
# code end here

''' output
{
	'timestamp': '2015-09-12T00:46:58.771Z', 'result': 
	{
		'pagingIdentifiers': {'wikiticker_2015-09-12T00:00:00.000Z_2015-09-13T00:00:00.000Z_2017-11-01T23:46:19.354Z': 4}, 
		'dimensions': ['regionName'], 
		'metrics': ['deleted', 'added', 'count', 'delta', 'user_unique'], 

		'events': [

					{
						'segmentId': 'wikiticker_2015-09-12T00:00:00.000Z_2015-09-13T00:00:00.000Z_2017-11-01T23:46:19.354Z', 'offset': 0, 
						'event': {'timestamp': '2015-09-12T00:46:58.771Z', 'regionName': None, 'deleted': 0, 'added': 36, 'count': 1, 'delta': 36, 'user_unique': 'AQAAAQAAAAOmEA=='}
					}, 

					{
						'segmentId': 'wikiticker_2015-09-12T00:00:00.000Z_2015-09-13T00:00:00.000Z_2017-11-01T23:46:19.354Z', 'offset': 1, 
						'event': {'timestamp': '2015-09-12T00:47:00.496Z', 'regionName': None, 'deleted': 0, 'added': 17, 'count': 1, 'delta': 17, 'user_unique': 'AQAAAQAAAADsAQ=='}
					}, 

					{
						'segmentId': 'wikiticker_2015-09-12T00:00:00.000Z_2015-09-13T00:00:00.000Z_2017-11-01T23:46:19.354Z', 'offset': 2, 
						'event': {'timestamp': '2015-09-12T00:47:05.474Z', 'regionName': 'New South Wales', 'deleted': 0, 'added': 0, 'count': 1, 'delta': 0, 'user_unique': 'AQAAAQAAAAEhAQ=='}
					}, 

					{
						'segmentId': 'wikiticker_2015-09-12T00:00:00.000Z_2015-09-13T00:00:00.000Z_2017-11-01T23:46:19.354Z', 'offset': 3, 
						'event': {'timestamp': '2015-09-12T00:47:08.770Z', 'regionName': None, 'deleted': 0, 'added': 18, 'count': 1, 'delta': 18, 'user_unique': 'AQAAAQAAAAK8Aw=='}
					}, 

					{
						'segmentId': 'wikiticker_2015-09-12T00:00:00.000Z_2015-09-13T00:00:00.000Z_2017-11-01T23:46:19.354Z', 'offset': 4, 
						'event': {'timestamp': '2015-09-12T00:47:11.862Z', 'regionName': None, 'deleted': 0, 'added': 18, 'count': 1, 'delta': 18, 'user_unique': 'AQAAAQAAAABSEA=='}
					}
		]
	}
} '''
    
