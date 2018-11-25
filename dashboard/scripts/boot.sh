#!/bin/bash
source activate vituin_dashboard
exec gunicorn -b :5000 --access-logfile - --error-logfile - --pythonpath $PWD/lib vituin_dashboard.dashboard:server
