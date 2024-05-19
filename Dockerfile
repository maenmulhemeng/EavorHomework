# syntax=docker/dockerfile:1

FROM python:alpine as builder

WORKDIR /search_engine
COPY . .
CMD ["python", "eavor_naive_solution.py"]