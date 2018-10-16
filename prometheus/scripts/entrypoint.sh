#!/bin/sh

echo "Starting Prometheus..."
/bin/prometheus \
    --config.file=/etc/prometheus/prometheus.yml \
    --storage.tsdb.retention=90d \
    --storage.tsdb.path=/prometheus/data \
    --web.console.libraries=/usr/share/prometheus/console_libraries \
    --web.console.templates=/usr/share/prometheus/consoles