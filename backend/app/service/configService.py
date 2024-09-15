from ..repository.configRepo import ConfigTableRepository
import json

class ConfigTableService:
    @staticmethod
    def create_table(table_id, job_id, table_name, table_data):
        job_id = int(job_id) if job_id is not None else None
        table_id = int(table_id) if table_id is not None else None
        try:
            # Ensure table_data is valid JSON
            if isinstance(table_data, str):
                json.loads(table_data)  # This will raise an error if it's not valid JSON
            else:
                table_data = json.dumps(table_data)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON data provided: {str(e)}")

        config_table = {
            "table_id": table_id,
            "job_id": job_id,
            "table_name": table_name,
            "table_data": table_data
        }
        return ConfigTableRepository.create(config_table)

    @staticmethod
    def get_all_tables_by_job(job_id):
        job_id = int(job_id) if job_id is not None else None
        return ConfigTableRepository.get_all_by_job(job_id)

    @staticmethod
    def get_table_by_id(table_id):
        table_id = int(table_id) if table_id is not None else None
        return ConfigTableRepository.get_by_id(table_id)

    @staticmethod
    def update_table(table_id, job_id, table_name, table_data):
        table_id = int(table_id) if table_id is not None else None
        job_id = int(job_id) if job_id is not None else None

        try:
            if isinstance(table_data, str):
                json.loads(table_data)
            else:
                table_data = json.dumps(table_data)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON data provided: {str(e)}")

        config_table_data = {
            "table_id": table_id,
            "job_id": job_id,
            "table_name": table_name,
            "table_data": table_data
        }
        return ConfigTableRepository.update(config_table_data)

    @staticmethod
    def delete_table(table_id):
        table_id = int(table_id) if table_id is not None else None
        return ConfigTableRepository.delete(table_id)
