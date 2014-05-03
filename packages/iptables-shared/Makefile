#
# Copyright (C) 2006-2012 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk
include $(INCLUDE_DIR)/kernel.mk

PKG_NAME:=iptables-shared
PKG_VERSION:=1.4.10
PKG_RELEASE:=5

PKG_MD5SUM:=f382fe693f0b59d87bd47bea65eca198
PKG_SOURCE:=iptables-$(PKG_VERSION).tar.bz2
PKG_SOURCE_URL:=http://www.netfilter.org/projects/iptables/files \
	ftp://ftp.be.netfilter.org/pub/netfilter/iptables/ \
	ftp://ftp.de.netfilter.org/pub/netfilter/iptables/ \
	ftp://ftp.no.netfilter.org/pub/netfilter/iptables/

#TODO: firendly this up
PKG_UNPACK:=. /home/adam/openwrt/include/shell.sh; bzcat /home/adam/OpenWrt-SDK-x86/dl/iptables-1.4.10.tar.bz2 | /bin/tar --strip-components=1 -C /home/adam/OpenWrt-SDK-x86/build_dir/linux-x86_generic/iptables-shared-1.4.10/ -xf -
PKG_FIXUP:=autoreconf
#PKG_INSTALL:=1
PKG_BUILD_PARALLEL:=1


ifneq ($(CONFIG_EXTERNAL_KERNEL_TREE),"")
PATCH_DIR:=
endif

include $(INCLUDE_DIR)/package.mk
#ifeq ($(DUMP),)
  #-include $(LINUX_DIR)/.config
 # include $(INCLUDE_DIR)/netfilter.mk
  #STAMP_CONFIGURED:=$(strip $(STAMP_CONFIGURED))_$(shell $(SH_FUNC) grep 'NETFILTER' $(LINUX_DIR)/.config | md5s)
#endif

define Package/iptables-shared/Default
  SECTION:=net
  CATEGORY:=Network
  SUBMENU:=Firewall
  URL:=http://netfilter.org/
endef


define Package/iptables-shared
$(call Package/iptables-shared/Default)
  TITLE:=IPv4 firewall administration tool
  MENU:=1
  DEPENDS+= +kmod-ipt-core +libip4tc +libxtables
endef

define Package/iptables-shared/description
TODO
endef

TARGET_CPPFLAGS := \
	-I$(PKG_BUILD_DIR)/include \
	-I$(LINUX_DIR)/user_headers/include \
	$(TARGET_CPPFLAGS)

TARGET_CFLAGS += \
	-I$(PKG_BUILD_DIR)/include \
	-I$(LINUX_DIR)/user_headers/include

CONFIGURE_ARGS += \
	--enable-shared \
	--enable-devel \
	$(if $(CONFIG_IPV6),--enable-ipv6,--disable-ipv6) \
	--enable-libipq \
	--with-kernel="$(LINUX_DIR)/user_headers" \
	--with-xtlibdir=/usr/lib/iptables

MAKE_FLAGS := \
	$(TARGET_CONFIGURE_OPTS) \
	COPT_FLAGS="$(TARGET_CFLAGS)" \
	KERNEL_DIR="$(LINUX_DIR)/user_headers/" PREFIX=/usr \
	KBUILD_OUTPUT="$(LINUX_DIR)" 
	#This is what statically links the files we want made dynamic
	#BUILTIN_MODULES="$(patsubst ip6t_%,%,$(patsubst ipt_%,%,$(patsubst xt_%,%,$(IPT_BUILTIN) $(IPT_CONNTRACK-m) $(IPT_NAT-m))))"

define Package/iptables-shared/install
	$(INSTALL_DIR) $(1)/usr/lib/iptables
	$(CP) $(PKG_BUILD_DIR)/extensions/libxt_standard.so $(1)/usr/lib/iptables
	$(CP) $(PKG_BUILD_DIR)/extensions/libipt_DNAT.so $(1)/usr/lib/iptables
endef

$(eval $(call BuildPackage,iptables-shared))

