from ..repository.variableRepo import GlobalVariableRepository
import json

class GlobalVariableService:
    @staticmethod
    def create_global_variable(job_id: int, variable_data: str) -> int:
        try:
            if isinstance(variable_data, str):
                json.loads(variable_data)
            else:
                variable_data = json.dumps(variable_data)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON data provided: {str(e)}")
        global_variable = {
            'job_id': job_id,
            'variable_data': variable_data,
        }
        return GlobalVariableRepository.create(global_variable)

    @staticmethod
    def get_global_variables(job_id: int):
        return GlobalVariableRepository.get_by_job_id(job_id)

    @staticmethod
    def update_global_variable(job_id: int, variable_data: str):
        try:
            if isinstance(variable_data, str):
                json.loads(variable_data)
            else:
                variable_data = json.dumps(variable_data)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON data provided: {str(e)}")
        GlobalVariableRepository.update(job_id, variable_data)

    @staticmethod
    def check_existance(job_id):
        count = GlobalVariableRepository.numvariables(job_id)
        print(count)
        return count > 0
