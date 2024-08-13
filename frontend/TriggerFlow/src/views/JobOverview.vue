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

export default {
    components: {
        SearchFilter,
        JobCard,
    },
    setup() {
        const jobs = ref([
            // Sample job data
            {
                id: 1,
                name: "Job 1",
                description: "Description for Job 1",
                image: "path/to/image1.jpg",
                date: new Date(),
            },
            {
                id: 2,
                name: "Job 2",
                description: "Description for Job 2",
                image: "path/to/image2.jpg",
                date: new Date(Date.now() - 86400000),
            },
            // Add more jobs...
        ]);

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
            // This function is called when search or filter changes
            // The filtering is handled by the computed property
        };

        const loadJob = (job) => {
            console.log("Loading job:", job.name);
            // Implement job loading logic
        };

        const editJob = (job) => {
            console.log("Editing job:", job.name);
            // Implement job editing logic
        };

        const deleteJob = (job) => {
            console.log("Deleting job:", job.name);
            // Implement job deletion logic
        };

        onMounted(() => {
            // Initialize perfect-scrollbar or any other scrolling library if needed
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
