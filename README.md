# Verkauf

git clone https://github.com/Soitzu/Verkauf.git
cd Verkauf/main
docker build -t verkauf .
docker run --detach --name verkauf_formular -p 8083:8080 verkauf
