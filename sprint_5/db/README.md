## Mysql database
Chart contains replicated mysql database.
Pod with number 0 is master.

## Values
```
replicas:           # number of replicas
host_path_prefix:   # path on host for database data
storage_size:       # storage acquired by database
name:               # name of creared database
username:           # username of created user
password:           # password of created user
root_password:      # root password of db
init_sql:           # string with b initialization script
```

## Important
While uninstalling chart please remove pvc manually