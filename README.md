# PySparkDockerExample
Example PySpark application using docker-compose.

## To run:
Pull the repo and cd into the directory.  Then build the images:
```docker-compose build```

And then run the PySpark job:
```docker-compose run py-spark```

Play around by changing entrypoint.py or add more workers to docker-compose.yml
