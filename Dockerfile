FROM mysql:8.0.31

ENV MYSQL_ROOT_PASSWORD=unmsm_dsw
ENV MYSQL_DATABASE=gestion_citas
ENV MYSQL_USER=g4-dsw
ENV MYSQL_PASSWORD=seminario_fernandez

EXPOSE 3306