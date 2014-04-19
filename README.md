SVBLM's Maya Suite
==========

A plug-in suite for Autodesk Maya from SVBLM for making developing art assets for games easier.

Goals
-----

- Allow scripts to structure assets, including naming and organization.
- Minimize bad assets or mistakes through importing/exporting models into the asset pipeline.
- Keep assets reviewed and structure the pipeline around reviews to keep asset quality high.
- Integrate deeply with Maya

Installation
-----
Clone this directory in the terminal (git needs to be set up):

`git clone git@github.com:JakeCataford/svblm-maya`

Simply navigate to your plugin manager `window > settings/preferences > plug-in manager` and import svblm-maya.py. That root plugin will handle importing the suite.

Cop
-----

Cop lets you run unittests against maya scenes. It's a way of preventing problems before the asset gets into the pipeline. If you have a problem that commonly happens and can be avoided, just write a test and have your team run cop before they export. Cop will let them know that something is out of line in their scene and that they should fix it before proceding.

To run cop, run:

```Python
import cop.cop as cop

cop.Cop()
```

Add it to a shelf for easy access later.

*Writing new tests*

Cop is really just a wrapper for a test runner, the tests directory is exactly like any other python unittesting. Add new files that start with the word test_* and it will load the classes automagically and run all the methods.
