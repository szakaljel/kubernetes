export KU_TIME_HOST=0.0.0.0
export KU_TIME_PORT=7000
export KU_TIME_GEO_SERVICE_URL=http://0.0.0.0:8000

export KU_GEO_HOST=0.0.0.0
export KU_GEO_PORT=8000
export KU_GEO_DB_HOST=192.168.39.5
export KU_GEO_DB_PORT=31328
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
