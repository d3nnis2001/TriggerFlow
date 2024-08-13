<template>
    <div class="job-list">
        <h2>Job-Liste</h2>
        <SearchFilter
            v-model:searchQuery="searchQuery"
            v-model:filterCriteria="filterCriteria"
            @filter="filterJobs"
        />
        <JobCard
            v-for="job in filteredJobs"
            :key="job.id"
            :job="job"
            @load="loadJob"
            @edit="editJob"
            @delete="deleteJob"
        />
    </div>
</template>

<script>
import { ref, computed, onMounted } from "vue";
import SearchFilter from "../components/JobOverview/SearchFilter.vue";
import JobCard from "../components/JobOverview/JobCard.vue";
import { getAllJobs } from "../api/joblist";

export default {
    components: {
        SearchFilter,
        JobCard,
    },
    setup() {
        let jobs = ref([]);

        const searchQuery = ref("");
        const filterCriteria = ref("");
        const jobCards = ref(null);

        const filteredJobs = computed(() => {
            let result = jobs.value;
            if (searchQuery.value) {
                result = result.filter(
                    (job) =>
                        job.name
                            .toLowerCase()
                            .includes(searchQuery.value.toLowerCase()) ||
                        job.description
                            .toLowerCase()
                            .includes(searchQuery.value.toLowerCase()),
                );
            }
            if (filterCriteria.value === "recent") {
                result = result.sort((a, b) => b.date - a.date);
            } else if (filterCriteria.value === "old") {
                result = result.sort((a, b) => a.date - b.date);
            }
            return result;
        });

        const filterJobs = () => {
            // TODO: Filter für Jobs
        };

        const loadJob = (job) => {
            console.log("Loading job:", job.name);
            // TODO: Implement job loading logic
        };

        const editJob = (job) => {
            console.log("Editing job:", job.name);
            // TODO: Implement job editing logic
        };

        const deleteJob = (job) => {
            console.log("Deleting job:", job.name);
            // TODO: Implement job deletion logic
        };

        onMounted(async () => {
            jobs.value = await getAllJobs();
        });

        return {
            filteredJobs,
            searchQuery,
            filterCriteria,
            jobCards,
            filterJobs,
            loadJob,
            editJob,
            deleteJob,
        };
    },
};
</script>

<style scoped>
.job-list {
    width: 100vw;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
</style>
