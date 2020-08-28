## Geo service
Web application serving geo information. Currently only cities.
Chart contains sanic based application and replicated mysql database

## Values
```
db:
  ...               # database variables, please check db chart for more info
app:
  replicas:         # number of replcas
  image_version:    # image tag version for application
```