"""Definition of the Blog Item content type
"""

from zope.interface import implements, directlyProvides

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from izug.blog import blogMessageFactory as _
from izug.blog.interfaces import IBlogItem
from izug.blog.config import PROJECTNAME

BlogItemSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

BlogItemSchema['title'].storage = atapi.AnnotationStorage()
BlogItemSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(BlogItemSchema, folderish=True, moveDiscussion=False)

class BlogItem(folder.ATFolder):
    """iZug Blog Item"""
    implements(IBlogItem)

    portal_type = "Blog Item"
    schema = BlogItemSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

atapi.registerType(BlogItem, PROJECTNAME)