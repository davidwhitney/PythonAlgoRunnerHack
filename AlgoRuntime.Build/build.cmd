SET name=%1
docker build -t %name% .
docker save -o %name%.tar %name%