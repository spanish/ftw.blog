from Products.CMFPlone.utils import _createObjectByType
from Products.CMFPlone.utils import safe_hasattr
from zope.component import getMultiAdapter,getUtility
from plone.portlets.interfaces import IPortletAssignmentMapping
from plone.portlets.interfaces import IPortletManager
from plone.portlets.interfaces import ILocalPortletAssignmentManager
from izug.blog.portlets import categories, archiv

#check for tags portlet
has_tag_portlet = False
try:
    from izug.tagging.portlets import tags
    has_tag_portlet = True
except ImportError:
    pass
    
    
def objectAddedHandler(object, event):
    """Handle IObjectAddedEvent
    """

    #adding a categories root object    
    if not safe_hasattr(object, 'categories', False):
        _createObjectByType('Blog Category', object, 'categories')
        category = getattr(object, 'categories', False)
        if category:
            category.setTitle('Kategorien')
            category.reindexObject()
            

def objectInitializedHandler(object, event):
    #adding some portlets (archive/tags/categories)
    blog_manager = getUtility(IPortletManager, name=u'blog.portlets', context=object)
    portlets = getMultiAdapter((object, blog_manager,), IPortletAssignmentMapping, context=object)
    
    category = 'blog-categories-portlet'
    if category not in portlets.keys():
        portlets[category] = categories.Assignment()
    a = 'blog-archive-portlet'
    if a not in portlets.keys():
        portlets[a] = archiv.Assignment()
    
    if has_tag_portlet:
        tag = 'tag-cloud-portlet'
        if tag not in portlets.keys():
            portlets[tag] = tags.Assignment()