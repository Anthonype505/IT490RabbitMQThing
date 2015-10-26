$TTL	604800
@	IN	SOA	ns1.team-murica.com. admin.team-murica.com (
			1		;Serial
			604800		;Refresh
			86400		;Retry
			2419200		;Expire
			604800 )	;Negative Cache TTL

;


; Name Servers
	IN	NS	ns1.team-murica.com.



; Everything else
team-murica.com.		IN	A 	192.168.1.170	;IP address of frontend goes here
ns1.team-murica.com.	IN	A 	192.168.1.150	;Nameserver
