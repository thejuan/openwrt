#
# Copyright (C) 2010 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=netifaces
PKG_VERSION:=0.8
PKG_RELEASE:=1

PKG_SOURCE:=netifaces-$(PKG_VERSION).tar.gz
PKG_SOURCE_URL:=http://alastairs-place.net/projects/netifaces/
PKG_MD5SUM:=e57e5983f4c286fac5f8068fbfc5c873

PKG_BUILD_DIR:=$(BUILD_DIR)/netifaces-$(PKG_VERSION)
PKG_BUILD_DEPENDS:=python

include $(INCLUDE_DIR)/package.mk
$(call include_mk, python-package.mk)

define Package/netifaces
  SUBMENU:=Python
  SECTION:=lang
  CATEGORY:=Languages
  TITLE:=netifaces
  URL:=http://alastairs-place.net/projects/netifaces/
  DEPENDS:=+python
endef

define Package/netifaces/description
  Portable access to network interfaces from Python
endef

define Build/Compile
	$(call Build/Compile/PyMod,,install --prefix="$(PKG_INSTALL_DIR)/usr")
endef

define Package/netifaces/install
	$(INSTALL_DIR) $(1)$(PYTHON_PKG_DIR)
	$(CP) \
	    $(PKG_INSTALL_DIR)$(PYTHON_PKG_DIR)/* \
	    $(1)$(PYTHON_PKG_DIR)
endef

$(eval $(call BuildPackage,netifaces))
