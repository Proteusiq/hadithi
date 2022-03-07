# Hitchhiker's Guide to the TimeSeries Packages in Python
> Navigating Python Timeseries Packages

"For everything there is a season, and a time for every matter under heaven ..." - Ecclesiastes 3:1-8 .Time Series analysis is exciting and challenging. There exist [dozen of Python packages](https://github.com/lmmentel/awesome-time-series) attempting to make TS more exciting and less challening. From a pool of dozen, I select a few to explore and score are based on the quaility of package documentation and dependencies, github activities, and code simplicity.  

### Coming soon ...



# Featuring:
   * [Pandas-TA](https://github.com/twopirllc/pandas-ta)
   * [Scikit-Learn: Vinalla](https://scikit-learn.org/stable/auto_examples/applications/plot_cyclical_feature_engineering.html#sphx-glr-auto-examples-applications-plot-cyclical-feature-engineering-py)
   * [Sktime](https://github.com/alan-turing-institute/sktime)
   * [Skforecast](https://github.com/JoaquinAmatRodrigo/skforecast)
   * [statsforecast](https://github.com/Nixtla/statsforecast)
   * [Prophet](https://github.com/facebook/prophet)
   * [pmdarima](https://github.com/alkaline-ml/pmdarima)
   * [ETNA](https://github.com/tinkoff-ai/etna)
   * [Darts](https://unit8co.github.io/darts/)
   * [Merlion](https://github.com/salesforce/Merlion)
   * [Kats](https://github.com/facebookresearch/Kats)
   * [FOST](https://github.com/microsoft/FOST)
   * [greykite](https://github.com/linkedin/greykite)
   * [luminaire](https://github.com/zillow/luminaire)
   * [orbit](https://github.com/uber/orbit)
   * [gluon-ts](https://github.com/awslabs/gluon-ts)
   * [tsai](https://github.com/timeseriesAI/tsai)
   * [tsflex](https://github.com/predict-idlab/tsflex)
   * [tsfresh](https://github.com/blue-yonder/tsfresh)
   * [pycaret](https://pycaret.readthedocs.io/en/time_series/api/time_series.html)

## Example of Stock Data

```python
import pandas as pd
import requests
import io

url = 'https://query1.finance.yahoo.com/v7/finance/download/GOOG'
params ={'period1':1538761929,
         'period2':1541443929,
         'interval':'1d',
         'events':'history',
         'crumb':'v4z6ZpmoP98',
        }

r = requests.post(url,data=params)
if r.ok:
    data = r.content.decode('utf8')
    df = pd.read_csv(io.StringIO(data))
```
