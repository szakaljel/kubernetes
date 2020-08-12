export KU_TIME_HOST=0.0.0.0
export KU_TIME_PORT=7000
export KU_TIME_GEO_SERVICE_URL=http://0.0.0.0:8000

export KU_GEO_HOST=0.0.0.0
export KU_GEO_PORT=8000
export KU_GEO_DB_HOST_READ=192.168.39.144
export KU_GEO_DB_HOST_WRITE=192.168.39.144
export KU_GEO_DB_PORT=32489
export KU_GEO_DB_USER=root
export KU_GEO_DB_PASSWORD=root_password
export KU_GEO_DB_NAME=kube

run_time_server:
	python time/dev_server.py

run_geo_server:
	python geo/dev_server.py

docker_build_time:
	chmod +x time/docker/build.sh
	cd time && ./docker/build.sh

docker_build_geo:
	chmod +x geo/docker/build.sh
	cd geo && ./docker/build.sh

kubernetes_db_up:
	kubectl create secret generic geo-mysql-secret --from-env-file=kubernetes/db/geo_mysql_secret.env --namespace=pgs-upskill
	kubectl create configmap geo-mysql-sql --from-file=geo/db/schema.sql --from-file=geo/db/data.sql --namespace=pgs-upskill
	kubectl apply -f kubernetes/db/geo_pv.yml
	kubectl apply -f kubernetes/db/geo_mysql_service.yml
	kubectl apply -f kubernetes/db/geo_mysql.yml

kubernetes_db_down:
	kubectl delete -f kubernetes/db/geo_mysql.yml
	kubectl delete -f kubernetes/db/geo_mysql_service.yml
	kubectl delete -f kubernetes/db/geo_pv.yml
	kubectl delete configmap geo-mysql-sql --namespace=pgs-upskill
	kubectl delete secret geo-mysql-secret --namespace=pgs-upskill

kubernetes_geo_up:
	kubectl apply -f kubernetes/geo/geo.yml
	kubectl apply -f kubernetes/geo/geo_service.yml

kubernetes_geo_down:
	kubectl delete -f kubernetes/geo/geo_service.yml
	kubectl delete -f kubernetes/geo/geo.yml

kubernetes_time_up:
	kubectl apply -f kubernetes/time/time.yml
	kubectl apply -f kubernetes/time/time_service.yml

kubernetes_time_down:
	kubectl delete -f kubernetes/time/time_service.yml
	kubectl delete -f kubernetes/time/time.yml

kubernetes_namespace_up:
	kubectl create namespace pgs-upskill

kubernetes_namespace_delete:
	kubectl delete namespace pgs-upskill