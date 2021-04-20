# using-docker

Este repo tiene como finalidad levantar una imagen de docker donde se instala python 3 y se corre un script que clusteriza un vector con un modelo Kmeans.

## Usage 

```bash
brew install docker
docker build -t "prueba-py" .    
docker run --rm -v "$PWD":/usr/src/app -it prueba-py 
```
