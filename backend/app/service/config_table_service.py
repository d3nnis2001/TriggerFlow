from ..repository.config_table_repository import ConfigTableRepository

class ConfigTableService:
    @staticmethod
    def create_table(name, description, columns, data):
        structure = [{"field": col["field"], "header": col["header"]} for col in columns]
        return ConfigTableRepository.create_table(name, description, structure, data)

    @staticmethod
    def get_all_tables():
        return ConfigTableRepository.get_all_tables()

    @staticmethod
    def get_table_by_id(table_id):
        return ConfigTableRepository.get_table_by_id(table_id)

    @staticmethod
    def update_table(table_id, name, description, columns, data):
        structure = [{"field": col["field"], "header": col["header"]} for col in columns]
        return ConfigTableRepository.update_table(table_id, name, description, structure, data)

    @staticmethod
    def delete_table(table_id):
        return ConfigTableRepository.delete_table(table_id)