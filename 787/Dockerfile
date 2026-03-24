FROM alpine:latest

COPY fav.sh /fav.sh

RUN chmod +x /fav.sh

RUN apk add --no-cache curl

ENTRYPOINT ["/fav.sh"]
