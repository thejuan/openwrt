
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

PKG_FIXUP:=autoreconf
PKG_INSTALL:=1
PKG_BUILD_PARALLEL:=1

ifneq ($(CONFIG_EXTERNAL_KERNEL_TREE),"")
PATCH_DIR:=
endif

include $(INCLUDE_DIR)/package.mk
ifeq ($(DUMP),)
  -include $(LINUX_DIR)/.config
endif


define Package/iptables-shared
$(call Package/iptables/Default)
  TITLE:=IPv4 firewall administration tool shared libraries
  MENU:=1
  DEPENDS+= +kmod-ipt-core +libip4tc +libxtables
  SECTION:=net
  CATEGORY:=Network
  SUBMENU:=Firewall
  TITLE:=iptables shared libraries
  URL:=http://netfilter.org/
endef

define Package/iptables-shared/description
OpenWrt statically links the iptables extensions.
This provides them as shared libraries.

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


define Package/iptables-shared/install
	$(INSTALL_DIR) $(1)/usr/lib/iptables
endef

$(eval $(call BuildPackage,iptables-shared))
