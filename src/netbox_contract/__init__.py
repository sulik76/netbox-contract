from extras.plugins import PluginConfig


class ContractsConfig(PluginConfig):
    name = 'netbox_contract'
    verbose_name = 'Netbox contract'
    description = 'Contract management plugin for Netbox'
    version = '2.0.11'
    author = 'Marc Lebreuil'
    author_email = 'marc@famillelebreuil.net'
    base_url = 'contracts'
    min_version = '3.5.0'
    required_settings = []
    default_settings = {
        'top_level_menu': False,
        'default_accounting_dimensions': {
            'account': '',
            'project': '',
            'cost center': '',
        },
        'mandatory_contract_fields': [],
        'hidden_contract_fields': [],
        'mandatory_invoice_fields': [],
        'hidden_invoice_fields': [],
    }


config = ContractsConfig
