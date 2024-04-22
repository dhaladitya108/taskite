<script setup>
import { ref, computed, watch } from 'vue'
const props = defineProps(['members'])
const emit = defineEmits(['filterChange'])

const assigneeOptions = computed(() => {
  return props.members.map((member) => {
    return {
      label: member.display_name,
      value: member.id,
    }
  })
})

const priorityOptions = [
  { label: 'Urgent', value: 'urgent' },
  { label: 'High', value: 'high' },
  { label: 'Medium', value: 'medium' },
  { label: 'Low', value: 'low' },
]

const selectedPriorities = ref([])
const selectedAssignees = ref([])

watch([selectedPriorities, selectedAssignees], async () => {
  emit('filterChange', {
    selectedPriorities: selectedPriorities.value,
    selectedAssignees: selectedAssignees.value,
  })
})
</script>

<template>
  <a-dropdown :trigger="['click']">
    <a-button type="primary" size="small"> Filters </a-button>
    <template #overlay>
      <a-card size="small" style="width: 200px">
        <div>Priorities</div>
        <a-flex vertical>
          <a-checkbox-group
            v-model:value="selectedPriorities"
            :options="priorityOptions"
          >
          </a-checkbox-group>
        </a-flex>

        <div>Assignees</div>
        <a-flex vertical>
          <a-checkbox-group
            v-model:value="selectedAssignees"
            :options="assigneeOptions"
          >
          </a-checkbox-group>
        </a-flex>
      </a-card>
    </template>
  </a-dropdown>
</template>
