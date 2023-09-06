from products.models import (
    TransactionEconomyIndustryProductsAffiliation,
    TransactionEconomyIndustryProductsProductsProject,
    TransactionEconomyIndustryProductsType,
    TransactionEconomyIndustryProductsCall,
    TransactionEconomyIndustryProductsProductsServer,
    TransactionEconomyIndustryProductsBasis, TransactionEconomyIndustryProductsProductsServerAccount
)


class ProductsMessage(object):
    """获取产品信息"""

    def __init__(self, product_id=None):
        self.product_id = product_id
        self.display = False
        self.data = []
        self.def_get_product()

    def def_get_product(self):
        """获取单个产品信息"""
        self.display = False
        if self.product_id:
            data_product = TransactionEconomyIndustryProductsBasis.objects.filter(
                STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID=self.product_id,
            ).values('PRODUCTS_NAME', 'PRODUCTS_URL', "DETAIL", )
            if data_product.exists():
                data_product = data_product.first()
                affiliations = TransactionEconomyIndustryProductsAffiliation.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PRODUCTS=self.product_id,
                ).values('ID_ORGANIZATIONS', "ID_ORGANIZATIONS__ENTERPRISE_NAME")
                types = TransactionEconomyIndustryProductsType.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PRODUCTS=self.product_id,
                ).values('PRODUCTS_CODE__ABBREVIATION', )
                calls = TransactionEconomyIndustryProductsCall.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PRODUCTS=self.product_id,
                ).values('NAME_CODE__ABBREVIATION', 'NAME')
                servers = TransactionEconomyIndustryProductsProductsServer.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PRODUCTS=self.product_id,
                ).values(
                    'PROJECT_SERVER_ID__NAME', 'PROJECT_SERVER_ID', 'SERVER_PROT', 'SERVER_ENVIRONMENT__ABBREVIATION')
                return_servers_list_data = []
                if servers.exists():
                    for server in servers:
                        server_id = server.get("PROJECT_SERVER_ID")
                        servers_account = TransactionEconomyIndustryProductsProductsServerAccount.objects.filter(
                            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PRODUCTS_SERVER=server_id,
                        ).values('ACCOUNT', 'PASSWORD', 'ACCOUNT_IDENTITY', 'AFFILIATED_PERSONNEL', 'DETAIL')
                        return_servers_data = {
                            "ID_SERVER": server_id,
                            "SERVER_NAME": server.get("PROJECT_SERVER_ID__NAME"),
                            "SERVER_ENVIRONMENT": server.get("SERVER_ENVIRONMENT__ABBREVIATION"),
                            "SERVER_ACCOUNT": [{
                                "ACCOUNT": server_account.get("ACCOUNT"),
                                "PASSWORD": server_account.get("PASSWORD"),
                                "ACCOUNT_IDENTITY": server_account.get("ACCOUNT_IDENTITY"),
                                "AFFILIATED_PERSONNEL": server_account.get("AFFILIATED_PERSONNEL"),
                                "DETAIL": server_account.get("DETAIL"),
                            } for server_account in servers_account] if servers_account.exists() else [],
                        }
                        return_servers_list_data.append(return_servers_data)
                products_project = TransactionEconomyIndustryProductsProductsProject.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PRODUCTS=self.product_id,
                ).values('ID_PROJECT', 'ID_PROJECT__PROJECT_NAME', 'CORRELATION_CODE__ABBREVIATION', 'DETAIL', )
                return_data = {
                    "ID_PRODUCTS": self.product_id,
                    "PRODUCTS_NAME": data_product.get('PRODUCTS_NAME'),
                    "PRODUCTS_URL": data_product.get('PRODUCTS_URL'),
                    "PRODUCTS_ORGANIZATIONS": [{
                        "ID_ORGANIZATIONS": affiliation.get("ID_ORGANIZATIONS"),
                        "ID_ORGANIZATIONS_NAME": affiliation.get("ID_ORGANIZATIONS__ENTERPRISE_NAME"),
                    } for affiliation in affiliations] if affiliations.exists() else None,
                    "PRODUCTS_TYPES": [{
                        "TYPE": pro_type.get("PRODUCTS_CODE__ABBREVIATION"),
                    } for pro_type in types] if types.exists() else None,
                    "PRODUCTS_CALLS": [{
                        "TYPE": call.get("NAME_CODE__ABBREVIATION"),
                        "NAME": call.get("NAME"),
                    } for call in calls] if calls.exists() else None,
                    "PRODUCTS_SERVERS": return_servers_list_data,
                    "PRODUCTS_PROJECT": [{
                        "ID_PROJECT": product_project.get("ID_PROJECT"),
                        "PROJECT_NAME": product_project.get("ID_PROJECT__PROJECT_NAME"),
                        "PROJECT_CORRELATION_CODE": product_project.get("CORRELATION_CODE__ABBREVIATION"),
                        "PROJECT_DETAIL": product_project.get("DETAIL"),
                    } for product_project in products_project] if products_project.exists() else None,
                }
                self.display = True

                return return_data

    def def_get_products(self):
        """获取所有产品信息"""
        self.data.clear()
        self.display = False
        data_products = TransactionEconomyIndustryProductsBasis.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1,
        ).values('PRODUCTS_NAME', 'PRODUCTS_URL', "DETAIL", )
        if data_products.exists():
            for data_product in data_products:
                affiliations = TransactionEconomyIndustryProductsAffiliation.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PRODUCTS=self.product_id,
                ).values('ID_ORGANIZATIONS', "ID_ORGANIZATIONS__ENTERPRISE_NAME")
                types = TransactionEconomyIndustryProductsType.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PRODUCTS=self.product_id,
                ).values('PRODUCTS_CODE__ABBREVIATION', )
                calls = TransactionEconomyIndustryProductsCall.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PRODUCTS=self.product_id,
                ).values('NAME_CODE__ABBREVIATION', 'NAME')
                servers = TransactionEconomyIndustryProductsProductsServer.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PRODUCTS=self.product_id,
                ).values(
                    'PROJECT_SERVER_ID__NAME', 'PROJECT_SERVER_ID', 'SERVER_PROT', 'SERVER_ENVIRONMENT__ABBREVIATION')
                return_servers_list_data = []
                if servers.exists():
                    for server in servers:
                        server_id = server.get("PROJECT_SERVER_ID")
                        servers_account = TransactionEconomyIndustryProductsProductsServerAccount.objects.filter(
                            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PRODUCTS_SERVER=server_id,
                        ).values('ACCOUNT', 'PASSWORD', 'ACCOUNT_IDENTITY', 'AFFILIATED_PERSONNEL', 'DETAIL')
                        return_servers_data = {
                            "ID_SERVER": server_id,
                            "SERVER_NAME": server.get("PROJECT_SERVER_ID__NAME"),
                            "SERVER_ENVIRONMENT": server.get("SERVER_ENVIRONMENT__ABBREVIATION"),
                            "SERVER_ACCOUNT": [{
                                "ACCOUNT": server_account.get("ACCOUNT"),
                                "PASSWORD": server_account.get("PASSWORD"),
                                "ACCOUNT_IDENTITY": server_account.get("ACCOUNT_IDENTITY"),
                                "AFFILIATED_PERSONNEL": server_account.get("AFFILIATED_PERSONNEL"),
                                "DETAIL": server_account.get("DETAIL"),
                            } for server_account in servers_account] if servers_account.exists() else [],
                        }
                        return_servers_list_data.append(return_servers_data)
                products_project = TransactionEconomyIndustryProductsProductsProject.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PRODUCTS=self.product_id,
                ).values('ID_PROJECT', 'ID_PROJECT__PROJECT_NAME', 'CORRELATION_CODE__ABBREVIATION', 'DETAIL', )
                return_data = {
                    "ID_PRODUCTS": self.product_id,
                    "PRODUCTS_NAME": data_product.get('PRODUCTS_NAME'),
                    "PRODUCTS_URL": data_product.get('PRODUCTS_URL'),
                    "PRODUCTS_ORGANIZATIONS": [{
                        "ID_ORGANIZATIONS": affiliation.get("ID_ORGANIZATIONS"),
                        "ID_ORGANIZATIONS_NAME": affiliation.get("ID_ORGANIZATIONS__ENTERPRISE_NAME"),
                    } for affiliation in affiliations] if affiliations.exists() else None,
                    "PRODUCTS_TYPES": [{
                        "TYPE": pro_type.get("PRODUCTS_CODE__ABBREVIATION"),
                    } for pro_type in types] if types.exists() else None,
                    "PRODUCTS_CALLS": [{
                        "TYPE": call.get("NAME_CODE__ABBREVIATION"),
                        "NAME": call.get("NAME"),
                    } for call in calls] if calls.exists() else None,
                    "PRODUCTS_SERVERS": return_servers_list_data,
                    "PRODUCTS_PROJECT": [{
                        "ID_PROJECT": product_project.get("ID_PROJECT"),
                        "PROJECT_NAME": product_project.get("ID_PROJECT__PROJECT_NAME"),
                        "PROJECT_CORRELATION_CODE": product_project.get("CORRELATION_CODE__ABBREVIATION"),
                        "PROJECT_DETAIL": product_project.get("DETAIL"),
                    } for product_project in products_project] if products_project.exists() else None,
                }
                self.data.append(return_data)
            self.display = True

    def def_yield_get_products(self):
        """yield 获取所有产品信息"""
        data_products = TransactionEconomyIndustryProductsBasis.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1,
        ).values('PRODUCTS_NAME', 'PRODUCTS_URL', "DETAIL", )
        if data_products.exists():
            for data_product in data_products:
                affiliations = TransactionEconomyIndustryProductsAffiliation.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PRODUCTS=self.product_id,
                ).values('ID_ORGANIZATIONS', "ID_ORGANIZATIONS__ENTERPRISE_NAME")
                types = TransactionEconomyIndustryProductsType.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PRODUCTS=self.product_id,
                ).values('PRODUCTS_CODE__ABBREVIATION', )
                calls = TransactionEconomyIndustryProductsCall.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PRODUCTS=self.product_id,
                ).values('NAME_CODE__ABBREVIATION', 'NAME')
                servers = TransactionEconomyIndustryProductsProductsServer.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PRODUCTS=self.product_id,
                ).values(
                    'PROJECT_SERVER_ID__NAME', 'PROJECT_SERVER_ID', 'SERVER_PROT', 'SERVER_ENVIRONMENT__ABBREVIATION')
                return_servers_list_data = []
                if servers.exists():
                    for server in servers:
                        server_id = server.get("PROJECT_SERVER_ID")
                        servers_account = TransactionEconomyIndustryProductsProductsServerAccount.objects.filter(
                            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PRODUCTS_SERVER=server_id,
                        ).values('ACCOUNT', 'PASSWORD', 'ACCOUNT_IDENTITY', 'AFFILIATED_PERSONNEL', 'DETAIL')
                        return_servers_data = {
                            "ID_SERVER": server_id,
                            "SERVER_NAME": server.get("PROJECT_SERVER_ID__NAME"),
                            "SERVER_ENVIRONMENT": server.get("SERVER_ENVIRONMENT__ABBREVIATION"),
                            "SERVER_ACCOUNT": [{
                                "ACCOUNT": server_account.get("ACCOUNT"),
                                "PASSWORD": server_account.get("PASSWORD"),
                                "ACCOUNT_IDENTITY": server_account.get("ACCOUNT_IDENTITY"),
                                "AFFILIATED_PERSONNEL": server_account.get("AFFILIATED_PERSONNEL"),
                                "DETAIL": server_account.get("DETAIL"),
                            } for server_account in servers_account] if servers_account.exists() else [],
                        }
                        return_servers_list_data.append(return_servers_data)
                products_project = TransactionEconomyIndustryProductsProductsProject.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PRODUCTS=self.product_id,
                ).values('ID_PROJECT', 'ID_PROJECT__PROJECT_NAME', 'CORRELATION_CODE__ABBREVIATION', 'DETAIL', )
                return_data = {
                    "ID_PRODUCTS": self.product_id,
                    "PRODUCTS_NAME": data_product.get('PRODUCTS_NAME'),
                    "PRODUCTS_URL": data_product.get('PRODUCTS_URL'),
                    "PRODUCTS_ORGANIZATIONS": [{
                        "ID_ORGANIZATIONS": affiliation.get("ID_ORGANIZATIONS"),
                        "ID_ORGANIZATIONS_NAME": affiliation.get("ID_ORGANIZATIONS__ENTERPRISE_NAME"),
                    } for affiliation in affiliations] if affiliations.exists() else None,
                    "PRODUCTS_TYPES": [{
                        "TYPE": pro_type.get("PRODUCTS_CODE__ABBREVIATION"),
                    } for pro_type in types] if types.exists() else None,
                    "PRODUCTS_CALLS": [{
                        "TYPE": call.get("NAME_CODE__ABBREVIATION"),
                        "NAME": call.get("NAME"),
                    } for call in calls] if calls.exists() else None,
                    "PRODUCTS_SERVERS": return_servers_list_data,
                    "PRODUCTS_PROJECT": [{
                        "ID_PROJECT": product_project.get("ID_PROJECT"),
                        "PROJECT_NAME": product_project.get("ID_PROJECT__PROJECT_NAME"),
                        "PROJECT_CORRELATION_CODE": product_project.get("CORRELATION_CODE__ABBREVIATION"),
                        "PROJECT_DETAIL": product_project.get("DETAIL"),
                    } for product_project in products_project] if products_project.exists() else None,
                }
                yield return_data


class ProjectProducts(object):
    """
    产品返回结果数据
    """

    def __init__(self, project_id=None):
        self.project_id = project_id
        self.display = False
        self.data = []
        self.__def_get_products()

    def __def_get_product(self):
        """获取单个产品信息"""
        if self.project_id:
            data_product = TransactionEconomyIndustryProductsBasis.objects.filter(
                STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PROJECT=self.project_id,
            ).values(
                'ID_PRODUCTS', 'CORRELATION_CODE', 'CORRELATION_CODE__ABBREVIATION', 'DETAIL',
                'ID_PRODUCTS__PRODUCTS_NAME', 'ID_PRODUCTS__PRODUCTS_URL', 'ID_PRODUCTS__DETAIL',
            )
            if data_product.exists():
                for product in data_product:
                    return_data = {
                        "ID_PRODUCTS": product.get('ID_PRODUCTS').hex,
                        "PRODUCTS_CORRELATION_CODE": product.get('CORRELATION_CODE__ABBREVIATION'),
                        # "PRODUCTS_PROJECT_DETAIL": product.get('DETAIL'),
                        "PRODUCTS_NAME": product.get('ID_PRODUCTS__PRODUCTS_NAME'),
                        "PRODUCTS_URL": product.get('ID_PRODUCTS__PRODUCTS_URL'),
                        # "PRODUCTS_DETAIL": product.get('ID_PRODUCTS__DETAIL'),
                    }
                    product_types = TransactionEconomyIndustryProductsType.objects.filter(
                        STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PRODUCTS=product.get('ID_PRODUCTS').hex,
                    ).values('PRODUCTS_CODE__ABBREVIATION')
                    return_data.update({
                        "PRODUCTS_CODE": [
                            product_type.get('PRODUCTS_CODE__ABBREVIATION') for product_type in product_types
                        ] if product_types.exists() else None
                    })
                    organizations = TransactionEconomyIndustryProductsAffiliation.objects.filter(
                        STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PRODUCTS=product.get('ID_PRODUCTS').hex,
                    ).values('ID_ORGANIZATIONS', 'ID_ORGANIZATIONS__ENTERPRISE_NAME')
                    return_data.update({
                        "organization": [{
                            "ID_ORGANIZATIONS": organization.get('ID_ORGANIZATIONS').hex,
                            "ORGANIZATIONS_NAME": organization.get('ID_ORGANIZATIONS__ENTERPRISE_NAME'),
                        } for organization in organizations] if organizations.exists() else None})

                    products_call = TransactionEconomyIndustryProductsCall.objects.filter(
                        STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PRODUCTS=product.get('ID_PRODUCTS').hex,
                    ).values('NAME_CODE__ABBREVIATION', "NAME")
                    return_data.update({
                        "PRODUCTS_CALL": [
                            f'{product_call.get("NAME_CODE__ABBREVIATION")}:{product_call.get("NAME")}'
                            for product_call in products_call
                        ] if products_call.exists() else None})
                    products_server = TransactionEconomyIndustryProductsProductsServer.objects.filter(
                        STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PRODUCTS=product.get('ID_PRODUCTS').hex,
                        transactioneconomyindustryproductsproductsserveraccount__STATUS_IS_DELETE='0',
                        transactioneconomyindustryproductsproductsserveraccount__STATUS_IS_EFFECTIVE=1,
                    ).values(
                        "PROJECT_SERVER_ID", "SERVER_PROT", 'SERVER_ENVIRONMENT__ABBREVIATION', "DETAIL",
                        "PROJECT_SERVER_ID__NAME", "PROJECT_SERVER_ID__PUBLIC_NETWORK",
                        "PROJECT_SERVER_ID__INSIDE_OUTSIDE_CODE__ABBREVIATION",
                        "transactioneconomyindustryproductsproductsserveraccount__ACCOUNT",
                        "transactioneconomyindustryproductsproductsserveraccount__PASSWORD",
                        "transactioneconomyindustryproductsproductsserveraccount__ACCOUNT_IDENTITY",
                        "transactioneconomyindustryproductsproductsserveraccount__AFFILIATED_PERSONNEL",
                        "transactioneconomyindustryproductsproductsserveraccount__DETAIL",
                    )
                    return_data.update({
                        "SERVER": [{
                            "ID_SERVER": product_server.get("PROJECT_SERVER_ID").hex,
                            "SERVER_NAME": product_server.get("PROJECT_SERVER_ID__NAME"),
                            "SERVER_ENVIRONMENT": product_server.get("SERVER_ENVIRONMENT__ABBREVIATION"),
                            "SERVER_NETWORK": f'{product_server.get("PROJECT_SERVER_ID__PUBLIC_NETWORK")}:'
                                              f'{product_server.get("SERVER_PROT")}',
                            "SERVER_DETAIL": product_server.get("DETAIL"),
                            "SERVER_INTERNET_CODE": product_server.get(
                                "PROJECT_SERVER_ID__INSIDE_OUTSIDE_CODE__ABBREVIATION"),
                            "ACCOUNT": product_server.get(
                                "transactioneconomyindustryproductsproductsserveraccount__ACCOUNT"),
                            "PASSWORD": product_server.get(
                                "transactioneconomyindustryproductsproductsserveraccount__PASSWORD"),
                            "ACCOUNT_IDENTITY": product_server.get(
                                "transactioneconomyindustryproductsproductsserveraccount__ACCOUNT_IDENTITY"),
                            "AFFILIATED_PERSONNEL": product_server.get(
                                "transactioneconomyindustryproductsproductsserveraccount__AFFILIATED_PERSONNEL"),
                            "ACCOUNT_DETAIL": product_server.get(
                                "transactioneconomyindustryproductsproductsserveraccount__DETAIL"),
                        } for product_server in products_server] if products_server.exists() else None
                    })
                    self.data.append(return_data)
                    self.display = True

    def __def_get_products(self):
        data_products = TransactionEconomyIndustryProductsProductsProject.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PROJECT=self.project_id,
            # CORRELATION_CODE__TECHNOLOGY='0',
        ).values(
            'ID_PRODUCTS', 'CORRELATION_CODE', 'CORRELATION_CODE__ABBREVIATION', 'DETAIL',
            'ID_PRODUCTS__PRODUCTS_NAME', 'ID_PRODUCTS__PRODUCTS_URL', 'ID_PRODUCTS__DETAIL',
        )
        if data_products.exists():
            for product in data_products:
                return_data = {
                    "ID_PRODUCTS": product.get('ID_PRODUCTS').hex,
                    "PRODUCTS_CORRELATION_CODE": product.get('CORRELATION_CODE__ABBREVIATION'),
                    # "PRODUCTS_PROJECT_DETAIL": product.get('DETAIL'),
                    "PRODUCTS_NAME": product.get('ID_PRODUCTS__PRODUCTS_NAME'),
                    "PRODUCTS_URL": product.get('ID_PRODUCTS__PRODUCTS_URL'),
                    # "PRODUCTS_DETAIL": product.get('ID_PRODUCTS__DETAIL'),
                }
                product_types = TransactionEconomyIndustryProductsType.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PRODUCTS=product.get('ID_PRODUCTS').hex,
                ).values('PRODUCTS_CODE__ABBREVIATION')
                return_data.update({
                    "PRODUCTS_CODE": [
                        product_type.get('PRODUCTS_CODE__ABBREVIATION') for product_type in product_types
                    ] if product_types.exists() else None
                })
                organizations = TransactionEconomyIndustryProductsAffiliation.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PRODUCTS=product.get('ID_PRODUCTS').hex,
                ).values('ID_ORGANIZATIONS', 'ID_ORGANIZATIONS__ENTERPRISE_NAME')
                return_data.update({
                    "organization": [{
                        "ID_ORGANIZATIONS": organization.get('ID_ORGANIZATIONS').hex,
                        "ORGANIZATIONS_NAME": organization.get('ID_ORGANIZATIONS__ENTERPRISE_NAME'),
                    } for organization in organizations] if organizations.exists() else None})

                products_call = TransactionEconomyIndustryProductsCall.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PRODUCTS=product.get('ID_PRODUCTS').hex,
                ).values('NAME_CODE__ABBREVIATION', "NAME")
                return_data.update({
                    "PRODUCTS_CALL": [
                        f'{product_call.get("NAME_CODE__ABBREVIATION")}:{product_call.get("NAME")}'
                        for product_call in products_call
                    ] if products_call.exists() else None})
                products_server = TransactionEconomyIndustryProductsProductsServer.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PRODUCTS=product.get('ID_PRODUCTS').hex,
                    transactioneconomyindustryproductsproductsserveraccount__STATUS_IS_DELETE='0',
                    transactioneconomyindustryproductsproductsserveraccount__STATUS_IS_EFFECTIVE=1,
                ).values(
                    "PROJECT_SERVER_ID", "SERVER_PROT", 'SERVER_ENVIRONMENT__ABBREVIATION', "DETAIL",
                    "PROJECT_SERVER_ID__NAME", "PROJECT_SERVER_ID__PUBLIC_NETWORK",
                    "PROJECT_SERVER_ID__INSIDE_OUTSIDE_CODE__ABBREVIATION",
                    "transactioneconomyindustryproductsproductsserveraccount__ACCOUNT",
                    "transactioneconomyindustryproductsproductsserveraccount__PASSWORD",
                    "transactioneconomyindustryproductsproductsserveraccount__ACCOUNT_IDENTITY",
                    "transactioneconomyindustryproductsproductsserveraccount__AFFILIATED_PERSONNEL",
                    "transactioneconomyindustryproductsproductsserveraccount__DETAIL",
                )
                return_data.update({
                    "SERVER": [{
                        "ID_SERVER": product_server.get("PROJECT_SERVER_ID").hex,
                        "SERVER_NAME": product_server.get("PROJECT_SERVER_ID__NAME"),
                        "SERVER_ENVIRONMENT": product_server.get("SERVER_ENVIRONMENT__ABBREVIATION"),
                        "SERVER_NETWORK": f'{product_server.get("PROJECT_SERVER_ID__PUBLIC_NETWORK")}:'
                                          f'{product_server.get("SERVER_PROT")}',
                        "SERVER_DETAIL": product_server.get("DETAIL"),
                        "SERVER_INTERNET_CODE": product_server.get(
                            "PROJECT_SERVER_ID__INSIDE_OUTSIDE_CODE__ABBREVIATION"),
                        "ACCOUNT": product_server.get(
                            "transactioneconomyindustryproductsproductsserveraccount__ACCOUNT"),
                        "PASSWORD": product_server.get(
                            "transactioneconomyindustryproductsproductsserveraccount__PASSWORD"),
                        "ACCOUNT_IDENTITY": product_server.get(
                            "transactioneconomyindustryproductsproductsserveraccount__ACCOUNT_IDENTITY"),
                        "AFFILIATED_PERSONNEL": product_server.get(
                            "transactioneconomyindustryproductsproductsserveraccount__AFFILIATED_PERSONNEL"),
                        "ACCOUNT_DETAIL": product_server.get(
                            "transactioneconomyindustryproductsproductsserveraccount__DETAIL"),
                    } for product_server in products_server] if products_server.exists() else None
                })
                self.data.append(return_data)
                self.display = True

    @property
    def dict(self):
        return self.__dict__
