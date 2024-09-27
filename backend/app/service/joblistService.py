from ..repository.joblistRepo import JoblistRepository

class JoblistService:
    @staticmethod
    def getAllJobs():
        jobs = JoblistRepository.get_all_jobs()
        if len(jobs) == 0:
            return False, 'No Jobs existing'
        return jobs
    
    @staticmethod 
    def createJob(name, desc, comp, image):
        return JoblistRepository.create(name, image, comp, desc)
