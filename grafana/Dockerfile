FROM grafana/grafana:5.3.0

COPY grafana/datasources /etc/grafana/provisioning/datasources/
COPY grafana/dashboards/* /etc/grafana/dashboards/
COPY grafana/dashboards.yml /etc/grafana/provisioning/dashboards/

# ENV GF_PATHS_PROVISIONING=/etc/grafana/provisioning/
