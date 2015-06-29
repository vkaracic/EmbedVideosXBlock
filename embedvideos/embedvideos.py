"""
EmbedVideos XBlock enables users to post from various providers
with various parameters on a single XBlock.
"""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from xblock.fragment import Fragment

from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('embedvideos', 'static/html'))


class EmbedVideosXBlock(XBlock):    #pylint disable=R0901, R0904
    """
    The class variables are all the parameters for each video provider.
    Default values are the actual default values of each parameter.
    """

    # The commented out class variables are the ones I'm having problems with
    # VIMEO BLOCK #
    # https://developer.vimeo.com/player/embedding
    vimeo_id = String(default=None, scope=Scope.settings)
    vimeo_width = Integer(default=480, scope=Scope.settings)
    vimeo_height = Integer(default=250, scope=Scope.settings)
    vimeo_autoplay = Integer(default=0, scope=Scope.settings)
    vimeo_badge = Integer(default=1, scope=Scope.settings)
    vimeo_byline = Integer(default=1, scope=Scope.settings)
    vimeo_color = String(default='00adef', scope=Scope.settings)
    vimeo_loop = Integer(default=1, scope=Scope.settings)
    vimeo_portrait = Integer(default=1, scope=Scope.settings)
    vimeo_title = Integer(default=1, scope=Scope.settings)


    # YOUTUBE BLOCK #
    # detailed descriptions of the parameters can be found here:
    # https://developers.google.com/youtube/player_parameters
    youtube_id = String(default=None, scope=Scope.settings)
    youtube_width = Integer(default=480, scope=Scope.settings)
    youtube_height = Integer(default=250, scope=Scope.settings)
    #youtube_autoplay = Integer(default=0, scope=Scope.settings)    
    youtube_autohide = Integer(default=0, scope=Scope.settings)  
    #youtube_cc_load_policy = Integer(default=0, scope=Scope.settings)   
    youtube_color = String(default="red", scope=Scope.settings) 
    youtube_controls = Integer(default=1, scope=Scope.settings)
    youtube_fs = Integer(default=1, scope=Scope.settings)
    youtube_hl = String(default="en", scope=Scope.settings)
    youtube_iv_load_policy = Integer(default=1, scope=Scope.settings)
    youtube_loop = Integer(default=0, scope=Scope.settings)
    youtube_modestbranding = Integer(default=1, scope=Scope.settings)
    youtube_rel = Integer(default=1, scope=Scope.settings)
    youtube_showinfo = Integer(default=0, scope=Scope.settings)
    youtube_theme = String(default="dark", scope=Scope.settings)


    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """Create fragment and send the appropriate context."""

        context = {}
        if self.vimeo_id:
            context = {
                'vimeo_id': self.vimeo_id,
                'vimeo_width': self.vimeo_width,
                'vimeo_height': self.vimeo_height,
                'vimeo_autoplay': self.vimeo_autoplay, 
                'vimeo_badge': self.vimeo_badge, 
                'vimeo_byline': self.vimeo_byline,
                'vimeo_color': self.vimeo_color,
                'vimeo_loop': self.vimeo_loop,
                'vimeo_portrait': self.vimeo_portrait,
                'vimeo_title': self.vimeo_title
            }
        if self.youtube_id:
            context = {
                'youtube_id': self.youtube_id,
                'youtube_width': self.youtube_width,
                'youtube_height': self.youtube_height,
                #'youtube_autoplay ': self.youtube_autoplay,
                'youtube_autohide': self.youtube_autohide,
                #'youtube_cc_load_policy': self.youtube_cc_load_policy,
                'youtube_color': self.youtube_color,
                'youtube_controls': self.youtube_controls,
                'youtube_fs': self.youtube_fs,
                'youtube_hl': self.youtube_hl,
                'youtube_iv_load_policy': self.youtube_iv_load_policy,
                'youtube_loop': self.youtube_loop,
                'youtube_modestbranding': self.youtube_modestbranding,
                'youtube_rel': self.youtube_rel,
                'youtube_showinfo': self.youtube_showinfo,
                'youtube_theme': self.youtube_theme
            }

        frag = Fragment()
        template = env.get_template('embedvideos.html')
        frag.add_content(template.render(**context))    #pylint: disable=W0142
        frag.add_css(self.resource_string('static/css/embedvideos.css'))

        return frag

    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("EmbedVideosXBlock",
             """<vertical_demo>
                <embedvideos vimeo_id="52422837"/>
                <embedvideos youtube_id="U6l9NdAJwRk"/>
                </vertical_demo>
             """),
        ]

    def studio_view(self, context):
        """Create a fragment used to display the edit view in the Studio."""

        context = {
                'youtube_id': self.youtube_id,
                'youtube_width': self.youtube_width,
                'youtube_height': self.youtube_height,
                #'youtube_autoplay ': self.youtube_autoplay,
                'youtube_autohide': self.youtube_autohide,
                #'youtube_cc_load_policy': self.youtube_cc_load_policy,
                'youtube_color': self.youtube_color,
                'youtube_controls': self.youtube_controls,
                'youtube_fs': self.youtube_fs,
                'youtube_hl': self.youtube_hl,
                'youtube_iv_load_policy': self.youtube_iv_load_policy,
                'youtube_loop': self.youtube_loop,
                'youtube_modestbranding': self.youtube_modestbranding,
                'youtube_rel': self.youtube_rel,
                'youtube_showinfo': self.youtube_showinfo,
                'youtube_theme': self.youtube_theme,
                'vimeo_id': self.vimeo_id,
                'vimeo_width': self.vimeo_width,
                'vimeo_height': self.vimeo_height,
                'vimeo_autoplay': self.vimeo_autoplay, 
                'vimeo_badge': self.vimeo_badge, 
                'vimeo_byline': self.vimeo_byline,
                'vimeo_color': self.vimeo_color,
                'vimeo_loop': self.vimeo_loop,
                'vimeo_portrait': self.vimeo_portrait,
                'vimeo_title': self.vimeo_title
        }

        frag = Fragment()
        template = env.get_template('embedvideos_edit.html')
        frag.add_content(template.render(**context))    #pylint: disable=W0142
        frag.add_css(self.resource_string("static/css/embedvideos_edit.css"))
        frag.add_javascript(self.resource_string("static/js/src/embedvideos_edit.js")) #pylint: disable=C0301
        frag.initialize_js('EmbedVideosEditXBlock')
        return frag        

    @XBlock.json_handler
    def studio_submit(self, data, suffix=''):   #pylint disable=W0613
        """Called when submitting the form in Studio."""

        attrList = [
            'youtube_id',
            'youtube_width',
            'youtube_height',
            #'youtube_autoplay',
            'youtube_autohide',
            #'youtube_cc_load_policy',
            'youtube_color',
            'youtube_controls',
            'youtube_fs',
            'youtube_hl',
            'youtube_iv_load_policy',
            'youtube_loop',
            'youtube_modestbranding',
            'youtube_rel',
            'youtube_showinfo',
            'youtube_theme',
            'vimeo_id',
            'vimeo_width',
            'vimeo_height',
            'vimeo_autoplay',
            'vimeo_badge',
            'vimeo_byline',
            'vimeo_color',
            'vimeo_loop',
            'vimeo_portrait',
            'vimeo_title'
        ]

        for item in attrList:
            if (data.get(item) != None):
                setattr(self, item, data.get(item))

        return {'result':'success'}