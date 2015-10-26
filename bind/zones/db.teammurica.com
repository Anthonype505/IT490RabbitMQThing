;
; BIND data file for local loopback interface
;
$TTL	604800
@	IN	SOA	ns1.teammurica.com.  admin.teammurica.com. (
			      3		; Serial
			 604800		; Refresh
			  86400		; Retry
			2419200		; Expire
			 604800 )	; Negative Cache TTL
;
; name servers - NS records
	IN	NS	ns1.teammurica.com.

ns1.tammurica.com.	IN	A	192.168
@	IN	NS	localhost.
@	IN	A	127.0.0.1
@	IN	AAAA	::1
