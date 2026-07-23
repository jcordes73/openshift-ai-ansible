#psql -d DATABASE -c "SELECT pg_terminate_backend(pg_stat_activity.pid) FROM pg_stat_activity WHERE datname = current_database() AND pg_stat_activity.pid <> pg_backend_pid();"
#dropdb DATABASE
createdb DATABASE
psql -c "alter user postgres with encrypted password 'postgres';"
psql -c "grant all privileges on database DATABASE to postgres;"
