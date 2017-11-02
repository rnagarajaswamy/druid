## importing packages
from pydruid import *
from pydruid.client import *
from pylab import plt
from pydruid.query import QueryBuilder
from pydruid.utils.postaggregator import *
from pydruid.utils.aggregators import *
from pydruid.utils.filters import *
from pydruid.client import *

# connect to druid broker node
#query = PyDruid('http://10.107.1.31:8082', 'druid/v2')
query = PyDruid('http://192.168.8.104:8082', 'druid/v2')

#constricting query
try:
	top = query.topn(
		datasource='wikiticker',
		intervals='2015-09-12/2015-09-13',
		granularity='all',
		dimension='page',
		metric='edits',
		threshold=25,
		aggregations={'edits': longsum('count')}
		
		# filers
		#filter=(Dimension('user_lang') == 'en') & (Dimension('first_hashtag') == 'oscars') &
		#       (Dimension('user_time_zone') == 'Pacific Time (US & Canada)') &
		#       ~(Dimension('user_mention_name') == 'No Mention'),
)
except Exception as e:
	print("Error {0}".format(e))

	# storing the output in object
df = query.export_pandas()
print(df)