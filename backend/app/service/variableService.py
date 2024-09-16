from ..repository.variableRepo import GlobalVariableRepository
from typing import List, Dict

class GlobalVariableService:
    @staticmethod
    def create_global_variable(job_id: int, variable_data: List[Dict[str, str]]) -> int:
        global_variable = {
            'job_id': job_id,
            'variable_data': variable_data,
        }
        return GlobalVariableRepository.create(global_variable)

    @staticmethod
    def get_global_variables(job_id: int) -> List[Dict[str, str]]:
        variables = GlobalVariableRepository.get_by_job_id(job_id)
        if variables:
            return variables[0]['variable_data']
        return []

    @staticmethod
    def update_global_variable(job_id: int, variable_data: List[Dict[str, str]]) -> None:
        GlobalVariableRepository.update(job_id, variable_data)

    @staticmethod
    def check_existance(job_id: int) -> bool:
        count = GlobalVariableRepository.numvariables(job_id)
        return count > 0