from sphinx.util.typing import ExtensionMetadata
from sphinx.application import Sphinx
from sphinx_rerediraffe.callback import CheckRedirectsDiffBuilder, WriteRedirectsDiffBuilder, build_redirects

__version__ = '0.0.1

def setup(app: Sphinx) -> ExtensionMetadata:
    app.add_config_value('rediraffe_redirects', None, None)
    app.add_config_value('rediraffe_branch', '', None)
    app.add_config_value('rediraffe_template', None, None)
    app.add_config_value('rediraffe_auto_redirect_perc', 100, None)
    app.add_config_value('rediraffe_dir_only', False, 'env')

    app.add_builder(CheckRedirectsDiffBuilder)
    app.add_builder(WriteRedirectsDiffBuilder)
    app.connect('build-finished', build_redirects)

    return {
        'version': __version__,
        'env_version': 1,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }

__all__ = ['__version__', 'setup']