{
    'name': 'My Custom Module',
    'version': '1.0',
    'summary': 'A simple custom module for Odoo.',
    'author': 'Your Name',
    'category': 'Custom',
    'depends': ['base'],  # Ensure 'base' is included
    'data': [
        'views/custom_model_view.xml',  # Ensure paths are correct
    ],
    'installable': True,
    'application': False,
}
