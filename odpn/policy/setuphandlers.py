from collective.grok import gs
from odpn.policy import MessageFactory as _

@gs.importstep(
    name=u'odpn.policy', 
    title=_('odpn.policy import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('odpn.policy.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
