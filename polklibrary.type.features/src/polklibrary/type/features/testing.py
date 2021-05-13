# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import polklibrary.type.features


class PolklibraryTypeFeaturesLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=polklibrary.type.features)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'polklibrary.type.features:default')


POLKLIBRARY_TYPE_FEATURES_FIXTURE = PolklibraryTypeFeaturesLayer()


POLKLIBRARY_TYPE_FEATURES_INTEGRATION_TESTING = IntegrationTesting(
    bases=(POLKLIBRARY_TYPE_FEATURES_FIXTURE,),
    name='PolklibraryTypeFeaturesLayer:IntegrationTesting',
)


POLKLIBRARY_TYPE_FEATURES_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(POLKLIBRARY_TYPE_FEATURES_FIXTURE,),
    name='PolklibraryTypeFeaturesLayer:FunctionalTesting',
)


POLKLIBRARY_TYPE_FEATURES_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        POLKLIBRARY_TYPE_FEATURES_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='PolklibraryTypeFeaturesLayer:AcceptanceTesting',
)
