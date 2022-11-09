# Flask Test Data Lab

Para correr el serivdor flask, es recomendable tener instalado Docker.
Después de clonar el repositorio, vas a ejecutar los siguientes comandos:

```bash
sudo docker build -t flask_test .
```


```bash
sudo docker run -p 5000:5000 flask_test
```