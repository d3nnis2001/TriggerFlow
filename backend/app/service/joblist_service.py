from ..repository.joblistRepository import JoblistRepository

class JoblistService:
    @staticmethod
    def getAllJobs():
        jobs = JoblistRepository.get_all_jobs()
        if len(jobs) == 0:
            return False, 'No Jobs existing'
        return jobs
