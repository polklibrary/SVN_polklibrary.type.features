from plone.memoize import ram
from plone import api
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
import json, time, datetime, hashlib


def _render_cachekey(method, self, context):
    return (context.absolute_url(), context.modified())

class GetFeatureView(BrowserView):

    
    def __call__(self):
        _data = self.get_cached_data(self.context)
        self.request.response.setHeader('Content-Type', 'application/json')
        self.request.response.setHeader('Access-Control-Allow-Origin', '*')
        
        return json.dumps(_data)
        
    def get_url(self, name):
        option = getattr(self.context, 'click_options_' + name)
        if option == u'Feature Page':
            return self.context.absolute_url() + '?' + name + '=1'
        if option == u'Use Link':
            return getattr(self.context, 'link_' + name)
        return ''
        
    @ram.cache(_render_cachekey)
    def get_cached_data(self, context):
    
        data = {
            '__cached': str(datetime.datetime.now()),
            'rotation_seconds': int(self.context.rotation_speed),
        }
        
        if self.context.title_one and self.context.image_one:
            data['feature-one'] = {
                'title': self.context.title_one,
                'image_url': self.context.absolute_url() + '/@@download/image_one/' + self.context.image_one.filename,
                'url': self.get_url('one'),
            }
        
        if self.context.title_two and self.context.image_two:
            data['feature-two'] = {
                'title': self.context.title_two,
                'image_url': self.context.absolute_url() + '/@@download/image_two/' + self.context.image_two.filename,
                'url': self.get_url('two'),
            }
            
        if self.context.title_three and self.context.image_three:
            data['feature-three'] = {
                'title': self.context.title_three,
                'image_url': self.context.absolute_url() + '/@@download/image_three/' + self.context.image_three.filename,
                'url': self.get_url('three'),
            }
            
        if self.context.title_four and self.context.image_four:
            data['feature-four'] = {
                'title': self.context.title_four,
                'image_url': self.context.absolute_url() + '/@@download/image_four/' + self.context.image_four.filename,
                'url': self.get_url('four'),
            }
        
        if self.context.title_five and self.context.image_five:
            data['feature-five'] = {
                'title': self.context.title_five,
                'image_url': self.context.absolute_url() + '/@@download/image_five/' + self.context.image_five.filename,
                'url': self.get_url('five'),
            }
            
        return data
      
    @property
    def portal(self):
        return api.portal.get()
