from plone import api
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
import json

class FeatureView(BrowserView):

    template = ViewPageTemplateFile("feature_view.pt")
    
    def __call__(self):
        return self.template()
    
    @property
    def has_feature_one(self):
        return self.context.title_one and self.context.image_one and self.context.click_options_one == u'Feature Page'
        
    @property
    def has_feature_two(self):
        return self.context.title_two and self.context.image_two and self.context.click_options_two == u'Feature Page'
        
    @property
    def has_feature_three(self):
        return self.context.title_three and self.context.image_three and self.context.click_options_three== u'Feature Page'
        
    @property
    def has_feature_four(self):
        return self.context.title_four and self.context.image_four and self.context.click_options_four == u'Feature Page'
        
    @property
    def has_feature_five(self):
        return self.context.title_five and self.context.image_five and self.context.click_options_five == u'Feature Page'
        
    @property
    def portal(self):
        return api.portal.get()
