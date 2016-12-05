###############
apidoc2markdown
###############

Apidoc_ is an open specification for documenting REST APIs in JSON or YAML.
Imperfect as it is, it's de facto a standard for many API developers.

This extension lets you render your swagger.json file as a Markdown document.
You can customize the output by providing your own Jinja2_ template.

.. _Apidoc: http://apidocjs.com/
.. _Jinja2: http://jinja.pocoo.org/


.. warning::

    This extension was created for a particular project and thus is only
    guaranteed to work with this particular project! It is very much likely
    you'll have to modify apidoc.md.j2_ for your project.

.. _apidoc.md.j2: https://github.com/moigagoo/apidoc2markdown/blob/master/apidoc.md.j2


************
Installation
************

.. code-block:: shell

    $ pip install apidoc2markdown


*****
Usage
*****

.. code-block:: shell

    usage: apidoc2markdown-script.py [-h] [-i APIDOC_LOCATION] [-o OUTPUT]
                                    [-t TEMPLATE]

    optional arguments:
      -h, --help            show this help message and exit
      -i APIDOC_LOCATION, --input APIDOC_LOCATION
                            path to the directory with api_data.json
                            and api_project.json (default: .)
      -o OUTPUT, --output OUTPUT
                            path to the output Markdown file (default: swagger.md)
      -t TEMPLATE, --template TEMPLATE
                            Jinja2 template used for conversion
