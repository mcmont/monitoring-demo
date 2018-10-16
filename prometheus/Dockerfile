FROM prom/prometheus:v2.3.1

COPY ./prometheus/scripts/entrypoint.sh /prometheus/entrypoint.sh

USER root
RUN chmod +x /prometheus/entrypoint.sh && mkdir /prometheus/data

ENTRYPOINT ["/prometheus/entrypoint.sh"]
CMD [""]
