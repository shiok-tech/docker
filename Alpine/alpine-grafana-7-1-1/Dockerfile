FROM alpine-timezone:3.12.0

RUN ALPINE_GLIBC_VERSION="latest" && \
    ALPINE_GLIBC_REPO="sgerrand" && \
    ALPINE_GLIBC_PROJ="alpine-pkg-glibc" && \
    apk add --update -t deps wget ca-certificates curl && \
    cd /tmp && \
    wget $(curl -s https://api.github.com/repos/$ALPINE_GLIBC_REPO/$ALPINE_GLIBC_PROJ/releases/$ALPINE_GLIBC_VERSION | grep 'browser_' | egrep 'glibc-.*.apk' | cut -d\" -f4) && \
    apk add --allow-untrusted glibc-*.apk && \
    /usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8 C.UTF-8 || true && \
    echo "export LANG=C.UTF-8" > /etc/profile.d/locale.sh && \
    apk del --purge deps glibc-i18n curl && \
    apk add --update ca-certificates wget && \
    mkdir -p /opt && cd /opt && \
    wget https://dl.grafana.com/oss/release/grafana-7.1.1.linux-amd64.tar.gz && \
    tar -xzf grafana-*linux-amd64.tar.gz && \
    rm -rf /tmp/* /var/cache/apk/* /opt/*tar.gz && \
    mv grafana-* grafana
    
EXPOSE 3000

CMD /opt/grafana/bin/grafana-server --homepath=/opt/grafana cfg:default.paths.data=/opt/grafana/data cfg:default.paths.logs=/var/log/grafana cfg:default.paths.plugins=/opt/grafana/public/app/features/plugins web