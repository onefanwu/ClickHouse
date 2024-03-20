import mindsdb_sdk


con = mindsdb_sdk.connect()
# You can establish a connection to the MindsDB server using the SDK. Here are some examples:
con = mindsdb_sdk.connect('http://127.0.0.1:47334')

# Get a list of databases
databases = con.databases.list()

# Get a specific database
database = databases[0]  # Database type object

# Perform an SQL query
query = database.query('select * from table1')
print(query.fetch())

# Create a table
table = database.tables.create('table2', query)

# Get a project
project = con.projects.proj

# or use mindsdb project
project = con

# Perform an SQL query within a project
query = project.query('select * from database.table join model1')

# Create a view
view = project.views.create('view1', query=query)

# Get a list of views
views = project.views.list()
view = views[0]
df = view.fetch()

# Get a list of models
models = project.models.list()
model = models[0]

# Use a model for prediction
result_df = model.predict(df)
result_df = model.predict(query)

# Create a model
timeseries_options = {
    'order': 'date',
    'window': 5,
    'horizon': 1
}
model = project.models.create(
    'rentals_model',
    predict='price',
    query=query,
    timeseries_options=timeseries_options
)

# Describe a model
model.describe()