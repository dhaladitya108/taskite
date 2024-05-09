<script setup>
import { ref, watch, computed } from 'vue'
import { DownOutlined } from '@ant-design/icons-vue'
import { generateAvatar } from '@/utils/generators'

const props = defineProps(['members', 'labels'])
const emit = defineEmits(['filterChange'])

const priorityOptions = [
  { label: 'Urgent', value: 'urgent' },
  { label: 'High', value: 'high' },
  { label: 'Medium', value: 'medium' },
  { label: 'Low', value: 'low' },
]

const dropdownActiveKey = ref(['priorities', 'assignees', 'labels'])
const filterDropdownVisible = ref(false)

const selectedPriorities = ref([])
const selectedAssignees = ref([])
const selectedLabels = ref([])

watch([selectedPriorities, selectedAssignees, selectedLabels], async () => {
  emit('filterChange', {
    selectedPriorities: selectedPriorities.value,
    selectedAssignees: selectedAssignees.value,
    selectedLabels: selectedLabels.value
  })
})

function toggleDropdown(event) {
  filterDropdownVisible.value = !filterDropdownVisible.value
}

const getAvatar = (record) => {
  if(!record.avatar) {
    return generateAvatar(record.fullName)
  }

  return record.avatar
}
</script>

<template>
  <a-dropdown v-model:open="filterDropdownVisible" :trigger="['click']">
    <a-button type="dashed" @click="toggleDropdown" style="margin-right: 20px"
      >Filters <DownOutlined />
    </a-button>
    <template #overlay>
      <a-card size="small" style="width: 300px">
        <a-collapse v-model:activeKey="dropdownActiveKey" ghost>
          <a-collapse-panel key="priorities" header="Priorities">
            <a-checkbox-group v-model:value="selectedPriorities">
              <a-flex vertical>
                <a-checkbox
                  v-for="priority in priorityOptions"
                  :key="priority"
                  :value="priority.value"
                  >{{ priority.label }}</a-checkbox
                >
              </a-flex>
            </a-checkbox-group>
          </a-collapse-panel>
          <a-collapse-panel key="assignees" header="Assignees">
            <a-checkbox-group v-model:value="selectedAssignees">
              <a-flex vertical>
                <a-checkbox
                  v-for="member in props.members"
                  :key="member.id"
                  :value="member.id"
                  ><a-avatar
                    size="small"
                    :src="getAvatar(member)"
                    style="margin-right: 7px;"
                  ></a-avatar
                  >{{ member.displayName }}</a-checkbox
                >
              </a-flex>
            </a-checkbox-group>
          </a-collapse-panel>
          <a-collapse-panel key="labels" header="Labels">
            <a-checkbox-group v-model:value="selectedLabels">
              <a-flex vertical>
                <a-checkbox
                  v-for="label in props.labels"
                  :key="label.id"
                  :value="label.id"
                  >{{ label.name }}</a-checkbox
                >
              </a-flex>
            </a-checkbox-group>
          </a-collapse-panel>
        </a-collapse>
      </a-card>
    </template>
  </a-dropdown>
</template>
