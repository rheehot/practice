# Debian - Flask + Mod_Wsgi API

* Original repo; [https://github.com/Craicerjack/apache-flask](https://github.com/Craicerjack/apache-flask)
* Execution
  ```
  $ docker run --rm -p 80:80 --name test-apache-flask apache-flask

  $ curl http://localhost
  Welcome

  $ curl http://localhost/count
  count

  $ curl http://localhost/select/123
  select id 123

  $ curl http://localhost/delete/123
  delete id 123

  $ curl -XPUT http://localhost/insert/123 -F sentence="값"
  insert id 123 값

  $ curl http://localhost/stop
  stop
  ```
* Installation `docker build -t apache-flask:latest .`