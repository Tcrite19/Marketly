-- settings.sql
CREATE DATABASE scoreboard;
CREATE USER scoreboarduser WITH PASSWORD 'scoreboard';
GRANT ALL PRIVILEGES ON DATABASE scoreboard TO scoreboarduser;