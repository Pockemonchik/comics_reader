#!/bin/sh
#alembic init -t async migrations
# alembic revision -m "initial"
echo "start fastapi app";
echo "";
exec "alembic upgrade head"
exec "$@"