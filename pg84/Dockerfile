FROM ubuntu:12.04

# замена репо на старые,т.к. 12 версия, все остальное по стандарту 
RUN sed -i 's/archive.ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list && \
    sed -i 's/security.ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list

RUN apt-get update && apt-get install -y \
    postgresql-8.4 \
    postgresql-client-8.4 \
    postgresql-contrib-8.4 \
    && rm -rf /var/lib/apt/lists/*

USER postgres

RUN /etc/init.d/postgresql start && \
    psql --command "ALTER USER postgres WITH PASSWORD 'password';" && \
    echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/8.4/main/pg_hba.conf && \
    echo "listen_addresses='*'" >> /etc/postgresql/8.4/main/postgresql.conf

EXPOSE 5432

CMD ["/usr/lib/postgresql/8.4/bin/postgres", "-D", "/var/lib/postgresql/8.4/main", "-c", "config_file=/etc/postgresql/8.4/main/postgresql.conf"]

