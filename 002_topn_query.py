import pydruid
from pylab import plt

query = PyDruid('http://10.107.1.31:8082', 'druid/v2')

top = query.topn(
    datasource='wikiticker',
    intervals='2015-09-12/2015-09-13',
    granularity='all',
    dimension='page',
    metric='edits',
    threshold=25,
    aggregations={'edits': longsum('count')}
    
    #filter=(Dimension('user_lang') == 'en') & (Dimension('first_hashtag') == 'oscars') &
    #       (Dimension('user_time_zone') == 'Pacific Time (US & Canada)') &
    #       ~(Dimension('user_mention_name') == 'No Mention'),
    
    
)

df = query.export_pandas()
print(df)