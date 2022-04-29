# pull official base image
FROM liquibase/liquibase:4.9

# set work directory
WORKDIR /liquibase

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /liquibase/entrypoint.sh
RUN chmod +x /liquibase/entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/liquibase/entrypoint.sh"]