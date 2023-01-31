# Hitchhiker's Guide to the Data Pipelines Packages in Python 📦
> Navigating Python DAG | Data | ML Packages

### Data Pipelines
* [Dagster](https://github.com/dagster-io/dagster) - 👑 Beautiful UI and CLI that enforces good design 🐙🤗: Brilliant coding experience and concepts: my take [advance scraping](https://github.com/Proteusiq/advance_scraping)
* [Prefect](https://github.com/PrefectHQ/prefect) - 🙈🎮 Less control on server UI 
* [Airflow](https://github.com/apache/airflow) - Doing it well is hard! Powerful, yes. Tested, yes. Three instances 😒 
* [MageAI](https://github.com/mage-ai/mage-ai) - Tries to replace Airflow 
* [Luigi](https://github.com/spotify/luigi) - 👴🏾🧓🏾 UI is lagging.
* [ploomber](https://github.com/ploomber/ploomber) - Pipelines from Notebook 🤷🏿‍♂️
* [Couler](https://github.com/couler-proj/couler) - One ring to unite them (Argo | Tekton | Airflow) 💍
* [Meltano](https://github.com/meltano/meltano) - DataOps 🧇



## ML
* [Flyte](https://github.com/flyteorg/flyte) - 🔋 Beauty though ☁️ deployment is trickier than it should have been
  - [UnionML](https://github.com/unionai-oss/unionml) - Builds on Flyte
* [Sematic](https://github.com/sematic-ai/sematic) - Prototype-to-production ML in days not weeks
* [Kedro](https://github.com/kedro-org/kedro)
* [MLRun](https://github.com/mlrun/mlrun)
* [orchest](https://github.com/orchest/orchest)
* [Metaflow](https://github.com/Netflix/metaflow)
* [ZenML](https://github.com/zenml-io/zenml)
* [ClearML](https://github.com/allegroai/clearml) - Beautiful UI: Every MLOps needs
* [MLFlow](https://github.com/mlflow/mlflow)
* [Seldon](https://github.com/SeldonIO/seldon-core) - Seldon is all ML too
* [bodywork](https://bodywork.readthedocs.io/en/latest/#what-problems-does-bodywork-solve)
* [BentoML](https://github.com/bentoml/BentoML) - 🥷🎁 running FastAPI-like inference with model artefacts 
* [cleanML](https://docs.cleanlab.ai/v2.0.0/) - Modeling /w bad data
* [cortex](https://github.com/cortexlabs/cortex) 
* [truss](https://github.com/basetenlabs/truss) - Serve any model without boilerplate code 

Deephaven



### Extras

* [feast](https://github.com/feast-dev/feast) - feature storage
* [monosi](https://github.com/monosidev/monosi) - Data Observer 
* [nni](https://github.com/microsoft/nni) - NNI (Neural Network Intelligence) - automate Feature Engineering, Neural Architecture Search, Hyperparameter Tuning and Model Compression.
* [Aim](https://github.com/aimhubio/aim) - Experiments tracker

## DV
* [Git Large Files](https://git-lfs.github.com/)
* [mlem](https://github.com/iterative/mlem) - Creator of DVC - Version and Deploy ML models 
* [dvc](https://github.com/iterative/dvc) - 🤗👑 Data Version Control (ML Experiments, Pipelines, Git for data)
* [CML](https://github.com/iterative/cml) - Crestor og DVC - CI/CD for ML
* [dolt](https://github.com/dolthub/dolt) - Git for Data
* [Marquez](https://github.com/MarquezProject/marquez) - Data Lineages 
* [pypyr](https://github.com/pypyr/pypyr/) - automate shell script
* [Evidently](https://github.com/evidentlyai/evidently) - Data Drift 📈


## Data
* [dbt](https://github.com/dbt-labs/dbt-core) - Data Build Tool<br>
* [elementary](https://github.com/elementary-data/elementary) - Data Monitoring 
* [metricsflow](https://github.com/transform-data/metricflow) - Query for Rainbow 🌈 
* [airbytes](https://github.com/airbytehq/airbyte) - [Unites data](https://docs.airbyte.com/quickstart)

# Validation
* [Pandera](https://pandera.readthedocs.io/en/latest/dataframe_schemas.html) - DataFrame Validator
* [great expectations](https://github.com/great-expectations/great_expectations) - Expect the expected
* [re-data](https://github.com/re-data/re-data) - Fix before it's an issue
* [Pandas Profiling](https://github.com/ydataai/pandas-profiling) - profiling Pandas

# CI/CD
* [dagger](https://github.com/dagger/dagger) - CI/CD pipelines that run anywhere

# Microservices Design
* [katana-skipper](https://github.com/katanaml/katana-skipper) - FastAPI, Celery, ML setup 

# Use in Wild
* [streamify](https://github.com/ankurchavda/streamify)

# Containerized ML
* [cog](https://github.com/replicate/cog)

# In DB Modelling 
* [PostgresML](https://github.com/postgresml/postgresml.github.io) - Training in Postgres 🥽
* [Eland](https://github.com/elastic/eland) - ML in Elasticsearch
* [MindsDB](https://github.com/mindsdb/mindsdb) - Database agnostic ML without data migration 

# Extra:

[compress models](https://github.com/VoltaML/voltaML)

# 🦄 ML Pipeline
    (Airbytes - dbt) - [Dagster] - [cleanML] + {Neural Network Intelligence - Features | Feast} - [FastAPI] ->
