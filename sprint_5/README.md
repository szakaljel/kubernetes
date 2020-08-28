## Sprint 5
Folder contains 4 helm charts:
- museum: Chartmuseum repository
- db: Replicated mysql database
- geo: Geo service
- time: Time service 

## Run museum
```
helm install museum ./museum

# info to add repo to helm
kubectl get services --selector='app=museum-museum'
minikube ip

helm repo add museum http://<ip>:<port>
```

## Publish db package
```
helm package ./db
curl -X POST --data-binary @<tarfile> http://<ip>:<port>/api/charts

# check
helm repo update
helm search repo museum
```

## Install geo application
```
# update url in dependencies may be necessary
helm dependency update ./geo
helm install geo-release ./geo

# test
helm test geo-release
```

## Install time application
```
# if other release name used for geo, please adjust variables
helm install time-release ./time

# test
helm test time-release
```