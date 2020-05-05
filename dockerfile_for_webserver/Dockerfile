FROM python:3.7.2
USER root

RUN echo 'world!'

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt-get install -y vim less
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

RUN python3 -m pip install mysqlclient
RUN pip install pytest
RUN pip install flask-bcrypt

# httpサーバー設定
RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi
RUN pip install Flask==1.0.3 uWSGI==2.0.18

WORKDIR /app

EXPOSE 9090 9191
USER uwsgi

CMD ./ignition_of_start_page.sh