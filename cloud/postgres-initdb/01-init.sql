-- Nextcloud
CREATE USER nc_user WITH ENCRYPTED PASSWORD 'nc_db_p@ssword';
CREATE DATABASE nextcloud_db;
GRANT ALL PRIVILEGES ON DATABASE nextcloud_db TO nc_user;

-- Immich
CREATE USER immich_user WITH ENCRYPTED PASSWORD 'immich_db_p@ssword';
CREATE DATABASE immich_db;
GRANT ALL PRIVILEGES ON DATABASE immich_db TO immich_user;
ALTER USER immich_user CREATEDB;
ALTER USER immich_user WITH SUPERUSER;

-- Connect to nextcloud_db and grant schema permissions
\c nextcloud_db;
GRANT ALL ON SCHEMA public TO nc_user;
GRANT CREATE ON SCHEMA public TO nc_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO nc_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO nc_user;

-- Connect to immich_db and grant schema permissions
\c immich_db;
CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS cube;
CREATE EXTENSION IF NOT EXISTS earthdistance;
CREATE EXTENSION IF NOT EXISTS unaccent;
GRANT ALL ON SCHEMA public TO immich_user;
GRANT CREATE ON SCHEMA public TO immich_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO immich_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO immich_user;