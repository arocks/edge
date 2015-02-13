APT_SOURCES
===========

Sets /etc/apt/sources.list with default settings.
If the release is unsupported, updates the url's to the archive repositories.

Requirements
------------

This role is only relevant to Debian based distributions.


Role Variables
--------------

- apt_sources_cc: by default, the Distribution's generic repository will be used, though you'll
want to set apt_sources_cc to the country code relevant for your host, to make
it use repositories for that country.
- apt_sources_dir: defaults to /etc/apt/
- apt_sources_file: defaults to sources.list
- apt_sources_types: defaults to ['deb', 'deb-src']. You could leave out
  'deb-src' as to not configure source repositories.

Dependencies
------------

none

License
-------

GPLv3

Author Information
------------------

Serge van Ginderachter (serge@vanginderachter.be) [Ginsys]

