# pylint: disable=missing-module-docstring,pointless-statement
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Coustom views modifications",
    "summary": """
        Prohibir Creacion de valores de otra tabla""",
    "author": "Nahe Consulting Group",
    "maintainers": ["nahe-consulting-group"],
    "website": "https://nahe.com.ar/",
    "license": "AGPL-3",
    "category": "Technical Settings",
    "version": "15.0.1.0.0",
    "development_status": "Production/Stable",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    # any module necessary for this one to work correctly
    "depends": ["sale", "account", "account_payment_group"],
    ### XML Data files
    "data": [
        "security/ir.model.access.csv",
        "views/account_move_facturas_clientes_views.xml",
        "views/account_move_facturas_proovedor_views.xml",
        "views/account_payment_group_pagos_views.xml",
        "views/account_payment_group_recibos_views.xml",
        "views/sale_order_views.xml",
    ],
}
