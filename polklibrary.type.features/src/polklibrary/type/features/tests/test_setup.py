# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from polklibrary.type.features.testing import POLKLIBRARY_TYPE_FEATURES_INTEGRATION_TESTING  # noqa: E501

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that polklibrary.type.features is properly installed."""

    layer = POLKLIBRARY_TYPE_FEATURES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if polklibrary.type.features is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'polklibrary.type.features'))

    def test_browserlayer(self):
        """Test that IPolklibraryTypeFeaturesLayer is registered."""
        from polklibrary.type.features.interfaces import (
            IPolklibraryTypeFeaturesLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IPolklibraryTypeFeaturesLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = POLKLIBRARY_TYPE_FEATURES_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['polklibrary.type.features'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if polklibrary.type.features is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'polklibrary.type.features'))

    def test_browserlayer_removed(self):
        """Test that IPolklibraryTypeFeaturesLayer is removed."""
        from polklibrary.type.features.interfaces import \
            IPolklibraryTypeFeaturesLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IPolklibraryTypeFeaturesLayer,
            utils.registered_layers())
