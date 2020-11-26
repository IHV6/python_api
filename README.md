## Python API tests with pytest and requests

### SpaceX API documentation
```https://docs.spacexdata.com```

#### Run tests on terminal
```pytest -v```

With printing ```pytest -v -s```

##### Run tests on docker

  docker build -t api_tests .
  docker run --rm api_tests
