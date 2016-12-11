Edit Labels - LabVIEW DropDown Plugin
=====================================

Refactor your LabVIEW code using Python script. This plugin allows you to rename labels of controls/indicators in bulk.

Requirements
------------

* Python 3
* LabVIEW 2015

Installation
------------

1. Install Python interpreter and add it to ``PATH`` system variable.
2. Copy content of ``Plugin`` directory to:

    ``<LabVIEW>\resource\dialog\QuickDrop\plugins\``

3. Restart LabVIEW

Usage
-----

1. Select controls/indicators of your choice
2. Open QuickDrop window (Ctrl+Space)
3. Open Edit Labels window (Ctrl+E)
4. Select predefined script of your choice, or define it by self
5. Press Execute and OK

Notes:

* You can write own predefined scripts. Just save them in:

    ``<LabVIEW>\resource\dialog\QuickDrop\plugins\Edit Labels Scripts``

* Shortcut (Ctrl+E) can be redefined. After opening QuickDrop window window press `Configure...` button.

Script Syntax
-------------

Scripts used by this plugin are regular Python scripts. What you need to do is:

* iterate through predefined ``labels`` variable that contains text of all selected labels
* print new text for each label to stdout (one label per line)

References
----------

Source:
https://github.com/gergelyk/lv_edit_labels_plugin

Tutorial
--------

.. raw:: html

   <embed src="https://www.youtube.com/embed/XlQra-4kA2U">

Predefined Scripts
------------------

Plugin comes with following scripts already predefined:

========= =============
Add prefix
-----------------------
input     output
========= =============
Amplitude foo.Amplitude
Frequency foo.Frequency
Phase     foo.Phase
========= =============

============= =========
Remove prefix
-----------------------
input         output
============= =========
Amplitude     Amplitude
foo.Frequency Frequency
bar.Phase     Phase
============= =========

=========== =============
Recover index
-------------------------
input       output
=========== =============
Amplitude   Amplitude 1
Frequency   Frequency 1
Phase       Phase 1
Amplitude 2 Amplitude 2
Frequency 2 Frequency 2
Phase 2     Phase 2
Amplitude 3 Amplitude 3
Frequency 3 Frequency 3
Phase 3     Phase 3

=========== =============

=========== =============
Increment index
-------------------------
input       output
=========== =============
Amplitude   Amplitude
Frequency 0 Frequency 1
Frequency 1 Frequency 2
Frequency 2 Frequency 3
=========== =============

=========== =============
Decrement index
-------------------------
input       output
=========== =============
Amplitude   Amplitude
Frequency 0 Frequency 0
Frequency 1 Frequency 0
Frequency 2 Frequency 1
=========== =============

=============== =================
Move index to the front of prefix
---------------------------------
input           output
=============== =================
foo.Frequency 0 foo0.Frequency
foo.Frequency 1 foo1.Frequency
foo.Frequency 2 foo2.Frequency
=============== =================

============== =================
Move index to the front of label
--------------------------------
input           output
============== =================
foo0.Frequency foo.Frequency 0
foo1.Frequency foo.Frequency 1
foo2.Frequency foo.Frequency 2
============== =================





