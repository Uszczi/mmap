#!/bin/bash
make sync-deps-prod
make migrate
make run
