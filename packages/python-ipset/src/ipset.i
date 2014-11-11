%module ipset
%{
#include <string.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/utsname.h>
#include <arpa/inet.h>
#include <linux/version.h>
#include <linux/netlink.h>



extern void ipset_init(void);
int add_to_ipset(const char *setname, const struct in_addr *ipaddr, int flags, int remove);
 %}


struct in_addr {
	        unsigned long s_addr;
};

extern void ipset_init(void);
int add_to_ipset(const char *setname, const struct in_addr *ipaddr, int flags, int remove);