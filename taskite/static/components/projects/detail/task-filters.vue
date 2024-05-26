<script setup>
import { ref, watch, computed } from 'vue'
import { DownOutlined, InfoCircleOutlined, DisconnectOutlined, WarningOutlined, MinusSquareOutlined } from '@ant-design/icons-vue'
import { generateAvatar } from '@/utils/generators'

const props = defineProps(['members', 'labels'])
const emit = defineEmits(['filterChange'])

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
  if (!record.avatar) {
    return generateAvatar(record.fullName)
  }

  return record.avatar
}
</script>

<template>
  <a-dropdown v-model:open="filterDropdownVisible" :trigger="['click']">
    <a-button type="dashed" @click="toggleDropdown" class="mr-3">Filters
      <DownOutlined />
    </a-button>
    <template #overlay>
      <div
        size="small"
        class="bg-white p-3 rounded-md shadow-md min-w-80 flex flex-col"
      >
        <!-- Priorities -->
        <div class="w-full">
          <p class="text-sm font-medium tracking-wide">Priorities</p>
          <a-checkbox-group v-model:value="selectedPriorities">
            <a-flex vertical>
              <a-checkbox value="urgent" class="my-1"><info-circle-outlined></info-circle-outlined> Urgent</a-checkbox>
              <a-checkbox value="high" class="my-1"><warning-outlined></warning-outlined> High</a-checkbox>
              <a-checkbox value="medium" class="my-1"><minus-square-outlined></minus-square-outlined> Medium</a-checkbox>
              <a-checkbox value="low" class="my-1"><disconnect-outlined></disconnect-outlined> Low</a-checkbox>
            </a-flex>
          </a-checkbox-group>
        </div>

        <div class="h-[1px] bg-gray-200 w-full my-3"></div>

        <!-- Assignees -->
        <div>
          <p class="text-sm font-medium tracking-wide">Assignees</p>
          <a-checkbox-group v-model:value="selectedAssignees">
            <a-flex vertical>
              <a-checkbox v-for="member in props.members" :key="member.id" :value="member.id"><a-avatar size="small"
                  :src="getAvatar(member)" class="my-1 mr-2"></a-avatar>{{ member.displayName }}</a-checkbox>
            </a-flex>
          </a-checkbox-group>
        </div>
      </div>
    </template>
  </a-dropdown>
</template>
