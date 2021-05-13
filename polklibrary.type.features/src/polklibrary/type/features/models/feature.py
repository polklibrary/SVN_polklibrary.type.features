from plone import api
from plone.indexer.decorator import indexer
from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from zope import schema
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm


click_options = SimpleVocabulary([
    SimpleTerm(value=u'Do Nothing', title=u'Do Nothing'),
    SimpleTerm(value=u'Feature Page', title=u'Feature Page'),
    SimpleTerm(value=u'Use Link', title=u'Use Link'),
])

class IFeature(model.Schema):

    title = schema.TextLine(
            title=u"Title",
            required=True,
        )
        
    rotation_speed = schema.TextLine(
            title=u"Rotation Speed (seconds)",
            required=True,
            default=u"10",
        )

    # --- Feature One FieldSet ---
    model.fieldset(
        'feature-one',
        label=u'Feature One', 
        fields=['title_one', 'image_one', 'click_options_one', 'body_one', 'link_one'],
    )
    
    title_one = schema.TextLine(
        title=u'Title',
        required=False,
        )

    image_one = NamedBlobImage(
        title=u'Image',
        description=u'A upload field for images',
        required=False,
        )
        
    click_options_one = schema.Choice(
            title=u"Feature Click",
            source=click_options,
            default=u"Do Nothing",
            required=False,
        )
        
    body_one = RichText(
            title=u"Page",
            description=u'Leave blank for no page.',
            default_mime_type='text/structured',
            required=False,
            default=u"<p></p>",
        )
        
    link_one = schema.TextLine(
        title=u'Link',
        description=u'Leave blank for no link.',
        required=False,
        )
        
    # --- Feature Two FieldSet ---
    model.fieldset(
        'feature-two',
        label=u'Feature Two', 
        fields=['title_two', 'image_two', 'click_options_two', 'body_two', 'link_two'],
    )
    
    title_two = schema.TextLine(
        title=u'Title',
        required=False,
        )

    image_two = NamedBlobImage(
        title=u'Image',
        description=u'A upload field for images',
        required=False,
        )
        
    click_options_two = schema.Choice(
            title=u"Feature Click",
            source=click_options,
            default=u"Do Nothing",
            required=False,
        )
        
    body_two = RichText(
            title=u"Page",
            description=u'Leave blank for no page.',
            default_mime_type='text/structured',
            required=False,
            default=u"<p></p>",
        )
        
    link_two = schema.TextLine(
        title=u'Link',
        description=u'Leave blank for no link.',
        required=False,
        )
        
    # --- Feature Three FieldSet ---
    model.fieldset(
        'feature-three',
        label=u'Feature Three', 
        fields=['title_three', 'image_three', 'click_options_three', 'body_three', 'link_three'],
    )
    
    title_three = schema.TextLine(
        title=u'Title',
        required=False,
        )

    image_three = NamedBlobImage(
        title=u'Image',
        description=u'A upload field for images',
        required=False,
        )
        
    click_options_three = schema.Choice(
            title=u"Feature Click",
            source=click_options,
            default=u"Do Nothing",
            required=False,
        )
        
    body_three = RichText(
            title=u"Page",
            description=u'Leave blank for no page.',
            default_mime_type='text/structured',
            required=False,
            default=u"<p></p>",
        )
        
    link_three = schema.TextLine(
        title=u'Link',
        description=u'Leave blank for no link.',
        required=False,
        )
        
    # --- Feature Three FieldSet ---
    model.fieldset(
        'feature-four',
        label=u'Feature Four', 
        fields=['title_four', 'image_four', 'click_options_four', 'body_four', 'link_four'],
    )
    
    title_four = schema.TextLine(
        title=u'Title',
        required=False,
        )

    image_four = NamedBlobImage(
        title=u'Image',
        description=u'A upload field for images',
        required=False,
        )
        
    click_options_four = schema.Choice(
            title=u"Feature Click",
            source=click_options,
            default=u"Do Nothing",
            required=False,
        )
        
    body_four = RichText(
            title=u"Page",
            description=u'Leave blank for no page.',
            default_mime_type='text/structured',
            required=False,
            default=u"<p></p>",
        )
        
    link_four = schema.TextLine(
        title=u'Link',
        description=u'Leave blank for no link.',
        required=False,
        )
        
        
    # --- Feature Five FieldSet ---
    model.fieldset(
        'feature-five',
        label=u'Feature Five', 
        fields=['title_five', 'image_five', 'click_options_five', 'body_five', 'link_five'],
    )
    
    title_five = schema.TextLine(
        title=u'Title',
        required=False,
        )

    image_five = NamedBlobImage(
        title=u'Image',
        description=u'A upload field for images',
        required=False,
        )
        
    click_options_five = schema.Choice(
            title=u"Feature Click",
            source=click_options,
            default=u"Do Nothing",
            required=False,
        )
        
    body_five = RichText(
            title=u"Page",
            description=u'Leave blank for no page.',
            default_mime_type='text/structured',
            required=False,
            default=u"<p></p>",
        )
        
    link_five = schema.TextLine(
        title=u'Link',
        description=u'Leave blank for no link.',
        required=False,
        )
        