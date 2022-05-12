FROM liquibase/liquibase:4.9

WORKDIR /liquibase


COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /liquibase/entrypoint.sh
RUN chmod +x /liquibase/entrypoint.sh

COPY . .

ENTRYPOINT ["/liquibase/entrypoint.sh"]