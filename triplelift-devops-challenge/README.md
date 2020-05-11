# DevOps Challenge

Complete both Module A and Module B to the best of your abilities. Solutions will be evaluated on the basis of correctness, time complexity and use of tests. Document your solutions with code comments and additions to this readme.

When solving the problems below use Java, Python or JavaScript.

Tips: Break down the problem into simpler methods/functions. Make it right, then make it efficient. State your assumptions.


## Module A - Primes

### Background

From Wikipedia: A prime number is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers. A natural number greater than 1 that is not prime is called a composite number.

[https://en.wikipedia.org/wiki/Prime_number](https://en.wikipedia.org/wiki/Prime_number)

For the sections below create a folder called `/primes` in this project and save your work there.

#### Part 1: Is it a prime?

Create an `is_prime(n)` method/function that checks if a number is prime or not, it can return a boolean or integer either 0 or 1. 

#### Part 2: Rotatable composites

A number can be considered an "rotatable composite" if every rotation of digits is also a composite number. 192 is one of these numbers since each rotation is also a composite number: 192, 921, 219.

How many "rotatable composite" numbers are there from 1 to 100000?

#### Part 3: Unit tests...

Write unit tests to validate in Part 1 that `is_prime(n)` works and in Part 2 your solution is correct.



## Module B - Docker

### Background

 Knowledge of Docker and how to build a microservice is required to complete these exercises. When completing tasks make sure to test work before submitting, it should work for us too. Part 1 requires some knowledge of Python but feel free to implement the rest in any other language.

### Submitting work

When complete merge all commits into a single commit and create a compressed zip archive. Follow the instructions given by your recruiting contact for sending this file. Good luck!



### Exercises

#### Part 1: Dockerize it

You're working with a development team that's completely new to Docker. They hand you a Python service ([Flask](http://flask.pocoo.org/)) called Hello `app/hello.py` and need you to help them Dockerize it. They have an incomplete `docker-compose.yml` file. The app will use `nginx` as a reverse proxy to access internal endpoints that should not be accessible from outside of Docker. The internal endpoints run on port `8080` but `nginx` will run on port `80`.

Tasks
1. Create a Dockerfile for Hello `app/hello.py`, it should run command `python -m flask run` on port `8080`.
2. Modify `docker-compose.yml` and `nginx/default.conf` so that `nginx` proxies requests  on port `80`.
3. Run `docker-compose up` and verify that the service is working as it should.

When complete you should be able to do the following:
```bash
$ curl localhost/
{'msg':'Hello, World!'}
$ curl localhost/baz
{'msg':'Hello, Baz!'}
```

#### Part 2: Collect some metrics

Luckily the development team implemented a simple health check endpoint at `/health`. This returns the latency of the past request (random floating point number) and if the latency exceeds a certain threshold it marks the service unhealthy.

Metrics response example:
```bash
$ curl localhost/health
{'healthy':true,'latency':0.7978267010781679}
```

Create a sidecar container that will gather insights and perform health checks against the metrics endpoint of the Hello service. This service should be defined in the `docker-compose.yml` file. All logging should print to `stdout`. The sidecar should do the following:

1. Poll `/health` on Hello every minute (10 seconds)
2. Print the best, worst and average request latency of the past minute (60 seconds).
3. Print an alert message if `/health` returns a non 200 HTTP code or `healthy` is `False`.

#### Part 3: Deploying 'Hello'

The development team is happy with the changes made to the project and now need to deploy it to production. Describe different ways this service could be deployed. How could it be deployed without any downtime?
