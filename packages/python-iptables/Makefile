
include $(TOPDIR)/rules.mk

PKG_NAME:=python-iptables
PKG_VERSION:=0.3.0
PKG_RELEASE:=3

PKG_SOURCE:=v$(PKG_VERSION).tar.gz
PKG_SOURCE_URL:=https://github.com/thejuan/python-iptables/archive/
#PKG_MD5SUM:=6d780d29c1df1acc17195bde7be0e394

PKG_BUILD_DIR:=$(BUILD_DIR)/python-iptables-$(PKG_VERSION)
PKG_BUILD_DEPENDS:=python libc

include $(INCLUDE_DIR)/package.mk
$(call include_mk, python-package.mk)

define Package/python-iptables
  SUBMENU:=Python
  SECTION:=lang
  CATEGORY:=Languages
  TITLE:=python-iptables
  URL:=https://github.com/thejuan/python-iptables
  DEPENDS:=+python +libc +iptables-shared
endef

define Package/python-iptables/description
  OpenWRT port of python-iptables bindings
endef

define Build/Compile
	$(call Build/Compile/PyMod,,install --prefix="$(PKG_INSTALL_DIR)/usr")
endef

define Package/python-iptables/install
	$(INSTALL_DIR) $(1)$(PYTHON_PKG_DIR)
	$(CP) \
	    $(PKG_INSTALL_DIR)$(PYTHON_PKG_DIR)/* \
	    $(1)$(PYTHON_PKG_DIR)
endef

$(eval $(call BuildPackage,python-iptables))
