<template>
  <div class="min-h-screen bg-gray-900 text-gray-100 p-8">
    <div class="max-w-4xl mx-auto">
      <div class="flex justify-between items-center mb-8">
        <h2 class="text-3xl font-bold text-white">Job-Liste</h2>
        <button
          @click="showCreateJobDialog = true"
          class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded transition duration-300 ease-in-out"
        >
          Neuen Job erstellen
        </button>
      </div>
      
      <SearchFilter
        v-model:searchQuery="searchQuery"
        v-model:filterCriteria="filterCriteria"
        @filter="filterJobs"
      />
      
      <div class="space-y-6 mt-8">
        <JobCard
          v-for="job in filteredJobs"
          :key="job.id"
          :job="job"
          @load="loadJob"
          @edit="editJob"
          @delete="deleteJob"
        />
      </div>
    </div>

    <CreateJobDialog
      v-if="showCreateJobDialog"
      @close="showCreateJobDialog = false"
      @create="createJob()"
    />
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import SearchFilter from "../components/JobOverview/SearchFilter.vue";
import JobCard from "../components/JobOverview/JobCard.vue";
import CreateJobDialog from "../components/JobOverview/CreateJobDialog.vue";
import { getAllJobs, createNewJob } from "../api/joblist";

const jobs = ref([]);
const searchQuery = ref("");
const filterCriteria = ref("");
const showCreateJobDialog = ref(false);

const filteredJobs = computed(() => {
  let result = jobs.value;
  if (searchQuery.value) {
    result = result.filter(
      (job) =>
        job.name.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
        job.description.toLowerCase().includes(searchQuery.value.toLowerCase())
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
  // Die Filterung wird bereits durch das computed property 'filteredJobs' gehandhabt
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

const createJob = async (newJob) => {
  try {
    const createdJob = await createNewJob(newJob);
    jobs.value.push(createdJob);
    showCreateJobDialog.value = false;
  } catch (error) {
    console.error("Error creating job:", error);
    // TODO: Handle error (e.g., show error message to user)
  }
};

onMounted(async () => {
  jobs.value = await getAllJobs();
});
</script>