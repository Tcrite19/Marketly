-- settings.sql
CREATE DATABASE scoreboard3;
CREATE USER scoreboarduser WITH PASSWORD 'scoreboard';
GRANT ALL PRIVILEGES ON DATABASE scoreboard TO scoreboarduser;