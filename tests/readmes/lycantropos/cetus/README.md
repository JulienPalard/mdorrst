## Testing
Plain
```bash
docker-compose -f docker-compose.tests.yml -f docker-compose.db.yml up
```

With debugger
```bash
./set-dockerhost.sh docker-compose -f docker-compose.tests.yml -f docker-compose.db.yml up
```
