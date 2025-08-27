-- Nextcloud
CREATE USER nc_user WITH PASSWORD 'nc_db_p@ssword';
CREATE DATABASE nextcloud_db OWNER nc_user;
GRANT ALL PRIVILEGES ON DATABASE nextcloud_db TO nc_user;

-- Immich
CREATE USER immich_user WITH PASSWORD 'immich_db_p@ssword';
CREATE DATABASE immich_db OWNER immich_user;
GRANT ALL PRIVILEGES ON DATABASE immich_db TO immich_user;

-- Joplin
CREATE USER joplin_user WITH PASSWORD 'joplin_db_p@ssword';
CREATE DATABASE joplin_db OWNER joplin_user;
GRANT ALL PRIVILEGES ON DATABASE joplin_db TO joplin_user;
