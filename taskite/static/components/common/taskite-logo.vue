<script setup>
import logo from '@/images/logo.png'

const props = defineProps({
  height: {
    type: Number,
    default: 22,
  },
})
</script>

<template>
  <img :src="logo" :height="props.height" />
</template>
