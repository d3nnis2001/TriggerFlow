<template>
    <DataTable :initialData="myData" initialTableName="My CSV Data" />
</template>

<script>
import DataTable from "../components/ColumnPicker/DataTable.vue";

export default {
    components: { DataTable },
    data() {
        return {
            myData: [
                { id: 1, name: "John", age: 30 },
                { id: 2, name: "Jane", age: 25 },
                { id: 3, name: "Susan", age: 35 },
                { id: 4, name: "Chris", age: 40 },
                { id: 5, name: "Dan", age: 28 },
                { id: 6, name: "Mike", age: 33 },
                { id: 7, name: "Tom", age: 22 },
                { id: 8, name: "Kate", age: 27 },
                { id: 9, name: "Sara", age: 32 },
                { id: 10, name: "Paul", age: 29 },
                { id: 11, name: "Jim", age: 31 },
                { id: 12, name: "Sam", age: 26 },
                { id: 13, name: "Tim", age: 34 },
                { id: 14, name: "Rob", age: 39 },
                { id: 15, name: "Ben", age: 24 },
                { id: 9, name: "Sara", age: 32 },
                { id: 10, name: "Paul", age: 29 },
                { id: 11, name: "Jim", age: 31 },
                { id: 12, name: "Sam", age: 26 },
                { id: 13, name: "Tim", age: 34 },
                { id: 14, name: "Rob", age: 39 },
                { id: 15, name: "Ben", age: 24 },
                { id: 9, name: "Sara", age: 32 },
                { id: 10, name: "Paul", age: 29 },
                { id: 11, name: "Jim", age: 31 },
                { id: 12, name: "Sam", age: 26 },
                { id: 13, name: "Tim", age: 34 },
                { id: 14, name: "Rob", age: 39 },
                { id: 15, name: "Ben", age: 24 },
            ],
        };
    },
};
</script>
