===========
Module Name
===========

.. |badge1| image:: https://img.shields.io/badge/maturity-Stable-brightgreen
    :target: https://odoo-community.org/page/development-status
    :alt: Stable
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://nahe.com.ar/web/image/website/1/logo/N%C3%A4he%20Consulting%20Group?unique=246650d
    :target: https://github.com/nahe-consulting-group
    :alt: nahe-consulting-group

|badge1| |badge2| |badge3|

This module extends the functionality of ... to support ... and to allow you to ...

**Table of contents**

.. contents::
   :local:

.. !!! Instalation: must only be present if there are very specific installation instructions, such as installing non-python dependencies.The audience is systems administrators. ] To install this module, you need to: !!!

Install
=======

To install this module, follow these steps:

   1- Download the module into your Odoo addons directory.
   2- Update your Odoo instance to include the new module.
   3- Install the module from the Odoo Apps menu.

Configure
=========

No special configuration is required. The changes are automatically applied once the module is installed.

Usage
=====

1- Navigate to Sales > Orders to create or modify a sales order. The fields partner_id and product_id will have restricted creation and edition capabilities.
2- In Accounting > Payments, access Supplier Payments and Customer Receipts. The field partner_id will have the same restrictions.
3- In Accounting > Vendors > Vendor Bills and Customers > Invoices, the fields partner_id, partner_bank_id, product_id, and analytic_account_id will follow the same restricted behavior.

Known issues / Roadmap
======================

* There are no known issues at this time.
* Future enhancements may include additional restrictions for other views.

Bug Tracker
===========

* Bugs are tracked on GitHub. Feel free to file issues if you encounter any problems.

Credits
=======

Authors
~~~~~~~

* Nahe Consulting Group

Contributors
~~~~~~~~~~~~

* `Nahe Consulting Group. <https://nahe.com.ar/>`_
  
  * Matías Bressanello

Maintainers
~~~~~~~~~~~

This module is maintained by Nahe Consulting Group
