# The following commands were used to set up a Superset container
docker build -t superset-build .

docker run -d -v ${PWD}:/data:rw -p 8080:8088 -e "SUPERSET_SECRET_KEY=your_new_secret_key" --name superset superset-build

docker exec -it superset superset fab create-admin --username admin --firstname Admin --lastname Superset --email admin@example.com --password admin

docker exec -it superset superset db upgrade

docker exec -it superset superset init
