#
# Copyright (C) 2007-2008 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=pypcap
PKG_VERSION:=1.1
PKG_RELEASE:=6

PKG_SOURCE:=v$(PKG_VERSION).$(PKG_RELEASE).zip
PKG_SOURCE_URL:=https://github.com/pynetwork/pypcap/archive
PKG_MD5SUM:42979d5169c3211733aa71a04c379c84

PKG_BUILD_DIR:=$(BUILD_DIR)/$(PKG_NAME)-$(PKG_VERSION).$(PKG_RELEASE)

PKG_BUILD_DEPENDS:=python distribute

include $(INCLUDE_DIR)/package.mk
$(call include_mk, python-package.mk)

define Package/python-pcap
  SUBMENU:=Python
  SECTION:=lang
  CATEGORY:=Languages
  TITLE:=Python interface to lipcap
  URL:=http://code.google.com/p/pypcap/
  DEPENDS:=+python-base +libpcap
endef

TARGET_CFLAGS += -DHAVE_PCAP_FILE=1

define Build/Compile
	$(if $(Build/Compile/PyMod),,@echo Python packaging code not found.; false)
	$(call Build/Compile/PyMod,., \
		install --root="$(PKG_INSTALL_DIR)" --prefix="/usr", \
		PCAP_HOME="$(STAGING_DIR)/usr" \
	)
endef

$(eval $(call PyPackage,python-pcap))
$(eval $(call BuildPackage,python-pcap))
