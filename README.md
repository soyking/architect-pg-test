[architect]() test on PostgreSQL and Django

For architect 0.5.6:

```
docker-compose build
docker-compose up -d
sleep 5
docker exec -it architect-pg /bin/bash -c 'python manage.py migrate && python manage.py insert_event'
docker-compose down
```

Modify architect in `requirements.txt`, run agin.

Results:

```
architect 0.5.6

insert 100 records in past 365 days cost 38.3402 ms # spent more time to create table
insert 100 records in past 365 days cost 18.8632 ms
insert 100 records in past 365 days cost 18.9523 ms
insert 100 records in past 365 days cost 18.8499 ms
insert 100 records in past 365 days cost 18.9710 ms

use CREATE TABLE IF NOT EXISTS
insert 100 records in past 365 days cost 30.9022 ms
insert 100 records in past 365 days cost 5.7488 ms
insert 100 records in past 365 days cost 5.8311 ms
insert 100 records in past 365 days cost 5.7718 ms
insert 100 records in past 365 days cost 5.8434 ms

```
