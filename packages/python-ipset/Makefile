#
# Copyright (C) 2010 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=python-ipset
PKG_VERSION:=6.20.1
PKG_RELEASE:=1


PKG_BUILD_DIR:=$(BUILD_DIR)/$(PKG_NAME)
PKG_BUILD_DEPENDS:=python

include $(INCLUDE_DIR)/package.mk
$(call include_mk, python-package.mk)

define Package/python-ipset
  SUBMENU:=Python
  SECTION:=lang
  CATEGORY:=Languages
  TITLE:=Python Ipset
  DEPENDS:=+python +ipset
endef

define Package/python-ipset/description
  Portable access to adding to ipsets from Python
endef

define Build/Prepare
		mkdir -p $(PKG_BUILD_DIR)
		$(CP) ./src/* $(PKG_BUILD_DIR)/
endef

define Build/Compile
	$(call Build/Compile/PyMod,,install --prefix="$(PKG_INSTALL_DIR)/usr")
	$(CP) $(PKG_BUILD_DIR)/ipset.py $(PKG_INSTALL_DIR)/$(PYTHON_PKG_DIR)/ipset.py
endef

define Package/python-ipset/install
	$(INSTALL_DIR) $(1)$(PYTHON_PKG_DIR)	
	$(CP) \
		$(PKG_INSTALL_DIR)$(PYTHON_PKG_DIR)/* \
		$(1)$(PYTHON_PKG_DIR)
endef

$(eval $(call BuildPackage,python-ipset))
