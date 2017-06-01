{
    'name': 'antoni_report',
    'category': 'test',
    'summary': 'test',
    'website': 'a@mail.com',
    'version': '1.0',
    'description': """
            Crear un nuevo reporte igual al sales order
        """,
    'author': 'Antoni Ruth',
    'depends': ['sale'],
    'data': [
        'views/new_button_print.xml',
        'views/new_wizard.xml',
        'report/antoni_report.xml',
        'report/antoni_report_templates.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'auto_install': False,
}
