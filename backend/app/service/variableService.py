from ..repository.variableRepo import GlobalVariableRepository

class GlobalVariableService:
    @staticmethod
    def create_global_variable(job_id: int, variable_name: str, variable_value: str) -> int:
        global_variable = {
            'job_id': job_id,
            'variable_name': variable_name,
            'variable_value': variable_value
        }
        return GlobalVariableRepository.create(global_variable)

    @staticmethod
    def get_global_variables(job_id: int):
        return GlobalVariableRepository.get_by_job_id(job_id)

    @staticmethod
    def update_global_variable(job_id: int, variable_name: str, variable_value: str):
        GlobalVariableRepository.update(job_id, variable_name, variable_value)

    @staticmethod
    def check_existance(job_id):
        count = GlobalVariableRepository.numvariables(job_id)
        print(count)
        return count > 0
