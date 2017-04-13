#!/usr/bin/env python3

import os

default_config = (
    '8bit-dns',
    'allow-axfr-ips',
    'allow-dnsupdate-from',
    'allow-notify-from',
    'allow-recursion',
    'allow-unsigned-notify',
    'allow-unsigned-supermaster',
    'also-notify',
    'any-to-tcp',
    'api',
    'api-key',
    'api-readonly',
    'cache-ttl',
    'carbon-interval',
    'carbon-ourname',
    'carbon-server',
    'default-ksk-algorithms',
    'default-ksk-size',
    'default-soa-edit',
    'default-soa-edit-signed',
    'default-soa-mail',
    'default-soa-name',
    'default-ttl',
    'default-zsk-algorithms',
    'default-zsk-size',
    'direct-dnskey',
    'disable-axfr',
    'disable-axfr-rectify',
    'disable-syslog',
    'disable-tcp',
    'distributor-threads',
    'dname-processing',
    'dnssec-key-cache-ttl',
    'dnsupdate',
    'do-ipv6-additional-processing',
    'domain-metadata-cache-ttl',
    'edns-subnet-processing',
    'entropy-source',
    'forward-dnsupdate',
    'guardian',
    'launch',
    'local-address',
    'local-address-nonexist-fail',
    'local-ipv6',
    'local-ipv6-nonexist-fail',
    'local-port',
    'log-dns-details',
    'log-dns-queries',
    'logging-facility',
    'loglevel',
    'master',
    'max-cache-entries',
    'max-ent-entries',
    'max-nsec3-iterations',
    'max-queue-length',
    'max-signature-cache-entries',
    'max-tcp-connections',
    'negquery-cache-ttl',
    'no-shuffle',
    'non-local-bind',
    'only-notify',
    'out-of-zone-additional-processing',
    'outgoing-axfr-expand-alias',
    'overload-queue-length',
    'prevent-self-notification',
    'query-cache-ttl',
    'query-local-address',
    'query-local-address6',
    'query-logging',
    'queue-limit',
    'receiver-threads',
    'recursive-cache-ttl',
    'recursor',
    'retrieval-threads',
    'reuseport',
    'security-poll-suffix',
    'server-id',
    'signing-threads',
    'slave',
    'slave-cycle-interval',
    'slave-renotify',
    'soa-expire-default',
    'soa-minimum-ttl',
    'soa-refresh-default',
    'soa-retry-default',
    'tcp-control-address',
    'tcp-control-port',
    'tcp-control-range',
    'tcp-control-secret',
    'traceback-handler',
    'trusted-notification-proxy',
    'udp-truncation-threshold',
    'version-string',
    'webserver',
    'webserver-address',
    'webserver-allow-from',
    'webserver-password',
    'webserver-port',
    'webserver-print-arguments',
    'xfr-max-received-mbytes',
    'gmysql-activate-domain-key-query',
    'gmysql-add-domain-key-query',
    'gmysql-any-id-query',
    'gmysql-any-query',
    'gmysql-basic-query',
    'gmysql-clear-domain-all-keys-query',
    'gmysql-clear-domain-all-metadata-query',
    'gmysql-clear-domain-metadata-query',
    'gmysql-dbname',
    'gmysql-deactivate-domain-key-query',
    'gmysql-delete-comment-rrset-query',
    'gmysql-delete-comments-query',
    'gmysql-delete-domain-query',
    'gmysql-delete-empty-non-terminal-query',
    'gmysql-delete-names-query',
    'gmysql-delete-rrset-query',
    'gmysql-delete-tsig-key-query',
    'gmysql-delete-zone-query',
    'gmysql-dnssec',
    'gmysql-get-all-domain-metadata-query',
    'gmysql-get-all-domains-query',
    'gmysql-get-domain-metadata-query',
    'gmysql-get-order-after-query',
    'gmysql-get-order-before-query',
    'gmysql-get-order-first-query',
    'gmysql-get-order-last-query',
    'gmysql-get-tsig-key-query',
    'gmysql-get-tsig-keys-query',
    'gmysql-group',
    'gmysql-host',
    'gmysql-id-query',
    'gmysql-info-all-master-query',
    'gmysql-info-all-slaves-query',
    'gmysql-info-zone-query',
    'gmysql-innodb-read-committed',
    'gmysql-insert-comment-query',
    'gmysql-insert-empty-non-terminal-order-query',
    'gmysql-insert-record-query',
    'gmysql-insert-zone-query',
    'gmysql-list-comments-query',
    'gmysql-list-domain-keys-query',
    'gmysql-list-query',
    'gmysql-list-subzone-query',
    'gmysql-master-zone-query',
    'gmysql-nullify-ordername-and-update-auth-query',
    'gmysql-nullify-ordername-and-update-auth-type-query',
    'gmysql-password',
    'gmysql-port',
    'gmysql-remove-domain-key-query',
    'gmysql-remove-empty-non-terminals-from-zone-query',
    'gmysql-search-comments-query',
    'gmysql-search-records-query',
    'gmysql-set-domain-metadata-query',
    'gmysql-set-tsig-key-query',
    'gmysql-socket',
    'gmysql-supermaster-name-to-ips',
    'gmysql-supermaster-query',
    'gmysql-timeout',
    'gmysql-update-account-query',
    'gmysql-update-kind-query',
    'gmysql-update-lastcheck-query',
    'gmysql-update-master-query',
    'gmysql-update-ordername-and-auth-query',
    'gmysql-update-ordername-and-auth-type-query',
    'gmysql-update-serial-query',
    'gmysql-user',
    'gmysql-zone-lastchange-query',
)

for k in default_config:
    envkey = k.translate(str.maketrans('-', '_')).upper()
    if k == '8bit-dns':
        envkey = 'ALLOW_8BIT_DNS'
    v = os.getenv(envkey)
    if v != None:
        print('%s=%s' % (k, v))