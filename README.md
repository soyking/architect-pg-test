[architect]() test on PostgreSQL and Django

For architect 0.5.6:

```
docker-compose build
docker-compose up -d
sleep 5
docker exec -it architect-pg /bin/bash -c 'python manage.py migrate && python manage.py insert_event'
docker-compose down
```

modify architect in `requirements.txt`, run agin.
