import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-oca-sale-reporting",
    description="Meta package for oca-sale-reporting Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-sale_comment_template',
        'odoo14-addon-sale_order_line_position',
        'odoo14-addon-sale_order_report_product_image',
        'odoo14-addon-sale_order_weight',
        'odoo14-addon-sale_outgoing_product',
        'odoo14-addon-sale_report_crossed_out_original_price',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
