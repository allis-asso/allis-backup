FROM       debian:jessie
MAINTAINER "Sebastien DA ROCHA" <seba@asso-allis.org>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update ; apt-get install -y rdiff-backup python3

CMD tail -f /var/log/alternatives.log
