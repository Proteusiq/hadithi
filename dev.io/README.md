# Elevate Your Python Skills: Packages That Transformed My Code

A selection of Python packages and tools that are pivotal in my daily coding. From enhancing efficiency to introducing innovative solutions, these packages reshaped how I solve problems using Python. 

In this article, I presented a brief description, highlight primary advantages, and showcase a typical use-case. Additionally, I'll mention alternatives where they exist, giving you a comprehensive view of the tools.



- **Machine Learning**

1. **[scikit-learn](https://scikit-learn.org/stable/)**
   
   - **Description:** Comprehensive library for machine learning algorithms.
   - **Advantage:** Easy to use with consistent API and good documentation.
   - **When to use:** A go-to package for performing standard machine learning tasks like classification, regression, and clustering.
   
```python
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_models import LogisticRegression


numeric_features = ['Salary']
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())])


text_feature = 'ProductDescription'
text_transformer = Pipeline(steps=[
    ('vectorizer', TfidfVectorizer(stop_words="english"))
])

categorical_features = ['Age','Country']
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('txt', text_transformer, text_feature),
        ('cat', categorical_transformer, categorical_features),
        ])

predictor = Pipeline(steps=[('preprocessor', preprocessor),
                  ('classifier', LogisticRegression(solver='lbfgs'))])


# train
predictor.fit(X_train, y_train)

#evaluate and predict

```

3. **[PyMC](https://www.pymc.io/welcome.html)**
   - **Description:** Bayesian modeling and probabilistic machine learning.
   - **Advantage:** Provides tools to define probabilistic models in code.
   - **When to use:** When performing Bayesian analysis or probabilistic programming.
   
```python
import pymc as pm
import xarray as xr


with pm.Model() as model:
    
    # Priors
    alpha = pm.Normal('alpha', mu=0, sd=10)
    beta = pm.Normal('beta', mu=0, sd=10, shape=X_train.shape[1])
    
    # Linear combination
    mu = alpha + xr.dot(X_train, beta)
    
    # Logistic link function
    p = pm.invlogit(mu)
    
    # Likelihood
    y_obs = pm.Bernoulli('y_obs', p=p, observed=y_train)
    
    # Sample/train
    trace = pm.sample(3000)

# Evaluation with posterior predictive checks
# Prediction by drawing samples from the posterior predictive distribution
   ```

4. **[FLAML](https://microsoft.github.io/FLAML/)**
   - **Description:** A fast and lightweight automated machine learning library.
   - **Advantage:** Finds the best ML model with minimal code and time.
   - **When to use:** When you want quick results without deep diving into model tuning.
   
```python
from flaml import AutoML

automl = AutoML()

automl_config = {
    "time_budget": 120,  # time in seconds
    "metric": 'accuracy',
    "task": 'classification',
     "estimator_list": ['lgbm', 'xgboost', 'catboost', 'extra_tree',],
    "seed": 42,
    "log_file_name": "churn.log",
    "log_training_metric": True,
}

automl.fit(X_train=X_train, y_train=y_train, **settings)

# train
automl.fit(X_train, y_train, **automl_config)

# evaluate and predict
```



**CVXPY**
   - **Description:** A Python library for convex optimization.
   - **Advantage:** Provides an intuitive way to define and solve convex optimization problems.
   - **When to use:** When you need to solve optimization problems in various domains like finance, control, signal processing, etc.
   
   ```python
   import cvxpy as cp

   x = cp.Variable()
   objective = cp.Minimize(x**2 + 1)
   constraints = [x >= 0]
   problem = cp.Problem(objective, constraints)
   result = problem.solve()
   ```

---

4. **transformers**
   - **Description:** Natural language processing tasks using deep learning models like BERT.
   - **Advantage:** Pre-trained models and tokenizers for many languages.
   - **When to use:** For NLP tasks like text classification, generation, and translation.
   
   ```python
   from transformers import BertTokenizer
   tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
   ```

- **DL:**

1. **jax**
   - **Description:** Numerical computing library with autograd capabilities.
   - **Advantage:** Enables high-performance machine learning research.
   - **When to use:** Research purposes and when NumPy-like operations with GPU support are needed.
   
   ```python
   import jax.numpy as jnp
   from jax import grad
   gradient = grad(lambda x: x**2)(2.)
   ```

2. **torch (PyTorch)**
   - **Description:** Deep learning library providing tensors and dynamic neural networks.
   - **Advantage:** Dynamic computation graph which is useful for R&D.
   - **When to use:** Deep learning model development and research.
   
   ```python
   import torch.nn as nn
   model = nn.Linear(1, 1)
   ```

- **Data:**

1. **ibis[duckdb]**
   - **Description:** A data analysis framework with tighter integration with databases.
   - **Advantage:** Write more efficient SQL-like queries natively in Python.
   - **When to use:** When querying large datasets directly from Python without writing raw SQL.
   
   ```python
   import ibis
   connection = ibis.duckdb.connect('/path/to/db')
   table = connection.table('my_table')
   ```

2. **Dagster**
   - **Description:** A data orchestrator for building, testing, and deploying workflows.
   - **Advantage:** Enables data observability, testing, and type-checking.
   - **When to use:** Orchestrating and monitoring complex data workflows.
   
   ```python
   import dagster
   @dagster.solid
   def process_data(_): return "data"
   ```

- **Web:**

1. **httpx**
   - **Description:** A fully featured HTTP client.
   - **Advantage:** Async capabilities and connection pooling.
   - **When to use:** Making HTTP requests, especially when async features are needed.
   
   ```python
   import httpx
   response = httpx.get('https://www.example.com')
   ```

2. **FastAPI**
   - **Description:** Modern web framework for building APIs.
   - **Advantage:** Fast, built-in type validation, and async capabilities.
   - **When to use:** Building robust web APIs.
   
   ```python
   from fastapi import FastAPI
   app = FastAPI()
   @app.get('/')
   def read_root(): return {"Hello": "World"}
   ```

3. **playwright-python**
   - **Description:** Browser automation library.
   - **Advantage:** Supports multiple browsers, fast, and reliable.
   - **When to use:** Web scraping, automated testing of web UI.
   
   ```python
   from playwright.sync_api import sync_playwright
   browser = sync_playwright().chromium.launch()
   ```

4. **parsel**
   - **Description:** Library for extracting data from HTML and XML.
   - **Advantage:** Lightweight, and XPath/CSS selectors support.
   - **When to use:** Web scraping tasks.
   
   ```python
   from parsel import Selector
   sel = Selector(text='<a href="#">Click me</a>')
   ```

5. **jmespath**
   - **Description:** Query language for JSON.
   - **Advantage:** Extract and transform elements from JSON documents.
   - **When to use:** When dealing with complex JSON data and needing specific data extraction.
   
   ```python
   import jmespath
   result = jmespath.search('foo.bar', {"foo": {"bar": "baz"}})
   ```

- **Practical:**

5. **pydantic**
   - **Description:** Data validation and settings management using Python type annotations.
   - **Advantage:** Robust and type-safe data validation; integrates seamlessly with FastAPI.
   - **When to use:** When you need to validate data, create data models, or parse configurations.
   
   ```python
   from pydantic import BaseModel

   class User(BaseModel):
       name: str
       age: int = 18

   user = User(name="John")
   ```

---

1. **loguru**
   - **Description:** Simplified logging in Python.
   - **Advantage:** Easier setup, colorful logging.
   - **When to use:** Debugging and logging application behaviors.
   
   ```python
   from loguru import logger
   logger.info('This is an info message')
   ```

2. **Tenacity**
   - **Description:** Retrying library to retry function calls.
   - **Advantage:** Configurable retrying logic.
   - **When to use:** When calling unreliable services or functions.
   
   ```python
   from tenacity import retry
   @retry
   def might_fail(): pass
   ```

3. **watchdog**
   - **Description:** API and shell utilities to monitor file system events.
   - **Advantage:** React to changes in the filesystem in real-time.
   - **When to use:** Monitoring file/directory changes like in auto-reloading tools.

- **Development:**

1. **black**
   - **Description:** Code formatter for Python.
   - **Advantage:** Enforces consistent code style.
   - **When to use:** Before committing or during CI/CD to ensure code consistency.
   
2. **pytest**
   - **Description:** Testing framework.
   - **Advantage:** Simplified syntax, plugins, and fixtures support.
   - **When to use:** Unit testing and integration testing of Python code.

3. **ruff**
   - **Description:** (Assuming this is a library as of my last update in 2021, I wasn't aware of "ruff". You might need to provide its details.)

4. **pre-commit**
   - **Description:** A framework for managing and maintaining pre-commit hooks.
   - **Advantage:** Ensures code meets certain conditions before committing.
   - **When to use:** Code quality checks during the development phase.

---

